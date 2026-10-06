#!/usr/bin/env python3
"""Builds the five pages of lartedellamore.com from the texts below.
Run:  python3 tools/build.py     (from the repository root)
Edit the words here, run it, and commit the changed .html files."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "amore@lartedellamore.com"
SITE = "https://lartedellamore.com"
APP = "https://lartedellamore.github.io/illuminated-life/"

NAV = [("index.html", "The house"), ("coaching.html", "Coaching"), ("photography.html", "Photography"),
       ("atelier.html", "Atelier"), ("about.html", "About")]


def page(slug, title, desc, rail, body):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{t}</a>' for h, t in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if slug == 'index.html' else slug}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="assets/crest-small.png">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to the text</a>
<div class="wrap">
<header class="top">
  <a class="mark" href="index.html">L&rsquo;arte dell&rsquo;amore</a>
  <nav aria-label="Pages">{nav}</nav>
</header>
<div class="page">
  <p class="rail">{rail}</p>
  <main class="col" id="main">
{body}
  </main>
</div>
<footer class="foot">
  <span>L&rsquo;arte dell&rsquo;amore &middot; Amsterdam &middot; Charity is the crown of life.</span>
  <nav aria-label="Footer"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="about.html#contact">Contact</a><a href="{APP}" rel="noopener">Illuminated Life</a></nav>
</footer>
</div>
</body>
</html>
"""


def contact(line):
    return f"""    <section class="sec" id="contact" aria-labelledby="c-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="c-t">{line}</h2>
      <p class="addr">{EMAIL}</p>
      <div class="row"><a class="btn" href="mailto:{EMAIL}">Write to me</a><span class="small">I answer within two working days, in English, Dutch, Spanish or French.</span></div>
    </section>"""


HOME = f"""    <section class="crest" aria-labelledby="h-t">
      <img src="assets/crest.webp" width="1100" height="1456" alt="The crest of L'arte dell'amore: a winged shield bearing three flaming hearts on a cross, a sword behind it, and a ribbon with the name.">
      <p class="eyebrow">Amsterdam &middot; coaching, photography, and things made by hand and by code</p>
      <h1 class="display" id="h-t">Charity is the <em>crown</em> of life.</h1>
      <p class="lede">L&rsquo;arte dell&rsquo;amore is a small house with one purpose: to help people see their life whole, and order it to love.</p>
    </section>

    <section class="sec" aria-labelledby="m-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Mission</p>
      <h2 class="h2" id="m-t">To bring the truth of love and grace to people everywhere.</h2>
      <div class="prose">
        <p>To honour and protect the dignity of every human being, and to serve the highest good in humility and unity.</p>
        <p>Through coaching, photography and apps, we help people see their gifts and their life as one whole, and build the virtues and habits of a life ordered to the good of all. That is where happiness begins.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="i-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">The house</p>
      <h2 class="h2" id="i-t">Seven rooms, one door.</h2>
      <ol class="index">
        <li><span class="n">i</span><a class="t" href="{APP}" rel="noopener">Illuminated Life</a><span class="state open">Open</span><span class="d">A Catholic rule of life across twelve fields of stewardship: the app, the book, and a plan for the home.</span></li>
        <li><span class="n">ii</span><a class="t" href="coaching.html">Health and lifestyle coaching</a><span class="state open">Open</span><span class="d">One to one, online or in person in Amsterdam.</span></li>
        <li><span class="n">iii</span><a class="t" href="photography.html">Photography</a><span class="state open">Open</span><span class="d">Weddings, engagements, families, and portraits for people and their work.</span></li>
        <li><span class="n">iv</span><a class="t" href="atelier.html#digital">Digital products</a><span class="state">In the making</span><span class="d">Catholicity OS for Notion, and Catholic Healing Arts.</span></li>
        <li><span class="n">v</span><a class="t" href="atelier.html#gifts">Gifts</a><span class="state">In the making</span><span class="d">Clothing and jewellery.</span></li>
        <li><span class="n">vi</span><a class="t" href="atelier.html#prints">Art prints</a><span class="state">In the making</span><span class="d">Drawn in gold fine line.</span></li>
        <li><span class="n">vii</span><a class="t" href="atelier.html#apps">Apps</a><span class="state">In the making</span><span class="d">Global Holy Rosary, Beatitude, Eternal Camino.</span></li>
      </ol>
    </section>

{contact("Begin with a conversation.")}"""

