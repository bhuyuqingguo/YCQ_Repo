# -*- coding: utf-8 -*-
"""单篇精要：案例统计与威胁态势（析光单篇体例）"""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); os.chdir(HERE)
from collections import Counter
from digest_stats import load, TYPES
import build
from xgengine import DocxBuilder, WD_ALIGN_PARAGRAPH
from cases_lib import clean
from thumbs import thumb

cs = load(); N = len(cs)
pct = lambda a, b=N: '%d％' % round(100 * a / b)
YRS = ['2023', '2024', '2025', '2026']
REGS = ['黑海', '红海—亚丁湾', '南海', '台海及东北亚', '东南亚海峡', '波罗的海—北海', '波斯湾', '东地中海', '印度洋', '加勒比', '其他']
CATS = ['岛屿防卫', '周边港口', '海上小岛', '远海机动编组', '海上交通线']
cat = Counter(c['category'] for c in cs); reg = Counter(c['R'] for c in cs); yr = Counter(c['Y'] for c in cs)
out = Counter(c['O'] for c in cs); conf = Counter(c['confidence'][:1] for c in cs)
dom = Counter(d for c in cs for d in (c.get('domains') or [])); pat = Counter(p for c in cs for p in (c.get('patterns') or []))
TT = Counter(t for c in cs for t in c['T'])
hit = out['遭袭受损'] + out['被击沉/摧毁']; dfd = out['防御成功'] + out['部分拦截']
G = {'高强度动能打击': ['导弹与火力打击', '有人机空袭'], '无人化打击': ['无人机', '无人艇', '水下威胁'],
     '低强度与灰色地带': ['灰色地带施压', '封锁与扣押', '登临/劫持/登陆', '海底设施破坏']}
gsub = {g: [c for c in cs if c['T'] & set(ks)] for g, ks in G.items()}
uy = {y: sum(1 for c in gsub['无人化打击'] if c['Y'] == y) for y in YRS}
def catc(k, o): return sum(1 for c in cs if c['category'] == k and c['O'] in o)
multi = sum(1 for c in cs if len(c['T']) >= 2)

def region_rows():
    rows = []
    for r in REGS:
        sub = [c for c in cs if c['R'] == r]
        if not sub: continue
        cc = Counter(c['category'] for c in sub).most_common(2)
        tt = Counter(t for c in sub for t in c['T'] if t != '其他').most_common(3)
        oc = Counter(c['O'] for c in sub).most_common(1)[0]
        rows.append([r, '%d（%s）' % (len(sub), pct(len(sub))), '、'.join('%s%d' % (k, v) for k, v in cc),
                     '、'.join(k for k, _ in tt), '%s居多（%d/%d）' % (oc[0], oc[1], len(sub))])
    return rows

def threat_rows():
    rows = []
    for g, ks in G.items():
        for k in ks:
            sub = [c for c in cs if k in c['T']]
            rr = Counter(c['R'] for c in sub).most_common(2)
            oc = Counter(c['O'] for c in sub).most_common(2)
            rows.append([g, k, str(len(sub)), '、'.join('%s%d' % x for x in rr),
                         '；'.join('%s%s' % (o, pct(v, len(sub))) for o, v in oc)])
    return rows

def tbl(key, cap, src, widths, head, rows):
    s = '!table %s|%s|%s|%s\n%s\n' % (key, cap, src, ','.join(map(str, widths)), '|'.join(head))
    s += '\n'.join('|'.join(r) for r in rows) + '\n!end\n'
    return s


COUNTRY = [('菲律宾', ['菲律宾', '菲方', '菲海警', '菲军', 'PCG', 'BRP']), ('越南', ['越南', '越方']),
           ('马来西亚', ['马来西亚', '马方', 'Petronas', '南康']), ('印度尼西亚', ['印尼', '印度尼西亚', 'Bakamla', '纳土纳']),
           ('新加坡与马六甲海峡', ['新加坡', '马六甲', 'ReCAAP'])]
