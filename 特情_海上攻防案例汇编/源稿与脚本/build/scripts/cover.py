# -*- coding: utf-8 -*-
"""
《析光》封面 / 封底 生成器（A4，参数化可编辑 SVG）

    python3 cover.py --issue "2026年第3期" --date "2026年7月" \\
        --title "无人上舰第一步，为什么是加油机" \\
        --lead "美海军以保障平台先行打通上舰全链条" \\
        --toc "环球瞭望｜北约防务创新提速" "装备透视｜MQ-25A全景调研" \\
        --out ./out

产出 cover.svg / back.svg（可再编辑）+ 同名 .png（300dpi 校样）。
坐标单位＝毫米，viewBox "0 0 210 297"，改版直接改数字即可。
品牌标从 assets/hongyan_mark.svg 内联嵌入，改标只改那个文件。
"""
import argparse
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), 'assets')

CREAM = '#F7F4EC'
GRID = '#E9E4D6'
NAVY = '#12233B'
ACCENT = '#2E93D6'
BRASS = '#A8842F'
GREY = '#8A8474'

FONT = "'黑体','SimHei','Noto Sans CJK SC',sans-serif"
FONT_S = "'楷体_GB2312','KaiTi','Noto Serif CJK SC',serif"

W, H = 210.0, 297.0
M = 18.0            # 版心边距
SAFE = 6.0          # 边缘安全区，此范围内不得有墨迹


def load_mark(scale=1.0, dx=0.0, dy=0.0):
    """内联品牌标，缩放到毫米坐标系。原始 viewBox 512 -> 目标 mm。"""
    path = os.path.join(ASSETS, 'hongyan_mark.svg')
    with open(path, encoding='utf-8') as f:
        svg = f.read()
    inner = svg.split('>', 1)[1].rsplit('</svg>', 1)[0]
    inner = re.sub(r'<title>.*?</title>', '', inner, flags=re.S)
    k = scale / 512.0
    return ('<g id="品牌标" transform="translate(%.3f,%.3f) scale(%.5f)">%s</g>'
            % (dx, dy, k, inner))


def _grid(step=7.0):
    ls = []
    x = step
    while x < W:
        ls.append('<line x1="%.1f" y1="0" x2="%.1f" y2="%.1f"/>' % (x, x, H))
        x += step
    y = step
    while y < H:
        ls.append('<line x1="0" y1="%.1f" x2="%.1f" y2="%.1f"/>' % (y, W, y))
        y += step
    return ('<g id="网格" stroke="%s" stroke-width="0.15" opacity="0.55">%s</g>'
            % (GRID, ''.join(ls)))


def _seal(cx, cy, r, issue, date, tilt=-8):
    """右上黄铜圆章：期号 + 日期，微倾斜盖章感。"""
    return f'''<g id="期号章" transform="rotate({tilt} {cx} {cy})">
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{BRASS}" stroke-width="0.9"/>
    <circle cx="{cx}" cy="{cy}" r="{r - 1.8}" fill="none" stroke="{BRASS}" stroke-width="0.35" opacity=".7"/>
    <text x="{cx}" y="{cy - 1.2}" text-anchor="middle" font-family={FONT!r}
          font-size="5.4" font-weight="700" fill="{BRASS}">{issue}</text>
    <line x1="{cx - r + 5}" y1="{cy + 1.2}" x2="{cx + r - 5}" y2="{cy + 1.2}"
          stroke="{BRASS}" stroke-width="0.3"/>
    <text x="{cx}" y="{cy + 6.2}" text-anchor="middle" font-family={FONT!r}
          font-size="3.6" fill="{BRASS}">{date}</text>
  </g>'''


def make_cover(issue='2026年第3期', date='2026年7月',
               title='本期专题标题', lead='一句导语',
               toc=(), classification='非密·内部资料'):
    toc_items = []
    y = 214.0
    for t in list(toc)[:5]:
        toc_items.append(
            f'<line x1="{M}" y1="{y - 4.4:.1f}" x2="{W - M}" y2="{y - 4.4:.1f}" '
            f'stroke="{GRID}" stroke-width="0.3"/>'
            f'<circle cx="{M + 1.4:.1f}" cy="{y - 1.4:.1f}" r="0.9" fill="{BRASS}"/>'
            f'<text x="{M + 5:.1f}" y="{y:.1f}" font-family={FONT!r} font-size="4.2" '
            f'fill="{NAVY}" opacity=".9">{t}</text>')
        y += 9.0

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm"
     viewBox="0 0 {W:.0f} {H:.0f}">
  <title>《析光》封面 {issue}</title>
  <rect width="{W}" height="{H}" fill="{CREAM}"/>
  {_grid()}

  <g id="顶栏刊眉">
    <text x="{M}" y="14" font-family={FONT!r} font-size="3.4"
          letter-spacing="1.1" fill="{NAVY}">XIGUANG · INTELLIGENCE</text>
    <text x="{W - M}" y="14" text-anchor="end" font-family={FONT!r}
          font-size="3.4" fill="{GREY}">{classification}</text>
    <line x1="{M}" y1="17" x2="{W - M}" y2="17" stroke="{NAVY}" stroke-width="0.5"/>
  </g>

  <g id="刊名">
    <text x="{M}" y="52" font-family={FONT!r} font-size="34"
          font-weight="700" fill="{NAVY}" letter-spacing="4">析光</text>
    <text x="{M + 1}" y="62" font-family={FONT!r} font-size="7.5"
          letter-spacing="5.5" fill="{BRASS}">XIGUANG</text>
    <text x="{M + 1}" y="70" font-family={FONT_S!r} font-size="4"
          fill="{GREY}">鸿眼 · 无人体系中心 科研情报刊物</text>
    <line x1="{M}" y1="76" x2="{M + 46}" y2="76" stroke="{BRASS}" stroke-width="1.2"/>
  </g>

  {_seal(W - M - 20, 48, 20, issue, date)}

  {load_mark(scale=62, dx=(W - 62) / 2, dy=92)}

  <g id="专题">
    <text x="{M}" y="180" font-family={FONT!r} font-size="10.5"
          font-weight="700" fill="{NAVY}">{title}</text>
    <text x="{M}" y="191" font-family={FONT_S!r} font-size="4.6"
          fill="{GREY}">{lead}</text>
  </g>

  <g id="本期目录">
    <text x="{M}" y="205" font-family={FONT!r} font-size="4"
          letter-spacing="2" fill="{BRASS}">本期目录 ｜ CONTENTS</text>
    {''.join(toc_items)}
  </g>

  <g id="底栏">
    <line x1="{M}" y1="272" x2="{W - M}" y2="272" stroke="{NAVY}" stroke-width="0.5"/>
    <text x="{W / 2}" y="280" text-anchor="middle" font-family={FONT!r}
          font-size="4.4" letter-spacing="2.6" fill="{NAVY}">看得早 · 看得懂 · 看得准 · 看得透</text>
    <text x="{W / 2}" y="287" text-anchor="middle" font-family={FONT_S!r}
          font-size="3.2" fill="{GREY}">析光·科研情报 ｜ 鸿眼·无人体系中心</text>
  </g>
