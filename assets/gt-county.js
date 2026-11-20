/* Ground Truth Texas: county locator map for County Watch pages. Nov. 20, 2026.
   Zooms the Texas county map (U.S. Census lines via us-atlas) to this county and marks the
   projects from /data/projects.json: this county's in red clay, neighbors' faded. */
{
const h1=document.querySelector('.hero h1');
const m=h1&&h1.textContent.match(/^\s*(.+?) County Watch/);
if(m){
const NAME=m[1].trim();
const r=Math.PI/180,sy0=Math.sin(27.5*r),n=(sy0+Math.sin(35*r))/2,c=1+sy0*(2*n-sy0),r0=Math.sqrt(c)/n;
const raw=(x,y)=>{const rho=Math.sqrt(c-2*n*Math.sin(y))/n;x*=n;return [rho*Math.sin(x),r0-rho*Math.cos(x)]};
const K=3972.4906330216386,yc=raw(0,33.6*r)[1];
const proj=(lng,lat)=>{const p=raw((lng+100)*r,lat*r);return [403.05162303717583+K*p[0],213.4018737868546-K*(p[1]-yc)]};
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const css=`.gt-loc{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:20px;align-items:center;margin:8px 0 8px;background:var(--card);border:1px solid var(--rule);padding:14px}
.gt-loc svg{width:100%;height:auto;display:block;max-height:340px}
.gt-loc .co path{fill:var(--paper);stroke:var(--rule);stroke-width:.5}
.gt-loc .co path.me{fill:color-mix(in srgb,var(--pine) 16%,var(--paper));stroke:var(--pine);stroke-width:1.4}
.gt-loc .st{fill:none;stroke:var(--muted);stroke-width:1}
.gt-loc circle{stroke:var(--card);stroke-width:.6}
.gt-loc circle.here{fill:#B4472A}.gt-loc circle.near{fill:var(--muted);opacity:.55}
.gt-loc circle.stopped{fill:var(--card);stroke:var(--pine);stroke-width:.8}
.gt-loc .cap b{font-family:"Libre Caslon Display",Georgia,serif;font-weight:400;font-size:2.2rem;line-height:1;display:block}
.gt-loc .cap p{margin:6px 0 0;color:var(--muted);font-size:.95rem}
.gt-loc .mini{display:block;max-width:150px;margin-bottom:10px}
@media (max-width:640px){.gt-loc{grid-template-columns:minmax(0,1fr)}}`;
const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
const fig=document.createElement('figure');fig.className='gt-loc';fig.setAttribute('aria-label',`${NAME} County on the map`);
document.querySelector('.hero').after(fig);
Promise.all([fetch('/assets/texas-base.svg').then(x=>x.text()),fetch('/data/projects.json',{cache:'no-store'}).then(x=>x.json())]).then(([svg,P])=>{
  fig.innerHTML=`<div class="cap"></div><div class="map">${svg}</div>`;
  const s=fig.querySelector('.map svg');
  const me=s.querySelector(`.co path[data-c="${CSS.escape(NAME)}"]`);
  if(!me){fig.remove();return}
  me.classList.add('me');me.parentNode.appendChild(me);
  const b=me.getBBox(),pad=Math.max(b.width,b.height)*.55;
  s.setAttribute('viewBox',`${b.x-pad} ${b.y-pad} ${b.width+2*pad} ${b.height+2*pad}`);
  const k=(b.width+2*pad)/800;
  const pts=P.filter(p=>typeof p.lat==='number');
  const mine=pts.filter(p=>p.county.split(' (')[0]===NAME);
  const near=pts.filter(p=>!mine.includes(p)).filter(p=>{const [x,y]=proj(p.lng,p.lat);return x>b.x-pad&&x<b.x+b.width+pad&&y>b.y-pad&&y<b.y+b.height+pad});
  const dot=(p,cls)=>{const [x,y]=proj(p.lng,p.lat);const t=`${p.name}, ${p.county} County`;
    return `<a href="${esc(p.link||'/texas')}" aria-label="${esc(t)}"><circle class="${cls}${p.status==='stopped'?' stopped':''}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(cls==='here'?9:6)*k}"><title>${esc(t)}</title></circle></a>`};
  const g=document.createElementNS('http://www.w3.org/2000/svg','g');g.innerHTML=near.map(p=>dot(p,'near')).join('')+mine.map(p=>dot(p,'here')).join('');s.appendChild(g);
  s.setAttribute('role','img');s.insertAdjacentHTML('afterbegin',`<title>${esc(NAME)} County with ${mine.length} mapped projects</title>`);
  const mini=new DOMParser().parseFromString(svg,'image/svg+xml').documentElement;
  mini.classList.add('mini');mini.setAttribute('aria-hidden','true');
  const mm=mini.querySelector(`.co path[data-c="${CSS.escape(NAME)}"]`);if(mm)mm.classList.add('me');
  fig.querySelector('.cap').append(mini);
  fig.querySelector('.cap').insertAdjacentHTML('beforeend',`<b>${mine.length}</b><p>${mine.length===1?'project':'projects'} on our map in ${esc(NAME)} County${near.length?`, and ${near.length} more nearby in gray`:''}. Tap a dot for its page.</p>`);
}).catch(()=>fig.remove());
}
}