scs = [c for c in cs if c['R'] in ('南海', '东南亚海峡')]
def ctry(c):
    if c['R'] == '东南亚海峡':
        return '新加坡与马六甲海峡'
    k = c.get('case_key', '')
    if k.startswith(('vn_', 'paracel', 'vanguard', 'scs_vietnam')):
        return '越南'
    if k.startswith(('scs_natuna',)):
        return '印度尼西亚'
    if k.startswith(('scs_luconia', 'scs_layang')):
        return '马来西亚'
    t = (c.get('attacker') or '') + (c.get('defender') or '') + (c.get('title_cn') or '') + (c.get('location_cn') or '')
    for n, ks in COUNTRY:
        if any(k in t for k in ks):
            return n
    return '其他'
scs_c = Counter(ctry(c) for c in scs)
scs_text = ('南海及东南亚海峡方向共收录案例%d个，其中南海%d个、马六甲—新加坡海峡%d个。按涉事对象分：%s。'
            % (len(scs), sum(1 for c in scs if c['R'] == '南海'), sum(1 for c in scs if c['R'] == '东南亚海峡'),
               '，'.join('%s方向%d个' % (k, v) for k, v in scs_c.most_common())) +
            '这一方向的总体特征是：没有发生火力交战，攻防围绕岛礁补给、执法管辖、油气作业和海峡航运安全展开，'
            '手段以水炮、拦阻、碰撞、登临、抵近、岛礁吹填扩建、执法巡查和联合巡逻为主。结果中灰色地带对峙%d个、遭袭受损%d个。'
            '各案中中方与相关国家的口径差异较大，详细版汇编均已并列给出。' % (sum(1 for c in scs if c['O'] == '灰色地带对峙'), sum(1 for c in scs if c['O'] in ('遭袭受损', '被击沉/摧毁'))))
scs_rows = [[c['code'], (c.get('date_start') or '')[:10], ctry(c), clean(c.get('title_cn')), c['O']] for c in sorted(scs, key=lambda c: c.get('date_start') or '')]
scs_table = tbl('t_scs', '南海及东南亚海峡方向案例一览', '本报告整理', [14, 20, 26, 78, 22], ['编号', '日期', '方向', '案例', '结果'], scs_rows)
scene_desc = {'岛屿防卫': '集中在2026年，大岛遭远程火力打击、近岸小岛被夺占和岛屿周边灰色地带施压三种情形并存',
              '周边港口': '是数量最多、结果最差的一类，攻击方普遍以导弹、无人机打击港内停泊舰船和港口设施',
              '海上小岛': '以南海岛礁补给对峙和海底设施损伤为主，多数不发生火力交战',
              '远海机动编组': '防御成功占多数，被击沉的主要是黑海俄舰、伊朗"德纳"号等缺乏有效防空掩护的单舰',
              '海上交通线': '商船、油轮遇袭和被扣押，是编组护航任务量和港口封控效果的直接体现'}
scene_text = '\n\n'.join('**%s（%d个）**：%s；结果中%s。主要分布在%s，主要威胁为%s。' % (
    k, cat[k], scene_desc[k],
    '、'.join('%s%d个' % x for x in Counter(c['O'] for c in cs if c['category'] == k).most_common(3)),
    '、'.join(r for r, _ in Counter(c['R'] for c in cs if c['category'] == k).most_common(3)),
    '、'.join(t for t, _ in Counter(t for c in cs if c['category'] == k for t in c['T'] if t != '其他').most_common(3))) for k in CATS)
scene_rows = [[k, str(cat[k]), pct(catc(k, ('遭袭受损', '被击沉/摧毁')), cat[k]), pct(catc(k, ('防御成功', '部分拦截')), cat[k]),
               pct(catc(k, ('灰色地带对峙',)), cat[k])] for k in CATS]
scene_table = tbl('t_scene', '各场景结果比例', '本报告统计', [40, 24, 32, 32, 32], ['场景', '案例数', '攻方得手', '守方拦截', '灰色地带对峙'], scene_rows)
ATLAS_PLACEHOLDER = '\n# 四、典型案例实景图录\n\n以下按场景收录有公开照片的案例，每案一图。照片取自维基共享资源收录的各国军方、政府公开图片，多数为涉事舰艇、港口或装备的资料照片，并非事件现场，图注中注明。\n\n{{atlas}}\n'

