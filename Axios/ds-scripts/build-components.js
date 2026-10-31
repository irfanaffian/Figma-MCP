async function ensurePage(){let p=figma.root.children.find(x=>x.name==='Components');if(!p){p=figma.createPage();p.name='Components';}await figma.setCurrentPageAsync(p);
 for(const s of ["Regular","Medium","SemiBold"])await figma.loadFontAsync({family:"Plus Jakarta Sans",style:s});
 let root=p.findChild(n=>n.name==='Axios / Components');
 if(!root){root=figma.createAutoLayout('VERTICAL',{name:'Axios / Components',itemSpacing:96});root.set({paddingTop:80,paddingBottom:80,paddingLeft:80,paddingRight:80});root.fills=[{type:'SOLID',color:{r:1,g:1,b:1}}];p.appendChild(root);root.counterAxisSizingMode='AUTO';}
 return {p,root};}
async function section(root,title,note){const ts=Object.fromEntries((await figma.getLocalTextStylesAsync()).map(s=>[s.name,s]));
 let s=root.findChild(n=>n.name==='Section / '+title);if(s)s.remove();
 s=figma.createAutoLayout('VERTICAL',{name:'Section / '+title,itemSpacing:24});s.fills=[];root.appendChild(s);
 const t=figma.createText();await t.setTextStyleIdAsync(ts['Axios/Heading/H2'].id);t.characters=title;s.appendChild(t);
 if(note){const d=figma.createText();await d.setTextStyleIdAsync(ts['Axios/Body/SM'].id);d.characters=note;d.fills=[{type:'SOLID',color:{r:.5,g:.48,b:.45}}];s.appendChild(d);}
 return s;}
async function makeSet(sec,name,items,opts={}){
 const comps=[];const stats=[];
 for(const [src,vname] of items){const n=await figma.getNodeByIdAsync(src);if(!n)throw new Error('missing '+src);
  const c=n.clone();sec.appendChild(c);if('layoutPositioning' in c)c.layoutPositioning='AUTO';
  if(c.type==='INSTANCE')c.detachInstance();
  stats.push(await axiosTokenize(c));
  const comp=figma.createComponentFromNode(c);comp.name=vname;comps.push(comp);}
 let node;
 if(comps.length===1){node=comps[0];node.name=name;}
 else{node=figma.combineAsVariants(comps,sec);node.name=name;node.layoutMode='HORIZONTAL';node.layoutWrap='WRAP';node.itemSpacing=24;node.counterAxisSpacing=24;node.set({paddingTop:24,paddingBottom:24,paddingLeft:24,paddingRight:24});node.primaryAxisSizingMode='AUTO';node.counterAxisSizingMode='AUTO';node.counterAxisAlignItems='MIN';
  if(opts.bg)node.fills=[{type:'SOLID',color:opts.bg}];}
 if(opts.label){const def=(comps[0].findOne(x=>x.type==='TEXT')||{}).characters||'Label';
  const key=(node.type==='COMPONENT_SET'?node:comps[0]).addComponentProperty('Label','TEXT',def);
  for(const c of comps){const t=c.findOne(x=>x.type==='TEXT');if(t)t.componentPropertyReferences={characters:key};}}
 if(opts.desc)node.description=opts.desc;
 return {id:node.id,name:node.name,variants:comps.length,stats};}
