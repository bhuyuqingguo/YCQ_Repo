# -*- coding: utf-8 -*-
"""
《析光》封面/封底生成器 —— 对齐创刊号 V7 封面 / V4 封底

版式常数全部由创刊号原件逐像素实测标定（见 references/版式规范.md 第八节）。
画布 1500×2120（A4 比例，约 181dpi），米色纸底 + 100px 浅网格。

用法：
    from xiguang_cover import make_cover, make_back
    make_cover('封面.png',
               title=['帕兰提尔(Palantir)', '深度调研分析'],
               subtitle='军工企业智能转型战略参考',
               issue='第 一 期')
    make_back('封底.png', issue='第 一 期', date='2026 年 7 月')

设计原则：字号固定、**字距按目标宽度求解**（fit_track），因此换标题、换期次
后版心宽度仍与创刊号一致，不会因字数变化而破版。
字体一律按文件路径硬绑定，禁止依赖字体名解析。
"""
import os

from PIL import Image, ImageDraw, ImageFont

# ---------- 画布 ----------
W, H = 1500, 2120
MARGIN = 108
GRID_STEP, GRID_W = 100, 2

# ---------- 实测色值 ----------
CREAM = (247, 244, 236)
GRID = (239, 236, 228)
NAVY = (18, 35, 59)
ACCENT = (46, 147, 214)
BRASS = (168, 132, 47)
GREY = (138, 132, 116)
FAINT = (212, 208, 197)
TICK = (126, 142, 156)

# ---------- 字体（按路径硬绑定） ----------
FDIR = '/usr/share/fonts/opentype/noto/'
F_BLACK = FDIR + 'NotoSansCJK-Black.ttc'
F_BOLD = FDIR + 'NotoSansCJK-Bold.ttc'
F_MED = FDIR + 'NotoSansCJK-Medium.ttc'
F_REG = FDIR + 'NotoSansCJK-Regular.ttc'

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    '..', 'assets', 'hongyan_logo.png')


def font(path, size):
    return ImageFont.truetype(path, size)


def canvas():
    im = Image.new('RGB', (W, H), CREAM)
    d = ImageDraw.Draw(im)
    for x in range(0, W, GRID_STEP):
        d.rectangle([x, 0, x + GRID_W - 1, H], fill=GRID)
    for y in range(0, H, GRID_STEP):
        d.rectangle([0, y, W, y + GRID_W - 1], fill=GRID)
    return im, d


def fit_track(d, text, f, target_w):
    """求解字距，使整行展开后正好等于目标宽度。"""
    base = sum(d.textlength(c, font=f) for c in text)
    n = max(len(text) - 1, 1)
    return (target_w - base) / n


def tracked(d, xy, text, f, fill, track=0, anchor='ls', target_w=None):
    """字距展开绘制。anchor: ls 左 / rs 右 / ms 居中。返回实际总宽。"""
    if target_w is not None:
        track = fit_track(d, text, f, target_w)
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + track * (len(text) - 1)
    x, y = xy
    if anchor == 'rs':
        x -= total
    elif anchor == 'ms':
        x -= total / 2.0
    for c, w in zip(text, widths):
        d.text((x, y), c, font=f, fill=fill, anchor='ls')
        x += w + track
    return total


def paste_logo(im, cx, cy, ring_r=100, reticle=False):
    """鸿眼标。资产环半径 100（画布 224，中心 112）。
    reticle=True 时加十字瞄准刻线：跨环绘制，半径 ring_r-7 到 ring_r+7。"""
    logo = Image.open(LOGO).convert('RGBA')
    side = int(round(224 * ring_r / 100.0))
    logo = logo.resize((side, side), Image.LANCZOS)
    im.paste(logo, (int(cx - side / 2), int(cy - side / 2)), logo)
    if reticle:
        d = ImageDraw.Draw(im)
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            d.line([cx + dx * (ring_r - 7), cy + dy * (ring_r - 7),
                    cx + dx * (ring_r + 7), cy + dy * (ring_r + 7)],
                   fill=TICK, width=2)


def prism_beams(im, focus=(745, 1055)):
    """棱镜分光光带（封面主视觉）。极低透明度长三角，自焦点散开，
    透明度经比对原件下调——光带只应是气氛，不得压过文字。"""
    layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fx, fy = focus
    beams = [
        (-260, -420, 130, (46, 147, 214, 14)),
        (-120, -700, 70, (168, 132, 47, 8)),
        (1900, -60, 46, (46, 147, 214, 23)),
        (1980, 120, 34, (192, 57, 43, 17)),
        (1900, 300, 40, (168, 132, 47, 15)),
        (1500, 900, 52, (46, 147, 214, 15)),
        (1180, 1300, 30, (46, 147, 214, 20)),
    ]
    for ex, ey, hw, rgba in beams:
        d.polygon([(fx, fy), (ex, ey - hw), (ex, ey + hw)], fill=rgba)
    im.paste(Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB'),
             (0, 0))


