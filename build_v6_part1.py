# Part 1: HEAD + CSS + HTML SCREENS
content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
<title>The Affinity of Vissan</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Cinzel:wght@400;500;600&family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#181818;--gold:#F0C95B;--gold-d:rgba(240,201,91,.35);
  --cream:#F5ECD0;--cream-d:rgba(245,236,208,.60);
  --border:rgba(240,201,91,.30);--border-hi:rgba(245,236,208,.50);
  --r:8px;
}
html,body{width:100%;height:100%;overflow:hidden;background:var(--bg);color:var(--cream);
  font-family:\'Cormorant Garamond\',Georgia,serif;-webkit-tap-highlight-color:transparent;}
.screen{position:fixed;inset:0;z-index:10;display:flex;flex-direction:column;
  opacity:0;pointer-events:none;transition:opacity .45s ease;overflow:hidden;background:var(--bg);}
.screen.active{opacity:1;pointer-events:all;}
.scroll-y{overflow-y:auto;-webkit-overflow-scrolling:touch;}
.scroll-y::-webkit-scrollbar{width:0;}
/* TYPOGRAPHY */
.t-disp{font-family:\'Cinzel Decorative\',serif;color:var(--gold);font-weight:700;letter-spacing:.04em;}
.t-cinzel{font-family:\'Cinzel\',serif;}
/* BUTTON */
.btn{font-family:\'Cinzel\',serif;font-size:.62rem;letter-spacing:.42em;text-transform:uppercase;
  color:var(--cream);background:transparent;border:1px solid var(--border-hi);border-radius:6px;
  padding:14px 28px;cursor:pointer;transition:all .25s ease;display:inline-block;white-space:nowrap;}
.btn:hover,.btn:active{background:rgba(245,236,208,.07);border-color:var(--gold);}
.btn:disabled{opacity:.38;pointer-events:none;}
/* DIVIDER */
.divider{height:1px;background:linear-gradient(90deg,transparent,rgba(240,201,91,.35),transparent);}
/* ── LANDING ── */
#s-land{overflow-y:auto;}
.land-title{text-align:center;padding:28px 20px 0;}
.land-title h1{font-family:\'Cinzel Decorative\',serif;font-size:clamp(2rem,9vw,2.8rem);
  color:var(--gold);font-weight:700;line-height:1.15;letter-spacing:.06em;text-transform:uppercase;}
.land-image{width:100%;aspect-ratio:390/280;flex-shrink:0;overflow:hidden;margin-top:20px;}
.land-image img{width:100%;height:100%;object-fit:cover;object-position:center;}
.land-body{padding:28px 28px 0;text-align:center;flex:1;}
.land-subtitle{font-family:\'Cinzel\',serif;font-size:.7rem;letter-spacing:.38em;text-transform:uppercase;
  color:var(--gold);margin-bottom:20px;}
.land-para{font-size:1.05rem;line-height:1.82;color:var(--cream-d);margin-bottom:16px;}
.land-tagline{font-style:italic;font-size:1.05rem;color:var(--gold);margin-bottom:32px;}
.land-cta{display:flex;justify-content:center;padding:0 28px 52px;}
/* ── AVATAR SELECT ── */
.sel-hero{width:100%;height:52vw;max-height:260px;flex-shrink:0;overflow:hidden;position:relative;}
.sel-hero img{width:100%;height:100%;object-fit:cover;object-position:center top;}
.sel-hero::after{content:\'\';position:absolute;inset:0;
  background:linear-gradient(to bottom,transparent 30%,var(--bg) 100%);}
.sel-header{padding:16px 20px 14px;text-align:center;}
.sel-header h2{font-family:\'Cinzel Decorative\',serif;font-size:clamp(1.5rem,6vw,2rem);
  color:var(--gold);font-weight:700;margin-bottom:4px;}
.sel-header p{font-family:\'Cinzel\',serif;font-size:.65rem;letter-spacing:.32em;
  text-transform:uppercase;color:rgba(240,201,91,.5);}
.avatar-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;flex:1;overflow:hidden;}
.av-card{position:relative;overflow:hidden;cursor:pointer;border:2px solid transparent;
  transition:border-color .2s ease;aspect-ratio:1/1;}
.av-card.selected{border-color:var(--gold);}
.av-card img{width:100%;height:100%;object-fit:cover;object-position:top center;
  filter:brightness(.78)saturate(.85);transition:filter .3s ease;}
.av-card.selected img,.av-card:hover img{filter:brightness(.9)saturate(1);}
.av-card::after{content:\'\';position:absolute;inset:0;
  background:linear-gradient(to bottom,transparent 40%,rgba(24,24,24,.88) 100%);}
.av-card-name{position:absolute;bottom:10px;left:0;right:0;text-align:center;z-index:3;
  font-family:\'Cinzel\',serif;font-size:.85rem;color:var(--cream);letter-spacing:.06em;}
.av-card.selected::before{content:\'YOU\';position:absolute;top:8px;right:8px;z-index:5;
  font-family:\'Cinzel\',serif;font-size:.42rem;letter-spacing:.32em;color:var(--gold);
  background:rgba(24,24,24,.88);padding:3px 7px;border:1px solid var(--gold-d);border-radius:3px;}
.sel-cta{padding:12px 20px 36px;display:flex;justify-content:center;}
/* ── INTEREST SELECT ── */
.int-topbar{display:flex;align-items:center;padding:14px 20px 0;flex-shrink:0;}
.int-back{font-family:\'Cinzel\',serif;font-size:.58rem;letter-spacing:.3em;text-transform:uppercase;
  color:rgba(245,236,208,.45);background:none;border:none;cursor:pointer;
  display:flex;align-items:center;gap:5px;padding:0;}
.int-back:hover{color:var(--cream);}
.int-header{padding:10px 20px 14px;text-align:left;flex-shrink:0;}
.int-header h2{font-family:\'Cinzel Decorative\',serif;font-size:clamp(1.4rem,6vw,1.9rem);
  color:var(--gold);font-weight:700;margin-bottom:4px;}
.int-header p{font-family:\'Cinzel\',serif;font-size:.65rem;letter-spacing:.32em;
  text-transform:uppercase;color:rgba(240,201,91,.5);}
.int-scroll{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;
  padding:0 20px 120px;position:relative;}
.int-scroll::-webkit-scrollbar{display:none;}
.int-cards-wrap{position:relative;width:100%;}
.int-card{width:200px;height:200px;border-radius:var(--r);overflow:hidden;
  border:1.5px solid rgba(245,236,208,.35);cursor:pointer;position:absolute;
  transition:border-color .25s,transform .25s;}
.int-card:hover,.int-card.selected{border-color:var(--gold);border-width:2px;}
.int-card img{width:100%;height:100%;object-fit:cover;object-position:top;
  filter:brightness(.78)saturate(.82);transition:filter .3s;}
.int-card.selected img,.int-card:hover img{filter:brightness(.9)saturate(1);}
.int-card::after{content:\'\';position:absolute;inset:0;
  background:linear-gradient(to bottom,transparent 40%,rgba(24,24,24,.9) 100%);}
.int-card-info{position:absolute;bottom:0;left:0;right:0;padding:8px 10px;z-index:3;}
.int-card-sub{font-family:\'Cinzel\',serif;font-size:.44rem;letter-spacing:.3em;
  text-transform:uppercase;color:rgba(240,201,91,.5);margin-bottom:2px;}
.int-card-name{font-family:\'Cinzel Decorative\',serif;font-size:.9rem;font-weight:700;}
.int-card.selected::before{content:\'PURSUING\';position:absolute;top:8px;right:8px;z-index:5;
  font-family:\'Cinzel\',serif;font-size:.4rem;letter-spacing:.28em;color:var(--gold);
  background:rgba(24,24,24,.9);padding:3px 7px;border:1px solid var(--gold-d);border-radius:3px;}
.int-footer{position:fixed;bottom:0;left:0;right:0;z-index:20;padding:14px 20px 40px;
  background:linear-gradient(to top,var(--bg) 60%,transparent);
  display:flex;flex-direction:column;align-items:center;gap:8px;}
.int-villain-hint{font-style:italic;font-size:.82rem;color:rgba(200,80,80,.55);
  text-align:center;min-height:1.2em;}
/* ── BIO SCREEN ── */
#s-bio{overflow-y:auto;}
.bio-topnav{display:flex;align-items:center;justify-content:space-between;
  padding:16px 20px 10px;flex-shrink:0;}
.bio-nav-btn{font-family:\'Cinzel\',serif;font-size:.58rem;letter-spacing:.28em;
  text-transform:uppercase;color:rgba(245,236,208,.45);background:none;border:none;
  cursor:pointer;display:flex;align-items:center;gap:5px;min-width:80px;transition:color .2s;}
.bio-nav-btn:hover{color:var(--cream);}
.bio-nav-btn.right{justify-content:flex-end;}
.bio-name-center{text-align:center;}
.bio-char-name{display:block;font-family:\'Cinzel Decorative\',serif;font-size:1.4rem;
  font-weight:700;color:var(--gold);}
.bio-char-sub{display:block;font-family:\'Cinzel\',serif;font-size:.6rem;letter-spacing:.3em;
  text-transform:uppercase;color:rgba(240,201,91,.5);margin-top:2px;}
.bio-portrait-wrap{padding:14px 28px 0;flex-shrink:0;}
.bio-portrait-card{border-radius:var(--r);overflow:hidden;border:1.5px solid var(--gold);
  aspect-ratio:331/496;}
.bio-portrait-card img{width:100%;height:100%;object-fit:cover;object-position:top center;}
.bio-desc{padding:20px 28px 0;text-align:center;}
.bio-desc p{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1rem;
  line-height:1.82;color:var(--cream-d);}
.bio-play-cta{padding:20px 28px 44px;display:flex;justify-content:center;}
/* ── ENCOUNTER ── */
#s-encounter{overflow:hidden;}
.enc-portrait{width:100%;height:40vh;min-height:220px;flex-shrink:0;position:relative;overflow:hidden;}
.enc-portrait img{width:100%;height:100%;object-fit:cover;object-position:top center;}
.enc-portrait::after{content:\'\';position:absolute;inset:0;
  background:linear-gradient(to bottom,transparent 30%,rgba(24,24,24,.96) 100%);}
.enc-portrait-footer{position:absolute;bottom:0;left:0;right:0;z-index:5;
  display:flex;align-items:flex-end;justify-content:space-between;padding:0 14px 10px;}
.enc-left{display:flex;align-items:flex-end;gap:8px;}
.enc-avatar{width:36px;height:36px;border-radius:50%;overflow:hidden;
  border:1.5px solid var(--gold);flex-shrink:0;}
.enc-avatar img{width:100%;height:100%;object-fit:cover;object-position:top;}
.enc-name-block{display:flex;flex-direction:column;gap:2px;}
.enc-act-label{font-family:\'Cinzel\',serif;font-size:.5rem;letter-spacing:.28em;
  text-transform:uppercase;color:rgba(240,201,91,.55);}
.enc-char-name{font-family:\'Cinzel Decorative\',serif;font-size:1rem;font-weight:700;}
/* PIPS */
.enc-pips{display:flex;gap:3px;margin-top:4px;}
.enc-pip{width:22px;height:3px;border-radius:2px;opacity:.35;transition:opacity .3s,box-shadow .3s;}
.enc-pip.done{opacity:1;}
.enc-pip.active{opacity:1;}
/* BAROMETER */
.barometer{display:flex;flex-direction:column;align-items:flex-end;gap:3px;}
.baro-label{font-family:\'Cinzel\',serif;font-size:.45rem;letter-spacing:.28em;
  text-transform:uppercase;color:rgba(240,201,91,.55);}
.baro-track{width:90px;height:4px;background:rgba(255,255,255,.1);
  border:1px solid rgba(240,201,91,.3);border-radius:2px;overflow:visible;position:relative;}
.baro-fill{height:100%;border-radius:2px;
  background:linear-gradient(90deg,#7a1020,#C9A84C,#F0D080);
  transition:width .6s ease;position:relative;}
.baro-arrow{position:absolute;right:-4px;top:-6px;width:0;height:0;
  border-left:4px solid transparent;border-right:4px solid transparent;
  border-top:7px solid var(--gold);opacity:0;transition:opacity .4s;}
.baro-arrow.show{opacity:1;}
.baro-mood{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:.75rem;
  font-style:italic;color:rgba(240,201,91,.7);}
/* DIALOGUE PANEL */
.enc-panel{flex:1;display:flex;flex-direction:column;overflow:hidden;}
.dialogue-area{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:14px 16px 8px;}
.dialogue-area::-webkit-scrollbar{width:0;}
.dlg-line{margin-bottom:12px;animation:fadeup .38s ease both;}
.dlg-who{font-family:\'Cinzel\',serif;font-size:.48rem;letter-spacing:.3em;
  text-transform:uppercase;margin-bottom:3px;}
.dlg-who.narrator{color:rgba(240,201,91,.38);}
.dlg-who.interest{color:inherit;}/* set dynamically */
.dlg-who.player{color:#A8C5DA;}
.dlg-who.villain{color:rgba(200,80,80,.75);}
.dlg-text{font-size:1rem;line-height:1.72;color:rgba(245,236,208,.82);}
.dlg-text.it{font-style:italic;color:rgba(245,236,208,.55);}
.dlg-text.moment{font-style:italic;color:var(--gold);
  border-left:2px solid var(--gold-d);padding-left:10px;}
.dlg-text.spook{color:rgba(245,236,208,.75);}
/* ENC FOOTER */
.enc-footer{flex-shrink:0;border-top:1px solid rgba(240,201,91,.10);padding:10px 14px 20px;}
.choices-lbl{font-family:\'Cinzel\',serif;font-size:.5rem;letter-spacing:.3em;
  text-transform:uppercase;color:rgba(245,236,208,.4);margin-bottom:8px;}
.choices-grid{display:flex;flex-direction:column;gap:6px;}
.choice-btn{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:.95rem;font-style:italic;
  color:var(--cream-d);background:transparent;border:1px solid rgba(245,236,208,.2);
  border-radius:6px;padding:9px 14px;cursor:pointer;text-align:left;
  transition:all .2s ease;line-height:1.4;}
.choice-btn:hover{border-color:var(--gold);background:rgba(240,201,91,.06);color:var(--cream);}
.choice-btn:disabled{opacity:.42;pointer-events:none;}
.choice-tag{font-family:\'Cinzel\',serif;font-size:.44rem;letter-spacing:.28em;
  text-transform:uppercase;color:rgba(240,201,91,.65);display:block;margin-bottom:3px;}
.continue-row{display:none;justify-content:flex-end;margin-top:8px;}
.continue-row.show{display:flex;}
.btn-continue{font-family:\'Cinzel\',serif;font-size:.55rem;letter-spacing:.38em;
  text-transform:uppercase;color:var(--gold);background:transparent;
  border:1px solid rgba(240,201,91,.4);border-radius:5px;padding:10px 20px;cursor:pointer;
  transition:all .25s;}
.btn-continue:hover{border-color:var(--gold);background:rgba(240,201,91,.08);}
/* ── RESULT SCREEN ── */
.result-title-wrap{padding:36px 24px 20px;text-align:center;flex-shrink:0;}
.result-title-wrap h1{font-family:\'Cinzel Decorative\',serif;font-size:clamp(1.6rem,7vw,2.4rem);
  font-weight:700;letter-spacing:.04em;line-height:1.2;}
.result-scene{position:relative;flex-shrink:0;height:300px;overflow:hidden;}
.result-scene-bg{width:100%;height:100%;object-fit:cover;filter:brightness(.72);}
.result-portrait{position:absolute;left:50%;bottom:-10px;transform:translateX(-50%);
  width:48%;aspect-ratio:1/1;border-radius:var(--r);overflow:hidden;
  border:1.5px solid rgba(245,236,208,.55);}
.result-portrait img{width:100%;height:100%;object-fit:cover;object-position:top;}
.result-body{padding:24px 28px 8px;text-align:center;flex:1;}
.result-body p{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1.05rem;
  line-height:1.82;color:var(--cream-d);margin-bottom:16px;}
.result-goal-lbl{font-family:\'Cinzel\',serif;font-size:.6rem;letter-spacing:.38em;
  text-transform:uppercase;color:var(--gold);display:block;margin-bottom:16px;}
.result-cta{padding:0 28px 48px;display:flex;flex-direction:column;align-items:center;gap:12px;}
/* ── TRUE ENDING ── */
#s-true-end{overflow-y:auto;}
.true-scene{position:relative;height:320px;flex-shrink:0;overflow:hidden;}
.true-scene img.true-bg{width:100%;height:100%;object-fit:cover;filter:brightness(.6);}
.true-scene img.true-portrait{position:absolute;left:50%;bottom:0;transform:translateX(-50%);
  width:55%;border-radius:var(--r) var(--r) 0 0;object-fit:cover;object-position:top;
  border:1.5px solid rgba(240,201,91,.5);}
.true-body{padding:32px 28px 0;text-align:center;flex:1;}
.true-title{font-family:\'Cinzel Decorative\',serif;font-size:clamp(1.8rem,7vw,2.6rem);
  color:var(--gold);font-weight:700;letter-spacing:.06em;margin-bottom:12px;}
.true-char{font-family:\'Cinzel\',serif;font-size:.65rem;letter-spacing:.38em;
  text-transform:uppercase;color:rgba(240,201,91,.55);margin-bottom:24px;}
.true-narration{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1.1rem;
  line-height:1.92;color:var(--cream-d);margin-bottom:20px;}
.true-moment{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1.15rem;
  font-style:italic;color:var(--gold);border-left:2px solid var(--gold-d);
  padding:4px 0 4px 14px;text-align:left;margin-bottom:28px;}
.true-cta{padding:0 28px 60px;display:flex;justify-content:center;}
/* ANIMATIONS */
@keyframes fadeup{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@keyframes fadein{from{opacity:0}to{opacity:1}}
</style>
</head>
<body>

<!-- ══ 1. LANDING ══ -->
<section class="screen active" id="s-land">
  <div class="land-title">
    <h1>THE AFFINITY<br>OF VISSAN</h1>
  </div>
  <div class="land-image">
    <img id="img-land" src="" alt="Vissan">
  </div>
  <div class="land-body">
    <div class="land-subtitle">AN AI-DRIVEN VISUAL NOVEL</div>
    <p class="land-para">In the realm of Vissan, vampire nobility rules from obsidian towers above a kingdom that has not seen full sunlight in three centuries.</p>
    <p class="land-para">Below their spires, humans born with arcane gifts and elves bound by ancient oaths navigate a world where every alliance is a weapon — and every emotion, a door.</p>
    <p class="land-tagline">Some doors should not be opened carelessly.</p>
  </div>
  <div class="land-cta">
    <button class="btn" onclick="goTo(\'s-avatar\')">ENTER VISSAN</button>
  </div>
</section>

<!-- ══ 2. AVATAR SELECT ══ -->
<section class="screen" id="s-avatar">
  <div class="sel-hero">
    <img id="img-avatar-hero" src="" alt="">
  </div>
  <div class="sel-header">
    <h2>Who Are You?</h2>
    <p>Step 1 · Choose Your Character</p>
  </div>
  <div class="avatar-grid" id="avatar-grid"></div>
  <div class="sel-cta">
    <button class="btn" onclick="onChoosePursue()">CHOOSE WHO TO PURSUE →</button>
  </div>
</section>

<!-- ══ 3. INTEREST SELECT ══ -->
<section class="screen" id="s-interest">
  <div class="int-topbar">
    <button class="int-back" onclick="goTo(\'s-avatar\')">← BACK</button>
  </div>
  <div class="int-header">
    <h2>Who to Pursue?</h2>
    <p>Step 2 · Choose Your Love Interest</p>
  </div>
  <div class="int-scroll">
    <div class="int-cards-wrap" id="int-cards-wrap"></div>
  </div>
  <div class="int-footer">
    <div class="int-villain-hint" id="int-villain-hint"></div>
    <button class="btn" id="btn-start" disabled onclick="startEncounter()">BEGIN THE STORY →</button>
  </div>
</section>

<!-- ══ 4. BIO ══ -->
<section class="screen" id="s-bio">
  <div class="bio-topnav">
    <button class="bio-nav-btn" onclick="bioPrev()">← <span id="bio-prev-name"></span></button>
    <div class="bio-name-center">
      <span class="bio-char-name" id="bio-char-name"></span>
      <span class="bio-char-sub" id="bio-char-sub"></span>
    </div>
    <button class="bio-nav-btn right" onclick="bioNext()"><span id="bio-next-name"></span> →</button>
  </div>
  <div class="bio-portrait-wrap">
    <div class="bio-portrait-card">
      <img id="bio-portrait-img" src="" alt="">
    </div>
  </div>
  <div class="bio-desc"><p id="bio-desc-p"></p></div>
  <div class="bio-play-cta">
    <button class="btn" id="bio-play-btn">PLAY AS …</button>
  </div>
</section>

<!-- ══ 5. ENCOUNTER ══ -->
<section class="screen" id="s-encounter">
  <div class="enc-portrait">
    <img id="enc-portrait-img" src="" alt="">
    <div class="enc-portrait-footer">
      <div class="enc-left">
        <div class="enc-avatar"><img id="enc-avatar-img" src="" alt=""></div>
        <div class="enc-name-block">
          <span class="enc-act-label" id="act-badge"></span>
          <span class="enc-char-name" id="enc-interest-name"></span>
          <div class="enc-pips" id="enc-pips"></div>
        </div>
      </div>
      <div class="barometer">
        <div class="baro-label">INTEREST</div>
        <div class="baro-track">
          <div class="baro-fill" id="baro-fill" style="width:30%">
            <div class="baro-arrow" id="baro-arrow"></div>
          </div>
        </div>
        <div class="baro-mood" id="baro-mood">—</div>
      </div>
    </div>
  </div>
  <div class="enc-panel">
    <div class="dialogue-area scroll-y" id="dialogue-area"></div>
    <div class="enc-footer">
      <div class="choices-lbl" id="choices-lbl"></div>
      <div class="choices-grid" id="choices-grid"></div>
      <div class="continue-row" id="continue-row">
        <button class="btn-continue" id="btn-continue" onclick="onContinue()">CONTINUE →</button>
      </div>
    </div>
  </div>
</section>

<!-- ══ 6. RESULT ══ -->
<section class="screen" id="s-result">
  <div class="result-title-wrap">
    <h1 id="result-title" class="t-disp"></h1>
  </div>
  <div class="result-scene">
    <img class="result-scene-bg" id="result-bg-img" src="" alt="">
    <div class="result-portrait">
      <img id="result-portrait-img" src="" alt="">
    </div>
  </div>
  <div class="result-body">
    <p id="result-msg"></p>
    <span class="result-goal-lbl">What is your next goal?</span>
  </div>
  <div class="result-cta" id="result-cta"></div>
</section>

<!-- ══ 7. TRUE ENDING ══ -->
<section class="screen" id="s-true-end">
  <div class="true-scene">
    <img class="true-bg" id="true-bg-img" src="" alt="">
    <img class="true-portrait" id="true-portrait-img" src="" alt="">
  </div>
  <div class="true-body">
    <div class="true-title" id="true-title">The Affinity of Vissan</div>
    <div class="true-char" id="true-char"></div>
    <p class="true-narration" id="true-narration"></p>
    <div class="true-moment" id="true-moment"></div>
  </div>
  <div class="true-cta">
    <button class="btn" onclick="goTo(\'s-avatar\');resetState()">PLAY AGAIN</button>
  </div>
</section>

<!-- ASSET PLACEHOLDERS (replaced by inject_assets.py) -->
<script>
var IMG={kohan:'__IMG_KOHAN__',andam:'__IMG_ANDAM__',catarina:'__IMG_CATARINA__',max:'__IMG_MAX__'};
var BG={village:'__BG_VILLAGE__',forest:'__BG_FOREST__',castle:'__BG_CASTLE__',world:'__BG_WORLD__'};
</script>

<!-- GAME SCRIPT OPENS BELOW -->
<script>
'''

with open('/Users/KaterinaHuezo/Desktop/affections-of-vissan/affections_of_vissan_v6.html', 'w') as f:
    f.write(content)
print("Part 1 written:", len(content), "chars")
