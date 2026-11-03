"use strict";
let records=[];
const q=document.getElementById("q"),kind=document.getElementById("kind"),count=document.getElementById("count"),out=document.getElementById("results");
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
function render(){
 const term=q.value.trim().toLowerCase(),type=kind.value;
 const hits=records.filter(r=>(!type||r.type===type)&&(!term||(String(r.id)+" "+r.name+" "+(r.npcId||"")+" "+(r.npcName||"")).toLowerCase().includes(term))).slice(0,150);
 count.textContent=hits.length+" results shown (max 150); "+records.length+" indexed records";
 out.replaceChildren(...hits.map(r=>{
  const a=document.createElement("article"),h=document.createElement("h3"),p=document.createElement("p"),d=document.createElement("details"),s=document.createElement("summary"),pre=document.createElement("pre"),link=document.createElement("a");
  h.textContent=r.name+" · "+r.type+" #"+r.id;
  p.textContent=r.type==="loot"?r.evidence+" · NPC "+(r.npcName||"name unavailable")+" (#"+r.npcId+") · chance "+r.chance+" · not runtime verified":"Archived source record · live verification not claimed";
  s.textContent="Source, provenance, and record details";pre.textContent=JSON.stringify(r,null,2);d.append(s,pre);
  link.href=r.sourceUrl||"https://github.com/uncle-bone/CoA-Research/blob/main/"+r.source;link.target="_blank";link.rel="noopener";link.textContent="Open source file ↗";
  a.append(h,p,d,link);return a;
 }));
}
q.addEventListener("input",render);kind.addEventListener("change",render);
fetch("./data/research-explorer-v2.json").then(r=>{if(!r.ok)throw Error("Index not deployed");return r.json()}).then(x=>{records=x;render()}).catch(e=>{count.textContent="Research index unavailable: "+e.message+". Open the release or source manifest above."});
