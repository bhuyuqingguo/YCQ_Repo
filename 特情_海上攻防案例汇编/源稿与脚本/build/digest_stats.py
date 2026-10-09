from cases_lib import *
from make_figs import outcome_class
from collections import Counter
REG={'黑海':'黑海','亚速海':'黑海','红海-亚丁湾':'红海—亚丁湾','东地中海':'东地中海','波斯湾-霍尔木兹-阿曼湾':'波斯湾','阿拉伯海-印度洋':'印度洋','波罗的海-北海':'波罗的海—北海','南海':'南海','台海':'台海及东北亚','东海-西太':'台海及东北亚','日本海-朝鲜半岛':'台海及东北亚','马六甲-新加坡海峡':'东南亚海峡','加勒比':'加勒比'}
TYPES=['导弹与火力打击','无人机','有人机空袭','无人艇','水下威胁','登临/劫持/登陆','封锁与扣押','灰色地带施压','海底设施破坏']
def tt(c):
    t=(c.get('attack_means_cn') or '')+(c.get('title_cn') or '')+(c.get('subtitle_cn') or '')
    s=set()
    if any(k in t for k in ['弹道导弹','巡航导弹','ATACMS','风暴阴影','海王星','导弹','迫击炮','火箭弹']): s.add('导弹与火力打击')
    if any(k in t for k in ['无人机','沙希德','天竺葵','Shahed']): s.add('无人机')
    if any(k in t for k in ['战机','空袭','空中精确打击','F-35','F-16','舰载机','轰炸']): s.add('有人机空袭')
    if any(k in t for k in ['无人艇','爆炸艇','Magura','Sea Baby','海宝宝','USV','萨尔甘','无人系统']): s.add('无人艇')
    if any(k in t for k in ['潜航器','水雷','鱼雷','UUV','布雷']): s.add('水下威胁')
    if any(k in t for k in ['登临','劫持','机降','登船','海盗','登陆','渗透','特种','登岛']): s.add('登临/劫持/登陆')
    if any(k in t for k in ['扣押','扣船','拦检','封锁','拦停','伪旗','禁运','改旗']): s.add('封锁与扣押')
    if any(k in t for k in ['水炮','冲撞','拦阻','碰撞','演习','巡查','逼近','炮击','干扰','滋扰','GNSS','不明无人机','抵近']): s.add('灰色地带施压')
    if any(k in t for k in ['锚','海缆','电缆','管线']): s.add('海底设施破坏')
    return s or {'其他'}
def load():
    cs=number(load_all())
    for c in cs:
        c['R']=REG.get(c.get('region'),'其他'); c['Y']=(c.get('date_start') or '')[:4]; c['O']=outcome_class(c.get('outcome')); c['T']=tt(c)
    return cs
if __name__=='__main__':
    cs=load()
    print(Counter(x for c in cs for x in c['T']).most_common())
    for c in cs:
        if '其他' in c['T']: print(c['code'],c['title_cn'],'|',(c.get('attack_means_cn') or '')[:60])
