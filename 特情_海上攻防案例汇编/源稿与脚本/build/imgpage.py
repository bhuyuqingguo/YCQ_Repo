# -*- coding: utf-8 -*-
"""图片采集清单页：在用户浏览器中热链预览 + 一键打包下载（JSZip），供回传嵌入 docx/PDF。"""
import html
import json

TPL = r"""<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>特情配图采集清单</title>
<style>
:root{--cream:#F7F4EC;--navy:#12233B;--accent:#2E93D6;--brass:#A8842F;--alert:#C0392B;--grey:#8A8474}
body{background:var(--cream);color:#222;font-family:"Noto Sans CJK SC","PingFang SC","Microsoft YaHei",sans-serif;margin:0 auto;max-width:1100px;padding:0 16px 60px}
.band{background:var(--navy);color:#fff;padding:10px 16px;margin:0 -16px;font-size:13px;letter-spacing:.1em}
h1{color:var(--navy);font-size:22px;margin:18px 0 6px}
.note{background:#fff;border-left:5px solid var(--brass);padding:10px 14px;font-size:14px;line-height:1.8}
.bar{position:sticky;top:0;background:var(--cream);padding:10px 0;z-index:5;border-bottom:1px solid #E9E4D6;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
button{background:var(--navy);color:#fff;border:0;padding:9px 16px;font-size:14px;border-radius:4px;cursor:pointer}
button.alt{background:var(--brass)}
#st{font-size:13px;color:var(--grey)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px;margin-top:12px}
.card{background:#fff;border:1px solid #E9E4D6;padding:8px;font-size:12px;line-height:1.5;min-width:0}
.card img{width:100%;height:150px;object-fit:cover;background:#eee}
.card .k{color:var(--brass);font-weight:bold}
.card a{color:var(--accent);word-break:break-all}
.ok{color:#1F8A70}.bad{color:var(--alert)}
</style></head><body>
<div class="band">XIGUANG · 析光特情 · 配图采集清单</div>
<h1>海上岛屿·港口·小岛·远海编组遭袭与防卫案例汇编 —— 配图采集清单</h1>
<div class="note">本页图片全部直接热链 Wikimedia Commons 等原始图源，由您的浏览器加载。<b>用法：</b>点击“一键打包下载”，浏览器会逐张抓取原图并打包为 <code>xiguang_imgs.zip</code>（含 manifest.json 对照表）；下载完成后把该压缩包传回对话，我会把原图嵌入 docx/PDF 版并按图号重排。个别图片如抓取失败（卡片标红），可点开链接手动另存，文件名按卡片上的“保存名”命名后一并打包。</div>
<div class="bar"><button id="go">一键打包下载（__N__ 张）</button><button class="alt" id="txt">下载链接清单 urls.txt</button><span id="st"></span></div>
<div class="grid" id="g"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
<script>
const ITEMS = __DATA__;
const g = document.getElementById('g');
ITEMS.forEach((it, i) => {
  const d = document.createElement('div'); d.className = 'card'; d.id = 'c' + i;
  d.innerHTML = `<img loading="lazy" src="${it.url}" onerror="this.style.opacity=.2;document.getElementById('s${i}').innerHTML='<span class=bad>预览失败</span>'">
  <div><span class="k">${it.case}</span> ${it.desc}</div>
  <div>保存名：<code>${it.save_as}</code> <span id="s${i}"></span></div>
  <div><a href="${it.page}" target="_blank">原图页面</a> · <a href="${it.url}" target="_blank">原图直链</a></div>`;
  g.appendChild(d);
});
function extOf(u, type){ if(type && type.includes('png')) return '.png'; if(type && type.includes('webp')) return '.webp'; const m=u.toLowerCase().match(/\.(jpe?g|png|webp|gif|tiff?)(\?|$)/); return m? '.'+m[1].replace('jpeg','jpg'):'.jpg'; }
document.getElementById('txt').onclick = () => {
  const blob = new Blob([ITEMS.map(it => it.save_as + '\t' + it.url).join('\n')], {type:'text/plain'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'urls.txt'; a.click();
};
async function shrink(blob){
  // 统一压成长边不超过 1600px 的 JPEG（质量 0.82），单张通常 150-400KB
  try{
    const bmp = await createImageBitmap(blob);
    const k = Math.min(1, 1600/Math.max(bmp.width,bmp.height));
    const c = document.createElement('canvas'); c.width=Math.round(bmp.width*k); c.height=Math.round(bmp.height*k);
    const g = c.getContext('2d'); g.fillStyle='#fff'; g.fillRect(0,0,c.width,c.height); g.drawImage(bmp,0,0,c.width,c.height);
    return await new Promise(r=>c.toBlob(r,'image/jpeg',0.82));
  }catch(e){ return null; }
}
function thumbUrl(u){ // upload.wikimedia.org 原图 -> 1280px 缩略图
  const m = u.match(/^(https:\/\/upload\.wikimedia\.org\/wikipedia\/commons\/)([0-9a-f]\/[0-9a-f]{2}\/)(.+)$/);
  if(!m) return null; let n=m[3]; let t=n; if(/\.(svg|tiff?)$/i.test(n)) t=n+'.png';
  return m[1]+'thumb/'+m[2]+n+'/1280px-'+t;
}
async function getBlob(u){
  for (const x of [thumbUrl(u), u]) { if(!x) continue;
    try{ const r=await fetch(x,{mode:'cors'}); if(r.ok) return await r.blob(); }catch(e){} }
  throw new Error('fetch failed');
}
function save(blob,name){ const a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download=name; a.click(); }
document.getElementById('go').onclick = async () => {
  const LIMIT = 25*1024*1024; // 每卷不超过 25MB
  const st = document.getElementById('st'); let zip = new JSZip(), size = 0, vol = 1, ok = 0, bad = 0; const man = [];
  const flush = async () => { zip.file('manifest_part'+vol+'.json', JSON.stringify(man.filter(m=>m.vol===vol),null,1));
    const b = await zip.generateAsync({type:'blob'}); save(b, 'xiguang_imgs_part'+vol+'.zip'); vol++; zip = new JSZip(); size = 0;
    await new Promise(r=>setTimeout(r,800)); };
  for (let i = 0; i < ITEMS.length; i++) {
    const it = ITEMS[i]; st.textContent = `抓取中 ${i+1}/${ITEMS.length}（成功 ${ok}，失败 ${bad}，第 ${vol} 卷）`;
    try {
      const raw = await getBlob(it.url); const small = (await shrink(raw)) || raw;
      if (size + small.size > LIMIT && size > 0) await flush();
      const name = it.save_as + '.jpg'; zip.file(name, small); size += small.size; ok++;
      man.push({...it, file:name, vol:vol}); document.getElementById('s'+i).innerHTML = '<span class="ok">已打包（第'+vol+'卷）</span>';
    } catch(e) { bad++; man.push({...it, file:null, error:String(e), vol:vol}); document.getElementById('s'+i).innerHTML = '<span class="bad">抓取失败</span>'; }
  }
  await flush();
  st.textContent = `完成：成功 ${ok} 张，失败 ${bad} 张，共 ${vol-1} 卷（每卷不超过 25MB）。请把各卷 zip 依次传回对话。`;
};
</script></body></html>"""


def build(items, path):
    s = TPL.replace('__DATA__', json.dumps(items, ensure_ascii=False)).replace('__N__', str(len(items)))
    open(path, 'w', encoding='utf-8').write(s)
    return path