COACHING = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Health and lifestyle coaching</p>
      <h1 class="display" id="h-t">Your whole life, <em>in order</em>.</h1>
      <p class="lede">One-to-one coaching for people who are tired of fixing one corner of life while the rest waits. We look at body, mind, heart and home together, and change one thing at a time.</p>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="w-t">How we work</h2>
      <ol class="steps">
        <li><b>A first conversation</b><span>You tell me where you are and what you hope for. I tell you plainly whether I can help.</span></li>
        <li><b>The whole picture</b><span>We map your life as it is: sleep, food, movement, work, relationships, rest, prayer if that is part of your life.</span></li>
        <li><b>One field at a time</b><span>We choose the one change that will carry the others, and make it small enough to keep.</span></li>
        <li><b>Habits that hold</b><span>We meet regularly, adjust what did not work, and build until the habit no longer needs me.</span></li>
      </ol>
    </section>

    <section class="sec" aria-labelledby="p-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="p-t">Practical</h2>
      <dl class="terms">
        <dt>Where</dt><dd>Online, or in person in Amsterdam.</dd>
        <dt>Languages</dt><dd>English, Dutch, Spanish, French.</dd>
        <dt>Coach</dt><dd>Wietske, certified holistic health coach (Institute for Integrative Nutrition).</dd>
        <dt>Fees</dt><dd>Sent with the answer to your first message.</dd>
      </dl>
      <p class="small">Coaching supports healthy living. It does not diagnose or treat illness and is no substitute for your doctor or therapist.</p>
    </section>

{contact("Tell me where you are.")}"""

PHOTO = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Photography</p>
      <h1 class="display" id="h-t">Capturing beauty through the <em>art</em> of photography.</h1>
      <p class="lede">Weddings, engagements, families and portraits. Unhurried, in natural light, and made to be printed and kept.</p>
    </section>

    <section class="sec" aria-labelledby="g-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="g-t">Portfolio</h2>
      <div class="mounts">
        <div class="mount wide"><span>Wedding</span></div>
        <div class="mount"><span>Engagement</span></div>
        <div class="mount"><span>Family</span></div>
        <div class="mount"><span>Portrait</span></div>
        <div class="mount"><span>Business portrait</span></div>
      </div>
    </section>

    <section class="sec" aria-labelledby="s-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="s-t">What I photograph</h2>
      <dl class="terms">
        <dt>Weddings</dt><dd>The whole day, from the quiet before to the last dance.</dd>
        <dt>Engagements</dt><dd>An hour or two somewhere that matters to you both.</dd>
        <dt>Families</dt><dd>At home or outdoors, including newborn and pregnancy.</dd>
        <dt>Portraits</dt><dd>Personal portraits, and authentic, professional headshots for your work.</dd>
      </dl>
    </section>

{contact("Tell me about your day.")}"""

ATELIER = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Atelier</p>
      <h1 class="display" id="h-t">Made slowly, <em>for keeps</em>.</h1>
      <p class="lede">Tools, gifts and prints from the same house. One is open today. The others are in the making, and listed here so you know what is coming.</p>
    </section>

    <section class="sec" aria-labelledby="il-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Open</p>
      <h2 class="h2" id="il-t">Illuminated Life</h2>
      <div class="prose">
        <p>One Master entrusts one steward with twelve fields in three rings: Person, Household and World. The app keeps your rule of life, your diary and the Church&rsquo;s year. It never scores you, and everything stays on your own device.</p>
        <p>With it comes the book, <i>Illuminated: The Image of God, Embodied</i>.</p>
      </div>
      <div class="row"><a class="btn" href="{APP}" rel="noopener">Open Illuminated Life</a></div>
    </section>

    <section class="sec" id="digital" aria-labelledby="d-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="d-t">Digital products</h2>
      <dl class="terms">
        <dt>Catholicity OS</dt><dd>A Notion workspace for the whole of a Catholic life, built on the same three rings.</dd>
        <dt>Catholic Healing Arts</dt><dd>Details to follow.</dd>
      </dl>
    </section>

    <section class="sec" id="apps" aria-labelledby="a-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="a-t">Apps</h2>
      <dl class="terms">
        <dt>Global Holy Rosary</dt><dd>Pray the Rosary for every nation in its own language and watch the world map turn gold.</dd>
        <dt>Beatitude</dt><dd>A Catholic social app that rewards love instead of popularity.</dd>
        <dt>Eternal Camino</dt><dd>A travel companion with a page for every country.</dd>
      </dl>
    </section>

    <section class="sec" id="prints" aria-labelledby="pr-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="pr-t">Art prints</h2>
      <p class="prose">Drawings in gold fine line on natural paper.</p>
    </section>

    <section class="sec" id="gifts" aria-labelledby="gf-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="gf-t">Gifts</h2>
      <p class="prose">Clothing in natural fabrics, and jewellery.</p>
    </section>

