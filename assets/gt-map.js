/* Ground Truth Texas: home page map. Draws every project in /data/projects.json on the
   Texas county map (U.S. Census boundaries via us-atlas). Nov. 20, 2026. */
{
const box=document.getElementById('gt-map');
if(box){
const r=Math.PI/180,sy0=Math.sin(27.5*r),n=(sy0+Math.sin(35*r))/2,c=1+sy0*(2*n-sy0),r0=Math.sqrt(c)/n;
const raw=(x,y)=>{const rho=Math.sqrt(c-2*n*Math.sin(y))/n;x*=n;return [rho*Math.sin(x),r0-rho*Math.cos(x)]};
const K=3972.4906330216386,yc=raw(0,33.6*r)[1];
const proj=(lng,lat)=>{const p=raw((lng+100)*r,lat*r);return [403.05162303717583+K*p[0],213.4018737868546-K*(p[1]-yc)]};
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');
const label={data:'Data center',crypto:'Crypto mine',power:'Power plant',industrial:'Industrial plant'};
Promise.all([fetch('/assets/texas-base.svg').then(r=>r.text()),fetch('/data/projects.json',{cache:'no-store'}).then(r=>r.json())]).then(([svg,P])=>{
  box.innerHTML=svg;
  const s=box.querySelector('svg');s.setAttribute('role','img');
  const counties=new Set(P.map(p=>p.county.split(' (')[0]));
  s.querySelectorAll('.co path').forEach(el=>{if(counties.has(el.dataset.c))el.classList.add('on')});
  const pts=P.filter(p=>typeof p.lat==='number'&&typeof p.lng==='number');
  const g=document.createElementNS('http://www.w3.org/2000/svg','g');g.setAttribute('class','pt');
  g.innerHTML=pts.map(p=>{const [x,y]=proj(p.lng,p.lat);const t=`${p.name}, ${p.county} County (${label[p.type]||'Project'}${p.status==='stopped'?', stopped':''})`;
    return `<a href="${esc(p.link||'/texas')}" aria-label="${esc(t)}"><circle class="${esc(p.type)}${p.status==='stopped'?' stopped':''}" cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4.6"><title>${esc(t)}</title></circle></a>`}).join('');
  s.appendChild(g);
  s.insertAdjacentHTML('afterbegin',`<title>Map of Texas: ${pts.length} tracked projects in ${counties.size} counties</title>`);
  const set=(id,v)=>{const e=document.getElementById(id);if(e)e.textContent=v};
  set('gt-n',pts.length);set('gt-c',counties.size);set('gt-s',P.filter(p=>p.status==='stopped'&&p.type!=='industrial').length);
}).catch(()=>{box.innerHTML='<p class="gt-fail">The map didn’t load. <a href="/texas">Open the statewide map</a>.</p>'});
}
}
