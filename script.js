/* ===== CONFIG (edit these) ===== */
const GAME = "Scrap Detective";
const GAME_URL = "https://scarp-detective.onrender.com/";
const FORM_URL = "https://xy.com"; // <- put your Google Form link here
const RELEASE_DATE = null;         // e.g. "2027-03-01T00:00:00" — null shows "TBA"
const EULA_VERSION = "v1";         // bump to re-prompt everyone

const PAGES = [
  ["index.html","Home"],["story.html","Story"],["characters.html","Characters"],
  ["features.html","Features"],["feedback-and-preregistration.html","Pre-Register"],
  ["info.html","Info"],["legal.html","Legal"]
];
const $ = (s,r=document)=>r.querySelector(s), $$ = (s,r=document)=>[...r.querySelectorAll(s)];
const safe = (f)=>{try{return f()}catch(e){return null}};

/* ===== THEME ===== */
const savedTheme = safe(()=>localStorage.getItem("sd_theme"));
if(savedTheme) document.documentElement.dataset.theme = savedTheme;

/* ===== NAV + FOOTER ===== */
function buildChrome(){
  const here = location.pathname.split("/").pop() || "index.html";
  const links = PAGES.map(([h,t])=>`<a href="${h}" class="${h===here?'active':''}">${t}</a>`).join("")
    + `<a href="${GAME_URL}" class="ext" target="_blank" rel="noopener">▶ Play Game</a>`;
  document.body.insertAdjacentHTML("afterbegin",
   `<div id="progress"></div><canvas id="petals"></canvas>
    <header class="nav"><div class="wrap">
      <a class="logo" href="index.html">🔍 ${GAME}</a>
      <nav class="links" id="links">${links}
        <button class="icon-btn" id="themeBtn" title="Toggle theme">🌓</button></nav>
      <button class="icon-btn" id="burger" aria-label="Menu">☰</button>
    </div></header>`);
  document.body.insertAdjacentHTML("beforeend",
   `<footer><div class="wrap"><div class="fgrid">
      <div><h3 style="color:var(--red)">${GAME}</h3><p style="color:var(--muted)">A story of a scrap kid, a cruel world, and the choices that make him.</p></div>
      <div><b>Explore</b>${PAGES.slice(0,4).map(([h,t])=>`<a href="${h}">${t}</a>`).join("")}<a href="${GAME_URL}" target="_blank" rel="noopener">▶ Play Game</a></div>
      <div><b>Community</b><a href="feedback-and-preregistration.html">Pre-Register</a><a href="${FORM_URL}" target="_blank" rel="noopener">Feedback Form</a><a href="info.html">Contact</a><a href="info.html#faq">FAQ</a></div>
      <div><b>Legal</b><a href="legal.html#eula">EULA</a><a href="legal.html#privacy">Privacy</a><a href="legal.html#terms">Terms</a><a href="#" id="reEula">Review EULA</a></div>
     </div><p class="copy">© <span id="yr"></span> ${GAME}. All rights reserved.</p></div></footer>
    <button class="btn primary" id="toTop">↑</button>
    <div id="eula"><div class="modal" role="dialog" aria-modal="true" aria-labelledby="eulaT">
      <h2 id="eulaT">End User License Agreement</h2>
      <div class="body" id="eulaBody"><!-- ADD YOUR EULA TEXT HERE (HTML allowed) --></div>
      <div class="act">
        <label><input type="checkbox" id="eulaChk"> I have read and accept the EULA</label>
        <button class="btn primary" id="eulaOk" disabled>Accept</button>
        <button class="btn ghost" id="eulaNo">Decline</button>
      </div></div></div>`);
  $("#yr").textContent = new Date().getFullYear();
  $("#burger").onclick = ()=>$("#links").classList.toggle("open");
  $("#themeBtn").onclick = ()=>{
    const d=document.documentElement, n=d.dataset.theme==="light"?"dark":"light";
    d.dataset.theme=n; safe(()=>localStorage.setItem("sd_theme",n));
  };
  // any <a data-game> links to the game, any <a data-form> links to the Google Form
  $$("[data-game]").forEach(a=>{a.href=GAME_URL;a.target="_blank";a.rel="noopener"});
  $$("[data-form]").forEach(a=>{a.href=FORM_URL;a.target="_blank";a.rel="noopener"});
  // embedded copy of the form: <iframe data-formframe>
  $$("[data-formframe]").forEach(f=>{f.src=FORM_URL+(FORM_URL.includes("?")?"&":"?")+"embedded=true"});
}

