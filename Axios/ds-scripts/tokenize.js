// helper: bind node tree to Axios tokens only on exact matches (no visual change)
async function axiosTokenize(root){
 const NEWC=new Set(["VariableCollectionId:399:2022","VariableCollectionId:399:2075","VariableCollectionId:399:2099"]);
 const vars=(await figma.variables.getLocalVariablesAsync()).filter(v=>NEWC.has(v.variableCollectionId));
 const byName=Object.fromEntries(vars.map(v=>[v.name,v]));
 const hex=c=>[c.r,c.g,c.b].map(x=>Math.round(x*255).toString(16).padStart(2,'0')).join('');
 const prim={};for(const v of vars){if(v.variableCollectionId!=="VariableCollectionId:399:2022"||v.resolvedType!=='COLOR')continue;const c=Object.values(v.valuesByMode)[0];prim[hex(c)+'@'+Math.round((c.a??1)*100)]=v;}
 const SEM={text:{'21211f@100':'text/primary','807a73@100':'text/secondary','807a73@60':'text/muted','ffffff@100':'text/inverse','ffffff@70':'text/inverse-secondary','ffffff@80':'text/inverse-label'},
  fill:{'21211f@100':'bg/inverse','ffffff@100':'bg/page','f7f5f0@100':'bg/cream','e9e3d6@100':'bg/sand','f4f4f4@100':'bg/button-light','ffffff@16':'glass/fill','21211f@12':'border/subtle','21211f@40':'overlay/scrim','241a12@13':'overlay/tint','9a5540@100':'accent/clay','7a8c5c@100':'accent/sage','ffffff@35':'on-photo/line'},
  stroke:{'21211f@100':'border/strong','21211f@12':'border/subtle','21211f@16':'border/default','ffffff@24':'glass/border','ffffff@35':'on-photo/line','c6bdae@100':'border/footer','9a5540@100':'accent/clay'}};
 const alphaOf=async v=>{let x=v;for(let i=0;i<4;i++){const val=Object.values(x.valuesByMode)[0];if(val&&val.type==='VARIABLE_ALIAS'){x=await figma.variables.getVariableByIdAsync(val.id);}else return val.a??1;}return 1;};
 const ts=(await figma.getLocalTextStylesAsync()).filter(s=>s.name.startsWith('Axios/'));
 const tkey=(st,sz,lh,ls,tc)=>[st,sz,lh.unit==='AUTO'?'A':lh.unit[0]+Math.round(lh.value*10)/10,Math.round(ls.value*10)/10,tc||'ORIGINAL'].join('|');
 const tsMap={};for(const s of ts){if(s.name==='Axios/Display/Wordmark')continue;tsMap[tkey(s.fontName.style,s.fontSize,s.lineHeight,s.letterSpacing,s.textCase)]=s;}
 const es=(await figma.getLocalEffectStylesAsync()).find(s=>s.name==='Axios/Glass blur');
 const space={};for(const v of vars)if(/^space\//.test(v.name))space[Object.values(v.valuesByMode)[0]]=v;
 const rad={4:byName['radius/sm'],8:byName['radius/md'],12:byName['radius/lg'],999:byName['radius/pill']};
 const st={paints:0,texts:0,space:0,radius:0,fx:0};
 const nodes=[root,...('findAll' in root?root.findAll(()=>true):[])];
 for(const n of nodes){
  for(const prop of ['fills','strokes']){if(!(prop in n)||n[prop]===figma.mixed||!n[prop].length)continue;let ch=false;const arr=[];
   for(const p of n[prop]){if(p.type!=='SOLID'||p.boundVariables&&p.boundVariables.color){arr.push(p);continue;}
    const k=hex(p.color)+'@'+Math.round((p.opacity??1)*100);const role=n.type==='TEXT'?'text':prop==='strokes'?'stroke':'fill';
    let v=SEM[role][k]?byName['color/'+SEM[role][k]]:prim[k]||prim[hex(p.color)+'@100'];
    if(!v){arr.push(p);continue;}
    const a=await alphaOf(v);const base=Object.assign({},p,{opacity:a<1?1:(p.opacity??1)});
    if(a===1&&(p.opacity??1)<1&&!SEM[role][k]&&!prim[k]){/*primitive solid + paint opacity*/}
    arr.push(figma.variables.setBoundVariableForPaint(base,'color',v));ch=true;st.paints++;}
   if(ch)n[prop]=arr;}
  if(n.type==='TEXT'){const segs=n.getStyledTextSegments(['fontName','fontSize','lineHeight','letterSpacing','textCase']);
   if(segs.length===1&&!n.textStyleId){const s=segs[0];const m=tsMap[tkey(s.fontName.style,s.fontSize,s.lineHeight,s.letterSpacing,s.textCase)];
    if(m&&s.fontName.family==='Plus Jakarta Sans'){await figma.loadFontAsync(s.fontName);await n.setTextStyleIdAsync(m.id);st.texts++;}}}
  if('layoutMode' in n&&n.layoutMode&&n.layoutMode!=='NONE'){for(const f of ['paddingTop','paddingRight','paddingBottom','paddingLeft']){const v=space[n[f]];if(v&&n[f]>0){n.setBoundVariable(f,v);st.space++;}}
   if(n.primaryAxisAlignItems!=='SPACE_BETWEEN'&&space[n.itemSpacing]&&n.itemSpacing>0){n.setBoundVariable('itemSpacing',space[n.itemSpacing]);st.space++;}}
  if('cornerRadius' in n&&n.cornerRadius!==figma.mixed&&rad[n.cornerRadius]){const v=rad[n.cornerRadius];for(const c of ['topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius'])n.setBoundVariable(c,v);st.radius++;}
  if(es&&'effects' in n&&n.effects.length===1&&n.effects[0].type==='BACKGROUND_BLUR'&&n.effects[0].radius===16&&!n.effectStyleId){await n.setEffectStyleIdAsync(es.id);st.fx++;}}
 return st;}