{contact("Ask to be told when something opens.")}"""

ABOUT = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">About</p>
      <h1 class="display" id="h-t">The art of <em>love</em>, practised.</h1>
      <p class="lede">I am Wietske: a holistic health and lifestyle coach and a photographer in Amsterdam. L&rsquo;arte dell&rsquo;amore gathers my work under one roof.</p>
    </section>

    <section class="sec" aria-labelledby="b-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="b-t">What I believe</h2>
      <div class="prose">
        <p>Every person carries a dignity that is given, never earned. A good life is one life, where body, mind, heart, home and work serve the same end.</p>
        <p>Charity is the crown of that life. Everything made in this house is meant to help someone love a little better: a coaching hour, a photograph of the people you love, a tool that keeps your day in order.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="v-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="v-t">Mission and vision</h2>
      <div class="panel">
        <p class="eyebrow">Mission</p>
        <p class="lede">To bring the truth of love and grace to people everywhere, to honour and protect the dignity of every human being, and to serve the highest good in humility and unity.</p>
        <p class="eyebrow">Vision</p>
        <p class="lede">Through coaching, photography and apps, we help people see their gifts and their life as one whole, and build the virtues and habits of a life ordered to the good of all, which is where happiness begins.</p>
      </div>
    </section>

{contact("Write to me.")}"""

PAGES = [
    ("index.html", "L'arte dell'amore", "Coaching, photography and tools for a life ordered to love. Amsterdam.", "L&rsquo;arte dell&rsquo;amore &nbsp;&middot;&nbsp; <b>Amsterdam</b>", HOME),
    ("coaching.html", "Coaching · L'arte dell'amore", "One-to-one holistic health and lifestyle coaching, online or in Amsterdam.", "Coaching &nbsp;&middot;&nbsp; <b>one to one</b>", COACHING),
    ("photography.html", "Photography · L'arte dell'amore", "Wedding, engagement, family and portrait photography from Amsterdam.", "Photography &nbsp;&middot;&nbsp; <b>natural light</b>", PHOTO),
    ("atelier.html", "Atelier · L'arte dell'amore", "Illuminated Life, digital products, apps, art prints and gifts.", "Atelier &nbsp;&middot;&nbsp; <b>made slowly</b>", ATELIER),
    ("about.html", "About · L'arte dell'amore", "Wietske, holistic health coach and photographer in Amsterdam.", "About &nbsp;&middot;&nbsp; <b>Wietske</b>", ABOUT),
]

for slug, title, desc, rail, body in PAGES:
    (ROOT / slug).write_text(page(slug, title, desc, rail, body), encoding="utf-8")

# A body-only copy of the home page with the stylesheet inlined, for previewing outside GitHub.
css = (ROOT / "css/site.css").read_text(encoding="utf-8").replace('url("../assets/', 'url("assets/')
home = (ROOT / "index.html").read_text(encoding="utf-8")
inner = re.search(r"<body>(.*)</body>", home, re.S).group(1)
(ROOT / "tools/preview.html").write_text(f"<title>L'arte dell'amore</title>\n<style>\n{css}\n</style>\n{inner}", encoding="utf-8")
print("built", [p[0] for p in PAGES])
