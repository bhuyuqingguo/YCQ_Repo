"""图录用缩略图：每案取第一张本地照片，居中裁成 4:3。"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from cases_lib import case_images
TD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'imgs_thumb')
USED = set()
def thumb(c, used=None):
    ims = [i for i in case_images(c) if i.get('local')]
    if not ims: return None
    if used is not None:
        fresh = [i for i in ims if i['url'] not in used]
        im = (fresh or ims)[0]; used.add(im['url'])
        out = os.path.join(TD, c['case_key'] + '_atlas.jpg')
        if os.path.exists(out): os.remove(out)
    else:
        im = ims[0]; out = os.path.join(TD, c['case_key'] + '.jpg')
    if not os.path.exists(out):
        os.makedirs(TD, exist_ok=True)
        p = Image.open(im['local']).convert('RGB'); w, h = p.size; r = 4 / 3
        if w / h > r: nw = int(h * r); p = p.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else: nh = int(w / r); p = p.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
        p.thumbnail((800, 600)); p.save(out, 'JPEG', quality=80)
    return out, im