black_sea_ports = sum(1 for c in cs if c['R'] == '黑海' and c['category'] == '周边港口')
red_fleet = sum(1 for c in cs if c['R'] == '红海—亚丁湾' and c['category'] == '远海机动编组')
red_fleet_ok = sum(1 for c in cs if c['R'] == '红海—亚丁湾' and c['category'] == '远海机动编组' and c['O'] in ('防御成功', '部分拦截'))
AP = ('南海', '台海及东北亚', '东南亚海峡')
ap_n = sum(1 for c in cs if c['R'] in AP)
ap_gray = sum(1 for c in cs if c['R'] in AP and c['O'] == '灰色地带对峙')
y26_gulf = sum(1 for c in cs if c['R'] == '波斯湾' and c['Y'] == '2026')

MD = f"""
:::lead
本精要从统计角度对我部《海上岛屿·港口·小岛·远海编组遭袭与防卫案例汇编（2023—2026）》所收录的{N}个案例作宏观归纳，回答三个问题：案例分布在哪里、各地是什么类型、威胁形势怎样分类和演变。总的看法是：**海上攻防的重心在向静止目标和无人化手段两个方向移动**。港口类案例中遭袭受损或被击沉、摧毁的占{pct(catc('周边港口', ('遭袭受损', '被击沉/摧毁')), cat['周边港口'])}，远海编组类案例中防御成功或部分拦截的占{pct(catc('远海机动编组', ('防御成功', '部分拦截')), cat['远海机动编组'])}；有无人平台参与的案例占比由2024年的{pct(uy['2024'], yr['2024'])}升至2026年前三季度的{pct(uy['2026'], yr['2026'])}。
:::

# 一、案例总体呈现

## （一）总量与构成

汇编共收录2023年1月至2026年9月的海上攻防案例{N}个。按场景分，周边港口{cat['周边港口']}个、远海机动编组{cat['远海机动编组']}个、海上交通线（商船遇袭，关联案例）{cat['海上交通线']}个、岛屿防卫{cat['岛屿防卫']}个、海上小岛（含礁、平台、离岸设施）{cat['海上小岛']}个。按年份分，2023年{yr['2023']}个、2024年{yr['2024']}个、2025年{yr['2025']}个、2026年1—9月{yr['2026']}个，2026年未满一年已接近2024年水平。按可信度分，A级（多源交叉印证）{conf['A']}个、B级{conf['B']}个、C级{conf['C']}个，A、B两级合计占{pct(conf['A'] + conf['B'])}，以下统计以全部案例为口径。

从结果看，攻击方得手（遭袭受损或被击沉、摧毁）的案例{hit}个，占{pct(hit)}；防御方成功或部分拦截的{dfd}个，占{pct(dfd)}；其余{out['灰色地带对峙']}个为未发生火力交战的灰色地带对峙，占{pct(out['灰色地带对峙'])}。

## （二）空间分布：两大主战场加七个方向

{{fig:d_world}}给出案例的全球分布。黑海{reg['黑海']}个、红海—亚丁湾{reg['红海—亚丁湾']}个，两地合计占{pct(reg['黑海'] + reg['红海—亚丁湾'])}，是三年来海上攻防的两个主战场；亚太方向合计{ap_n}个，其中南海{reg['南海']}个、台海及东北亚{reg['台海及东北亚']}个、马六甲—新加坡海峡{reg['东南亚海峡']}个；其余为波罗的海—北海{reg['波罗的海—北海']}个、波斯湾{reg['波斯湾']}个（其中{y26_gulf}个发生在2026年战争期间）、东地中海{reg['东地中海']}个、印度洋{reg['印度洋']}个、加勒比{reg['加勒比']}个，另有地中海中部、西非外海、红海西岸等零散案例{reg['其他']}个。

!fig d_world|f_world.png|案例全球分布（按场景着色、按结果区分符号）|本报告根据案例坐标绘制|158

## （三）各地类型：不同海域呈现不同的攻防形态

{{fig:d_region}}和{{tab:t_region}}给出各海域的场景构成、主要威胁类型和结果特征。可以把八个方向归为四种形态：

**港口攻防型：黑海。**黑海{reg['黑海']}个案例中周边港口类{black_sea_ports}个，攻防围绕塞瓦斯托波尔、新罗西斯克、敖德萨等港口展开，导弹、无人机、无人艇三类手段交替和组合使用，结果以遭袭受损和被击沉、摧毁为主。

**编组护航型：红海—亚丁湾。**该方向远海编组类案例{red_fleet}个，其中防御成功或部分拦截{red_fleet_ok}个；同时商船遇袭和港口遭空袭案例较多，形成"编队拦得住、商船和港口挨打"的格局。

**灰色地带型：亚太与波罗的海。**亚太方向{ap_n}个案例以岛屿防卫和海上小岛两类为主，其中{ap_gray}个为未交火的灰色地带对峙，手段以水炮、拦阻、碰撞、执法巡查和演习施压为主；波罗的海—北海以海底管线电缆损伤、无人机滋扰和影子船队拦检为主。

**高强度战争型：波斯湾与东地中海。**这两个方向的案例集中在2024年伊以互袭和2026年美以—伊朗战争期间，岛上基地、港口、能源设施和远海编组同时遭受导弹与无人机打击，水下布雷也在这里出现。印度洋、加勒比则以反海盗、封锁与扣押等低强度行动为主。

!fig d_region|d_region.png|各海域案例数量与场景构成|本报告统计|150

{tbl('t_region', '各海域案例构成与主要特征', '本报告统计（主要威胁类型按涉及案例数排序，一个案例可涉及多类）', [26, 22, 38, 42, 32], ['海域', '案例数（占比）', '主要场景', '主要威胁类型', '结果特征'], region_rows())}


## （四）时间分布：季度走势与年度—海域矩阵

{{fig:d_quarter}}按季度给出案例数及四个主要海域的走势，{{fig:d_year_region}}给出年度—海域矩阵。黑海在2023年三季度和2026年三季度两次出现高峰，红海在2024年一季度达到高峰后回落，波斯湾的案例几乎全部集中在2026年。

!fig d_quarter|d_quarter.png|案例季度走势（按起始日期）|本报告统计|158

!fig d_year_region|d_year_region.png|年度—海域案例分布矩阵|本报告统计|130

## （五）南海及东南亚方向

{scs_text}

!fig d_scs|f_scs.png|南海及东南亚海峡方向案例分布|本报告根据案例坐标绘制|130

{scs_table}

## （六）主要海域分布图

以下给出黑海、红海—亚丁湾、东地中海与波斯湾、波罗的海四个方向的案例分布，图中标注为案例编号，与详细版汇编一致。

!fig d_bs|f_blacksea.png|黑海方向案例分布|本报告根据案例坐标绘制|150

!fig d_rs|f_redsea.png|红海—亚丁湾方向案例分布|本报告根据案例坐标绘制|125

!fig d_me|f_mideast.png|东地中海与波斯湾方向案例分布|本报告根据案例坐标绘制|150

!fig d_bal|f_baltic.png|波罗的海—北海方向案例分布|本报告根据案例坐标绘制|150

# 二、分场景统计

{{fig:d_scene_out}}给出五类场景的结果构成，{{fig:d_scene_threat}}给出场景与威胁类型的交叉统计。

!fig d_scene_out|f_outcome.png|各场景结果构成|本报告统计|150

!fig d_scene_threat|d_scene_threat.png|场景—威胁类型交叉统计|本报告统计（一个案例可涉及多类威胁）|158

{scene_text}

{scene_table}

# 三、威胁形势判断

## （一）威胁的分类

按攻击方使用的手段，把全部案例涉及的威胁归为三个层级、九种类型（一个案例可涉及多种类型）：

**高强度动能打击**，包括导弹与火力打击（弹道导弹、巡航导弹、火箭弹、迫击炮等）和有人机空袭，涉及案例{len(gsub['高强度动能打击'])}个；

**无人化打击**，包括无人机、无人艇和水下威胁（无人潜航器、水雷、鱼雷），涉及案例{len(gsub['无人化打击'])}个；

**低强度与灰色地带行动**，包括灰色地带施压（水炮、冲撞、拦阻、抵近、演习、执法巡查、电磁干扰）、封锁与扣押、登临/劫持/登陆、海底设施破坏，涉及案例{len(gsub['低强度与灰色地带'])}个。

{{tab:t_threat}}和{{fig:d_threat}}给出各类威胁的案例数、主要海域和结果构成。

{tbl('t_threat', '威胁分类统计', '本报告统计（一个案例可涉及多类威胁；结果特征列出最常见的两类结果及其占比）', [32, 32, 16, 42, 38], ['层级', '威胁类型', '涉及案例', '主要海域', '结果特征'], threat_rows())}

!fig d_threat|d_threat.png|各类威胁涉及案例数与结果构成|本报告统计|150

## （二）统计反映的五个特点

**第一，导弹与无人机是两大主体威胁，数量相当。**导弹与火力打击涉及{TT['导弹与火力打击']}个案例，无人机涉及{TT['无人机']}个，两者都远多于其他类型。两类威胁的结果构成不同：导弹类案例中防御成功{sum(1 for c in cs if '导弹与火力打击' in c['T'] and c['O']=='防御成功')}个、被击沉或摧毁{sum(1 for c in cs if '导弹与火力打击' in c['T'] and c['O']=='被击沉/摧毁')}个，拦截成功主要来自红海与东地中海编队对反舰导弹、弹道导弹的拦截，被毁则主要是港内舰艇；无人机类案例中遭袭受损{sum(1 for c in cs if '无人机' in c['T'] and c['O']=='遭袭受损')}个，接近一半，主要来自港口和岛上基地被突防，被击沉、摧毁的极少。

**第二，无人艇和水下手段数量不大，但致毁率最高。**无人艇涉及{TT['无人艇']}个案例，其中被击沉、摧毁的{sum(1 for c in cs if '无人艇' in c['T'] and c['O']=='被击沉/摧毁')}个，比例在各类威胁中最高；水下威胁仅{TT['水下威胁']}个案例，但包括无人潜航器突入军港、海峡布雷封锁和潜艇击沉水面舰等影响最大的事件。

**第三，组合使用成为常态。**{multi}个案例（占{pct(multi)}）涉及两类以上威胁；按组织形态统计，"集群"标签出现{pat['集群']}次，"异构"{pat['异构']}次，"偷袭/突防"{pat['偷袭/突防']}次，"饱和"{pat['饱和']}次，而有证据表明平台间自主协同的"蜂群"仅{pat['蜂群']}次。多平台同时投送已很普遍，真正意义上的自主蜂群公开证据仍然很少。

**第四，空中仍是主要来袭方向，水面次之。**按作战域统计，涉及空中的案例{dom['空中']}个（占{pct(dom['空中'])}），水面{dom['水面']}个（{pct(dom['水面'])}），岸基{dom['岸基']}个，水下{dom['水下']}个，电磁{dom['电磁']}个。

**第五，灰色地带行动自成一类。**低强度与灰色地带行动涉及{len(gsub['低强度与灰色地带'])}个案例，主要分布在亚太、波罗的海、印度洋和加勒比，多数不发生火力交战，但直接决定岛礁补给、海底设施安全和航运通行，是岛屿和小岛类场景的主要威胁形态。

## （三）时间脉络：三条主线先后升温，无人化比例持续上升

{{fig:d_trend}}给出各年度主要威胁类型的占比和无人平台参与比例。从时间上看有三个变化：

一是**主战场接续转移**。2023—2024年以黑海港口与舰艇攻防、红海编队防空为主，2024年案例数最多；2025年红海对海军舰艇的攻击在5月美胡停火后基本停止，黑海打击转向新罗西斯克和影子船队油轮；2026年波斯湾爆发战争，红海南口出现岛屿易手，黑海双方互打航运，案例数再度上升。

二是**无人化比例持续上升**。有无人平台参与的案例占当年比例，2023年为{pct(uy['2023'], yr['2023'])}，2024年因红海导弹拦截和南海对峙案例集中而降至{pct(uy['2024'], yr['2024'])}，2025年回升至{pct(uy['2025'], yr['2025'])}，2026年前三季度达到{pct(uy['2026'], yr['2026'])}；其中无人机在2025年起超过导弹，成为占比最高的威胁类型。

三是**灰色地带与登临类行动比例下降、强度上升**。这类案例的占比在2024年后回落，但出现了联合拦截补给、渔船渗透岛屿、近岸岛屿被夺占等更高强度的形态。

!fig d_trend|d_trend.png|主要威胁类型占比变化与无人平台参与比例|本报告统计（2026年数据截至9月）|158

{{fig:d_outcome_year}}给出各年度结果构成。2024年防御成功的比例最高，主要来自红海与东地中海编队拦截；2025年起遭袭受损的比例上升到一半以上，与攻击重心转向港口、商船和岛上基地相吻合。

!fig d_outcome_year|d_outcome_year.png|各年度案例结果构成|本报告统计|140

## （四）作战域与组织形态

!fig d_dp|d_domain_pattern.png|案例按作战域与组织形态统计|本报告统计（一个案例可计入多项）|158

## （五）攻防成本量级

{{fig:d_cost}}把主要攻击平台、拦截手段和被毁目标放在同一对数坐标上。攻击方主力平台单价集中在2万至50万美元，常用舰空导弹在百万美元以上，"标准-3"达千万美元量级，两者相差两到三个数量级；这也是各国转向舰炮、激光制导火箭和激光武器处置无人机的直接原因。

!fig d_cost|f_cost.png|主要攻防手段单价量级对比|详细版汇编第七章，各项出处见该章参考文献|150

## （六）总体判断

:::judge 总体判断
- **从被攻击对象看，静止目标是主要受害者。**港口类案例中遭袭受损或被击沉、摧毁的占{pct(catc('周边港口', ('遭袭受损', '被击沉/摧毁')), cat['周边港口'])}，而远海编组类案例中防御成功或部分拦截的占{pct(catc('远海机动编组', ('防御成功', '部分拦截')), cat['远海机动编组'])}。攻击方普遍选择停泊舰艇、船坞、港口设施和岛上基地，而不是航行中的编队。
- **从攻击手段看，无人化是最清楚的趋势。**无人平台参与的案例从2024年的{pct(uy['2024'], yr['2024'])}升至2026年的{pct(uy['2026'], yr['2026'])}，无人机已成为占比最高的威胁类型，无人艇和水下手段数量少但致毁率高。
- **从组织方式看，组合打击已成常态。**近半数案例涉及两类以上威胁，导弹、无人机、无人艇同时来袭和"先打探测节点、再打主目标"的做法反复出现。
- **从地域看，威胁形态呈现明显分区。**黑海以港口攻防为主，红海以编组护航为主，亚太与波罗的海以灰色地带对峙为主，波斯湾与东地中海以国家间高强度打击为主，同一套防御体系难以通用。
- **从烈度看，高强度冲突与灰色地带并行。**{pct(out['灰色地带对峙'])}的案例没有发生火力交战，但岛礁补给、海底设施和航运通行受到的影响并不比火力打击小。
:::

""" + ATLAS_PLACEHOLDER + """
{{{{close}}}}
"""

