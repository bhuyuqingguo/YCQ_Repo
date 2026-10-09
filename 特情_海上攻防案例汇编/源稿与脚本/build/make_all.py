# -*- coding: utf-8 -*-
"""一键出版：出图 -> docx 两遍页码 -> PDF -> 质检 -> HTML/配图页 -> 数据导出"""
import csv, glob, json, os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)
subprocess.run([sys.executable, 'make_figs.py'], check=True, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, 'make_figs2.py'], check=True, stdout=subprocess.DEVNULL)
import build
from cases_lib import clean, fmt_date

ctx, docx = build.main()
print('docx:', docx)
out = build.OUT
pdf_filter = ('pdf:writer_pdf_Export:{"UseLosslessCompression":{"type":"boolean","value":false},'
              '"Quality":{"type":"long","value":70},"ReduceImageResolution":{"type":"boolean","value":true},'
              '"MaxImageResolution":{"type":"long","value":200},"ExportBookmarks":{"type":"boolean","value":true}}')
subprocess.run(['soffice', '--headless', '--convert-to', pdf_filter, '--outdir', out, docx],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1200)
pdf = os.path.splitext(docx)[0] + '.pdf'
print('pdf:', pdf, os.path.exists(pdf))
subprocess.run([sys.executable, 'qa_docx.py', docx])

# 像素质检（全页 30dpi）
import numpy as np
from PIL import Image
qd = os.path.join(HERE, 'tmp', 'qa'); shutil.rmtree(qd, ignore_errors=True); os.makedirs(qd)
subprocess.run(['pdftoppm', '-jpeg', '-r', '30', pdf, os.path.join(qd, 'p')], check=True)
bad = []
pages = sorted(glob.glob(os.path.join(qd, 'p-*.jpg')))
for i, f in enumerate(pages, 1):
    a = np.asarray(Image.open(f).convert('RGB')).astype(int)
    cream = ((a[:, :, 0] > 238) & (a[:, :, 1] > 232) & (a[:, :, 2] > 220) & (a[:, :, 2] < 245)).mean()
    dark = (a.sum(2) < 360).mean()
    ink = (a.sum(2) < 640).mean()
    b = 3
    edge = np.concatenate([a[:b].reshape(-1, 3), a[-b:].reshape(-1, 3), a[:, :b].reshape(-1, 3), a[:, -b:].reshape(-1, 3)])
    edge_ink = (edge.sum(1) < 400).mean()
    full = i in (1, len(pages))
    flags = []
    if not full and cream < 0.35: flags.append('cream=%.2f' % cream)
    if dark > 0.30 and not full: flags.append('dark=%.2f' % dark)
    if ink < 0.004 and not full: flags.append('空页? ink=%.4f' % ink)
    if edge_ink > 0.002 and not full: flags.append('edge=%.3f' % edge_ink)
    if flags: bad.append((i, flags))
print('像素质检：共 %d 页，异常 %d 页' % (len(pages), len(bad)), bad[:20])

html, imgp, nimg, hctx = build.build_html(build.load_sections())
print('html:', html, nimg, 'images')

# 案例数据导出
cs = ctx['cases']
data = []
for c in cs:
    d = {k: v for k, v in c.items() if not k.startswith('_')}
    data.append(d)
json.dump(data, open(os.path.join(out, '案例库_cases.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(out, '案例库_cases.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['编号', '场景', '日期', '海域', '地点', '标题', '攻击方', '防御方', '域', '组织形态', '结果', '攻击手段',
                '防御手段', '损失', '可信度', '纬度', '经度', '出处数', '首条出处'])
    for c in cs:
        s0 = (c.get('sources') or [{}])[0]
        w.writerow([c['code'], c['category'], fmt_date(c), c.get('region'), clean(c.get('location_cn')),
                    clean(c.get('title_cn')), clean(c.get('attacker')), clean(c.get('defender')),
                    '、'.join(c.get('domains') or []), '、'.join(c.get('patterns') or []), clean(c.get('outcome')),
                    clean(c.get('attack_means_cn')), clean(c.get('defense_means_cn')), clean(c.get('losses_cn')),
                    (c.get('confidence') or '')[:1], c.get('lat'), c.get('lon'), len(c.get('sources') or []),
                    s0.get('url', '')])
print('cases exported', len(cs))
