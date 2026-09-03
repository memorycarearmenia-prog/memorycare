#!/usr/bin/env python3
"""Pack the extracted paint tree into the compact rows the Figma builder reads.

Two encodings share one array, told apart by whether element 4 is a string:
  box : [x,y,w,h, bgIdx, borderIdx,borderW, radius, sideIdx,t,b,l,r]
  text: [x,y,w,h, text, colourIdx, size, weight, lineHeight, tracking,
         upper, align, serif]

Colours are indices into a fixed palette rather than hex strings, because
every colour the build produces is one of the twelve primitives -- checked,
not assumed: an unknown colour packs as -1 and would draw nothing.
"""
S='/tmp/claude-0/-home-user-memorycare/4db60f39-d33e-511c-b4b7-3028082570ce/scratchpad/layout'
PAL=[("#212212",1),("#212212",0.72),("#212212",0.56),("#212212",0.2),("#212212",0.1),
     ("#212212",0.08),("#7C8654",1),("#EFE5D5",1),("#F3F0E9",1),("#A4D6E8",1),
     ("#575E3B",1),("#8C3A2E",1)]
IDX={p:i for i,p in enumerate(PAL)}
AL={'start':0,'left':0,'center':1,'right':2,'end':2,'justify':0}
def ci(c):
    if not c: return -1
    k=('#%02X%02X%02X'%(round(c['r']*255),round(c['g']*255),round(c['b']*255)), round(c['a'],3))
    return IDX.get(k,-1)
tot=0; sizes=[]
for f in sorted(glob.glob(S+'/*.json')):
    b=os.path.basename(f)
    if b.startswith(('a_','b_','c_')): continue
    d=json.load(open(f)); rows=[]
    for n in d['nodes']:
        if n['text']:
            rows.append([n['x'],n['y'],n['w'],n['h'],n['text'],ci(n['color']),n['size'],
                         n['weight'],n['lh'] or 0, round(n['ls'],2) if n['ls'] else 0,
                         1 if n['upper'] else 0, AL.get(n.get('align') or 'start',0),
                         1 if n.get('serif') else 0])
        else:
            bdd=n.get('border') or {}
            allb=bdd.get('all')
            sd={k:v for k,v in bdd.items() if k!='all' and v} if not allb else {}
            fs=sd.get('b') or sd.get('t') or sd.get('l') or sd.get('r')
            rows.append([n['x'],n['y'],n['w'],n['h'],ci(n['bg']),
                         ci(allb['c']) if allb else -1, allb['w'] if allb else 0, n['radius'] or 0,
                         ci(fs['c']) if fs else -1,
                         (sd.get('t') or {}).get('w',0), (sd.get('b') or {}).get('w',0),
                         (sd.get('l') or {}).get('w',0), (sd.get('r') or {}).get('w',0)])
    p=S+'/b_'+b
    json.dump({'r':d['route'],'w':d['w'],'h':d['h'],'bg':ci(d['bg']),'n':rows},
              open(p,'w'), ensure_ascii=False, separators=(',',':'))
    tot+=os.path.getsize(p); sizes.append((os.path.getsize(p)/1024, b[:-5]))
sizes.sort(reverse=True)
print('суммарно %.0f KB'%(tot/1024))
for s,n in sizes: print('  %5.1f  %s'%(s,n))
