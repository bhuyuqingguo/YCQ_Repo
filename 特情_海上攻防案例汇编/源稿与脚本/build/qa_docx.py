import sys, zipfile, re
from lxml import etree
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def q(t): return '{%s}%s' % (W, t)
def main(path):
    z = zipfile.ZipFile(path)
    root = etree.fromstring(z.read('word/document.xml'))
    bad_bm = 0; bms = set()
    for p in root.iter(q('p')):
        kids = list(p)
        for i, k in enumerate(kids):
            if k.tag == q('bookmarkStart'):
                bms.add(k.get(q('name')))
            if k.tag == q('pPr') and i != 0:
                bad_bm += 1
    bad_rpr = 0
    for r in root.iter(q('r')):
        kids = list(r)
        if any(k.tag == q('rPr') for k in kids) and kids[0].tag != q('rPr'):
            bad_rpr += 1
    bad_tcpr = 0
    for tc in root.iter(q('tc')):
        kids = list(tc)
        if any(k.tag == q('tcPr') for k in kids) and kids[0].tag != q('tcPr'):
            bad_tcpr += 1
    instr = [t.text or '' for t in root.iter(q('instrText'))]
    anchors = [m.group(1) for s in instr for m in [re.search(r'HYPERLINK \\l "([^"]+)"', s)] if m]
    missing = [a for a in anchors if a not in bms]
    fc = {'begin': 0, 'separate': 0, 'end': 0}
    for f in root.iter(q('fldChar')):
        fc[f.get(q('fldCharType'))] += 1
    norf = 0
    for r in root.iter(q('r')):
        t = ''.join(x.text or '' for x in r.iter(q('t')))
        if t.strip():
            rpr = r.find(q('rPr'))
            if rpr is None or rpr.find(q('rFonts')) is None:
                norf += 1
    print('pPr非首位段落:', bad_bm, '| rPr非首位run:', bad_rpr, '| tcPr非首位单元格:', bad_tcpr)
    print('书签数:', len(bms), '| HYPERLINK锚点:', len(anchors), '| 找不到书签的锚点:', len(missing), missing[:5])
    print('fldChar begin/separate/end:', fc['begin'], fc['separate'], fc['end'])
    print('含文字但无rFonts的run:', norf)
    ok = bad_bm == 0 and bad_rpr == 0 and bad_tcpr == 0 and not missing and fc['begin'] == fc['separate'] == fc['end'] and norf == 0
    print('结论:', '全部通过' if ok else '不通过')
    return ok
if __name__ == '__main__':
    sys.exit(0 if main(sys.argv[1]) else 1)