</svg>
'''


def make_back(quote='看得早一步，是情报的全部价值所在。',
              issue='2026年第3期', date='2026年7月',
              unit='无人体系中心 科技情报组（鸿眼）',
              classification='非密·内部资料'):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm"
     viewBox="0 0 {W:.0f} {H:.0f}">
  <title>《析光》封底 {issue}</title>
  <rect width="{W}" height="{H}" fill="{NAVY}"/>
  <g id="网格" stroke="{ACCENT}" stroke-width="0.15" opacity="0.13">
    {_grid().split('>', 1)[1].rsplit('</g>', 1)[0]}
  </g>

  {load_mark(scale=44, dx=(W - 44) / 2, dy=64)}

  <g id="金句">
    <line x1="{W / 2 - 18}" y1="132" x2="{W / 2 + 18}" y2="132"
          stroke="{BRASS}" stroke-width="0.8"/>
    <text x="{W / 2}" y="152" text-anchor="middle" font-family={FONT_S!r}
          font-size="8" fill="{CREAM}">{quote}</text>
    <text x="{W / 2}" y="166" text-anchor="middle" font-family={FONT!r}
          font-size="4.2" letter-spacing="2.4" fill="{BRASS}">看得早 · 看得懂 · 看得准 · 看得透</text>
  </g>

  <g id="编制信息" fill="{CREAM}" opacity=".78" font-family={FONT!r} font-size="3.6">
    <line x1="{M}" y1="248" x2="{W - M}" y2="248" stroke="{BRASS}"
          stroke-width="0.4" opacity=".6"/>
    <text x="{M}" y="257">编制：{unit}</text>
    <text x="{M}" y="264">期次：《析光》{issue} · {date}</text>
    <text x="{M}" y="271">密级：{classification}　　仅供内部研究参考，请勿外传</text>
  </g>

  <text x="{W / 2}" y="285" text-anchor="middle" font-family={FONT!r}
        font-size="3.4" letter-spacing="2" fill="{BRASS}"
        opacity=".85">鸿眼 HONGEYE ｜ 析光 XIGUANG</text>
</svg>
'''


def render(svg_path, png_path, px_width=1400):
    """SVG -> PNG 校样。用 HTML 壳包一层再截元素，直接 goto SVG 会超时。"""
    from playwright.sync_api import sync_playwright
    with open(svg_path, encoding='utf-8') as f:
        svg = f.read()
    svg = svg.replace('width="210mm"', 'width="%dpx"' % px_width, 1)
    svg = svg.replace('height="297mm"',
                      'height="%dpx"' % int(px_width * H / W), 1)
    html = ('<body style="margin:0;background:#888">' + svg + '</body>')
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': px_width,
                                  'height': int(px_width * H / W)},
                        device_scale_factor=2)
        pg.set_content(html)
        pg.wait_for_timeout(500)
        pg.query_selector('svg').screenshot(path=png_path)
        b.close()
    return png_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--issue', default='2026年第3期')
    ap.add_argument('--date', default='2026年7月')
    ap.add_argument('--title', default='本期专题标题')
    ap.add_argument('--lead', default='一句导语')
    ap.add_argument('--toc', nargs='*', default=[])
    ap.add_argument('--quote', default='看得早一步，是情报的全部价值所在。')
    ap.add_argument('--classification', default='非密·内部资料')
    ap.add_argument('--out', default='.')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    jobs = [('cover.svg', make_cover(a.issue, a.date, a.title, a.lead,
                                     a.toc, a.classification)),
            ('back.svg', make_back(a.quote, a.issue, a.date,
                                   classification=a.classification))]
    for name, svg in jobs:
        p = os.path.join(a.out, name)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(svg)
        render(p, p.replace('.svg', '.png'))
        print('written:', p, '+ png')


if __name__ == '__main__':
    main()
