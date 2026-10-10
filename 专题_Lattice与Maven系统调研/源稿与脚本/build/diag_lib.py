# -*- coding: utf-8 -*-
"""自绘示意图基座：沿用《析光》调色板与按路径绑定的 CJK 字体，提供方框/箭头/分层等原语。"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
XG = os.path.abspath(os.path.join(HERE, '..', '..', '..', '特情_海上攻防案例汇编', '源稿与脚本', 'build'))
sys.path.insert(0, os.path.join(XG, 'scripts'))
sys.path.insert(0, XG)
from xiguang_figs import FP, FPB, PAL, plt  # noqa
import matplotlib.patches as mp  # noqa
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch  # noqa

FIGDIR = os.path.abspath(os.path.join(HERE, '..', 'figs'))
os.makedirs(FIGDIR, exist_ok=True)

NAVY, ACC, BRASS, ALERT, GREY, CREAM = PAL['navy'], PAL['accent'], PAL['brass'], PAL['alert'], PAL['grey'], PAL['cream']
GREEN = '#1F8A70'
PURPLE = '#6A4FA3'
LAT = '#2E93D6'   # Lattice / Anduril 主色
MAV = '#C0392B'   # Maven / Palantir 主色
JOINT = '#A8842F'  # 联合/政府
LIGHT = {LAT: '#DCEBF7', MAV: '#F6DEDA', JOINT: '#F1E7CF', NAVY: '#DDE2EA', GREEN: '#D7EEE6',
         PURPLE: '#E6E0F1', GREY: '#ECE8DE'}


def canvas(w=7.6, h=4.6, xlim=(0, 100), ylim=(0, 60)):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    fig.patch.set_facecolor(CREAM)
    ax.set_facecolor(CREAM)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axis('off')
    return fig, ax


def box(ax, x, y, w, h, text='', fc='white', ec=NAVY, size=7.5, bold=False, color=None, lw=0.9,
        r=0.8, ha='center', va='center', pad=1.2, ls='-', alpha=1.0, z=2):
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=%s' % r, fc=fc, ec=ec, lw=lw,
                       ls=ls, alpha=alpha, zorder=z)
    ax.add_patch(p)
    t = None
    if text:
        tx = x + w / 2 if ha == 'center' else (x + pad if ha == 'left' else x + w - pad)
        ty = y + h / 2 if va == 'center' else (y + h - pad if va == 'top' else y + pad)
        t = ax.text(tx, ty, text, fontproperties=(FPB(size) if bold else FP(size)), color=color or NAVY,
                    ha=ha, va=va, zorder=z + 1, linespacing=1.35)
        t._xg_box = p
    return p


def text(ax, x, y, s, size=7.5, bold=False, color=None, ha='center', va='center', z=5, rot=0, **kw):
    return ax.text(x, y, s, fontproperties=(FPB(size) if bold else FP(size)), color=color or NAVY,
                   ha=ha, va=va, zorder=z, rotation=rot, linespacing=1.35, **kw)


def arrow(ax, x0, y0, x1, y1, color=GREY, lw=1.0, style='-|>', ms=8, ls='-', rad=0.0, z=4):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                        linestyle=ls, connectionstyle='arc3,rad=%s' % rad, zorder=z,
                        shrinkA=0, shrinkB=0)
    ax.add_patch(a)
    return a


def tag(ax, x, y, s, color=ALERT, size=6.5):
    ax.text(x, y, s, fontproperties=FPB(size), color='white', ha='center', va='center', zorder=6,
            bbox=dict(boxstyle='round,pad=0.25', fc=color, ec='none'))


OVERLAP_LOG = []


def check_overlap(fig, name, tol=1.0):
    """排版质检：文字与文字互相遮挡、文字溢出所在方框、文字超出画布，均记录告警。"""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    items = []
    for ax in fig.axes:
        ticks = []
        if ax.axison:
            for axis in (ax.xaxis, ax.yaxis):
                for tk in axis.get_major_ticks():
                    for lab in (tk.label1, tk.label2):
                        if tk.get_visible() and lab.get_visible() and lab.get_text():
                            ticks.append(lab)
        for t in ax.texts + ticks:
            if not t.get_visible() or not t.get_text().strip():
                continue
            items.append((t, t.get_window_extent(r)))
        for t in ax.texts:
            bp = getattr(t, '_xg_box', None)
            if bp is not None:
                bb, pb = t.get_window_extent(r), bp.get_window_extent(r)
                if bb.x0 < pb.x0 - tol or bb.x1 > pb.x1 + tol or bb.y0 < pb.y0 - tol or bb.y1 > pb.y1 + tol:
                    OVERLAP_LOG.append((name, '溢出方框', t.get_text()[:24]))
    for t in fig.texts:
        items.append((t, t.get_window_extent(r)))
    for ax in fig.axes:
        ps = [q for q in ax.patches if isinstance(q, FancyBboxPatch) and q.get_visible()]
        bbs = [q.get_window_extent(r) for q in ps]
        for i in range(len(ps)):
            for j in range(i + 1, len(ps)):
                a, b = bbs[i], bbs[j]
                inter = a.x0 < b.x1 - tol and b.x0 < a.x1 - tol and a.y0 < b.y1 - tol and b.y0 < a.y1 - tol
                contain = (a.x0 <= b.x0 + tol and a.x1 >= b.x1 - tol and a.y0 <= b.y0 + tol and a.y1 >= b.y1 - tol) or \
                          (b.x0 <= a.x0 + tol and b.x1 >= a.x1 - tol and b.y0 <= a.y0 + tol and b.y1 >= a.y1 - tol)
                if inter and not contain and not getattr(ps[i], '_xg_free', False) and not getattr(ps[j], '_xg_free', False):
                    OVERLAP_LOG.append((name, '方框互压', '%d⟂%d' % (i, j)))
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i][1], items[j][1]
            if items[i][0].get_text() == items[j][0].get_text() and abs(a.x0 - b.x0) < 1 and abs(a.y0 - b.y0) < 1:
                continue
            if a.x0 < b.x1 - tol and b.x0 < a.x1 - tol and a.y0 < b.y1 - tol and b.y0 < a.y1 - tol:
                OVERLAP_LOG.append((name, '文字互压', items[i][0].get_text()[:20] + ' ⟂ ' + items[j][0].get_text()[:20]))


def save(fig, name):
    check_overlap(fig, name)
    p = os.path.join(FIGDIR, name)
    fig.savefig(p, facecolor=CREAM, bbox_inches='tight', pad_inches=0.06, dpi=200)
    plt.close(fig)
    return p