/* ===== EULA ===== */
function eula(){
  const key="sd_eula_"+EULA_VERSION, box=$("#eula");
  const show=()=>{box.classList.add("show");document.body.style.overflow="hidden"};
  const hide=()=>{box.classList.remove("show");document.body.style.overflow=""};
  if(!safe(()=>localStorage.getItem(key))) show();
  $("#eulaChk").onchange=e=>$("#eulaOk").disabled=!e.target.checked;
  $("#eulaOk").onclick=()=>{safe(()=>localStorage.setItem(key,new Date().toISOString()));hide()};
  $("#eulaBody").dataset.keep=$("#eulaBody").innerHTML;
  $("#eulaNo").onclick=()=>{$("#eulaBody").innerHTML="<p><b>You must accept the EULA to use this website.</b> Close this tab or review the agreement again.</p>"+$("#eulaBody").dataset.keep;};
  $("#reEula").onclick=e=>{e.preventDefault();$("#eulaChk").checked=false;$("#eulaOk").disabled=true;show()};
}

/* ===== SCROLL FX ===== */
function scrollFx(){
  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("show");io.unobserve(e.target)}}),{threshold:.12});
  $$(".reveal").forEach(el=>io.observe(el));
  addEventListener("scroll",()=>{
    const h=document.documentElement,p=h.scrollTop/(h.scrollHeight-h.clientHeight)*100;
    $("#progress").style.width=p+"%"; $("#toTop").style.display=h.scrollTop>500?"block":"none";
  });
  $("#toTop").onclick=()=>scrollTo({top:0});
  $$("[data-count]").forEach(el=>{
    const o=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;o.disconnect();
      const t=+el.dataset.count;let n=0;const s=setInterval(()=>{n+=Math.ceil(t/40);if(n>=t){n=t;clearInterval(s)}el.textContent=n},30)});
    o.observe(el);
  });
}

/* ===== FALLING PETALS ===== */
function petals(){
  const c=$("#petals"),x=c.getContext("2d");let W,H;
  const rs=()=>{W=c.width=innerWidth;H=c.height=innerHeight};rs();addEventListener("resize",rs);
  const P=Array.from({length:34},()=>({x:Math.random()*W,y:Math.random()*H,r:3+Math.random()*5,s:.4+Math.random()*1.1,d:Math.random()*6,c:Math.random()>.5?"#c0392b":"#e79700"}));
  (function f(){x.clearRect(0,0,W,H);P.forEach(p=>{p.y+=p.s;p.d+=.02;p.x+=Math.sin(p.d)*.8;
    if(p.y>H){p.y=-10;p.x=Math.random()*W}x.fillStyle=p.c;x.beginPath();x.ellipse(p.x,p.y,p.r,p.r/2,p.d,0,7);x.fill()});requestAnimationFrame(f)})();
}

/* ===== COUNTDOWN ===== */
function countdown(){
  const el=$("#countdown");if(!el)return;
  if(!RELEASE_DATE){el.innerHTML='<div style="min-width:0"><b>TBA</b>Release date to be announced</div>';return}
  const t=new Date(RELEASE_DATE).getTime();
  const tick=()=>{let d=Math.max(0,t-Date.now());
    const v=[["Days",86400000],["Hours",3600000],["Mins",60000],["Secs",1000]].map(([n,m])=>{const k=Math.floor(d/m);d-=k*m;return`<div><b>${k}</b>${n}</div>`});
    el.innerHTML=v.join("")};tick();setInterval(tick,1000);
}

/* ===== CHARACTER FILTER ===== */
function filters(){
  $$("[data-filter]").forEach(b=>b.onclick=()=>{
    $$("[data-filter]").forEach(x=>x.classList.remove("primary"));b.classList.add("primary");
    $$("[data-cat]").forEach(c=>c.style.display=(b.dataset.filter==="all"||c.dataset.cat===b.dataset.filter)?"":"none");
  });
}

/* ===== BOOT ===== */
document.addEventListener("DOMContentLoaded",()=>{
  buildChrome();eula();scrollFx();petals();countdown();filters();
});
