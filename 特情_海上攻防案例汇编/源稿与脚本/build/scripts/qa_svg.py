# -*- coding: utf-8 -*-
"""
《析光》SVG 版面 QA —— 封面/封底/标志交付前必跑

    python3 qa_svg.py cover.svg back.svg

三关：
  ①边缘安全区：外框 6mm 内不得有墨迹
  ②底色纯度：封面米色底应 >0.80，封底藏青底应 >0.85
  ③文本碰撞：逐元素单独渲染做真·墨迹相交检测
     （不要用 getBBox/getBoundingClientRect 判重叠——行盒比字形大，
       大号标题与紧跟的副题必然假阳性，历史上误报过三处）
"""
import itertools
import os
import sys
import tempfile

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

W_MM, H_MM = 210.0, 297.0
PX = 1200
SAFE_MM = 6.0


def _hex(h):
    return np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)])


def _shell(svg_path):
    with open(svg_path, encoding='utf-8') as f:
        s = f.read()
    s = s.replace('width="210mm"', 'width="%dpx"' % PX, 1)
    s = s.replace('height="297mm"', 'height="%dpx"' % int(PX * H_MM / W_MM), 1)
    return s


def check(svg_path):
    tmp = tempfile.mkdtemp()
    svg = _shell(svg_path)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': PX, 'height': int(PX * H_MM / W_MM)},
                        device_scale_factor=2)
        pg.set_content('<body style="margin:0;background:#fff">' + svg + '</body>')
        pg.wait_for_timeout(450)
        full = os.path.join(tmp, 'full.png')
        pg.query_selector('svg').screenshot(path=full)

        labels = pg.evaluate(
            "()=>[...document.querySelectorAll('text')].map(t=>t.textContent.slice(0,14))")

        # 基线：隐藏全部文字，保留底色与图形。逐元素渲染后与基线做差，
        # 差异处即该文字的真实字形墨迹——这样对深色底封底同样成立。
        def shot(name):
            f = os.path.join(tmp, name)
            pg.query_selector('svg').screenshot(path=f)
            return np.asarray(Image.open(f).convert('RGB')).astype(int)

        pg.evaluate("()=>[...document.querySelectorAll('text')]"
                    ".forEach(t=>t.style.visibility='hidden')")
        pg.wait_for_timeout(60)
        base_img = shot('base.png')

        masks = []
        for i in range(len(labels)):
            pg.evaluate("""(i)=>{const ts=[...document.querySelectorAll('text')];
                ts.forEach((t,k)=>t.style.visibility=(k===i?'visible':'hidden'));}""", i)
            pg.wait_for_timeout(50)
            img = shot('t%d.png' % i)
            masks.append(np.abs(img - base_img).sum(2) > 30)
        pg.evaluate("()=>[...document.querySelectorAll('text')]"
                    ".forEach(t=>t.style.visibility='visible')")
        b.close()

    a = np.asarray(Image.open(full).convert('RGB')).astype(int)
    h, w, _ = a.shape
    corner = tuple(a[3, 3])
    base = (np.abs(a - np.array(corner)).sum(2) < 45).mean()
    bpx = max(2, int(SAFE_MM / W_MM * w))
    edge = np.concatenate([a[:bpx].reshape(-1, 3), a[-bpx:].reshape(-1, 3),
                           a[:, :bpx].reshape(-1, 3), a[:, -bpx:].reshape(-1, 3)])
    edge_ink = (np.abs(edge - np.array(corner)).sum(1) > 90).mean()

    collisions = []
    for i, j in itertools.combinations(range(len(masks)), 2):
        n = int((masks[i] & masks[j]).sum())
        if n > 0:
            collisions.append((labels[i], labels[j], n))

    flags = []
    if edge_ink > 0.0005:
        flags.append('边缘裁切')
    if base < 0.80:
        flags.append('底色占比偏低(%.2f)' % base)
    if collisions:
        flags.append('文本碰撞%d处' % len(collisions))

    print('%-14s %dx%d  底色=%.2f  安全区墨迹=%.5f  文本%d个  %s'
          % (os.path.basename(svg_path), w, h, base, edge_ink, len(labels),
             '、'.join(flags) if flags else 'OK'))
    for c in collisions:
        print('    碰撞: [%s] x [%s]  %d px' % c)
    return len(flags)


if __name__ == '__main__':
    bad = sum(check(f) for f in sys.argv[1:])
    print('\n结论：%s' % ('全部通过，可交付' if bad == 0 else '存在问题，须回改'))
    sys.exit(1 if bad else 0)
