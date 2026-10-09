# -*- coding: utf-8 -*-
"""自绘图：析光调色板、按路径绑定 CJK 字体。"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scripts'))
from xiguang_figs import FP, FPB, PAL, plt  # noqa
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
from mpl_toolkits.basemap import Basemap
import datetime as dt
import numpy as np

CATCOL = {'岛屿防卫': '#2E93D6', '周边港口': '#C0392B', '海上小岛': '#A8842F', '远海机动编组': '#6A4FA3'}
SEA = '#DCE9F2'
LAND = '#EFEBDF'
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figs')
os.makedirs(FIGDIR, exist_ok=True)


def fpath(name):
    return os.path.join(FIGDIR, name)


def save(fig, name):
    p = fpath(name)
    fig.savefig(p, facecolor=PAL['cream'], bbox_inches='tight', pad_inches=0.08, dpi=200)
    plt.close(fig)
    return p


def basemap(ax, box, res='i', grid=None):
    lat0, lat1, lon0, lon1 = box
    m = Basemap(projection='merc', llcrnrlat=lat0, urcrnrlat=lat1, llcrnrlon=lon0, urcrnrlon=lon1,
                resolution=res, ax=ax)
    m.drawmapboundary(fill_color=SEA, linewidth=0.6, color=PAL['grey'])
    m.fillcontinents(color=LAND, lake_color=SEA)
    m.drawcoastlines(linewidth=0.45, color='#8A8474')
    m.drawcountries(linewidth=0.35, color='#B5AE9C')
    if grid:
        m.drawparallels(np.arange(-80, 90, grid), linewidth=0.2, color='#C9C2B0', labels=[1, 0, 0, 0],
                        fontsize=6.5, textcolor=PAL['grey'])
        m.drawmeridians(np.arange(-180, 180, grid), linewidth=0.2, color='#C9C2B0', labels=[0, 0, 0, 1],
                        fontsize=6.5, textcolor=PAL['grey'])
    return m


def label(ax, x, y, s, size=8, color=None, dx=0, dy=0, ha='left', va='center', bold=False, box=True):
    kw = {}
    if box:
        kw['bbox'] = dict(boxstyle='round,pad=0.15', fc=(1, 1, 1, 0.72), ec='none')
    ax.text(x + dx, y + dy, s, fontproperties=(FPB(size) if bold else FP(size)),
            color=color or PAL['navy'], ha=ha, va=va, zorder=6, **kw)


def legend_cats(ax, cats=None, loc='lower left', size=8, title=None):
    cats = cats or list(CATCOL)
    hs = [plt.Line2D([], [], marker='o', ls='', color=CATCOL[c], markersize=6, label=c) for c in cats]
    lg = ax.legend(handles=hs, loc=loc, frameon=True, prop=FP(size), title=title)
    lg.get_frame().set_facecolor('white'); lg.get_frame().set_alpha(0.85); lg.get_frame().set_edgecolor('#C9C2B0')
    if title:
        lg.get_title().set_fontproperties(FPB(size))
    return lg


def new_fig(w=7.2, h=4.2):
    fig, ax = plt.subplots(figsize=(w, h), dpi=200)
    fig.patch.set_facecolor(PAL['cream'])
    ax.set_facecolor(PAL['cream'])
    return fig, ax


def style_axes(ax, ygrid=True):
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(PAL['grey']); ax.spines[s].set_linewidth(0.7)
    ax.tick_params(colors=PAL['grey'], labelsize=7.5)
    if ygrid:
        ax.grid(axis='y', color=PAL['grid'], linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontproperties(FP(7.5))
