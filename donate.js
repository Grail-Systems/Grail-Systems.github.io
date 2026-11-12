(function(){
  if (/donate\.html$/.test(location.pathname) || document.getElementById('gs-donate')) return;
  if (document.querySelector('.float-help')) return;
  var C = {"href":"https://easttexaslegacy.org/donate.html","label":"Donate","aria":"Support the East Texas Legacy Coalition","bg":"#24493a","fg":"#f3f4f1","ring":"#9c7424","dbg":"#8fc1a8","dfg":"#121a16","font":"'Public Sans',system-ui,sans-serif"};
  var s = document.createElement('style');
  s.textContent = '#gs-donate{position:fixed;right:calc(14px + env(safe-area-inset-right));bottom:calc(14px + env(safe-area-inset-bottom));z-index:9999;font:700 16px/1 '+C.font+';text-decoration:none;padding:13px 18px;border-radius:999px;background:'+C.bg+';color:'+C.fg+';box-shadow:0 6px 18px -6px rgba(0,0,0,.45);border:2px solid '+C.bg+'}'
   + '#gs-donate:hover{background:'+C.fg+';color:'+C.bg+'}'
   + '#gs-donate:focus-visible{outline:3px solid '+C.ring+';outline-offset:3px}'
   + '@media (prefers-color-scheme:dark){#gs-donate{background:'+C.dbg+';color:'+C.dfg+';border-color:'+C.dbg+'}}'
   + '@media print{#gs-donate{display:none}}';
  document.head.appendChild(s);
  var a = document.createElement('a');
  a.id = 'gs-donate'; a.href = C.href; a.textContent = C.label;
  a.setAttribute('aria-label', C.aria);
  (document.body || document.documentElement).appendChild(a);
})();
