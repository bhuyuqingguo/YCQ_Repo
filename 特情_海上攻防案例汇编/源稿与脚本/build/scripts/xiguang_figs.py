# -*- coding: utf-8 -*-
"""
《析光》图表生成基座 —— CJK 字体硬绑定 + 定版调色板

⚠️ 唯一可靠的中文渲染方式：按【文件路径】构造 FontProperties，
   并逐元素传 fontproperties=。依赖 rcParams['font.family'] 或
   family='Noto Sans CJK SC' 会因字体缓存解析失败而出豆腐块。

用法：
    from xiguang_figs import FP, FPB, FPS, PAL, new_ax, save
    fig, ax = new_ax(figsize=(9, 4.5))
    ax.set_title('研制进度', fontproperties=FPB(15), color=PAL['navy'])
    ax.text(1, 2, '首飞', fontproperties=FP(11))
    save(fig, 'fig1.png')

表格也走这里：用 table_fig() 渲染为图，不要用 Word 原生表格。
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# ---------- 字体文件（按路径硬绑定） ----------
SANS = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
SANS_BOLD = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
SERIF = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'

for _f in (SANS, SANS_BOLD, SERIF):
    try:
        fm.fontManager.addfont(_f)
    except Exception:
        pass


def FP(size=11):
    """常规无衬线中文。"""
    return fm.FontProperties(fname=SANS, size=size)


def FPB(size=13):
    """加粗无衬线中文（标题）。"""
    return fm.FontProperties(fname=SANS_BOLD, size=size)


def FPS(size=11):
    """衬线中文（引文类）。"""
    return fm.FontProperties(fname=SERIF, size=size)


# ---------- 定版调色板 ----------
PAL = {
    'cream':  '#F7F4EC',
    'grid':   '#E9E4D6',
    'navy':   '#12233B',
    'accent': '#2E93D6',
    'brass':  '#A8842F',
    'alert':  '#C0392B',
    'grey':   '#8A8474',
    'white':  '#FFFFFF',
}
SERIES = [PAL['navy'], PAL['accent'], PAL['brass'], PAL['alert'], PAL['grey']]

plt.rcParams['axes.unicode_minus'] = False


def new_ax(figsize=(9, 4.5), dpi=200):
    """米色底画布，与版面同色，图表嵌入后浑然一体。"""
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(PAL['cream'])
    ax.set_facecolor(PAL['cream'])
    for s in ('top', 'right'):
        ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'):
        ax.spines[s].set_color(PAL['grey'])
        ax.spines[s].set_linewidth(0.8)
    ax.tick_params(colors=PAL['grey'], labelsize=9)
    ax.grid(axis='y', color=PAL['grid'], linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    return fig, ax


def apply_ticks(ax, xlabels=None, ylabels=None, size=10):
    """刻度标签也必须逐个绑字体，否则中文刻度出豆腐块。"""
    if xlabels is not None:
        ax.set_xticks(range(len(xlabels)))
        ax.set_xticklabels(xlabels, fontproperties=FP(size), color=PAL['navy'])
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_fontproperties(FP(size - 1))


def table_fig(headers, rows, col_widths=None, figsize=None, dpi=200):
    """把表格渲染成图（定版要求：不用 Word 原生表格）。"""
    n = len(rows) + 1
    figsize = figsize or (9, 0.42 * n + 0.4)
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor(PAL['cream'])
    ax.axis('off')
    t = ax.table(cellText=rows, colLabels=headers, loc='center',
                 cellLoc='center', colWidths=col_widths)
    t.auto_set_font_size(False)
    for (r, c), cell in t.get_celld().items():
        cell.set_edgecolor(PAL['grid'])
        cell.set_linewidth(0.8)
        txt = cell.get_text()
        if r == 0:
            cell.set_facecolor(PAL['navy'])
            txt.set_color(PAL['white'])
            txt.set_fontproperties(FPB(10))
        else:
            cell.set_facecolor(PAL['white'] if r % 2 else PAL['cream'])
            txt.set_color('#222222')
            txt.set_fontproperties(FP(9.5))
        cell.set_height(0.42 / (0.42 * n + 0.4) * 1.6)
    fig.tight_layout(pad=0.3)
    return fig


def save(fig, path):
    fig.savefig(path, facecolor=PAL['cream'], bbox_inches='tight', pad_inches=0.12)
    plt.close(fig)
    return path