# ================= 封面 =================
def make_cover(path, title, subtitle=None, issue='第 一 期',
               masthead='XIGUANG · INTELLIGENCE QUARTERLY',
               org='主办 · 无人体系中心 · 鸿眼科情团队',
               motto='看得早 · 看得懂 · 看得准 · 看得透',
               beams=True):
    """title: 1–2 行字符串列表；超过 2 行请自行断行取前两行。"""
    if isinstance(title, str):
        title = [title]
    im, _ = canvas()
    if beams:
        prism_beams(im)
    d = ImageDraw.Draw(im)

    # --- 顶栏 ---
    tracked(d, (MARGIN, 93), masthead, font(F_MED, 19), GREY, target_w=562)
    tracked(d, (W - MARGIN - 4, 93), issue, font(F_MED, 19), GREY, track=11,
            anchor='rs')
    d.rectangle([MARGIN, 126, W - MARGIN, 127], fill=NAVY)

    # --- 刊名区 ---
    tracked(d, (134, 438), '析光', font(F_BLACK, 255), NAVY, track=112)
    tracked(d, (285, 530), '科研情报刊物', font(F_MED, 27), GREY, target_w=313)

    # --- 鸿眼标（带瞄准刻线） ---
    paste_logo(im, 1271, 327, ring_r=103, reticle=True)
    d = ImageDraw.Draw(im)

    # --- 专题标题区 ---
    # 字号自适应：长标题按版心宽度等比缩字，两行取同一字号保持齐整
    d.rectangle([690, 995, 809, 998], fill=BRASS)
    max_w = W - 2 * MARGIN - 100          # 版心内再留 50px 呼吸位
    tsize = 80
    for line in title[:2]:
        f = font(F_BOLD, 80)
        need = sum(d.textlength(c, font=f) for c in line) + 2 * (len(line) - 1)
        if need > max_w:
            tsize = min(tsize, max(46, int(80 * max_w / need)))
    for line, by in zip(title[:2], (1168, 1296)):
        tracked(d, (W // 2, by), line, font(F_BOLD, tsize), NAVY, track=2,
                anchor='ms')
    if subtitle:
        ssize = 38
        f = font(F_MED, 38)
        need = sum(d.textlength(c, font=f) for c in subtitle) \
            + 4 * (len(subtitle) - 1) + 176      # 含两侧短线与间隙
        if need > max_w:
            ssize = max(24, int(38 * max_w / need))
        f = font(F_MED, ssize)
        wsub = tracked(d, (W // 2, 1412), subtitle, f, ACCENT, track=4,
                       anchor='ms')
        half = wsub / 2.0
        d.line([W // 2 - half - 68, 1400, W // 2 - half - 20, 1400],
               fill=ACCENT, width=2)
        d.line([W // 2 + half + 20, 1400, W // 2 + half + 68, 1400],
               fill=ACCENT, width=2)
    d.rectangle([690, 1501, 809, 1504], fill=BRASS)

    # --- 底栏 ---
    tracked(d, (MARGIN, 1920), masthead, font(F_REG, 19), FAINT, target_w=562)
    tracked(d, (W - MARGIN - 4, 1920), issue, font(F_REG, 19), FAINT, track=11,
            anchor='rs')
    d.rectangle([MARGIN, 1986, W - MARGIN, 1987], fill=NAVY)
    tracked(d, (MARGIN, 2043), org, font(F_MED, 25), GREY, target_w=452)
    tracked(d, (W - MARGIN, 2043), motto, font(F_BOLD, 25), BRASS,
            target_w=464, anchor='rs')

    im.save(path)
    return path


# ================= 封底 =================
def make_back(path, issue='第 一 期', date='2026 年 7 月',
              motto_lines=('看得早  ·  看得懂', '看得准  ·  看得透'),
              title='析光 · 科研情报刊物',
              org='主办 · 无人体系中心 · 鸿眼科情团队'):
    im, _ = canvas()
    paste_logo(im, 750, 856, ring_r=100, reticle=False)
    d = ImageDraw.Draw(im)

    f = font(F_BLACK, 52)
    for line, by in zip(motto_lines, (1144, 1254)):
        tracked(d, (W // 2, by), line, f, NAVY, target_w=512, anchor='ms')

    d.rectangle([706, 1738, 794, 1739], fill=BRASS)
    tracked(d, (W // 2, 1810), title, font(F_BOLD, 26), NAVY,
            target_w=311, anchor='ms')
    tracked(d, (W // 2, 1864), org, font(F_MED, 22), GREY,
            target_w=446, anchor='ms')
    tracked(d, (W // 2, 1918), '%s · %s' % (issue, date), font(F_MED, 22),
            GREY, target_w=291, anchor='ms')

    im.save(path)
    return path


if __name__ == '__main__':
    make_cover('/tmp/cover_proof.png',
               title=['帕兰提尔(Palantir)', '深度调研分析'],
               subtitle='军工企业智能转型战略参考')
    make_back('/tmp/back_proof.png')
    print('proofs written')
