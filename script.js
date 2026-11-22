document.documentElement.classList.add("js");

/* ===== CONFIG (edit these) ===== */
const GAME = "Scrap Detective";
const GAME_URL = "https://scarp-detective.onrender.com/";
const FORM_URL = "https://forms.gle/MQMB6QMC6rYMGHqR9";
const EMAIL = "depressivemasterpiece@gmail.com";
const EULA_VERSION = "v1"; // bump to ask everyone to accept again

const PAGES = [
  ["index.html","Home"],["story.html","Story"],["characters.html","Characters"],
  ["features.html","Features"],["feedback.html","Feedback"],
  ["info.html","Info"],["legal.html","Legal"]
];
const $ = (s,r=document)=>r.querySelector(s), $$ = (s,r=document)=>[...r.querySelectorAll(s)];
const safe = f=>{try{return f()}catch(e){return null}};

/* ===== THEME (applied immediately to avoid flash) ===== */
const savedTheme = safe(()=>localStorage.getItem("sd_theme"));
if(savedTheme) document.documentElement.dataset.theme = savedTheme;

/* ===== NAV + FOOTER + EULA MARKUP ===== */
function buildChrome(){
  const here = location.pathname.split("/").pop() || "index.html";
  const links = PAGES.map(([h,t])=>`<a href="${h}"${h===here?' class="active" aria-current="page"':''}>${t}</a>`).join("")
    + `<a href="${GAME_URL}" class="ext" target="_blank" rel="noopener">▶ Play Game</a>`;
  document.body.insertAdjacentHTML("afterbegin",
   `<a class="skip" href="#main">Skip to content</a><div id="progress"></div><canvas id="petals" aria-hidden="true"></canvas>
    <header class="nav"><div class="wrap">
      <a class="logo" href="index.html">🔍 ${GAME}</a>
      <nav class="links" id="links" aria-label="Main">${links}
        <button class="icon-btn" id="themeBtn" title="Toggle light/dark theme" aria-label="Toggle theme">🌓</button></nav>
      <button class="icon-btn" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="links">☰</button>
    </div></header>`);
  document.body.insertAdjacentHTML("beforeend",
   `<footer><div class="wrap"><div class="fgrid">
      <div><h3 style="color:var(--red)">${GAME}</h3><p style="color:var(--muted)">A story of a scrap kid, a cruel world, and the choices that make him.</p></div>
      <div><b>Explore</b>${PAGES.slice(0,4).map(([h,t])=>`<a href="${h}">${t}</a>`).join("")}<a href="${GAME_URL}" target="_blank" rel="noopener">▶ Play Game</a></div>
      <div><b>Community</b><a href="${FORM_URL}" target="_blank" rel="noopener">Feedback Form</a><a href="info.html">Contact &amp; Credits</a><a href="info.html#faq">FAQ</a></div>
      <div><b>Legal</b><a href="legal.html#privacy">Privacy Policy</a><a href="legal.html#copyright">Copyright Notice</a><a href="legal.html#eula">EULA</a><a href="legal.html#thirdparty">Third-Party Licenses</a><a href="#" id="reEula">Review EULA</a></div>
     </div><p class="copy">© 2026 depressivemasterpiece (Daksh and Trickinstin). All rights reserved. ${GAME}, its story, characters, code and artwork may not be copied, redistributed or republished without written permission.</p></div></footer>
    <button class="btn primary" id="toTop" aria-label="Back to top">↑</button>
    <div id="eula"><div class="modal" role="dialog" aria-modal="true" aria-labelledby="eulaT">
      <h2 id="eulaT">End User License Agreement</h2>
      <div class="body" id="eulaBody"><!-- ADD YOUR EULA TEXT HERE (HTML allowed) --></div>
      <div class="act">
        <label><input type="checkbox" id="eulaChk"> I have read and accept the EULA</label>
        <button class="btn primary" id="eulaOk" disabled>Accept</button>
        <button class="btn ghost" id="eulaNo">Decline</button>
      </div></div></div>`);

  $("#burger").onclick=e=>{const o=$("#links").classList.toggle("open");e.currentTarget.setAttribute("aria-expanded",o)};
  $("#themeBtn").onclick=()=>{
    const d=document.documentElement,n=d.dataset.theme==="light"?"dark":"light";
    d.dataset.theme=n;safe(()=>localStorage.setItem("sd_theme",n));
  };
  // attribute-driven links: data-game, data-form, data-mail
  $$("[data-game]").forEach(a=>{a.href=GAME_URL;a.target="_blank";a.rel="noopener"});
  $$("[data-form]").forEach(a=>{a.href=FORM_URL;a.target="_blank";a.rel="noopener"});
  $$("[data-mail]").forEach(a=>{a.href="mailto:"+EMAIL;if(!a.textContent.trim())a.textContent=EMAIL});
  const m=$("main");if(m)m.id="main";
}

