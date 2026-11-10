(function(){
  var END = new Date('2026-11-19T06:00:00Z');
  if (new Date() >= END) return;
  var NOTICE = 'https://ntvgcd.org/documents/1966/Agenda.pdf';
  var MAIL = 'mailto:tgriffin@pcgcd.org?subject=' + encodeURIComponent('Comment for the Nov. 18 GMA 11 meeting: keep Scenario 26.1');
  var css = '#gma11-bar{position:sticky;top:0;z-index:99998;background:#0f4c6e;color:#fff;font:600 15px/1.4 Arial,sans-serif;padding:10px 44px 10px 14px;text-align:center}' +
    '#gma11-bar a{color:#fff;text-decoration:underline}' +
    '#gma11-bar button{position:absolute;right:8px;top:6px;background:none;border:0;color:#fff;font-size:22px;cursor:pointer}' +
    '#gma11-pop{position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.6);display:flex;align-items:center;justify-content:center;padding:16px}' +
    '#gma11-pop .box{background:#fff;color:#1d2420;max-width:460px;width:100%;border-radius:10px;padding:22px 20px;font:16px/1.5 Arial,sans-serif;position:relative;max-height:90vh;overflow:auto}' +
    '#gma11-pop h2{margin:0 0 8px;font:800 22px/1.2 Arial,sans-serif;color:#0f4c6e}' +
    '#gma11-pop p{margin:0 0 10px}' +
    '#gma11-pop .go{display:block;text-align:center;background:#0f4c6e;color:#fff;padding:12px;border-radius:6px;font-weight:700;text-decoration:none;margin:12px 0 8px}' +
    '#gma11-pop .x{position:absolute;right:10px;top:6px;background:none;border:0;font-size:26px;cursor:pointer;color:#555}' +
    '#gma11-pop small{color:#555}';
  function run(){
    var s = document.createElement('style'); s.textContent = css; document.head.appendChild(s);
    var bar = document.createElement('div'); bar.id = 'gma11-bar';
    bar.innerHTML = '\uD83D\uDCA7 Our water. Their vote. <strong>Wed., Nov. 18, 10 AM</strong>, Nacogdoches City Hall. <a href="' + MAIL + '">Email your comment</a> · <a href="' + NOTICE + '" target="_blank" rel="noopener">Notice</a>' +
      '<button aria-label="Hide">\u00D7</button>';
    bar.querySelector('button').onclick = function(){ bar.remove(); };
    document.body.insertBefore(bar, document.body.firstChild);
    var seen = false; try { seen = sessionStorage.getItem('gma11-pop') === '1'; } catch(e) {}
    if (seen) return;
    var pop = document.createElement('div'); pop.id = 'gma11-pop';
    pop.innerHTML = '<div class="box" role="dialog" aria-label="Water vote alert"><button class="x" aria-label="Close">\u00D7</button>' +
      '<h2>\uD83D\uDCA7 OUR WATER. THEIR VOTE. NOV. 18.</h2>' +
      '<p><strong>Wednesday, Nov. 18, 10 AM</strong><br>Room 119, Nacogdoches City Hall, 202 E. Pilar</p>' +
      '<p>East Texas\u2019s four groundwater districts (Groundwater Management Area 11) are scheduled to vote on adopting the official limits on how far our aquifers can drop through 2080, and to send them to the state.</p>' +
      '<p>Ask them to <strong>keep Scenario 26.1</strong> and to hold meetings when working families can attend.</p>' +
      '<a class="go" href="' + MAIL + '">Email your comment to GMA 11</a>' +
      '<p><small>Or sign up to speak before the meeting starts (3 minutes). <a href="' + NOTICE + '" target="_blank" rel="noopener">Read the official notice</a>.<br>Protect Our Piney Woods and the East Texas Legacy Coalition</small></p></div>';
    function close(){ pop.remove(); try { sessionStorage.setItem('gma11-pop','1'); } catch(e) {} }
    pop.querySelector('.x').onclick = close;
    pop.onclick = function(ev){ if (ev.target === pop) close(); };
    document.body.appendChild(pop);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