def main():
    os.makedirs(os.path.join(HERE, 'content2'), exist_ok=True)
    md = MD.replace('{{fig:', '{fig:').replace('{{tab:', '{tab:').replace('{{{{close}}}}', '{{close}}')
    ctx = build.make_ctx()
    ab = []; used = set()
    for k in CATS:
        items = []
        for c in cs:
            if c['category'] != k: continue
            r = thumb(c, used)
            if not r: continue
            path, im = r
            d = im.get('desc') or ''
            if any(k in d for k in ('示意图', '位置图', '海图', '卫星影像', '航天照片', '航拍照片', '影像，示意')):
                note = '位置示意图，非事件现场'
            elif any(k in d for k in ('资料', '非事发', '非本', '非事件', '背景', '参考', '示意', '非作战', '非加沙', '非关岛', '非交战', '待核')):
                note = '资料照片，非事件现场'
            else:
                note = '事件相关影像'
            items.append({'path': path, 'code': c['code'], 'title': clean(c.get('title_cn')), 'note': note})
        if items:
            ab.append({'t': 'h1', 'text': '%s（%d案）' % (k, len(items)), 'anchor': 'atl_%d' % len(ab)})
            ab.append({'t': 'photogrid', 'items': items})
    ctx['atlas_blocks'] = ab
    blocks = build.parse_markup(md, ctx)
    build.resolve_numbers(blocks, ctx, include_remote=False)
    D = DocxBuilder(ctx, column='本期聚焦｜FOCUS', issue='特情 · 2026年10月')
    s = D.doc.sections[0]; D._page(s); D.header(s); D.footer(s, 'body'); D.pg_start(s, 1)
    D.masthead()
    D.title('停泊即暴露，无人化加速', '——海上岛屿、港口、小岛与远海编组遭袭与防卫案例统计精要（2023—2026）')
    D.render(blocks)
    out_dir = os.path.join(build.OUT)
    p = os.path.join(out_dir, '析光特情精要_海上攻防案例统计与威胁态势.docx')
    D.save(p)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out_dir, p],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    subprocess.run([sys.executable, 'qa_docx.py', p])
    print(p)

if __name__ == '__main__':
    main()