/* ===== EULA ===== */
function eula(){
  const key="sd_eula_"+EULA_VERSION,box=$("#eula"),body=$("#eulaBody");
  const keep=body.innerHTML;
  const show=()=>{box.classList.add("show");document.body.style.overflow="hidden";$("#eulaChk").focus()};
  const hide=()=>{box.classList.remove("show");document.body.style.overflow=""};
  if(!safe(()=>localStorage.getItem(key)))show();
  $("#eulaChk").onchange=e=>$("#eulaOk").disabled=!e.target.checked;
  $("#eulaOk").onclick=()=>{safe(()=>localStorage.setItem(key,new Date().toISOString()));hide()};
  $("#eulaNo").onclick=()=>{body.innerHTML="<p><b>You must accept the EULA to use this website.</b> Close this tab, or review the agreement again.</p>"+keep;body.scrollTop=0};
  $("#reEula").onclick=e=>{e.preventDefault();body.innerHTML=keep;$("#eulaChk").checked=false;$("#eulaOk").disabled=true;show()};
}

/* ===== SCROLL EFFECTS ===== */
function scrollFx(){
  const els=$$(".reveal");
  if("IntersectionObserver" in window){
    const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("show");io.unobserve(e.target)}}),{threshold:.1});
    els.forEach(el=>io.observe(el));
  }else els.forEach(el=>el.classList.add("show"));

  const bar=$("#progress"),top=$("#toTop");let tick=false;
  const upd=()=>{const h=document.documentElement,max=h.scrollHeight-h.clientHeight;
    bar.style.transform=`scaleX(${max>0?h.scrollTop/max:0})`;top.style.display=h.scrollTop>500?"block":"none";tick=false};
  addEventListener("scroll",()=>{if(!tick){tick=true;requestAnimationFrame(upd)}},{passive:true});
  top.onclick=()=>scrollTo({top:0});

  $$("[data-count]").forEach(el=>{
    if(!("IntersectionObserver" in window)){el.textContent=el.dataset.count;return}
    const o=new IntersectionObserver(([e])=>{if(!e.isIntersecting)return;o.disconnect();
      const t=+el.dataset.count;let n=0;const s=setInterval(()=>{n+=Math.ceil(t/30);if(n>=t){n=t;clearInterval(s)}el.textContent=n},35)});
    o.observe(el);
  });
}

/* ===== FALLING PETALS (light, pauses when tab hidden, off for reduced motion) ===== */
function petals(){
  const c=$("#petals");
  if(matchMedia("(prefers-reduced-motion: reduce)").matches){c.remove();return}
  const x=c.getContext("2d");let W,H,raf;
  const rs=()=>{W=c.width=innerWidth;H=c.height=innerHeight};rs();addEventListener("resize",rs);
  const n=innerWidth<700?12:26;
  const P=Array.from({length:n},()=>({x:Math.random()*W,y:Math.random()*H,r:3+Math.random()*5,s:.4+Math.random()*1.1,d:Math.random()*6,c:Math.random()>.5?"#c0392b":"#e79700"}));
  const f=()=>{x.clearRect(0,0,W,H);for(const p of P){p.y+=p.s;p.d+=.02;p.x+=Math.sin(p.d)*.8;
    if(p.y>H){p.y=-10;p.x=Math.random()*W}x.fillStyle=p.c;x.beginPath();x.ellipse(p.x,p.y,p.r,p.r/2,p.d,0,7);x.fill()}raf=requestAnimationFrame(f)};
  f();
  document.addEventListener("visibilitychange",()=>{if(document.hidden)cancelAnimationFrame(raf);else f()});
}

/* ===== CHARACTER FILTER ===== */
function filters(){
  $$("[data-filter]").forEach(b=>b.onclick=()=>{
    $$("[data-filter]").forEach(x=>{x.classList.remove("primary");x.classList.add("ghost")});
    b.classList.add("primary");b.classList.remove("ghost");
    $$("[data-cat]").forEach(c=>c.hidden=!(b.dataset.filter==="all"||c.dataset.cat===b.dataset.filter));
  });
}

/* ===== BOOT ===== */
document.addEventListener("DOMContentLoaded",()=>{buildChrome();eula();scrollFx();petals();filters()});
