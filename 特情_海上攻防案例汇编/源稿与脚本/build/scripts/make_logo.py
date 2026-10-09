# -*- coding: utf-8 -*-
"""
鸿眼 HONGEYE 品牌标 —— 参数化可编辑 SVG 生成器

生成三件：
    hongyan_mark.svg        标志本体（透明底，浅色版）
    hongyan_mark_dark.svg   深色底版（藏青底反白）
    hongyan_lockup.svg      标志 + 鸿眼 HONGEYE + 析光 XIGUANG 组合锁版

设计语义：
    外环双弧（飞鸿蓝 + 黄铜金）  = 双旋涡视野环，左右开口构成"眼"
    内侧双短弧                   = 旋涡尾，交代旋转方向
    中央飞翼剪影                 = 飞翼隐身轰炸机，藏青
    环上橙色节点 + 脉冲圈        = 预警指示

改色只改 SVG 顶部 <style> 里的 CSS 变量；改粗细改 --w-ring / --w-tail；
改飞翼大小改本脚本的 WING_SPAN 后重跑。
"""
import math
import os

CX = CY = 256.0
R_RING = 196.0      # 外环半径
W_RING = 16.0       # 外环线宽
R_TAIL = 132.0      # 旋涡尾半径
W_TAIL = 9.0        # 旋涡尾线宽
WING_SPAN = 150.0   # 飞翼半展长
WARN_DEG = 52.0     # 预警节点角位

PAL = dict(navy='#12233B', accent='#2E93D6', brass='#A8842F',
           warn='#E08A2E', cream='#F7F4EC', grey='#8A8474')


def pt(deg, r):
    """极坐标 -> SVG 坐标（y 轴向下）。"""
    a = math.radians(deg)
    return (CX + r * math.cos(a), CY - r * math.sin(a))


def arc(d0, d1, r, sweep):
    """输出 M...A... 弧线路径。sweep=0 屏幕逆时针，1 顺时针。"""
    x0, y0 = pt(d0, r)
    x1, y1 = pt(d1, r)
    large = 1 if abs(d1 - d0) > 180 else 0
    return ('M %.2f %.2f A %.2f %.2f 0 %d %d %.2f %.2f'
            % (x0, y0, r, r, large, sweep, x1, y1))


def wing_path(span=WING_SPAN):
    """飞翼剪影：机头在上，后缘双 W 折线，左右镜像。"""
    k = span / 150.0
    half = [(150, 44), (118, 16), (80, 50), (40, 20)]   # 右半：翼尖->后缘折点
    nose = (CX, CY - 96 * k)
    rear = (CX, CY + 56 * k)
    pts = [nose]
    pts += [(CX + x * k, CY + y * k) for x, y in half]
    pts += [rear]
    pts += [(CX - x * k, CY + y * k) for x, y in reversed(half)]
    return 'M ' + ' L '.join('%.2f %.2f' % p for p in pts) + ' Z'


STYLE = """
  <style>
    svg {
      --navy:   %(navy)s;   /* 藏青 · 飞翼主体 */
      --accent: %(accent)s; /* 飞鸿蓝 · 上弧 */
      --brass:  %(brass)s;  /* 黄铜金 · 下弧 */
      --warn:   %(warn)s;   /* 预警橙 · 指示节点 */
      --w-ring: %(wring).1f;
      --w-tail: %(wtail).1f;
    }
    .ring { fill:none; stroke-linecap:round; stroke-width:var(--w-ring); }
    .tail { fill:none; stroke-linecap:round; stroke-width:var(--w-tail); }
    .ring-up   { stroke:var(--accent); }
    .ring-down { stroke:var(--brass); }
    .tail-up   { stroke:var(--accent); opacity:.85; }
    .tail-down { stroke:var(--brass);  opacity:.85; }
    .wing      { fill:var(--navy); }
    .warn-dot  { fill:var(--warn); }
    .warn-ping { fill:none; stroke:var(--warn); stroke-width:2.5; opacity:.4; }
  </style>
"""


def build_mark(dark=False, bg=None):
    p = dict(PAL)
    if dark:
        p['navy'] = PAL['cream']          # 深色底上飞翼反白
    style = STYLE % dict(navy=p['navy'], accent=p['accent'], brass=p['brass'],
                         warn=p['warn'], wring=W_RING, wtail=W_TAIL)
    wx, wy = pt(WARN_DEG, R_RING)
    bg_rect = ''
    if bg:
        bg_rect = '  <rect id="bg" width="512" height="512" fill="%s"/>\n' % bg
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"
     width="512" height="512" role="img" aria-label="鸿眼 HONGEYE">
  <title>鸿眼 HONGEYE 品牌标</title>
{style}
{bg_rect}  <g id="视野环">
    <path class="ring ring-down" d="{arc(200, 340, R_RING, 0)}"/>
    <path class="ring ring-up"   d="{arc(20, 160, R_RING, 0)}"/>
  </g>
  <g id="旋涡尾">
    <path class="tail tail-down" d="{arc(345, 310, R_TAIL, 1)}"/>
    <path class="tail tail-up"   d="{arc(165, 130, R_TAIL, 1)}"/>
  </g>
  <g id="飞翼">
    <path class="wing" d="{wing_path()}"/>
  </g>
  <g id="预警指示">
    <circle class="warn-ping" cx="{wx:.2f}" cy="{wy:.2f}" r="25"/>
    <circle class="warn-dot"  cx="{wx:.2f}" cy="{wy:.2f}" r="13"/>
  </g>
</svg>
'''


def build_lockup(dark=False):
    """组合锁版：标志 + 鸿眼 HONGEYE + 析光 XIGUANG。"""
    ink = PAL['cream'] if dark else PAL['navy']
    sub = PAL['brass']
    mark = build_mark(dark=dark)
    inner = mark.split('>', 1)[1].rsplit('</svg>', 1)[0]
    bg = ('  <rect width="512" height="700" fill="%s"/>\n' % PAL['navy']) if dark else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 700"
     width="512" height="700" role="img" aria-label="鸿眼 析光 组合标">
  <title>鸿眼·析光 组合锁版</title>
{bg}  <g id="标志" transform="translate(0,10) scale(0.92) translate(22,0)">
{inner}
  </g>
  <g id="文字" text-anchor="middle"
     font-family="'黑体','SimHei','Noto Sans CJK SC',sans-serif">
    <text x="256" y="565" font-size="76" font-weight="700"
          letter-spacing="10" fill="{ink}">鸿眼</text>
    <text x="256" y="606" font-size="23" letter-spacing="11"
          fill="{sub}">HONGEYE</text>
    <line x1="146" y1="632" x2="366" y2="632" stroke="{sub}"
          stroke-width="1.5" opacity=".6"/>
    <text x="256" y="666" font-size="21" letter-spacing="6"
          fill="{ink}" opacity=".85">析光 XIGUANG · 科研情报</text>
  </g>
</svg>
'''


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    files = {
        'hongyan_mark.svg':      build_mark(dark=False),
        'hongyan_mark_dark.svg': build_mark(dark=True, bg=PAL['navy']),
        'hongyan_lockup.svg':    build_lockup(dark=False),
    }
    for name, svg in files.items():
        path = os.path.join(outdir, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(svg)
        print('written:', path)


if __name__ == '__main__':
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
