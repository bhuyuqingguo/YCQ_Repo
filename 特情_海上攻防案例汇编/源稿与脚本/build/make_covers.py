import sys
sys.path.insert(0, 'scripts')
import xiguang_cover as xc
from PIL import ImageFont, Image, ImageDraw
_o = xc.font
xc.font = lambda p, s: (ImageFont.truetype(p, s, index=2) if p.endswith('.ttc') else _o(p, s))

ISSUE = '特 情 · 2026 年 10 月'
ORG = '无人体系中心 · 鸿眼科情团队'
cov = xc.make_cover('cover.png',
    title=['海上岛屿·港口·小岛·远海编组', '遭袭与防卫案例汇编'],
    subtitle='全球典型案例集（2023—2026）',
    issue=ISSUE, org=ORG)
# 特情标签：藏青底白字，置于下金线之下
im = Image.open('cover.png'); d = ImageDraw.Draw(im)
f = xc.font(xc.F_BOLD, 44)
x0, y0, x1, y1 = 750-120, 1580, 750+120, 1660
d.rectangle([x0, y0, x1, y1], fill=xc.NAVY)
xc.tracked(d, (750, 1636), '特　情', f, (255,255,255), target_w=150, anchor='ms')
im.save('cover.png')
xc.make_back('back.png', issue='特 情', date='2026 年 10 月', org=ORG)
print('ok')
