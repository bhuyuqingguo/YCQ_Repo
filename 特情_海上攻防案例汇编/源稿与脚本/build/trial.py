import build, os, sys
secs=build.load_sections()
ctx=build.make_ctx()
blocks=build.parse_markup(secs['body'],ctx)
build.resolve_numbers(blocks,ctx,False)
ctx['body_blocks']=blocks; ctx['toc_entries']=build.collect_toc(blocks)
lof,lot=[],[]; fn=tn=0
for b in blocks:
  if b['t']=='figure' and b.get('local') and os.path.exists(b['local']): fn+=1; lof.append((fn,b['caption'],'fig_%d'%fn))
  elif b['t']=='table': tn+=1; lot.append((tn,b['caption'],'tab_%d'%tn))
ctx['lof'],ctx['lot']=lof,lot
p=build.build_docx(ctx,secs,{},os.path.join(build.HERE,'tmp','trial.docx'))
print(p, len(blocks), 'refs', len(ctx['refs'].order))
pdf=build.soffice_pdf(p, os.path.join(build.HERE,'tmp'))
print(pdf)
