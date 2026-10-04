
LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>ورود · TokenPanel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
  --glass:rgba(255,255,255,.05);--border:rgba(255,255,255,.12);
  --accent:#6366f1;--accent2:#8b5cf6;--cyan:#22d3ee;
  --txt:#f1f5f9;--t2:rgba(241,245,249,.62);--t3:rgba(241,245,249,.38);
}
html,body{height:100%}
body{font-family:Vazirmatn,sans-serif;background:#020208;color:var(--txt);display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.bg{position:fixed;inset:0;z-index:0;background:
 radial-gradient(1000px 620px at 85% -10%,rgba(99,102,241,.17),transparent 60%),
 radial-gradient(900px 560px at 8% 112%,rgba(139,92,246,.15),transparent 60%),
 radial-gradient(760px 520px at 50% 55%,rgba(34,211,238,.06),transparent 65%),#020208;
 animation:aurora 14s ease-in-out infinite alternate}
@keyframes aurora{0%{filter:hue-rotate(0deg) saturate(1)}100%{filter:hue-rotate(24deg) saturate(1.18)}}
.bg::before{content:'';position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.028) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.028) 1px,transparent 1px);background-size:44px 44px;-webkit-mask-image:radial-gradient(ellipse 72% 62% at 50% 45%,#000 25%,transparent 78%);mask-image:radial-gradient(ellipse 72% 62% at 50% 45%,#000 25%,transparent 78%)}
.orb{position:fixed;border-radius:50%;filter:blur(85px);opacity:.5;z-index:0;animation:orbFloat 17s ease-in-out infinite}
.orb1{width:400px;height:400px;background:rgba(99,102,241,.36);top:-120px;right:-100px}
.orb2{width:330px;height:330px;background:rgba(139,92,246,.3);bottom:-100px;left:-80px;animation-delay:-6s;animation-duration:20s}
.orb3{width:230px;height:230px;background:rgba(34,211,238,.2);top:56%;right:14%;animation-delay:-10s;animation-duration:23s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(-32px,28px) scale(1.1)}66%{transform:translate(26px,-22px) scale(.92)}}
.stage{position:relative;z-index:2;width:100%;max-width:432px;padding:22px}
.card{position:relative;background:linear-gradient(160deg,rgba(255,255,255,.075),rgba(255,255,255,.02));border:1px solid var(--border);border-radius:28px;padding:40px 34px 24px;backdrop-filter:blur(30px) saturate(170%);-webkit-backdrop-filter:blur(30px) saturate(170%);box-shadow:0 32px 90px rgba(0,0,0,.55),inset 0 1px 0 rgba(255,255,255,.14);animation:cardIn .85s cubic-bezier(.22,1,.36,1) both;overflow:hidden}
.card::before{content:'';position:absolute;inset:-1px;border-radius:28px;padding:1px;background:linear-gradient(135deg,rgba(99,102,241,.55),transparent 32%,transparent 62%,rgba(139,92,246,.5),rgba(34,211,238,.3));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;animation:borderFlow 6s linear infinite;background-size:220% 220%}
@keyframes borderFlow{0%{background-position:0% 0%}100%{background-position:100% 100%}}
@keyframes cardIn{from{opacity:0;transform:translateY(38px) scale(.93)}to{opacity:1;transform:none}}
.card-glow{position:absolute;top:-80px;left:50%;transform:translateX(-50%);width:280px;height:140px;background:radial-gradient(ellipse,rgba(99,102,241,.3),transparent 70%);filter:blur(30px);animation:glowPulse 5s ease-in-out infinite;pointer-events:none}
@keyframes glowPulse{0%,100%{opacity:.5}50%{opacity:1}}
.brand{display:flex;flex-direction:column;align-items:center;gap:14px;margin-bottom:28px}
.glyph{width:68px;height:68px;border-radius:23px;display:flex;align-items:center;justify-content:center;font-size:31px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2) 60%,var(--cyan));box-shadow:0 12px 34px rgba(99,102,241,.45),inset 0 1px 0 rgba(255,255,255,.4);position:relative;animation:glyphFloat 4.5s ease-in-out infinite}
.glyph::after{content:'';position:absolute;inset:-8px;border-radius:29px;border:1.5px solid transparent;border-top-color:rgba(139,92,246,.75);border-right-color:rgba(34,211,238,.45);animation:ringSpin 3.4s linear infinite}
@keyframes glyphFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
@keyframes ringSpin{to{transform:rotate(360deg)}}
.brand-name{font-size:28px;font-weight:900;letter-spacing:.4px;background:linear-gradient(90deg,#a5b4fc,#e0e7ff,#c4b5fd,#67e8f9,#a5b4fc);background-size:220% auto;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;animation:textFlow 4.5s linear infinite}
@keyframes textFlow{to{background-position:220% center}}
.brand-sub{font-size:11.5px;color:var(--t3);display:flex;align-items:center;gap:5px}
.brand-sub i{color:var(--accent2)}
h1{font-size:15.5px;font-weight:700;text-align:center;color:var(--t2);margin-bottom:22px;animation:fadeUp .6s .18s both}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.field{margin-bottom:16px;animation:fadeUp .6s .28s both}
.field label{display:block;font-size:12px;font-weight:600;color:var(--t2);margin-bottom:8px}
.inp-wrap{position:relative}
.inp-wrap .ic{position:absolute;right:14px;top:50%;transform:translateY(-50%);font-size:17px;color:var(--t3);pointer-events:none;transition:color .25s}
input[type=password],input[type=text]{width:100%;background:rgba(255,255,255,.045);border:1px solid var(--border);border-radius:14px;padding:13px 44px 13px 46px;font-family:inherit;font-size:14px;color:var(--txt);outline:none;transition:border-color .25s,box-shadow .25s,background .25s}
input::placeholder{color:var(--t3)}
input:focus{border-color:rgba(99,102,241,.65);background:rgba(99,102,241,.06);box-shadow:0 0 0 4px rgba(99,102,241,.14),0 0 22px rgba(99,102,241,.18)}
input:focus~.ic{color:#a5b4fc}
.eye{position:absolute;left:12px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:17px;padding:4px;transition:color .2s}
.eye:hover{color:var(--t2)}
.btn{position:relative;width:100%;display:flex;align-items:center;justify-content:center;gap:8px;border:none;border-radius:14px;padding:14px;font-family:inherit;font-size:14.5px;font-weight:800;color:#fff;cursor:pointer;background:linear-gradient(135deg,var(--accent),var(--accent2));box-shadow:0 10px 28px rgba(99,102,241,.4),inset 0 1px 0 rgba(255,255,255,.25);transition:transform .18s,box-shadow .25s,filter .25s;overflow:hidden;animation:fadeUp .6s .38s both}
.btn:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 14px 36px rgba(99,102,241,.5);filter:brightness(1.06)}
.btn:active:not(:disabled){transform:translateY(0) scale(.985)}
.btn:disabled{opacity:.75;cursor:not-allowed}
.btn::after{content:'';position:absolute;top:0;bottom:0;width:46%;left:-70%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-18deg);animation:btnShine 3.4s ease-in-out infinite}
@keyframes btnShine{0%,62%{left:-70%}92%,100%{left:150%}}
.hint{margin-top:15px;display:flex;align-items:center;justify-content:center;gap:7px;font-size:11px;color:var(--t3);background:rgba(255,255,255,.03);border:1px dashed rgba(255,255,255,.12);border-radius:11px;padding:9px;animation:fadeUp .6s .48s both}
.hint-label{display:flex;align-items:center;gap:5px}
.hint-val{color:#a5b4fc;font-weight:800;cursor:pointer;letter-spacing:.4px;transition:text-shadow .2s}
.hint-val:hover{text-shadow:0 0 12px rgba(165,180,252,.7)}
.err{display:none;align-items:center;gap:8px;background:rgba(239,68,68,.1);border:1px solid rgba(239,68,68,.35);color:#fca5a5;font-size:12px;border-radius:12px;padding:11px 13px;margin-bottom:14px;animation:shake .4s ease}
.err.show{display:flex}
@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(6px)}50%{transform:translateX(-6px)}75%{transform:translateX(3px)}}
.footer{margin-top:20px;text-align:center;font-size:11.5px;color:var(--t3);animation:fadeUp .6s .58s both}
.footer a{color:#a5b4fc;text-decoration:none;font-weight:700;display:inline-flex;align-items:center;gap:4px;transition:text-shadow .2s}
.footer a:hover{text-shadow:0 0 12px rgba(165,180,252,.7)}
@keyframes spin{to{transform:rotate(360deg)}}
@media(max-width:430px){.card{padding:32px 24px 20px}.brand-name{font-size:24px}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}
</style>
</head>
<body>
<div class="bg"></div>
<div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div>
<div class="stage">
  <div class="card">
    <div class="card-glow"></div>
    <div class="brand">
      <div class="glyph"><i class="ti ti-bolt"></i></div>
      <div class="brand-name">TokenPanel</div>
      <div class="brand-sub"><i class="ti ti-bolt"></i> VLESS Tunnel · v12</div>
    </div>
    <h1>برای ورود رمز عبور پنل را وارد کنید</h1>
    <div class="err" id="err"><i class="ti ti-alert-circle"></i><span id="err-text"></span></div>
    <form id="form">
      <div class="field">
        <label>رمز عبور</label>
        <div class="inp-wrap">
          <input type="password" id="pw" placeholder="رمز عبور را وارد کنید" autofocus required>
          <i class="ti ti-lock ic"></i>
          <button class="eye" type="button" onclick="togglePw(this)"><i class="ti ti-eye"></i></button>
        </div>
      </div>
      <button class="btn" type="submit" id="btn"><i class="ti ti-login-2"></i> ورود به داشبورد</button>
    </form>
    <div class="hint">
      <span class="hint-label"><i class="ti ti-key"></i> رمز پیش‌فرض سیستم:</span>
      <span class="hint-val" onclick="document.getElementById('pw').type='text';document.getElementById('pw').value='tokenshack';document.getElementById('pw').focus()">tokenshack</span>
    </div>
    <div class="footer"><i class="ti ti-code"></i> سازنده: <a href="https://t.me/tokenshack" target="_blank"><i class="ti ti-brand-telegram"></i> @tokenshack</a></div>
  </div>
</div>
<script>
function togglePw(btn){
  const pw=document.getElementById('pw');
  const show=pw.type==='password';
  pw.type=show?'text':'password';
  btn.innerHTML='<i class="ti '+(show?'ti-eye-off':'ti-eye')+'"></i>';
}
document.getElementById('form').addEventListener('submit',async e=>{
  e.preventDefault();
  const btn=document.getElementById('btn'),err=document.getElementById('err'),et=document.getElementById('err-text');
  err.classList.remove('show');btn.disabled=true;
  btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ورود...';
  try{
    const r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:document.getElementById('pw').value})});
    if(!r.ok){const d=await r.json().catch(()=>({}));throw new Error(d.detail||'خطا');}
    location.href='/dashboard';
  }catch(e){
    et.textContent=e.message;err.classList.add('show');
    btn.disabled=false;btn.innerHTML='<i class="ti ti-login-2"></i> ورود به داشبورد';
  }
});
</script>
</body></html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TokenPanel</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#030308;--bg2:#06060e;--bg3:#0a0a16;
  --card:rgba(255,255,255,0.045);--card-b:rgba(255,255,255,0.09);--card-bh:rgba(129,165,255,0.38);
  --accent:#4D8DFF;--accent2:#7FB0FF;--accent-d:rgba(77,141,255,0.12);
  --green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#3DDFA9;
  --red:#FF4D5E;--red-bg:rgba(255,77,94,0.1);--red-t:#FF8A96;
  --amber:#FFB020;--amber-bg:rgba(255,176,32,0.1);--amber-t:#FFD066;
  --purple:#A855F7;--purple-bg:rgba(168,85,247,0.12);
  --t1:#F4F7FF;--t2:#A7B4D6;--t3:#5F6C90;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 10px 34px rgba(0,0,0,0.45);
}
[data-theme="light"]{
  --bg:#EEF2FA;--bg2:#E3EAF6;--bg3:#D6E1F2;
  --card:rgba(255,255,255,0.72);--card-b:rgba(30,60,120,0.1);--card-bh:rgba(37,99,235,0.35);
  --accent:#2563EB;--accent2:#1D4ED8;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#047857;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#B91C1C;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#7C3AED;--purple-bg:rgba(124,58,237,0.08);
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --shadow:0 8px 26px rgba(30,50,90,0.1);
}
html{scroll-behavior:smooth}
html,body{height:100%}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;overflow-x:hidden}
body::before{content:'';position:fixed;inset:-22%;background:radial-gradient(ellipse 42% 32% at 16% 6%,rgba(77,141,255,.14),transparent 60%),radial-gradient(ellipse 40% 30% at 86% 18%,rgba(168,85,247,.11),transparent 60%),radial-gradient(ellipse 50% 36% at 50% 110%,rgba(16,185,129,.08),transparent 65%);filter:blur(10px);z-index:0;pointer-events:none;animation:aurora 18s ease-in-out infinite alternate}
@keyframes aurora{0%{transform:translateY(0) scale(1)}50%{transform:translateY(-2.5%) scale(1.04)}100%{transform:translateY(1.5%) scale(1.02)}}
body::after{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,.028) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.028) 1px,transparent 1px);background-size:44px 44px;z-index:0;pointer-events:none;mask-image:radial-gradient(ellipse 90% 72% at 50% 0%,#000 0%,transparent 80%);-webkit-mask-image:radial-gradient(ellipse 90% 72% at 50% 0%,#000 0%,transparent 80%)}
[data-theme="light"] body::before{opacity:.4}
[data-theme="light"] body::after{background-image:linear-gradient(rgba(20,50,110,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(20,50,110,.05) 1px,transparent 1px)}
.fx-orb{position:fixed;border-radius:50%;filter:blur(70px);z-index:0;pointer-events:none;opacity:.5;animation:orbFloat 12s ease-in-out infinite}
.fxo1{width:420px;height:420px;background:rgba(77,141,255,.12);top:-140px;right:-120px}
.fxo2{width:340px;height:340px;background:rgba(168,85,247,.1);bottom:-120px;left:-100px;animation-delay:3.5s;animation-duration:14s}
.fxo3{width:260px;height:260px;background:rgba(16,185,129,.08);top:44%;left:34%;animation-delay:6.5s;animation-duration:16s}
@keyframes orbFloat{0%,100%{transform:translate(0,0) scale(1)}33%{transform:translate(26px,-30px) scale(1.07)}66%{transform:translate(-20px,22px) scale(.94)}}
[data-theme="light"] .fx-orb{opacity:.25}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:3px}
::-webkit-scrollbar-thumb:hover{background:rgba(77,141,255,.45)}
[data-theme="light"] ::-webkit-scrollbar-thumb{background:rgba(20,50,110,.2)}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:rgba(6,7,14,.66);backdrop-filter:blur(26px) saturate(150%);-webkit-backdrop-filter:blur(26px) saturate(150%);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .3s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
[data-theme="light"] .sidebar{background:rgba(255,255,255,.65)}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b);position:relative;overflow:hidden}
.logo::after{content:'';position:absolute;bottom:0;right:0;left:0;height:1px;background:linear-gradient(90deg,transparent,rgba(77,141,255,.5),rgba(168,85,247,.4),transparent);animation:lineFlow 4s linear infinite;background-size:200% auto}
@keyframes lineFlow{to{background-position:200% center}}
.logo-img{width:38px;height:38px;border-radius:13px;position:relative;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:19px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2) 60%,var(--cyan));box-shadow:0 6px 18px rgba(99,102,241,.4),inset 0 1px 0 rgba(255,255,255,.35);animation:logoFloat 4.5s ease-in-out infinite}
.logo-img::after{content:'';position:absolute;inset:-5px;border-radius:17px;border:1.5px solid transparent;border-top-color:var(--accent2);border-right-color:rgba(34,211,238,.6);animation:ringSpin 3.4s linear infinite}
@keyframes ringSpin{to{transform:rotate(360deg)}}
@keyframes logoFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-3px)}}
.logo-name{font-size:13.5px;font-weight:800;background:linear-gradient(90deg,#7FB0FF,#C4B5FD,#7FB0FF);background-size:200% auto;-webkit-background-clip:text;background-clip:text;color:transparent;animation:textFlow 5s linear infinite}
[data-theme="light"] .logo-name{background:linear-gradient(90deg,#2563EB,#7C3AED,#2563EB);background-size:200% auto;-webkit-background-clip:text;background-clip:text}
@keyframes textFlow{to{background-position:200% center}}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer;transition:.2s}
.sb-close:hover{color:var(--red-t);border-color:rgba(255,77,94,.3)}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .22s cubic-bezier(.4,0,.2,1);margin:1px 6px;border-radius:9px 0 0 9px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0;transition:.22s}
.nav-it:hover{background:rgba(255,255,255,.05);color:var(--t1);transform:translateX(-3px)}
[data-theme="light"] .nav-it:hover{background:rgba(37,99,235,.07)}
.nav-it:hover i{color:var(--accent2)}
.nav-it.on{background:linear-gradient(90deg,rgba(77,141,255,.16),rgba(77,141,255,.02));color:var(--t1);border-right-color:var(--accent);font-weight:600;box-shadow:inset 0 0 22px rgba(77,141,255,.07)}
[data-theme="light"] .nav-it.on{background:linear-gradient(90deg,rgba(37,99,235,.12),rgba(37,99,235,.02))}
.nav-it.on i{color:var(--accent2);filter:drop-shadow(0 0 6px rgba(77,141,255,.55))}
.nav-badge{margin-right:auto;background:rgba(77,141,255,.16);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.tg-btn{display:flex;align-items:center;justify-content:center;gap:8px;background:linear-gradient(135deg,#0098e6,#0077bb);color:#fff;border-radius:9px;padding:10px;font-size:12.5px;font-weight:600;font-family:inherit;border:none;cursor:pointer;width:100%;transition:.22s}
.tg-btn:hover{filter:brightness(1.12);transform:translateY(-1px);box-shadow:0 6px 18px rgba(0,136,224,.35)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:rgba(255,255,255,.05);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.22s;margin-bottom:7px}
[data-theme="light"] .theme-btn{background:rgba(37,99,235,.06)}
.theme-btn:hover{background:var(--accent-d);color:var(--t1);transform:translateY(-1px)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(255,77,94,.2);cursor:pointer;width:100%;transition:.22s;margin-top:6px}
.logout-btn:hover{background:rgba(255,77,94,.2);transform:translateY(-1px);box-shadow:0 4px 14px rgba(255,77,94,.25)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:rgba(6,7,14,.75);backdrop-filter:blur(22px) saturate(150%);-webkit-backdrop-filter:blur(22px) saturate(150%);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
[data-theme="light"] .mob-top{background:rgba(255,255,255,.7)}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:15px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2));box-shadow:0 0 12px rgba(99,102,241,.45);animation:logoGlow 3s ease-in-out infinite}
@keyframes logoGlow{0%,100%{box-shadow:0 0 10px rgba(99,102,241,.3)}50%{box-shadow:0 0 20px rgba(139,92,246,.6)}}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn,.theme-mob{background:rgba(255,255,255,.05);border:1px solid var(--card-b);color:var(--t2);width:34px;height:34px;border-radius:8px;font-size:17px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.22s}
.menu-btn:hover,.theme-mob:hover{color:var(--t1);border-color:var(--card-bh);transform:translateY(-1px)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(4px)}
.overlay.show{display:block;animation:fadeIn .25s}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .3s;position:relative;z-index:10}
.pg{display:none}
.pg.on{display:block;animation:pgIn .45s cubic-bezier(.22,1,.36,1)}
@keyframes pgIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes fadeUp{from{opacity:0;transform:translateY(16px) scale(.99)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px;filter:drop-shadow(0 0 8px rgba(77,141,255,.45))}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#C4B5FD}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:linear-gradient(165deg,rgba(255,255,255,.06),rgba(255,255,255,.018));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;cursor:default;box-shadow:inset 0 1px 0 rgba(255,255,255,.06);animation:fadeUp .55s cubic-bezier(.22,1,.36,1) both}
[data-theme="light"] .metric{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6));box-shadow:inset 0 1px 0 rgba(255,255,255,.8),0 6px 20px rgba(30,50,90,.08)}
.metrics .metric:nth-child(2){animation-delay:.07s}
.metrics .metric:nth-child(3){animation-delay:.14s}
.metrics .metric:nth-child(4){animation-delay:.21s}
.metric::before{content:'';position:absolute;inset:0;background:linear-gradient(115deg,transparent 32%,rgba(255,255,255,.08) 48%,transparent 62%);transform:translateX(130%);transition:transform .75s ease;pointer-events:none}
.metric:hover::before{transform:translateX(-130%)}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.25s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:inset 0 1px 0 rgba(255,255,255,.06),0 14px 38px rgba(0,0,0,.45),0 0 24px rgba(77,141,255,.12)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
[data-theme="light"] .metric:hover{box-shadow:0 14px 30px rgba(30,50,90,.14)}
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-hero>*{animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both}
.traf-hero>:nth-child(2){animation-delay:.06s}
.traf-hero>:nth-child(3){animation-delay:.12s}
.traf-hero>:nth-child(4){animation-delay:.18s}
.traf-main-stat{background:linear-gradient(160deg,rgba(255,255,255,.07),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.07)}
[data-theme="light"] .traf-main-stat{background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;animation:cardGlow 7s ease-in-out infinite}
@keyframes cardGlow{0%,100%{opacity:.7;transform:scale(1)}50%{opacity:1;transform:scale(1.15)}}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1;text-shadow:0 0 22px rgba(77,141,255,.25)}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3);text-shadow:none}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.25s cubic-bezier(.4,0,.2,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
[data-theme="light"] .traf-mini{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,0,0,.4)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}
.traf-chart-card{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:inset 0 1px 0 rgba(255,255,255,.06),var(--shadow);margin-bottom:16px}
[data-theme="light"] .traf-chart-card{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px;filter:drop-shadow(0 0 8px rgba(77,141,255,.45))}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.18s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 10px rgba(77,141,255,.4)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}
@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px;transition:.25s}
.metric:hover .m-icon{transform:scale(1.12) rotate(-6deg)}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em;text-shadow:0 0 18px rgba(77,141,255,.2)}
.m-unit{font-size:12px;font-weight:400;color:var(--t3);text-shadow:none}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:inset 0 1px 0 rgba(255,255,255,.06),var(--shadow);position:relative;overflow:hidden}
[data-theme="light"] .vless-box{background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;animation:cardGlow 8s ease-in-out infinite}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.32);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em;transition:.25s}
.vless-box:hover .vl-code{border-color:var(--card-bh);box-shadow:0 0 18px rgba(77,141,255,.12)}
[data-theme="light"] .vl-code{background:rgba(37,99,235,.05)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .22s cubic-bezier(.4,0,.2,1);white-space:nowrap}
.btn i{font-size:13px}
.btn:hover{transform:translateY(-1px)}
.btn:active{transform:translateY(0) scale(.96)}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-p{position:relative;overflow:hidden;background:linear-gradient(135deg,#3D7BFF,#8B5CF6);color:#fff;box-shadow:0 4px 16px rgba(77,110,255,.35),inset 0 1px 0 rgba(255,255,255,.2)}
.btn-p::after{content:'';position:absolute;top:0;bottom:0;width:40%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-18deg);transition:left .6s ease}
.btn-p:hover::after{left:130%}
.btn-p:hover{box-shadow:0 8px 24px rgba(77,110,255,.5),inset 0 1px 0 rgba(255,255,255,.2)}
.btn-o{background:rgba(255,255,255,.03);border:1px solid var(--card-b);color:var(--t2);backdrop-filter:blur(8px)}
.btn-o:hover{background:var(--accent-d);border-color:var(--card-bh);color:var(--t1)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(77,141,255,.16)}
.btn-g:hover{background:rgba(77,141,255,.24);box-shadow:0 4px 14px rgba(77,141,255,.25)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(255,77,94,.2)}
.btn-d:hover{background:rgba(255,77,94,.22);box-shadow:0 4px 14px rgba(255,77,94,.25)}
.btn-pur{background:var(--purple-bg);color:#C4B5FD;border:1px solid rgba(168,85,247,.2)}
.btn-pur:hover{background:rgba(168,85,247,.24);box-shadow:0 4px 14px rgba(168,85,247,.28)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(255,176,32,.2)}
.btn-amber:hover{background:rgba(255,176,32,.22);box-shadow:0 4px 14px rgba(255,176,32,.25)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:all .25s cubic-bezier(.4,0,.2,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.05);animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both}
[data-theme="light"] .card{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.g2>*,.g3>*{animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both}
.g2>:nth-child(2),.g3>:nth-child(2){animation-delay:.08s}
.card:hover{border-color:var(--card-bh);box-shadow:inset 0 1px 0 rgba(255,255,255,.05),0 12px 30px rgba(0,0,0,.4)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent);filter:drop-shadow(0 0 6px rgba(77,141,255,.4))}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(255,255,255,.05);font-size:12px;transition:.2s}
[data-theme="light"] .sr{border-bottom-color:rgba(30,60,120,.07)}
.sr:hover{padding-right:3px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(255,255,255,.12);position:relative;cursor:pointer;transition:.28s;flex-shrink:0;border:none}
[data-theme="light"] .tog{background:rgba(20,50,110,.18)}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.28s cubic-bezier(.34,1.56,.64,1);box-shadow:0 1px 4px rgba(0,0,0,.4)}
.tog:hover{box-shadow:0 0 0 4px rgba(255,255,255,.05)}
.tog.on{background:linear-gradient(135deg,#10B981,#0D9668);box-shadow:0 0 14px rgba(16,185,129,.45)}
.tog.on::after{top:14px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.2s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(37,99,235,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(127,176,255,.5);background:rgba(0,0,0,.4);box-shadow:0 0 0 3px rgba(77,141,255,.12),0 0 18px rgba(77,141,255,.1)}
[data-theme="light"] .fi:focus,[data-theme="light"] .fs:focus{background:#fff}
.fs option{background:#0a0a16;color:var(--t1)}
[data-theme="light"] .fs option{background:#fff;color:#0F172A}
.cl{background:rgba(77,141,255,.07);border:1px solid rgba(77,141,255,.16);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(255,176,32,.2);color:var(--amber-t)}
.cl.amber i{color:var(--amber)}
.create-panel{background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),var(--shadow);margin-bottom:16px;position:relative}
[data-theme="light"] .create-panel{background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;animation:cardGlow 7s ease-in-out infinite}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,#3D7BFF,#8B5CF6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 20px rgba(77,110,255,.4);animation:iconFloat 4s ease-in-out infinite}
@keyframes iconFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px;transition:.25s}
[data-theme="light"] .cp-block{background:rgba(37,99,235,.03)}
.cp-block:hover{border-color:var(--card-bh)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(127,176,255,.55);box-shadow:0 0 0 3px rgba(77,141,255,.12),0 0 16px rgba(77,141,255,.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:rgba(255,255,255,.05);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.22s;white-space:nowrap}
.chip:hover{background:rgba(77,141,255,.18);color:var(--accent2);transform:translateY(-1px)}
.chip.active{background:linear-gradient(135deg,#3D7BFF,#8B5CF6);color:#fff;border-color:transparent;box-shadow:0 4px 14px rgba(77,110,255,.4)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.22s cubic-bezier(.4,0,.2,1);text-align:center;position:relative;background:rgba(0,0,0,.18)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(77,141,255,.12),0 0 22px rgba(77,141,255,.15)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.4);transition:.22s cubic-bezier(.34,1.56,.64,1)}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px;transition:.22s}
.proto-card:hover .proto-card-icon{transform:scale(1.1)}
.proto-card.active .proto-card-icon{background:linear-gradient(135deg,#3D7BFF,#8B5CF6);color:#fff;box-shadow:0 4px 12px rgba(77,110,255,.4)}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{position:relative;overflow:hidden;background:linear-gradient(135deg,#3D7BFF,#8B5CF6);color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(77,110,255,.4),inset 0 1px 0 rgba(255,255,255,.2);transition:.22s;white-space:nowrap}
.cp-submit-btn::after{content:'';position:absolute;top:0;bottom:0;width:40%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-18deg);transition:left .6s ease}
.cp-submit-btn:hover::after{left:130%}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(77,110,255,.5),inset 0 1px 0 rgba(255,255,255,.2)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
.srv-panel{background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),var(--shadow);position:relative}
[data-theme="light"] .srv-panel{background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none;animation:cardGlow 8s ease-in-out infinite}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,#3D7BFF,#8B5CF6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(77,110,255,.4);animation:iconFloat 4s ease-in-out infinite}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.22s cubic-bezier(.4,0,.2,1)}
[data-theme="light"] .srv-tile{background:rgba(37,99,235,.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:0 8px 22px rgba(0,0,0,.35),0 0 18px rgba(77,141,255,.1)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;transition:.22s}
.srv-tile:hover .srv-tile-icon{transform:scale(1.12) rotate(-5deg)}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}
@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.pw-panel{background:linear-gradient(160deg,rgba(255,255,255,.06),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:inset 0 1px 0 rgba(255,255,255,.07),var(--shadow);position:relative}
[data-theme="light"] .pw-panel{background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none;animation:cardGlow 8s ease-in-out infinite}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 20px rgba(168,85,247,.35);animation:iconFloat 4s ease-in-out infinite}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(168,85,247,.55);box-shadow:0 0 0 3px rgba(168,85,247,.12),0 0 18px rgba(168,85,247,.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex;transition:.2s}
.pw-eye:hover{color:var(--purple);transform:scale(1.1)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(255,255,255,.1);transition:.3s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.22s}
.pw-req.met{background:var(--green-bg);color:var(--green-t);box-shadow:0 0 12px rgba(16,185,129,.2)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(168,85,247,.32),inset 0 1px 0 rgba(255,255,255,.2);transition:.22s;position:relative;overflow:hidden}
.pw-submit::after{content:'';position:absolute;top:0;bottom:0;width:40%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.3),transparent);transform:skewX(-18deg);transition:left .6s ease}
.pw-submit:hover::after{left:130%}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(168,85,247,.45)}
.pw-submit:active{transform:translateY(0) scale(.98)}
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero>*{animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both}
.conn-hero>:nth-child(2){animation-delay:.06s}
.conn-hero>:nth-child(3){animation-delay:.12s}
.conn-hero>:nth-child(4){animation-delay:.18s}
.conn-hero-tile{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.25s cubic-bezier(.4,0,.2,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
[data-theme="light"] .conn-hero-tile{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 12px 30px rgba(0,0,0,.4)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent);opacity:.7}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;text-shadow:0 0 16px rgba(77,141,255,.2)}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}
.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite;box-shadow:0 0 8px rgba(16,185,129,.7)}
.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .28s cubic-bezier(.4,0,.2,1);position:relative;animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both;box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
[data-theme="light"] .conn-card-v2{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 34px rgba(0,0,0,.42),0 0 20px rgba(16,185,129,.1)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.12),transparent 70%);pointer-events:none;animation:cardGlow 6s ease-in-out infinite}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.14);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.2s}
.conn-ip-copy:hover{color:var(--accent2);transform:scale(1.15)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0;box-shadow:0 0 12px rgba(16,185,129,.15)}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:rgba(255,255,255,.07);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3DDFA9);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}
.conn-empty-v2{text-align:center;padding:70px 20px;background:linear-gradient(165deg,rgba(255,255,255,.045),rgba(255,255,255,.015));border:1px dashed var(--card-b);border-radius:20px;backdrop-filter:blur(14px)}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px;animation:iconFloat 3.4s ease-in-out infinite}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}
@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}
.sub-box{background:rgba(168,85,247,.08);border:1px solid rgba(168,85,247,.22);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:#C4B5FD;word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:rgba(255,255,255,.07);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s;position:relative;overflow:hidden}
.spfill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);width:45%;animation:shimmer 2.2s linear infinite}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.35;margin-bottom:12px;display:block;animation:iconFloat 3.4s ease-in-out infinite}
.empty p{font-size:12.5px;margin-top:4px}
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:linear-gradient(165deg,rgba(255,255,255,.05),rgba(255,255,255,.02));backdrop-filter:blur(16px);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.22s}
[data-theme="light"] .subs-search input{background:#fff}
.subs-search input:focus{border-color:rgba(168,85,247,.5);box-shadow:0 0 0 3px rgba(168,85,247,.12),0 0 18px rgba(168,85,247,.1)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}
.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:linear-gradient(165deg,rgba(255,255,255,.055),rgba(255,255,255,.02));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;transition:all .28s cubic-bezier(.4,0,.2,1);position:relative;animation:fadeUp .5s cubic-bezier(.22,1,.36,1) both;box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
[data-theme="light"] .sub-card{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.sub-card:hover{border-color:rgba(168,85,247,.45);transform:translateY(-4px);box-shadow:0 16px 38px rgba(0,0,0,.44),0 0 24px rgba(168,85,247,.1)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(168,85,247,.16),transparent 70%);pointer-events:none;animation:cardGlow 7s ease-in-out infinite}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(168,85,247,.35)}
.sub-card:hover .sub-card-icon{animation:iconFloat 2.4s ease-in-out infinite}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}
.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(124,58,237,.03)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b);transition:.2s}
.sub-card-stat:hover{background:rgba(168,85,247,.06)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}
.sub-card-url-row{margin:14px 20px 0;background:rgba(168,85,247,.09);border:1px dashed rgba(168,85,247,.28);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px;transition:.22s}
.sub-card-url-row:hover{border-color:rgba(168,85,247,.5);box-shadow:0 0 16px rgba(168,85,247,.1)}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#C4B5FD;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.2s}
.sub-card-url-copy:hover{color:#C4B5FD;transform:scale(1.15)}
.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}
.subs-empty-v2{text-align:center;padding:70px 20px;background:linear-gradient(165deg,rgba(255,255,255,.045),rgba(255,255,255,.015));border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1;backdrop-filter:blur(14px)}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px;animation:iconFloat 3.4s ease-in-out infinite}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}
@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}
.modal-v2{background:linear-gradient(170deg,rgba(14,15,26,.92),rgba(8,9,18,.88));backdrop-filter:blur(26px) saturate(160%);-webkit-backdrop-filter:blur(26px) saturate(160%);border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:popIn .32s cubic-bezier(.34,1.56,.64,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 24px 70px rgba(0,0,0,.6)}
[data-theme="light"] .modal-v2{background:rgba(255,255,255,.92)}
@keyframes popIn{from{opacity:0;transform:scale(.88) translateY(18px)}to{opacity:1;transform:none}}
.modal-v2-head{background:linear-gradient(155deg,rgba(168,85,247,.14) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(168,85,247,.2),transparent 70%);pointer-events:none;animation:cardGlow 6s ease-in-out infinite}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.2s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(255,77,94,.3);transform:rotate(90deg)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#6D48D6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(168,85,247,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.2s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.2s}
[data-theme="light"] .modal-v2-input{background:rgba(124,58,237,.04)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(168,85,247,.55);box-shadow:0 0 0 3px rgba(168,85,247,.14),0 0 18px rgba(168,85,247,.1);background:rgba(0,0,0,.4)}
[data-theme="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(77,141,255,.08);border:1px solid rgba(77,141,255,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.2s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#6D48D6);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(168,85,247,.4);transition:.2s;position:relative;overflow:hidden}
.modal-v2-btn-submit::after{content:'';position:absolute;top:0;bottom:0;width:40%;left:-60%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.3),transparent);transform:skewX(-18deg);transition:left .6s ease}
.modal-v2-btn-submit:hover::after{left:130%}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(168,85,247,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,#3D7BFF,#8B5CF6);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(77,110,255,.35)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.3);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.2s}
[data-theme="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(127,176,255,.5);box-shadow:0 0 0 3px rgba(77,141,255,.12)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.2s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(77,141,255,.22);transform:translateY(-1px)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}
.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.2s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:rgba(255,255,255,.05);transform:translateX(-2px)}
.lrow-v2.checked{background:rgba(77,141,255,.12);border-color:rgba(77,141,255,.28)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.2s;background:rgba(0,0,0,.2)}
.lrow-v2.checked .lrow-v2-check{background:linear-gradient(135deg,#3D7BFF,#8B5CF6);border-color:transparent;box-shadow:0 0 12px rgba(77,110,255,.4)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.4);transition:.2s cubic-bezier(.34,1.56,.64,1)}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;transition:.2s}
.lrow-v2.checked .lrow-v2-avatar{background:linear-gradient(135deg,#3D7BFF,#8B5CF6);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}
.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}
.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.62);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(6px)}
.modal-bg.open{display:flex;animation:fadeIn .22s}
.modal{background:linear-gradient(170deg,rgba(14,15,26,.92),rgba(8,9,18,.88));backdrop-filter:blur(26px) saturate(160%);-webkit-backdrop-filter:blur(26px) saturate(160%);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:popIn .32s cubic-bezier(.34,1.56,.64,1);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 24px 70px rgba(0,0,0,.6)}
[data-theme="light"] .modal{background:rgba(255,255,255,.92)}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none;transition:.2s}
.modal-close:hover{background:var(--red-bg);color:var(--red-t);transform:rotate(90deg)}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(255,255,255,.05)}
[data-theme="light"] .lrow{border-bottom-color:rgba(30,60,120,.07)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px) scale(.9);background:linear-gradient(170deg,rgba(14,15,26,.92),rgba(8,9,18,.88));backdrop-filter:blur(20px);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .32s cubic-bezier(.34,1.56,.64,1);z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:0 14px 40px rgba(0,0,0,.5);white-space:nowrap}
[data-theme="light"] .toast{background:rgba(255,255,255,.92)}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0) scale(1)}
.toast.ok{border-color:rgba(16,185,129,.35);background:linear-gradient(170deg,rgba(16,185,129,.16),rgba(16,185,129,.06));color:var(--green-t)}
.toast.err{border-color:rgba(255,77,94,.35);background:linear-gradient(170deg,rgba(255,77,94,.16),rgba(255,77,94,.06));color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600;transition:.2s}
.df-link:hover{filter:drop-shadow(0 0 8px rgba(77,141,255,.5));transform:translateY(-1px)}
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:linear-gradient(165deg,rgba(255,255,255,.05),rgba(255,255,255,.018));backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .26s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden;animation:fadeUp .45s cubic-bezier(.22,1,.36,1) both;box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
[data-theme="light"] .cfg-card{background:linear-gradient(165deg,rgba(255,255,255,.85),rgba(255,255,255,.6))}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 8px 28px rgba(0,0,0,.4),0 0 20px rgba(77,141,255,.08);transform:translateY(-2px)}
.cfg-card.is-off{opacity:.55}
.cfg-card.is-exp{opacity:.75}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-status-dot.pulse{animation:dotGlow 2.4s ease-in-out infinite}
@keyframes dotGlow{0%,100%{box-shadow:0 0 0 3px var(--green-bg),0 0 8px rgba(16,185,129,.35)}50%{box-shadow:0 0 0 4px var(--green-bg),0 0 18px rgba(16,185,129,.65)}}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.2s}
.cfg-uuid-mini:hover{background:rgba(77,141,255,.24);box-shadow:0 0 10px rgba(77,141,255,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(255,255,255,.07);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .5s ease;position:relative;overflow:hidden}
.ubar-f::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.4),transparent);width:45%;animation:shimmer 2.2s linear infinite}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#C4B5FD}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:linear-gradient(165deg,rgba(255,255,255,.05),rgba(255,255,255,.018));backdrop-filter:blur(18px);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.25s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.05);position:relative;transition:.2s}
[data-theme="light"] .log-item{border-bottom-color:rgba(30,60,120,.07)}
.log-item:hover{padding-right:4px}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0;transition:.25s}
.log-item:hover .log-ic{transform:scale(1.12)}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(255,255,255,.05)}
[data-theme="light"] .erow{border-bottom-color:rgba(30,60,120,.07)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}
@media(max-width:1050px){
  .sidebar{transform:translateX(100%)}
  .sidebar.open{transform:translateX(0);box-shadow:-10px 0 50px rgba(0,0,0,.5)}
  .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
.cl-row{display:flex;align-items:center;gap:12px;padding:11px 4px;border-bottom:1px solid var(--card-b);animation:fadeUp .45s cubic-bezier(.22,1,.36,1) both}
.cl-row:last-child{border-bottom:none}
.cl-dev{display:flex;align-items:center;gap:9px;min-width:170px}
.cl-dev-icon{width:34px;height:34px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2));box-shadow:0 4px 14px rgba(99,102,241,.35);flex-shrink:0}
.cl-dev-name{font-size:12px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:130px}
.cl-dev-sub{font-size:10px;color:var(--t3)}
.cl-ip{font-family:ui-monospace,monospace;font-size:12px;color:var(--t1);background:rgba(255,255,255,.04);border:1px solid var(--card-b);border-radius:8px;padding:4px 9px;cursor:pointer;transition:border-color .2s,background .2s}
.cl-ip:hover{border-color:rgba(99,102,241,.5);background:rgba(99,102,241,.08)}
.cl-site{font-family:ui-monospace,monospace;font-size:11.5px;color:#a5b4fc;direction:ltr}
.cl-lbl{font-size:11px;color:var(--t2)}
.cl-time{font-size:10.5px;color:var(--t3);white-space:nowrap}
.cl-chip{font-size:10px;font-weight:700;padding:3px 8px;border-radius:999px;white-space:nowrap}
.cl-chip.ok{background:rgba(16,185,129,.12);color:var(--green-t);border:1px solid rgba(16,185,129,.3)}
.cl-chip.err{background:rgba(239,68,68,.1);color:#fca5a5;border:1px solid rgba(239,68,68,.3)}
.cl-chip.live{background:rgba(16,185,129,.1);color:var(--green-t);border:1px solid rgba(16,185,129,.3);display:inline-flex;align-items:center;gap:5px}
.cl-note{font-size:10px;color:var(--t3)}
.cl-empty{padding:18px;text-align:center;color:var(--t3);font-size:12px}
[data-theme="light"] .cl-ip{background:rgba(37,99,235,.04)}
[data-theme="light"] .cl-site{color:#2563EB}
@media(max-width:640px){.cl-row{flex-wrap:wrap}.cl-dev{min-width:140px}.cl-note{display:none}}
@media(prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important}
}
</style>
</head>
<body>
<div class="fx-orb fxo1"></div><div class="fx-orb fxo2"></div><div class="fx-orb fxo3"></div>
<div class="toast" id="toast"></div>
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه جدید</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا برای مدیریت کانفیگ‌ها بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال تلگرام">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>صفحه پابلیک این گروه با یک لینک منحصر‌به‌فرد در اینترنت در دسترس خواهد بود.</span></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">انصراف</button>
        <button class="btn btn-pur" onclick="createSub()"><i class="ti ti-folder-plus"></i> ساخت گروه</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><i class="ti ti-bolt"></i></div>
    <span class="mob-title">TokenPanel</span>
  </div>
  <div class="mob-right">
    <button class="theme-mob" id="theme-mob-btn" onclick="toggleTheme()"><i class="ti ti-sun" id="theme-mob-icon"></i></button>
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><i class="ti ti-bolt"></i></div>
    <div><div class="logo-name">TokenPanel</div><div class="logo-sub">by @tokenshack</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">پنل</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> داشبورد</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-link-plus"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> سابسکریپشن</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area"></i> ترافیک</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-plug-connected"></i> اتصالات <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-it" data-pg="clients"><i class="ti ti-users-group"></i> اطلاعات متصلین</div>
    <div class="nav-sec">سیستم</div>
    <div class="nav-it" data-pg="security"><i class="ti ti-shield-lock"></i> امنیت</div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> خطاها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-wifi"></i> تست WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-settings"></i> تنظیمات</div>
    <div class="nav-it" data-pg="support"><i class="ti ti-headset"></i> پشتیبانی</div>
  </div>
  <div class="sb-foot">
    <button class="theme-btn" onclick="toggleTheme()"><i class="ti ti-moon" id="theme-icon"></i> <span id="theme-label">تم روشن</span></button>

    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-green"><span class="dot dg pulse"></span> فعال</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics">
    <div class="metric"><div class="m-icon"><i class="ti ti-plug-connected"></i></div><div class="m-label">اتصالات فعال</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span class="dot dg pulse"></span> WebSocket / XHTTP زنده</div></div>
    <div class="metric"><div class="m-icon"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric suc"><div class="m-icon suc"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric pur"><div class="m-icon pur"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-donut"></i> توزیع</div><div class="ch-sm"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-activity"></i> وضعیت سرویس</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-shield-check"></i> UUID Auth</span><span class="sr-v" style="color:var(--green-t)">● فعال · سخت‌گیرانه</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-circle-check"></i> VLESS / WS Tunnel</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-bolt"></i> Siz10a XHTTP Ultra</span><span class="sr-v" style="color:var(--green-t)">● فعال · 3 mode</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-folders"></i> Sub Groups</span><span class="sr-v" style="color:var(--green-t)">● فعال v12</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-rss"></i> Subscription API</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-clock"></i> آپتایم</span><span class="sr-v" id="uptime-inline">—</span></div>
      <div class="sr" style="flex-direction:column;align-items:flex-start;gap:4px">
        <div style="width:100%;display:flex;justify-content:space-between"><span class="sr-k"><i class="ti ti-gauge"></i> بار نسبی</span><span class="sr-v" id="bw-pct">—%</span></div>
        <div class="spbar" style="width:100%"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-list"></i> خلاصه کانفیگ‌ها <span class="ml-auto badge bg-blue" id="lsummary-badge">۰</span></div>
      <div id="lsummary">—</div>
    </div>
  </div>
  <div class="dash-footer">
    <span class="df-text">TokenPanel · Railway</span><a class="df-link" href="https://t.me/tokenshack" target="_blank"><i class="ti ti-brand-telegram"></i> @tokenshack</a>


  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> پورت اتصال</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر هم‌زمان</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-rss"></i> سابسکریپشن تکی (هر کانفیگ)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:12px">هر کانفیگ URL سابسکریپشن مخصوص دارد. از کارت کانفیگ روی آیکون <i class="ti ti-rss"></i> کلیک کنید.</p>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-database"></i> سابسکریپشن کامل (ادمین)</div>
      <p style="font-size:11.5px;color:var(--t3);line-height:1.8;margin-bottom:4px">شامل تمام کانفیگ‌های فعال.</p>
      <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
      <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
    </div>
  </div>
  <div class="card">
    <div class="card-title"><i class="ti ti-folders"></i> لینک سابسکریپشن گروه‌ها</div>
    <div id="sub-groups-list">در حال بارگذاری...</div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>
<section class="pg" id="pg-clients">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-users-group"></i> اطلاعات متصلین</div><div class="tb-sub">امنیت بیشتر: دستگاه، آی‌پی و سایت‌های درخواستی هر کلاینت</div></div>
    <div class="tb-right"><span class="badge bg-green" id="cl-live-badge">—</span><button class="btn btn-p btn-sm" onclick="loadClients()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-device-mobile"></i></div>
      <div class="conn-hero-label">کلاینت‌های زنده</div>
      <div class="conn-hero-val" id="cl-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-world"></i></div>
      <div class="conn-hero-label">سایت‌های بازدیدشده</div>
      <div class="conn-hero-val" id="cl-sites-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-login"></i></div>
      <div class="conn-hero-label">ورودهای اخیر پنل</div>
      <div class="conn-hero-val" id="cl-logins-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-shield-check"></i></div>
      <div class="conn-hero-label">وضعیت مانیتورینگ</div>
      <div class="conn-hero-val" style="font-size:15px;color:var(--green-t)">● فعال</div>
    </div>
  </div>

  <div class="card" style="margin-bottom:18px">
    <div class="card-title"><i class="ti ti-device-desktop"></i> کلاینت‌های متصل (دستگاه · آی‌پی · کانفیگ) <button class="btn btn-o btn-sm ml-auto" onclick="loadClients()"><i class="ti ti-refresh"></i></button></div>
    <div id="cl-live">—</div>
    <div class="empty" id="cl-live-empty" style="display:none"><i class="ti ti-users"></i><p>هیچ کلاینتی متصل نیست</p></div>
  </div>

  <div class="card" style="margin-bottom:18px">
    <div class="card-title"><i class="ti ti-world"></i> سایت‌های درخواست‌شده توسط کلاینت‌ها
      <span class="ml-auto" style="display:flex;gap:6px">
        <span class="cl-note">حداکثر ۴۰۰ آیتم · قدیمی‌ها خودکار حذف می‌شوند</span>
        <button class="btn btn-o btn-sm" onclick="clearSiteLogs()"><i class="ti ti-eraser"></i> پاک کردن</button>
      </span>
    </div>
    <div id="cl-sites">—</div>
    <div class="empty" id="cl-sites-empty" style="display:none"><i class="ti ti-world-search"></i><p>هنوز سایتی ثبت نشده</p></div>
  </div>

  <div class="card">
    <div class="card-title"><i class="ti ti-shield-lock"></i> ورودهای اخیر به پنل (دستگاه · آی‌پی)</div>
    <div id="cl-logins">—</div>
    <div class="empty" id="cl-logins-empty" style="display:none"><i class="ti ti-login-2"></i><p>هنوز ورودی ثبت نشده</p></div>
  </div>
</section>
<section class="pg" id="pg-security">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-shield-lock"></i> امنیت</div></div></div>
  <div class="g2">
    <div class="card">
      <div class="card-title"><i class="ti ti-lock"></i> رمزنگاری</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-certificate"></i> TLS/HTTPS</span><span class="sr-v" style="color:var(--green-t)">● فعال (443)</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-fingerprint"></i> Fingerprint</span><span class="sr-v">Chrome Spoof</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-network"></i> پروتکل‌ها</span><span class="sr-v">VLESS/WS + XHTTP Ultra</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-key"></i> هش رمز</span><span class="sr-v">SHA-256+Salt</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-cookie"></i> سشن</span><span class="sr-v">HttpOnly · 7 روز</span></div>
    </div>
    <div class="card">
      <div class="card-title"><i class="ti ti-shield-check"></i> کنترل دسترسی</div>
      <div class="sr"><span class="sr-k"><i class="ti ti-id-badge"></i> UUID Auth سخت‌گیرانه</span><span class="sr-v" style="color:var(--green-t)">● فعال v12</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-toggle-right"></i> فعال/غیرفعال کانفیگ</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-gauge"></i> سهمیه ترافیک</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-calendar-x"></i> تاریخ انقضا</span><span class="sr-v" style="color:var(--green-t)">● فعال</span></div>
      <div class="sr"><span class="sr-k"><i class="ti ti-lock"></i> رمز صفحه پابلیک ساب</span><span class="sr-v" style="color:var(--green-t)">● اختیاری · SHA-256</span></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> لاگ فعالیت‌ها</div><div class="tb-sub">تاریخچه‌ی کامل رخدادهای پنل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="log-timeline" id="logs-list">—</div><div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div></div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i></button></div></div>
  <div class="card"><div class="card-title"><i class="ti ti-bug"></i> لاگ خطاها</div><div id="errs-full">—</div></div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="card" style="max-width:660px">
    <div class="cl amber" style="margin-top:0;margin-bottom:12px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
    <div class="form-row" style="margin-bottom:12px">
      <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
      <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
      <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
    </div>
    <div class="form-row" style="margin-bottom:12px">
      <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
      <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
    </div>
    <div style="background:rgba(0,0,0,.3);border:1px solid var(--card-b);border-radius:10px;padding:14px;height:250px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9" id="ws-log">
      <p style="color:var(--t3)">منتظر اتصال...</p>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div></div></div>
  <div class="g2">
    <div class="srv-panel">
      <div class="srv-hero">
        <div class="srv-hero-icon"><i class="ti ti-server-2"></i></div>
        <div class="srv-hero-text">
          <div class="srv-hero-domain" id="set-host">—</div>
          <div class="srv-hero-sub"><span class="dot dg pulse"></span> آنلاین · Railway</div>
        </div>
      </div>
      <div class="srv-tiles">
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-route"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پورت پیش‌فرض</div><div class="srv-tile-val">443 (TLS) · قابل تغییر در هر کانفیگ</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-versions"></i></div><div class="srv-tile-text"><div class="srv-tile-label">نسخه</div><div class="srv-tile-val">TokenPanel v12</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-brand-fastapi"></i></div><div class="srv-tile-text"><div class="srv-tile-label">فریم‌ورک</div><div class="srv-tile-val">FastAPI + Uvicorn</div></div></div>
        <div class="srv-tile"><div class="srv-tile-icon"><i class="ti ti-cloud"></i></div><div class="srv-tile-text"><div class="srv-tile-label">پلتفرم</div><div class="srv-tile-val">Railway</div></div></div>
        <div class="srv-tile" style="grid-column:1/-1"><div class="srv-tile-icon"><i class="ti ti-device-floppy"></i></div><div class="srv-tile-text"><div class="srv-tile-label">ذخیره‌سازی</div><div class="srv-tile-val">JSON File (/data)</div></div></div>
      </div>
    </div>
    <div class="pw-panel">
      <div class="pw-hero">
        <div class="pw-hero-icon"><i class="ti ti-key"></i></div>
        <div class="pw-hero-text">
          <div class="pw-hero-title">تغییر رمز عبور</div>
          <div class="pw-hero-sub">رمز قوی انتخاب کنید و آن را جایی امن نگه دارید</div>
        </div>
      </div>
      <div class="pw-body">
        <div class="pw-field">
          <label>رمز فعلی</label>
          <input class="pw-input" type="password" id="cp-cur" placeholder="رمز فعلی را وارد کنید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cur',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-field" style="margin-bottom:6px">
          <label>رمز جدید</label>
          <input class="pw-input" type="password" id="cp-new" placeholder="حداقل ۴ کاراکتر" oninput="checkPwStrength(this.value)">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-new',this)"><i class="ti ti-eye"></i></button>
        </div>
        <div class="pw-strength" id="pw-strength-bar">
          <div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div><div class="pw-strength-seg"></div>
        </div>
        <div class="pw-strength-label" id="pw-strength-label"><i class="ti ti-shield"></i> قدرت رمز</div>
        <div class="pw-reqs">
          <span class="pw-req" id="req-len"><i class="ti ti-circle-dashed"></i> حداقل ۴ کاراکتر</span>
          <span class="pw-req" id="req-num"><i class="ti ti-circle-dashed"></i> شامل عدد</span>
          <span class="pw-req" id="req-case"><i class="ti ti-circle-dashed"></i> حروف بزرگ/کوچک</span>
        </div>
        <div class="pw-field" style="margin-bottom:18px">
          <label>تکرار رمز جدید</label>
          <input class="pw-input" type="password" id="cp-cf" placeholder="تکرار رمز جدید">
          <button class="pw-eye" type="button" onclick="togglePwField('cp-cf',this)"><i class="ti ti-eye"></i></button>
        </div>
        <button class="pw-submit" onclick="changePw()"><i class="ti ti-shield-check"></i> ذخیره رمز جدید</button>
      </div>
    </div>
  </div>
</section>
<section class="pg" id="pg-support">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-headset"></i> پشتیبانی</div></div></div>
  <div class="srv-panel">
    <div class="srv-hero">
      <div class="srv-hero-icon"><i class="ti ti-headset"></i></div>
      <div class="srv-hero-text">
        <div class="srv-hero-domain">پشتیبانی</div>
        <div class="srv-hero-sub"><span class="dot dg pulse"></span> راه‌های ارتباطی</div>
      </div>
    </div>
    <div class="srv-tiles">
      <a class="srv-tile" href="https://t.me/tokenshack" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-brand-telegram"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">سازنده پنل</div><div class="srv-tile-val">t.me/tokenshack</div></div>
      </a>
      <a class="srv-tile" href="https://t.me/tokenshack" target="_blank" style="text-decoration:none;cursor:pointer">
        <div class="srv-tile-icon"><i class="ti ti-headset"></i></div>
        <div class="srv-tile-text"><div class="srv-tile-label">پشتیبانی</div><div class="srv-tile-val">@tokenshack</div></div>
      </a>
    </div>
  </div>
</section>
</main>
<script>
let isDark=localStorage.getItem('tokenpanel-theme')!=='light';
function applyTheme(dark){
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  const icon=dark?'ti-sun':'ti-moon',label=dark?'تم روشن':'تم تاریک';
  document.getElementById('theme-icon').className='ti '+icon;
  document.getElementById('theme-label').textContent=label;
  const mobI=document.getElementById('theme-mob-icon');if(mobI)mobI.className='ti '+icon;
}
function toggleTheme(){isDark=!isDark;localStorage.setItem('tokenpanel-theme',isDark?'dark':'light');applyTheme(isDark)}
applyTheme(isDark);
function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp'],'xhttp-stream-one':['XHTTP ULTRA','pc-ultra']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/tokenshack';}catch(e){location.href='/tokenshack'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/tokenshack'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/tokenshack';throw new Error('unauthorized')}
  return r;
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,clients:loadClients,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    document.getElementById('m-conns').textContent=d.active_connections;
    document.getElementById('conns-nb').textContent=d.active_connections;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    document.getElementById('uptime-badge').textContent='Railway · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.active_connections+' اتصال';
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
async function loadActivity(){
  try{
    const r=await authF('/api/activity'),d=await r.json();
    const logs=(d.logs||[]).slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!logs.length){el.innerHTML='';em.style.display='block';return}
    em.style.display='none';
    const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
    const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
    el.innerHTML=logs.map(l=>`
      <div class="log-item">
        <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
        <div class="log-body">
          <div class="log-msg">${esc(l.message)}</div>
          <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
        </div>
      </div>
    `).join('');
  }catch(e){console.error(e)}
}
const _devIcon=dev=>{
  const d=(dev||'').toLowerCase();
  if(d.includes('iphone')||d.includes('ipad')||d.includes('ios'))return 'ti-device-mobile';
  if(d.includes('android')||d.includes('samsung')||d.includes('sm-')||d.includes('pixel'))return 'ti-device-mobile';
  if(d.includes('windows')||d.includes('mac')||d.includes('linux'))return 'ti-device-desktop';
  return 'ti-device-gamepad';
};
async function loadClients(){
  try{
    const r=await authF('/api/clients'),d=await r.json();
    document.getElementById('cl-live-badge').innerHTML='<span class="dot dg pulse"></span> '+(d.live_count||0)+' کلاینت';
    document.getElementById('cl-count').textContent=toFa(d.live_count||0);
    document.getElementById('cl-sites-count').textContent=toFa((d.sites||[]).length);
    document.getElementById('cl-logins-count').textContent=toFa((d.logins||[]).length);
    const liveEl=document.getElementById('cl-live'),liveEm=document.getElementById('cl-live-empty');
    const live=d.live||[];
    if(!live.length){liveEl.innerHTML='';liveEm.style.display='block'}
    else{
      liveEm.style.display='none';
      liveEl.innerHTML=live.map((c,i)=>`
        <div class="cl-row" style="animation-delay:${Math.min(i*40,400)}ms">
          <div class="cl-dev">
            <div class="cl-dev-icon"><i class="ti ${_devIcon(c.device)}"></i></div>
            <div><div class="cl-dev-name">${esc(c.device||'نامشخص')}</div><div class="cl-dev-sub">${esc(c.transport||'')}</div></div>
          </div>
          <span class="cl-ip" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i> ${esc(c.ip)}</span>
          <span class="cl-lbl">${esc(c.label||'نامشخص')}</span>
          <span class="cl-chip live"><span class="dot dg pulse"></span> زنده</span>
          <span class="cl-lbl">${esc(c.bytes_fmt||'')}</span>
          <span class="cl-time ml-auto">${c.connected_at?new Date(c.connected_at).toLocaleTimeString('fa-IR'):''}</span>
        </div>`).join('');
    }
    const sitesEl=document.getElementById('cl-sites'),sitesEm=document.getElementById('cl-sites-empty');
    const sites=d.sites||[];
    if(!sites.length){sitesEl.innerHTML='';sitesEm.style.display='block'}
    else{
      sitesEm.style.display='none';
      sitesEl.innerHTML=sites.map((s,i)=>`
        <div class="cl-row" style="animation-delay:${Math.min(i*30,400)}ms">
          <div class="cl-dev-icon" style="border-radius:10px"><i class="ti ti-world"></i></div>
          <span class="cl-site">${esc(s.address||'?')}${s.port?':'+s.port:''}</span>
          <span class="cl-lbl">${esc(s.label||'')}</span>
          <span class="cl-chip" style="background:rgba(99,102,241,.1);color:#a5b4fc;border:1px solid rgba(99,102,241,.25)">${esc(s.device||'')}</span>
          <span class="cl-ip" onclick="navigator.clipboard.writeText('${esc(s.ip||'')}').then(()=>toast('IP کپی شد','ok'))">${esc(s.ip||'')}</span>
          <span class="cl-time ml-auto">${s.time?new Date(s.time).toLocaleString('fa-IR'):''}</span>
        </div>`).join('');
    }
    const logEl=document.getElementById('cl-logins'),logEm=document.getElementById('cl-logins-empty');
    const logins=d.logins||[];
    if(!logins.length){logEl.innerHTML='';logEm.style.display='block'}
    else{
      logEm.style.display='none';
      logEl.innerHTML=logins.map((l,i)=>`
        <div class="cl-row" style="animation-delay:${Math.min(i*30,400)}ms">
          <div class="cl-dev-icon" style="border-radius:10px;${l.ok?'':'background:linear-gradient(135deg,#ef4444,#b91c1c)'}"><i class="ti ${l.ok?'ti-shield-check':'ti-shield-x'}"></i></div>
          <span class="cl-chip ${l.ok?'ok':'err'}">${l.ok?'ورود موفق':'ورود ناموفق'}</span>
          <span class="cl-ip" onclick="navigator.clipboard.writeText('${esc(l.ip||'')}').then(()=>toast('IP کپی شد','ok'))">${esc(l.ip||'')}</span>
          <span class="cl-lbl">${esc(l.device||'نامشخص')}</span>
          <span class="cl-time ml-auto">${l.time?new Date(l.time).toLocaleString('fa-IR'):''}</span>
        </div>`).join('');
    }
  }catch(e){console.error(e)}
}
async function clearSiteLogs(){
  try{await authF('/api/clients/sites',{method:'DELETE'});toast('لیست سایت‌ها پاک شد','ok');loadClients()}catch(e){console.error(e)}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    document.getElementById('links-nb').textContent=links.length;
    document.getElementById('links-pg-cnt').textContent=toFa(links.length)+' کانفیگ';
    document.getElementById('lsummary-badge').textContent=toFa(links.length);
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!links.length){grid.innerHTML='';empty.style.display='block';document.getElementById('lsummary').innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>کانفیگی وجود ندارد</p></div>';return}
    empty.style.display='none';
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return `<div class="cfg-card ${cardCls}">
    <div class="cfg-row">
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}</div>
        <div class="cfg-sub-meta">
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
    document.getElementById('lsummary').innerHTML=links.slice(0,6).map(l=>`<div class="sr"><span class="sr-k" style="gap:5px"><i class="ti ${l.expired?'ti-calendar-x':l.active?'ti-circle-check':'ti-circle-x'}" style="color:${l.expired?'var(--amber)':l.active?'var(--green)':'var(--red)'}"></i>${esc(l.label)}</span><span class="sr-v" style="font-size:10px">${fmtB(l.used_bytes)} / ${l.limit_bytes===0?'∞':fmtB(l.limit_bytes)}</span></div>`).join('');
  }catch(e){console.error(e)}
}
async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){window.open('https://api.qrserver.com/v1/create-qr-code/?size=300x300&data='+encodeURIComponent(link),'_blank')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'رمزدار':'پابلیک'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','ok'))" title="کپی"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}
async function deleteSub(sub_id){
  if(!confirm('حذف این گروه؟ کانفیگ‌ها حذف نمی‌شوند.'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info">
        <div class="lrow-v2-name">${esc(l.label)}</div>
        <div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
      </div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#A78BFA">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'· 🔒 رمزدار':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-globe"></i> پابلیک</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    document.getElementById('conns-live').innerHTML='<span class="dot dg pulse"></span> '+d.count+' اتصال';
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">ترافیک</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">مدت اتصال</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);}catch(e){}}
async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}
async function changePw(){
  const cur=document.getElementById('cp-cur').value,nw=document.getElementById('cp-new').value,cf=document.getElementById('cp-cf').value;
  if(!cur||!nw||!cf){toast('همه فیلدها را پر کنید','err');return}
  if(nw.length<4){toast('حداقل ۴ کاراکتر','err');return}
  if(nw!==cf){toast('تکرار رمز اشتباه','err');return}
  try{
    const r=await authF('/api/change-password',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({current_password:cur,new_password:nw})});
    const d=await r.json().catch(()=>({}));
    if(!r.ok)throw new Error(d.detail||'خطا');
    toast('رمز تغییر کرد ✓','ok');
    ['cp-cur','cp-new','cp-cf'].forEach(id=>document.getElementById(id).value='');
  }catch(e){toast('✗ '+e.message,'err')}
}
function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}
function checkPwStrength(val){
  const segs=document.querySelectorAll('#pw-strength-bar .pw-strength-seg');
  const label=document.getElementById('pw-strength-label');
  const reqLen=document.getElementById('req-len'),reqNum=document.getElementById('req-num'),reqCase=document.getElementById('req-case');
  const hasLen=val.length>=4,hasNum=/\d/.test(val),hasCase=/[a-z]/.test(val)&&/[A-Z]/.test(val),hasLong=val.length>=8;
  reqLen.classList.toggle('met',hasLen);
  reqNum.classList.toggle('met',hasNum);
  reqCase.classList.toggle('met',hasCase);
  let score=0;if(hasLen)score++;if(hasNum)score++;if(hasCase)score++;if(hasLong)score++;
  const colors=['#EF4444','#F59E0B','#3B82F6','#10B981'],labels=['خیلی ضعیف','ضعیف','متوسط','قوی'];
  segs.forEach((s,i)=>{s.style.background=i<score?colors[Math.max(0,score-1)]:'rgba(100,116,139,.2)'});
  if(val.length===0){label.innerHTML='<i class="ti ti-shield"></i> قدرت رمز';return}
  label.innerHTML=`<i class="ti ti-shield-check" style="color:${colors[Math.max(0,score-1)]}"></i> ${labels[Math.max(0,score-1)]}`;
}
function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  const c1=document.getElementById('ch1').getContext('2d');
  const grad1=makeGradient(c1,'rgba(59,130,246,.38)','rgba(59,130,246,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,
        titleColor:'#E8F4FF',bodyColor:'#7BAED4',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(59,130,246,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#3B82F6',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#3B82F6',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(59,130,246,.45)','rgba(59,130,246,.08)','rgba(59,130,246,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#3B82F6',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#3B82F6',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,27,46,.97)',borderColor:'rgba(59,130,246,.35)',borderWidth:1,
          titleColor:'#E8F4FF',bodyColor:'#9DC3E8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(59,130,246,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  ch2=new Chart(document.getElementById('ch2'),{
    type:'doughnut',
    data:{labels:['VLESS/WS','XHTTP Ultra','HTTP Proxy'],datasets:[{
      data:[55,35,10],
      backgroundColor:['#3B82F6','#10B981','#8B5CF6'],
      borderColor:getComputedStyle(document.documentElement).getPropertyValue('--card')||'#0d1b2e',
      borderWidth:4,hoverOffset:10,borderRadius:6,spacing:3
    }]},
    options:{
      responsive:true,maintainAspectRatio:false,cutout:'72%',
      plugins:{
        legend:{position:'bottom',labels:{color:'var(--t2)',font:{size:10,family:'Vazirmatn'},padding:12,usePointStyle:true,pointStyle:'circle'}},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(59,130,246,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(ws)ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  initCharts();
  document.getElementById('set-host').textContent=location.host;
  document.getElementById('sub-all-url')&&(document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all');
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-clients').classList.contains('on'))loadClients();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});
</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
<title>TokenPanel Sub</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#030309;--bg2:#06060f;--bg3:#0a0a18;
  --card:rgba(255,255,255,0.045);--card-b:rgba(255,255,255,0.09);--card-bh:rgba(129,165,255,0.38);
  --accent:#4D8DFF;--accent2:#7FB0FF;--accent-d:rgba(77,141,255,0.12);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.1);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.1);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.1);--purple-t:#BCA4F7;
  --t1:#EFF4FF;--t2:#8AA0C4;--t3:#48577A;
  --radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="light"]{{
  --bg:#F0F3FA;--bg2:#E5ECF8;--bg3:#D9E3F4;
  --card:#FFFFFF;--card-b:rgba(59,124,246,0.14);--card-bh:rgba(59,124,246,0.32);
  --accent:#2E63D6;--accent2:#1E4CB8;--accent-d:rgba(46,99,214,0.08);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.08);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.08);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.08);--purple-t:#5A3CAD;
  --t1:#101A30;--t2:#48577A;--t3:#8694B0;
  --shadow:0 12px 36px rgba(20,40,90,0.12);
}}
html,body{{min-height:100%;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 60% 40% at 18% 0%,rgba(77,141,255,0.14),transparent 62%),radial-gradient(ellipse 50% 36% at 85% 14%,rgba(168,85,247,0.11),transparent 60%),radial-gradient(ellipse 60% 40% at 50% 112%,rgba(16,185,129,0.07),transparent 62%),var(--bg);z-index:0;pointer-events:none;animation:aurora 18s ease-in-out infinite alternate}}
@keyframes aurora{{0%{{transform:translateY(0) scale(1)}}100%{{transform:translateY(-2.5%) scale(1.04)}}}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,0.03) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:13px;display:flex;align-items:center;justify-content:center;font-size:20px;color:#fff;background:linear-gradient(135deg,var(--accent),var(--accent2) 60%,#22d3ee);box-shadow:0 6px 18px rgba(139,92,246,.4),inset 0 1px 0 rgba(255,255,255,.35);flex-shrink:0;animation:glyphFloat 4.5s ease-in-out infinite}}
@keyframes glyphFloat{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-4px)}}}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}

.sub-info{{background:var(--card);backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,124,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,var(--accent) 0%,#2952C8 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(59,124,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#1D4ED8;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}

.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}

/* ── کارت کانفیگ به‌شکل بلیط دسترسی (signature element) ── */
.cfg-card{{background:var(--card);backdrop-filter:blur(20px) saturate(150%);-webkit-backdrop-filter:blur(20px) saturate(150%);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(96,148,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}

/* خط جداکننده‌ی بلیطی با دندانه‌های گرد، شبیه پاره‌خط بُرد بلیط */
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}

.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(46,99,214,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-p{{background:linear-gradient(135deg,#2F8FFF,#8B5CF6);color:#fff;box-shadow:0 3px 14px rgba(139,92,246,.35)}}
.btn-p:hover{{background:var(--accent2)}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(96,148,246,.16)}}
.btn-g:hover{{background:rgba(96,148,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

/* ── صفحه‌ی قفل / رمز ── */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);backdrop-filter:blur(24px) saturate(150%);-webkit-backdrop-filter:blur(24px) saturate(150%);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,124,246,.16),rgba(59,124,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(46,99,214,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);backdrop-filter:blur(24px) saturate(150%);-webkit-backdrop-filter:blur(24px) saturate(150%);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}

@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:19px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:32px 22px 22px}}
  .lock-form{{padding:20px 22px 26px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* v12 motion pack */
.sub-info,.stat-card,.cfg-card{{animation:fadeUpV .6s cubic-bezier(.22,1,.36,1) both}}
.stat-card:nth-child(1){{animation-delay:.05s}}.stat-card:nth-child(2){{animation-delay:.12s}}.stat-card:nth-child(3){{animation-delay:.19s}}.stat-card:nth-child(4){{animation-delay:.26s}}
.cfg-card{{transition:transform .25s cubic-bezier(.22,1,.36,1),box-shadow .25s,border-color .25s}}
.cfg-card:hover{{transform:translateY(-4px) scale(1.008);border-color:rgba(139,92,246,.45);box-shadow:0 18px 40px rgba(0,0,0,.45),0 0 24px rgba(139,92,246,.14)}}
.sub-info{{position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;inset:-1px;border-radius:inherit;padding:1px;background:linear-gradient(135deg,rgba(99,102,241,.55),transparent 35%,transparent 65%,rgba(34,211,238,.45));background-size:220% 220%;-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;animation:borderFlowV 7s linear infinite}}
@keyframes borderFlowV{{0%{{background-position:0% 0%}}100%{{background-position:100% 100%}}}}
@keyframes fadeUpV{{from{{opacity:0;transform:translateY(22px) scale(.985)}}to{{opacity:1;transform:none}}}}
.qr-box{{animation:popInV .45s cubic-bezier(.34,1.56,.64,1) both}}
@keyframes popInV{{from{{opacity:0;transform:scale(.85) translateY(16px)}}to{{opacity:1;transform:none}}}}
.btn{{position:relative;overflow:hidden}}
.btn::after{{content:'';position:absolute;top:0;bottom:0;width:45%;left:-70%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.3),transparent);transform:skewX(-18deg);animation:shineV 3.8s ease-in-out infinite;pointer-events:none}}
@keyframes shineV{{0%,60%{{left:-70%}}90%,100%{{left:150%}}}}
@media(prefers-reduced-motion:reduce){{*{{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}}}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><i class="ti ti-bolt"></i></div>
      <div><div class="brand-name">TokenPanel</div><div class="brand-sub">by @tokenshack</div></div>
    </div>
    <div class="top-actions">
      <button class="icon-btn" id="theme-toggle" onclick="toggleTheme()" title="تغییر تم"><i class="ti ti-sun" id="theme-icon"></i></button>

    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="footer">TokenPanel · <a href="https://t.me/tokenshack" target="_blank">@tokenshack</a></div>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let isDark=localStorage.getItem('tokenpanel-pub-theme')!=='light';
function applyTheme(dark){{
  document.documentElement.setAttribute('data-theme',dark?'dark':'light');
  document.getElementById('theme-icon').className='ti '+(dark?'ti-sun':'ti-moon');
}}
function toggleTheme(){{isDark=!isDark;localStorage.setItem('tokenpanel-pub-theme',isDark?'dark':'light');applyTheme(isDark)}}
applyTheme(isDark);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p==='xhttp-stream-one')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='https://api.qrserver.com/v1/create-qr-code/?size=260x260&data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const r=await fetch(url);
  return r.json();
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.links.filter(l=>l.active).length;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._subUrl  = subUrl;
  window._subName = d.name;
  window._links   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._subUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._subName + ' — کل گروه', window._subUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button>
    </div>

    <div class="stats-bar">
      <div class="stat-card">
        <div class="stat-label">کانفیگ‌های فعال</div>
        <div class="stat-val">${{toFa(activeCount)}}</div>
        <div class="stat-sub">از ${{toFa(d.links.length)}} کانفیگ</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">اتصالات زنده</div>
        <div class="stat-val">${{toFa(d.active_connections)}}</div>
        <div class="stat-sub" style="color:var(--green-t);display:flex;align-items:center;gap:4px"><span class="dot"></span> آنلاین</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">کل مصرف</div>
        <div class="stat-val" style="font-size:17px;margin-top:3px">${{esc(d.total_used_fmt)}}</div>
        <div class="stat-sub">همه کانفیگ‌ها</div>
      </div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        const pct = l.limit_bytes === 0 ? 0 : Math.min(100, l.used_bytes / l.limit_bytes * 100);
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const lim = l.limit_bytes === 0 ? '∞' : fmtB(l.limit_bytes);
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <span class="cfg-status ${{l.active ? 'ok' : 'no'}}">${{l.active ? '<i class="ti ti-circle-check"></i> فعال' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>${{esc(l.used_fmt)}} مصرف شده</span><span>سهمیه: ${{lim}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._links[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._links[${{i}}].label, window._links[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  setTimeout(() => autoRefresh(), 30000);
}}

function copyAllConfigs(){{
  const links=window._links||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}}

async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
