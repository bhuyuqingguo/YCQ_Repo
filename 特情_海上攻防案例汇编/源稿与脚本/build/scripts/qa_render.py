# -*- coding: utf-8 -*-
"""
《析光》交付前 QA 管线：docx -> PDF -> 逐页JPG -> 像素校验

用法：
    python3 qa_render.py "某某（析光刊物版）.docx"

输出每页指标；随后必须用 view 工具目检首页与含图页。
不合格必回改，不合格不交付。

判读基线（A4，70dpi 渲染）：
    cream  0.55–0.92   米色底占比。<0.5 说明底色没生效或图压满页
    dark   0.02–0.12   暗色文字占比。<0.01 基本是空页；>0.2 版面过挤
    color  >0.002      含图页的彩色占比。纯文字页接近 0 属正常
    edge   <0.002      外框 6px 内墨迹，超标说明内容被裁切
"""
import glob
import os
import subprocess
import sys

import numpy as np
from PIL import Image

SOFFICE = '/mnt/skills/public/docx/scripts/office/soffice.py'


def to_pdf(docx_path):
    workdir = os.path.dirname(os.path.abspath(docx_path)) or '.'
    subprocess.run(['python3', SOFFICE, '--headless', '--convert-to', 'pdf',
                    os.path.basename(docx_path)],
                   cwd=workdir, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL, check=False)
    pdf = os.path.splitext(docx_path)[0] + '.pdf'
    if not os.path.exists(pdf):
        raise RuntimeError('PDF 转换失败：%s' % pdf)
    return pdf


def to_pages(pdf_path, prefix='qapage', dpi=70):
    workdir = os.path.dirname(os.path.abspath(pdf_path)) or '.'
    for f in glob.glob(os.path.join(workdir, prefix + '-*.jpg')):
        os.remove(f)
    subprocess.run(['pdftoppm', '-jpeg', '-r', str(dpi),
                    os.path.basename(pdf_path), prefix],
                   cwd=workdir, check=True)
    return sorted(glob.glob(os.path.join(workdir, prefix + '-*.jpg')))


def metrics(jpg):
    a = np.asarray(Image.open(jpg).convert('RGB')).astype(int)
    h, w, _ = a.shape
    cream = ((a[:, :, 0] > 238) & (a[:, :, 1] > 232) &
             (a[:, :, 2] > 220) & (a[:, :, 2] < 245)).mean()
    dark = (a.sum(2) < 360).mean()
    color = ((np.abs(a[:, :, 0] - a[:, :, 2]) > 40) |
             (np.abs(a[:, :, 1] - a[:, :, 2]) > 40)).mean()
    b = 6
    edge = np.concatenate([a[:b].reshape(-1, 3), a[-b:].reshape(-1, 3),
                           a[:, :b].reshape(-1, 3), a[:, -b:].reshape(-1, 3)])
    edge_ink = (edge.sum(1) < 400).mean()
    return dict(cream=cream, dark=dark, color=color, edge=edge_ink)


def verdict(m):
    flags = []
    if m['cream'] < 0.50:
        flags.append('米色底异常')
    if m['dark'] < 0.01:
        flags.append('疑似空页')
    if m['dark'] > 0.20:
        flags.append('版面过挤')
    if m['edge'] > 0.002:
        flags.append('边缘裁切')
    return '、'.join(flags) if flags else 'OK'


def main(docx_path):
    pdf = to_pdf(docx_path)
    pages = to_pages(pdf)
    print('页数：%d    PDF：%s' % (len(pages), os.path.basename(pdf)))
    bad = 0
    for p in pages:
        m = metrics(p)
        v = verdict(m)
        bad += (v != 'OK')
        print('%-16s cream=%.2f dark=%.3f color=%.4f edge=%.4f  %s'
              % (os.path.basename(p), m['cream'], m['dark'],
                 m['color'], m['edge'], v))
    print('\n结论：%s' % ('全部通过，可交付' if bad == 0
                          else '%d 页需回改，不得交付' % bad))
    print('提示：像素校验只查版面，乱码与图注仍须 view 目检首页及含图页。')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1]) else 0)
