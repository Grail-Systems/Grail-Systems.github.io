// Public information request builder for County Watch pages.
// Settings come from <section id="ask" data-county data-city data-edc data-gcd data-companies>.
(() => {
  const box = document.getElementById('ask'); if (!box) return;
  const D = box.dataset, COUNTY = D.county;
  const NAMES = {city: D.city || 'City of [name]', county: COUNTY + ' County', edc: D.edc || '[City] Economic Development Corporation',
    gcd: D.gcd || '[Name] Groundwater Conservation District', other: 'Agency name'};
  const PRESETS = {city: ['emails','water','abate','meetings'], county: ['emails','abate','roads','meetings'], edc: ['emails','abate','codes','meetings'],
    gcd: ['emails','wells','meetings'], other: ['emails','meetings']};
  const css = document.createElement('style');
  css.textContent = `#ask .builder{background:var(--card);border:1px solid var(--rule);padding:22px;margin-top:16px}
#ask .grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
#ask label{display:block;font-weight:600;margin-bottom:4px}#ask .hint{font-weight:400;color:var(--muted);font-size:.9rem}
#ask input[type=text],#ask input[type=date],#ask select,#ask textarea{width:100%;padding:10px 12px;border:1.5px solid var(--rule);background:var(--paper);color:var(--ink);font:inherit;font-size:1rem;border-radius:4px}
#ask fieldset{border:0;padding:0;margin:18px 0 0}#ask legend{font-weight:700;margin-bottom:6px}
#ask .check{display:grid;grid-template-columns:22px 1fr;gap:8px;align-items:start;padding:8px 0;border-top:1px solid var(--rule);font-weight:400}
#ask .check input{margin-top:5px;width:18px;height:18px}#ask .check b{font-weight:600}
#ask .actions{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}
#ask button,#ask .btn{background:var(--pine);color:var(--paper);border:0;padding:11px 18px;font:inherit;font-weight:700;cursor:pointer;border-radius:4px;text-decoration:none;display:inline-block}
#ask button.alt,#ask .btn.alt{background:transparent;color:var(--pine);border:1.5px solid var(--pine)}
#ask textarea{min-height:260px;font-family:Georgia,serif;line-height:1.5}#ask .ok{color:var(--pine);font-weight:600;min-height:1.4em}
#ask ol.tips li{margin:6px 0}
#rbPrint{display:none}
@media print{body *{visibility:hidden}#rbPrint,#rbPrint *{visibility:visible}#rbPrint{display:block;position:absolute;left:0;top:0;width:100%;white-space:pre-wrap;font-family:Georgia,serif;font-size:12pt;line-height:1.5;color:#000}}`;
  document.head.appendChild(css);
  const opt = (v, t) => `<option value="${v}">${t}</option>`;
  const chk = (v, b, t) => `<label class="check"><input type="checkbox" value="${v}"><span><b>${b}</b> ${t}</span></label>`;
  const esc = s => String(s || '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  box.innerHTML = `<h2>Ask for the records yourself</h2>
<p>The deals, the emails and the water promises come out through public information requests. Filing one is free. Fill this in and it writes the letter for you, using language from requests the East Texas Legacy Coalition has filed in Angelina County.</p>
<div class="builder">
 <div class="grid2">
  <div><label for="rbType">Who are you asking?</label><select id="rbType">${opt('county','The county')}${opt('city','A city')}${opt('edc','An economic development corporation (EDC)')}${opt('gcd','A groundwater conservation district')}${opt('other','Someone else')}</select></div>
  <div><label for="rbAgency">Agency’s full name <span class="hint">(check the exact name on its website)</span></label><input type="text" id="rbAgency"></div>
  <div><label for="rbOfficer">Send it to <span class="hint">(records officer or office)</span></label><input type="text" id="rbOfficer" placeholder="Public Information Officer"></div>
  <div><label for="rbCo">Companies or projects to name <span class="hint">(separate with commas)</span></label><input type="text" id="rbCo" placeholder="${esc(D.companies || 'Company or project names')}"></div>
  <div><label for="rbSince">Starting date</label><input type="date" id="rbSince"></div>
  <div><label for="rbName">Your name</label><input type="text" id="rbName" placeholder="Jane Doe"></div>
  <div><label for="rbContact">Your email or mailing address</label><input type="text" id="rbContact" placeholder="jane@example.com"></div>
 </div>
 <fieldset><legend>What to ask for <span class="hint">(we check the usual ones for the agency you picked)</span></legend>
  ${chk('emails','Emails and messages with the companies.','Between officials or staff and the companies you named.')}
  ${chk('water','Water deals.','Any agreement, draft, offer or term sheet to supply water.')}
  ${chk('abate','Tax breaks.','Abatement applications, incentive agreements and letters of support.')}
  ${chk('roads','Road and development agreements.','Road-use, development and host agreements, drafts included.')}
  ${chk('wells','Well permits.','Applications, permits and pumping reports for big wells.')}
  ${chk('codes','Project code names.','Code names for prospects and the incentives offered.')}
  ${chk('meetings','Meeting records.','Agendas, minutes and recordings.')}
 </fieldset>
 <div class="actions"><button type="button" id="rbMake">Write my letter</button></div>
 <textarea id="rbLetter" aria-label="Your letter" placeholder="Your letter will appear here. You can edit it before you send it."></textarea>
 <div class="actions"><button type="button" id="rbCopy">Copy</button><a class="btn alt" id="rbMail" href="#">Open in email</a><button type="button" class="alt" id="rbPrintBtn">Print</button></div>
 <div class="ok" id="rbMsg" role="status"></div>
</div>
<h3 style="margin-top:22px">Good to know before you send it</h3>
<ol class="tips">
 <li><strong>Send it to the official address.</strong> Use the agency’s public information email, online portal, mail or front desk.</li>
 <li><strong>You don’t have to say why.</strong> The agency can’t ask what you want the records for. It can ask you to clarify or narrow the request.</li>
 <li><strong>They’re on a clock.</strong> If records can’t be produced within 10 business days, the agency has to tell you in writing when they will be. To withhold something, it generally has to ask the Attorney General within 10 business days.</li>
 <li><strong>Watch for a cost estimate.</strong> If charges will top $40, the agency has to send an itemized estimate first. You then have 10 business days to accept it, narrow the request or ask for a waiver, or the request counts as withdrawn.</li>
 <li><strong>Keep a copy</strong> of what you sent and the date you sent it. Then <a href="mailto:contact@grailsystems.io?subject=Records%20for%20${encodeURIComponent(COUNTY)}%20County%20Watch">send us what you get back</a>; we check everything before it goes up.</li>
</ol>
<span class="src">Sources: Texas Government Code §552.221(d), §552.222, §552.2615, §552.301. This is general information, not legal advice. The Attorney General’s Open Government Hotline answers questions for free: 512-478-6736.</span>`;
  const pr = document.createElement('div'); pr.id = 'rbPrint'; document.body.appendChild(pr);
  const $ = id => document.getElementById(id);
  const boxes = [...box.querySelectorAll('.check input')];
  const preset = () => { const t = $('rbType').value; boxes.forEach(b => b.checked = PRESETS[t].includes(b.value)); $('rbAgency').placeholder = NAMES[t]; };
  $('rbType').addEventListener('change', preset); preset();
  $('rbSince').value = new Date(new Date().getFullYear() - 1, 0, 1).toISOString().slice(0, 10);
  function build() {
    const v = id => $(id).value.trim();
    const agency = v('rbAgency') || $('rbAgency').placeholder;
    const co = v('rbCo') || '[company or project names]';
    const since = v('rbSince') ? new Date(v('rbSince') + 'T12:00:00').toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'}) : '[starting date]';
    const today = new Date().toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
    const items = {
      emails: `All communications, including emails, text messages, letters and calendar invitations, between ${agency} officials or staff and ${co}, or anyone acting on their behalf, from ${since} to the present.`,
      water: `Any proposed, draft or signed agreement, offer, term sheet or correspondence concerning the supply of water to ${co}, or to any proposed data center, cryptocurrency mining facility or power generation facility, from ${since} to the present.`,
      abate: `Any tax abatement application, proposed or signed incentive agreement (including under Tax Code Chapter 312 or Local Government Code Chapter 380 or 381), letter of support, and related correspondence concerning ${co}, from ${since} to the present.`,
      roads: `Any proposed, draft or signed road-use, development, host community or similar agreement with ${co}, and related correspondence with the agency's attorneys or consultants about those agreements, from ${since} to the present.`,
      wells: `All well permit applications, permits, permit amendments and annual production reports for non-exempt wells, filed from ${since} to the present, including the applicant, well location and requested or reported volume. Please include any application by or on behalf of ${co}.`,
      codes: `Records sufficient to show the project code names used for business prospects from ${since} to the present, and the incentives offered or discussed for each.`,
      meetings: `Agendas, minutes and audio or video recordings for any meeting, from ${since} to the present, at which ${co}, or any proposed data center, cryptocurrency mining facility or power generation facility, was discussed.`
    };
    const picked = boxes.filter(b => b.checked).map(b => items[b.value]);
    if (!picked.length) { $('rbMsg').textContent = 'Check at least one thing to ask for.'; return ''; }
    const letter = `${today}\n\n${v('rbOfficer') || 'Public Information Officer'}\n${agency}\n\nRe: Public Information Act request\n\nUnder the Texas Public Information Act, Chapter 552 of the Texas Government Code, I request copies of the following records:\n\n${picked.map((t, i) => (i + 1) + '. ' + t).join('\n\n')}\n\nI prefer electronic copies sent by email, if available.\n\nIf the cost of this request will exceed $40, please send me an itemized estimate before filling it, as required by Section 552.2615. If you believe any part of these records is excepted from disclosure, please release the remaining records and tell me which parts are being withheld and why.\n\nThank you for your help.\n\n${v('rbName') || '[Your name]'}\n${v('rbContact') || '[Your email or mailing address]'}`;
    $('rbLetter').value = letter; $('rbMsg').textContent = 'Done. Read it over and edit anything you want before you send it.';
    return letter;
  }
  $('rbMake').addEventListener('click', build);
  $('rbCopy').addEventListener('click', async () => {
    const t = $('rbLetter').value || build(); if (!t) return;
    try { await navigator.clipboard.writeText(t); $('rbMsg').textContent = 'Copied. Paste it into an email to the agency’s public information address.'; }
    catch (e) { $('rbLetter').select(); $('rbMsg').textContent = 'Press Ctrl+C (or long-press and Copy) to copy the letter.'; }
  });
  $('rbMail').addEventListener('click', e => { e.preventDefault(); const t = $('rbLetter').value || build(); if (!t) return;
    location.href = 'mailto:?subject=' + encodeURIComponent('Public Information Act request') + '&body=' + encodeURIComponent(t); });
  $('rbPrintBtn').addEventListener('click', () => { const t = $('rbLetter').value || build(); if (!t) return; pr.textContent = t; window.print(); });
})();
