# -*- coding: utf-8 -*-
"""配图采集清单页：浏览器端热链预览 + 一键打包下载（复用《析光》采集页模板，适配多候选直链与仅页面条目）。"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', '特情_海上攻防案例汇编', '源稿与脚本', 'build')))
import imgpage  # noqa

ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.abspath(os.path.join(ROOT, '..', 'research_notes', 'Lattice与Maven系统调研', 'images_candidates.json'))
OUT = os.path.join(ROOT, '成品', 'Lattice与Maven系统调研（配图采集清单）.html')
SEC = {'Lattice history': 'Lattice·沿革', 'Lattice hardware': 'Lattice·装备', 'Lattice cases': 'Lattice·案例',
       'Maven history': 'Maven·沿革', 'Maven cases': 'Maven·案例', 'cooperation': '合作与布局'}


def alt_urls(u):
    """DVIDS 直链的年月目录为推算值：补充前后各两个月的候选。"""
    m = re.match(r'^(https://d1ldvf68ux039x\.cloudfront\.net/thumbs/photos/)(\d{2})(\d{2})(/.*)$', u or '')
    if not m:
        return []
    yy, mm = int(m.group(2)), int(m.group(3))
    out = []
    for d in (-1, 1, -2, 2):
        y2, m2 = yy, mm + d
        if m2 < 1:
            y2, m2 = yy - 1, m2 + 12
        if m2 > 12:
            y2, m2 = yy + 1, m2 - 12
        out.append('%s%02d%02d%s' % (m.group(1), y2, m2, m.group(4)))
    return out


def main(src=SRC, out=OUT, title_note=''):
    data = json.load(open(src, encoding='utf-8'))
    items = []
    for d in data:
        url = d.get('image_url') or ''
        if not url and title_note:
            continue
        items.append({'case': SEC.get(d.get('section', ''), d.get('section', '补抓')), 'desc': d['caption_zh'][:80],
                      'url': url, 'alts': (d.get('alt_urls') or []) + alt_urls(url), 'page': d.get('page_url') or url,
                      'save_as': 'lm_' + d['id'], 'license': d.get('license', '')})
    tpl = imgpage.TPL
    tpl = tpl.replace('特情配图采集清单', 'Lattice与Maven配图采集清单')
    tpl = tpl.replace('XIGUANG · 析光特情 · 配图采集清单', 'XIGUANG · Lattice 与 Maven 系统调研 · 配图采集清单')
    tpl = tpl.replace('海上岛屿·港口·小岛·远海编组遭袭与防卫案例汇编 —— 配图采集清单', 'Lattice 与 Maven 系统调研 —— 配图采集清单')
    tpl = tpl.replace('本页图片全部直接热链 Wikimedia Commons 等原始图源',
                      '本页图片热链 Wikimedia Commons、DVIDS 等原始图源（另有少数仅给出页面链接的条目，卡片标注“需手动另存”）')
    tpl = tpl.replace('xiguang_imgs.zip', 'lm_imgs.zip').replace("'xiguang_imgs_part'", "'lm_imgs_part'")
    # 预览与抓取：无直链时提示手动；多候选直链依次尝试
    tpl = tpl.replace('''d.innerHTML = `<img loading="lazy" src="${it.url}"''',
                      '''d.innerHTML = it.url ? `<img loading="lazy" src="${it.url}"''')
    tpl = tpl.replace('''<a href="${it.url}" target="_blank">原图直链</a></div>`;''',
                      '''<a href="${it.url}" target="_blank">原图直链</a> · <span style="color:#8A8474">${it.license||''}</span></div>` : `<div style="height:150px;display:flex;align-items:center;justify-content:center;background:#ECE8DE;color:#A8842F">需手动另存（打开原图页面）</div>
  <div><span class="k">${it.case}</span> ${it.desc}</div>
  <div>保存名：<code>${it.save_as}</code> <span id="s${i}"></span></div>
  <div><a href="${it.page}" target="_blank">原图页面</a> · <span style="color:#8A8474">${it.license||''}</span></div>`;''')
    tpl = tpl.replace('''async function getBlob(u){
  for (const x of [thumbUrl(u), u]) { if(!x) continue;''', '''async function getBlob(u, alts){
  if(!u) throw new Error('no direct url');
  for (const x of [thumbUrl(u), u, ...(alts||[])]) { if(!x) continue;''')
    tpl = tpl.replace('const raw = await getBlob(it.url);', 'const raw = await getBlob(it.url, it.alts);')
    # 站点不允许跨域抓取时，经 wsrv.nl 图片中转（返回 CORS 头）再试
    tpl = tpl.replace('''    try{ const r=await fetch(x,{mode:'cors'}); if(r.ok) return await r.blob(); }catch(e){} }
  throw new Error('fetch failed');''', '''    try{ const r=await fetch(x,{mode:'cors'}); if(r.ok) return await r.blob(); }catch(e){} }
  for (const x of [u, ...(alts||[])]) {
    try{ const r=await fetch('https://wsrv.nl/?url='+encodeURIComponent(x)+'&w=1600&output=jpg',{mode:'cors'}); if(r.ok) return await r.blob(); }catch(e){} }
  throw new Error('fetch failed');''')
    assert 'wsrv.nl' in tpl
    assert 'getBlob(it.url, it.alts)' in tpl and 'needs' not in tpl
    if title_note:
        tpl = tpl.replace('—— 配图采集清单</h1>', '—— 配图采集清单（%s）</h1>' % title_note)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    imgpage.TPL = tpl
    imgpage.build(items, out)
    print(out, len(items))


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else '')
    else:
        main()
