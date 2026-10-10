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
    if text:
        tx = x + w / 2 if ha == 'center' else (x + pad if ha == 'left' else x + w - pad)
        ty = y + h / 2 if va == 'center' else (y + h - pad if va == 'top' else y + pad)
        ax.text(tx, ty, text, fontproperties=(FPB(size) if bold else FP(size)), color=color or NAVY,
                ha=ha, va=va, zorder=z + 1, linespacing=1.35)
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


def save(fig, name):
    p = os.path.join(FIGDIR, name)
    fig.savefig(p, facecolor=CREAM, bbox_inches='tight', pad_inches=0.06, dpi=200)
    plt.close(fig)
    return p
