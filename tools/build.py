#!/usr/bin/env python3
"""Builds lartedellamore.com in English (root) and Dutch (nl/) from the texts below.
Run:  python3 tools/build.py     (from the repository root)
Edit the words here, run it, and commit the changed .html files."""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "amore@lartedellamore.com"
SITE = "https://lartedellamore.com"
APP = "https://lartedellamore.github.io/illuminated-life/"
DONATE = "https://familyofpuregrace.wixsite.com/my-site/donate"
FOPG = "https://familyofpuregrace.wixsite.com/my-site"

SLUGS = ["index.html", "coaching.html", "photography.html", "atelier.html", "letter.html", "about.html"]
T = {
    "en": dict(nav=["The house", "Coaching", "Photography", "Atelier", "The Letter", "About"],
               skip="Skip to the text", foot="Charity is the crown of life.", contact="Contact",
               write="Write to me", answer="I answer within two working days, in English or Dutch. Slower on feast days and powder days.",
               other="Nederlands", other_code="nl", pages="Pages", footer="Footer"),
    "nl": dict(nav=["Het huis", "Coaching", "Fotografie", "Atelier", "De Brief", "Over mij"],
               skip="Ga naar de tekst", foot="De liefde is de kroon van het leven.", contact="Contact",
               write="Schrijf mij", answer="Ik antwoord binnen twee werkdagen, in het Nederlands of Engels. Iets trager op feestdagen en bij verse sneeuw.",
               other="English", other_code="en", pages="Pagina's", footer="Voettekst"),
}


def page(slug, title, desc, rail, body, lang="en"):
    t = T[lang]
    up = "" if lang == "en" else "../"          # path back to the site root
    other = ("nl/" + slug) if lang == "en" else ("../" + slug)
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == slug else ""}>{n}</a>' for h, n in zip(SLUGS, t["nav"]))
    tail = "" if slug == "index.html" else slug
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/{'' if lang == 'en' else 'nl/'}{tail}">
<link rel="alternate" hreflang="en" href="{SITE}/{tail}">
<link rel="alternate" hreflang="nl" href="{SITE}/nl/{tail}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="{up}assets/crest-small.png">
<link rel="stylesheet" href="{up}css/site.css">
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<div class="wrap">
<header class="top">
  <a class="mark" href="index.html"><img src="{up}assets/crest-small.png" alt="" width="360" height="476">L&rsquo;arte dell&rsquo;amore</a>
  <nav aria-label="{t["pages"]}">{nav}<a class="lang" href="{other}" lang="{t["other_code"]}" hreflang="{t["other_code"]}">{t["other"]}</a></nav>
</header>
<div class="page">
  <p class="rail">{rail}</p>
  <main class="col" id="main">
{body}
  </main>
</div>
<footer class="foot">
  <span>L&rsquo;arte dell&rsquo;amore &middot; Amsterdam &middot; {t["foot"]}</span>
  <nav aria-label="{t["footer"]}"><a href="mailto:{EMAIL}">{EMAIL}</a><a href="about.html#contact">{t["contact"]}</a><a href="{APP}" rel="noopener">Illuminated Life</a></nav>
</footer>
</div>
</body>
</html>
"""


def contact(line, lang="en"):
    t = T[lang]
    return f"""    <section class="sec" id="contact" aria-labelledby="c-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="c-t">{line}</h2>
      <p class="addr">{EMAIL}</p>
      <div class="row"><a class="btn" href="mailto:{EMAIL}">{t["write"]}</a><span class="small">{t["answer"]}</span></div>
    </section>"""


# ───────────────────────── English ─────────────────────────
SUBSCRIBE = f"mailto:{EMAIL}?subject=Subscribe%20to%20The%20Letter"

HOME = f"""    <section class="crest" aria-labelledby="h-t">
      <p class="eyebrow">Amsterdam &middot; coaching, photography, and things made by hand and by code</p>
      <h1 class="display" id="h-t">Charity is the <em>crown</em> of life.</h1>
      <p class="lede">L&rsquo;arte dell&rsquo;amore is a small house with a large hope: that you may see your life whole, and learn to spend it on love. I am still learning this myself, which is why the door is open.</p>
    </section>

    <section class="sec" aria-labelledby="m-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Mission</p>
      <h2 class="h2" id="m-t">To order the whole of life to love.</h2>
      <p class="lede">L&rsquo;arte dell&rsquo;amore accompanies people in the examination of conscience and the formation of virtue, so that each person may order their whole life to love: Love*, neighbour, and the common good.</p>
      <div class="prose">
        <p>I do this through personal coaching, photography that honours human relationships, digital tools for daily life, and works of art.</p>
      </div>
      <p class="eyebrow">Vision</p>
      <p class="lede">A world in which every person is received as bearing an inviolable dignity, knows their gifts, and has the habits and the freedom to spend their life for the good of others. I hold that this is the foundation of lasting joy, and of peace.</p>
      <p class="small">* God. &nbsp;&middot;&nbsp; <a href="about.html#v-t">Read my seven values</a></p>
    </section>

    <section class="sec" aria-labelledby="i-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">The house</p>
      <h2 class="h2" id="i-t">Seven rooms, one door.</h2>
      <ol class="index">
        <li><span class="n">i</span><a class="t" href="{APP}" rel="noopener">Illuminated Life</a><span class="state open">Open</span><span class="d">A rule of life across twelve fields of stewardship. No streaks, no points; the saints managed without a leaderboard.</span></li>
        <li><span class="n">ii</span><a class="t" href="coaching.html">Health and lifestyle coaching</a><span class="state open">Open</span><span class="d">One to one, online or in Amsterdam. From &euro;95 a session.</span></li>
        <li><span class="n">iii</span><a class="t" href="photography.html">Photography</a><span class="state open">Open</span><span class="d">Weddings, engagements, families and portraits. From &euro;195.</span></li>
        <li><span class="n">iv</span><a class="t" href="letter.html">The Letter</a><span class="state open">Free</span><span class="d">Once a week: one thing for the body, one for the mind, one story for the soul.</span></li>
        <li><span class="n">v</span><a class="t" href="atelier.html#digital">Digital products</a><span class="state">In the making</span><span class="d">Catholicity OS for Notion, and Catholic Healing Arts.</span></li>
        <li><span class="n">vi</span><a class="t" href="atelier.html#prints">Art prints and gifts</a><span class="state">In the making</span><span class="d">Gold fine line on natural paper; ethical and sustainably produced clothing.</span></li>
        <li><span class="n">vii</span><a class="t" href="atelier.html#apps">Apps</a><span class="state">In the making</span><span class="d">Global Holy Rosary, Beatitude, Eternal Camino.</span></li>
      </ol>
    </section>

{contact("Begin with a conversation.")}"""

COACHING = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Health and lifestyle coaching</p>
      <h1 class="display" id="h-t">Your whole life, <em>in order</em>.</h1>
      <p class="lede">Most people do not need more information about sleep, food or exercise. They need someone patient, honest and on their side while they change one thing. That is the whole job, and it is a beautiful one.</p>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="w-t">How I work</h2>
      <ol class="steps">
        <li><b>A first conversation</b><span>You tell me where you are and what you hope for. I tell you plainly whether I can help, and if I cannot, who might.</span></li>
        <li><b>The whole picture</b><span>I look with you at your life as it actually is: sleep, food, movement, work, the people you love, rest, and prayer if that is part of your life. No judgement. I have seen my own.</span></li>
        <li><b>One field at a time</b><span>I help you choose the one change that carries the others, and make it small enough to survive your worst week. I will not hand you a forty-step morning routine. Nobody has that kind of morning.</span></li>
        <li><b>Habits that hold</b><span>I meet you regularly, adjust what did not work, and build with you until the habit no longer needs me. Being made unnecessary is the goal.</span></li>
      </ol>
    </section>

    <section class="sec" aria-labelledby="f-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="f-t">Fees</h2>
      <dl class="terms">
        <dt>First conversation</dt><dd>20 minutes, free. You and I find out whether this suits.</dd>
        <dt>Single session</dt><dd><b>&euro;95</b> &middot; 60 minutes, online or in Amsterdam.</dd>
        <dt>A season together</dt><dd><b>&euro;540</b> &middot; three months, six sessions, with short messages in between. This is where real change usually happens.</dd>
      </dl>
      <p class="small">If the fee is the only thing standing between you and help, write to me anyway. I will find a way with you.</p>
    </section>

    <section class="sec" aria-labelledby="p-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="p-t">Practical</h2>
      <dl class="terms">
        <dt>Where</dt><dd>Online, or in person in Amsterdam.</dd>
        <dt>Languages</dt><dd>English and Dutch.</dd>
        <dt>Coach</dt><dd>Wietske, certified holistic health coach (Institute for Integrative Nutrition), studying for a bachelor&rsquo;s degree in Psychology.</dd>
      </dl>
      <p class="small">Coaching supports healthy living. It does not diagnose or treat illness and is no substitute for your doctor or therapist.</p>
    </section>

{contact("Tell me where you are.")}"""

PHOTO = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Photography</p>
      <h1 class="display" id="h-t">Capturing beauty through the <em>art</em> of photography.</h1>
      <p class="lede">A photograph is a small act of reverence: it says this person, this day, was worth keeping. I work unhurried, in natural light, and I have never once asked anyone to say cheese.</p>
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
      <h2 class="h2" id="s-t">What I photograph, and what it costs</h2>
      <dl class="terms">
        <dt>Weddings</dt><dd><b>&euro;1,950</b> &middot; The whole day, from the quiet before to the last dance. You receive the full edited gallery.</dd>
        <dt>Engagements</dt><dd><b>&euro;295</b> &middot; An hour or two somewhere that matters to you both. Also a gentle rehearsal for the wedding.</dd>
        <dt>Families</dt><dd><b>&euro;325</b> &middot; At home or outdoors, including newborn and pregnancy. Children may behave exactly as they are.</dd>
        <dt>Portraits</dt><dd><b>&euro;195</b> &middot; A personal portrait that looks like you on a good day, which is the truth.</dd>
        <dt>Business portraits</dt><dd><b>&euro;245</b> &middot; Authentic, professional headshots for your work.</dd>
      </dl>
      <p class="small">Prices are in euros. Travel within Amsterdam is included; further afield, I agree it with you beforehand.</p>
    </section>

{contact("Tell me about your day.")}"""

ATELIER = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Atelier</p>
      <h1 class="display" id="h-t">Made slowly, <em>for keeps</em>.</h1>
      <p class="lede">Tools, prints and gifts from the same house. One is open today. The rest are in the making, and I would sooner tell you that than pretend otherwise.</p>
    </section>

    <section class="sec" aria-labelledby="il-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Open &middot; free</p>
      <h2 class="h2" id="il-t">Illuminated Life</h2>
      <div class="prose">
        <p>One Master entrusts one steward with twelve fields in three rings: Person, Household and World. The app keeps your rule of life, your diary and the Church&rsquo;s year. It never scores you, it forgives a missed day at once, and everything stays on your own device.</p>
        <p>With it comes the book, <i>Illuminated: The Image of God, Embodied</i>.</p>
      </div>
      <div class="row"><a class="btn" href="{APP}" rel="noopener">Open Illuminated Life</a></div>
    </section>

    <section class="sec" id="digital" aria-labelledby="d-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="d-t">Digital products</h2>
      <dl class="terms">
        <dt>Catholicity OS</dt><dd>A Notion workspace for the whole of a Catholic life, built on the same three rings. Profits go to the building fund of Family of Pure Grace.</dd>
        <dt>Catholic Healing Arts</dt><dd>Details to follow.</dd>
      </dl>
    </section>

    <section class="sec" id="apps" aria-labelledby="a-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In the making</p>
      <h2 class="h2" id="a-t">Apps</h2>
      <dl class="terms">
        <dt>Global Holy Rosary</dt><dd>Pray the Rosary for every nation in its own language and watch the world map turn gold.</dd>
        <dt>Beatitude</dt><dd>A Catholic social app that rewards love instead of popularity. An unusual business model, I admit.</dd>
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
      <p class="prose">Ethical and sustainably produced clothing.</p>
    </section>

{contact("Ask to be told when something opens.")}"""

LETTER = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">The Letter &middot; weekly &middot; free</p>
      <h1 class="display" id="h-t">One letter a week, for the <em>whole</em> of you.</h1>
      <p class="lede">Short enough to read with one coffee. Three parts, every week, for body, mind and soul.</p>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="w-t">What arrives</h2>
      <ol class="steps">
        <li><b>The body</b><span>One practice from the world of biohacking, examined honestly: what the evidence supports, what is hype, and what your grandmother already knew.</span></li>
        <li><b>The mind</b><span>A short reflection from the Catholic theology of health and flourishing. The body as gift, rest as obedience, and why holiness and wellbeing are friends.</span></li>
        <li><b>The story</b><span>One Bible story read with a psychologist&rsquo;s eye, drawn from the books I am writing. Scripture has been reading us for a long time.</span></li>
      </ol>
    </section>

    <section class="sec" aria-labelledby="s-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="s-t">Sign up</h2>
      <div class="panel">
        <p class="lede">Send one email with the word <i>Subscribe</i>, and you are in.</p>
        <p class="addr">{EMAIL}</p>
        <div class="row"><a class="btn" href="{SUBSCRIBE}">Subscribe by email</a></div>
        <p class="small">I keep your email address and nothing else, and use it only for this letter. To stop, reply <i>stop</i> to any issue. No tricks, no selling of lists.</p>
      </div>
      <p class="small">The Letter shares ideas for healthy living and is not medical advice. Talk to your doctor before changing treatment, fasting or supplements.</p>
    </section>

{contact("Or simply say hello.")}"""

ABOUT = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">About</p>
      <h1 class="display" id="h-t">The art of <em>love</em>, practised.</h1>
      <p class="lede">I am Wietske: a health and lifestyle coach, a photographer, and a lifelong student of the human heart. I am not finished, which I have come to see as good news.</p>
    </section>

    <section class="sec" aria-labelledby="l-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">A life in motion</p>
      <h2 class="h2" id="l-t">Fifty-six countries, and still curious.</h2>
      <div class="prose">
        <p>I have travelled through more than 56 countries and photographed artists from all over the world. What I brought home is simple. People everywhere want the same few things: to be seen, to belong, and to live for something good.</p>
        <p>I am happiest outdoors and moving. I am a ski instructor, and I love the sports that demand your whole attention: kitesurfing, surfing and trail running. The sea and the mountain are excellent teachers of humility; they do not grade on effort. They taught me what I now teach: the body is a gift to be lived in, and courage is a habit.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Work and study</p>
      <h2 class="h2" id="w-t">Close to people, in their own homes.</h2>
      <div class="prose">
        <p>Over the years I have worked for more than 35 families, many of them high-profile. Inside a household you learn how a life really runs: its rhythms, its strains, and the quiet things that hold it together. You also learn discretion, which is love with its mouth closed.</p>
      </div>
      <dl class="terms">
        <dt>Coaching</dt><dd>Certified holistic health coach (Institute for Integrative Nutrition).</dd>
        <dt>Study</dt><dd>Bachelor&rsquo;s degree in Psychology, in progress.</dd>
        <dt>Photography</dt><dd>Weddings, families, portraits, and artists from around the world.</dd>
        <dt>Mountains</dt><dd>Ski instructor.</dd>
        <dt>Languages</dt><dd>English and Dutch.</dd>
        <dt>Volunteering</dt><dd>Effeta Amsterdam, Our Lady&rsquo;s Church, Look Up Amsterdam, and Family of Pure Grace.</dd>
        <dt>Built</dt><dd>Payag Experience, Siargao.</dd>
      </dl>
    </section>

    <section class="sec" aria-labelledby="f-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Charity</p>
      <h2 class="h2" id="f-t">Family of Pure Grace</h2>
      <div class="panel">
        <p class="lede">A home for orphaned children in Bugiri, Uganda.</p>
        <div class="prose">
          <p>Family of Pure Grace gives orphaned children care, shelter, food and schooling. I help raise funds to build a home for its 28 children, and profits from the Catholicity OS template go to the building fund.</p>
          <p>A slogan about charity ought to cost its author something. Donations go directly to Family of Pure Grace through their own page.</p>
        </div>
        <div class="row"><a class="btn" href="https://familyofpuregrace.wixsite.com/my-site/donate" rel="noopener">Donate to Family of Pure Grace</a><a href="https://familyofpuregrace.wixsite.com/my-site" rel="noopener">Meet the children</a></div>
      </div>
    </section>

    <section class="sec" aria-labelledby="b-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="b-t">What I believe</h2>
      <div class="prose">
        <p>Every person carries a dignity that is given, never earned. No success adds to it and no failure removes it. A good life is one life, where body, mind, heart, home and work serve the same end.</p>
        <p>Charity is the crown of that life. Everything made in this house is meant to help someone love a little better: a coaching hour, a photograph of the people you love, a tool that keeps your day in order. In the dark, God forms gold. I have found that to be true, and I work from there.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="v-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="v-t">Mission, vision and values</h2>
      <div class="panel">
        <p class="eyebrow">Mission</p>
        <p class="lede">L&rsquo;arte dell&rsquo;amore accompanies people in the examination of conscience and the formation of virtue, so that each person may order their whole life to love: Love*, neighbour, and the common good.</p>
        <p>I do this through personal coaching, photography that honours human relationships, digital tools for daily life, and works of art.</p>
        <p class="eyebrow">Vision</p>
        <p class="lede">A world in which every person is received as bearing an inviolable dignity, knows their gifts, and has the habits and the freedom to spend their life for the good of others. I hold that this is the foundation of lasting joy, and of peace.</p>
        <p class="small">* God.</p>
      </div>
      <dl class="terms">
        <dt>Human dignity</dt><dd>Every person has a worth that is given, not earned, and that no circumstance can remove.</dd>
        <dt>Charity</dt><dd>Love that acts for the good of another is the measure of everything I make. Charity is the crown of life.</dd>
        <dt>Truth</dt><dd>I begin with honest self-examination and I tell people the truth with gentleness.</dd>
        <dt>Integral development</dt><dd>I serve the whole person: body, mind, heart, home, work and spirit.</dd>
        <dt>Solidarity with the poor</dt><dd>My work is not complete unless it reaches those who have least.</dd>
        <dt>Humility</dt><dd>I am being perfected, not perfect. I serve one person at a time and begin again as often as needed.</dd>
        <dt>Beauty</dt><dd>What I make should be worthy of the people it serves, because beauty awakens the desire for the good.</dd>
      </dl>
    </section>

{contact("Write to me.")}"""


# ───────────────────────── Nederlands ─────────────────────────
ABONNEER = f"mailto:{EMAIL}?subject=Aanmelden%20voor%20De%20Brief"

NL_HOME = f"""    <section class="crest" aria-labelledby="h-t">
      <p class="eyebrow">Amsterdam &middot; coaching, fotografie, en dingen gemaakt met de hand en met code</p>
      <h1 class="display" id="h-t">De liefde is de <em>kroon</em> van het leven.</h1>
      <p class="lede">L&rsquo;arte dell&rsquo;amore is een klein huis met een grote hoop: dat je je leven als &eacute;&eacute;n geheel mag zien, en leert het aan liefde te besteden. Ik leer dat zelf ook nog, en daarom staat de deur open.</p>
    </section>

    <section class="sec" aria-labelledby="m-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Missie</p>
      <h2 class="h2" id="m-t">Het hele leven richten op de liefde.</h2>
      <p class="lede">L&rsquo;arte dell&rsquo;amore begeleidt mensen in het gewetensonderzoek en de vorming van deugd, zodat ieder mens zijn hele leven kan richten op de liefde: de Liefde*, de naaste en het algemeen welzijn.</p>
      <div class="prose">
        <p>Dat doe ik met persoonlijke coaching, fotografie die menselijke relaties eert, digitale hulpmiddelen voor het dagelijks leven en kunstwerken.</p>
      </div>
      <p class="eyebrow">Visie</p>
      <p class="lede">Een wereld waarin ieder mens wordt ontvangen als drager van een onschendbare waardigheid, zijn gaven kent, en de gewoonten en de vrijheid heeft om zijn leven te besteden aan het welzijn van anderen. Ik geloof dat dit het fundament is van blijvende vreugde, en van vrede.</p>
      <p class="small">* God. &nbsp;&middot;&nbsp; <a href="about.html#v-t">Lees mijn zeven waarden</a></p>
    </section>

    <section class="sec" aria-labelledby="i-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Het huis</p>
      <h2 class="h2" id="i-t">Zeven kamers, &eacute;&eacute;n deur.</h2>
      <ol class="index">
        <li><span class="n">i</span><a class="t" href="{APP}" rel="noopener">Illuminated Life</a><span class="state open">Open</span><span class="d">Een leefregel over twaalf velden van rentmeesterschap. Geen reeksen, geen punten; de heiligen redden het ook zonder ranglijst. (De app is in het Engels.)</span></li>
        <li><span class="n">ii</span><a class="t" href="coaching.html">Gezondheids- en leefstijlcoaching</a><span class="state open">Open</span><span class="d">E&eacute;n op &eacute;&eacute;n, online of in Amsterdam. Vanaf &euro;95 per sessie.</span></li>
        <li><span class="n">iii</span><a class="t" href="photography.html">Fotografie</a><span class="state open">Open</span><span class="d">Bruiloften, verlovingen, gezinnen en portretten. Vanaf &euro;195.</span></li>
        <li><span class="n">iv</span><a class="t" href="letter.html">De Brief</a><span class="state open">Gratis</span><span class="d">Eens per week: iets voor het lichaam, iets voor de geest, een verhaal voor de ziel.</span></li>
        <li><span class="n">v</span><a class="t" href="atelier.html#digital">Digitale producten</a><span class="state">In de maak</span><span class="d">Catholicity OS voor Notion, en Catholic Healing Arts.</span></li>
        <li><span class="n">vi</span><a class="t" href="atelier.html#prints">Kunstprints en geschenken</a><span class="state">In de maak</span><span class="d">Gouden fijne lijn op natuurlijk papier; ethisch en duurzaam geproduceerde kleding.</span></li>
        <li><span class="n">vii</span><a class="t" href="atelier.html#apps">Apps</a><span class="state">In de maak</span><span class="d">Global Holy Rosary, Beatitude, Eternal Camino.</span></li>
      </ol>
    </section>

{contact("Begin met een gesprek.", "nl")}"""

NL_COACHING = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Gezondheids- en leefstijlcoaching</p>
      <h1 class="display" id="h-t">Je hele leven, <em>op orde</em>.</h1>
      <p class="lede">De meeste mensen hebben niet meer informatie nodig over slaap, eten of bewegen. Ze hebben iemand nodig die geduldig en eerlijk is en aan hun kant staat, terwijl zij &eacute;&eacute;n ding veranderen. Dat is het hele werk, en het is mooi werk.</p>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="w-t">Hoe ik werk</h2>
      <ol class="steps">
        <li><b>Een eerste gesprek</b><span>Jij vertelt waar je staat en waar je op hoopt. Ik zeg eerlijk of ik kan helpen, en zo niet, wie misschien wel.</span></li>
        <li><b>Het hele plaatje</b><span>Ik kijk met je mee naar je leven zoals het werkelijk is: slaap, eten, beweging, werk, de mensen van wie je houdt, rust, en gebed als dat bij je leven hoort. Zonder oordeel. Ik heb het mijne ook gezien.</span></li>
        <li><b>E&eacute;n veld tegelijk</b><span>Ik help je de ene verandering te kiezen die de andere meetrekt, en maak haar klein genoeg om je slechtste week te overleven. Je krijgt van mij geen ochtendroutine van veertig stappen. Zo&rsquo;n ochtend heeft niemand.</span></li>
        <li><b>Gewoonten die blijven</b><span>Ik spreek je regelmatig, stel bij wat niet werkte, en bouw met je door tot de gewoonte mij niet meer nodig heeft. Overbodig worden is het doel.</span></li>
      </ol>
    </section>

    <section class="sec" aria-labelledby="f-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="f-t">Tarieven</h2>
      <dl class="terms">
        <dt>Eerste gesprek</dt><dd>20 minuten, gratis. Jij en ik ontdekken of het past.</dd>
        <dt>Losse sessie</dt><dd><b>&euro;95</b> &middot; 60 minuten, online of in Amsterdam.</dd>
        <dt>Een seizoen samen</dt><dd><b>&euro;540</b> &middot; drie maanden, zes sessies, met korte berichten tussendoor. Hier gebeurt de echte verandering meestal.</dd>
      </dl>
      <p class="small">Is het tarief het enige wat tussen jou en hulp in staat? Schrijf me toch. Ik zoek met je naar een weg.</p>
    </section>

    <section class="sec" aria-labelledby="p-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="p-t">Praktisch</h2>
      <dl class="terms">
        <dt>Waar</dt><dd>Online, of persoonlijk in Amsterdam.</dd>
        <dt>Talen</dt><dd>Nederlands en Engels.</dd>
        <dt>Coach</dt><dd>Wietske, gecertificeerd holistisch gezondheidscoach (Institute for Integrative Nutrition), bezig met een bachelor Psychologie.</dd>
      </dl>
      <p class="small">Coaching ondersteunt een gezonde leefstijl. Het stelt geen diagnoses, behandelt geen ziekten en vervangt je arts of therapeut niet.</p>
    </section>

{contact("Vertel me waar je staat.", "nl")}"""

NL_PHOTO = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Fotografie</p>
      <h1 class="display" id="h-t">Schoonheid vastleggen door de <em>kunst</em> van het fotograferen.</h1>
      <p class="lede">Een foto is een kleine daad van eerbied: ze zegt dat deze mens, deze dag, het bewaren waard was. Ik werk zonder haast, in natuurlijk licht, en ik heb nog nooit iemand gevraagd om &lsquo;cheese&rsquo; te zeggen.</p>
    </section>

    <section class="sec" aria-labelledby="g-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="g-t">Portfolio</h2>
      <div class="mounts">
        <div class="mount wide"><span>Bruiloft</span></div>
        <div class="mount"><span>Verloving</span></div>
        <div class="mount"><span>Gezin</span></div>
        <div class="mount"><span>Portret</span></div>
        <div class="mount"><span>Zakelijk portret</span></div>
      </div>
    </section>

    <section class="sec" aria-labelledby="s-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="s-t">Wat ik fotografeer, en wat het kost</h2>
      <dl class="terms">
        <dt>Bruiloften</dt><dd><b>&euro;1.950</b> &middot; De hele dag, van de stilte vooraf tot de laatste dans. Je ontvangt de volledige bewerkte galerij.</dd>
        <dt>Verlovingen</dt><dd><b>&euro;295</b> &middot; Een uur of twee op een plek die voor jullie telt. Ook een zachte generale repetitie voor de bruiloft.</dd>
        <dt>Gezinnen</dt><dd><b>&euro;325</b> &middot; Thuis of buiten, ook newborn en zwangerschap. Kinderen mogen precies zijn zoals ze zijn.</dd>
        <dt>Portretten</dt><dd><b>&euro;195</b> &middot; Een persoonlijk portret waarop je eruitziet zoals op een goede dag, en dat is de waarheid.</dd>
        <dt>Zakelijke portretten</dt><dd><b>&euro;245</b> &middot; Authentieke, professionele portretten voor je werk.</dd>
      </dl>
      <p class="small">Prijzen in euro&rsquo;s. Reizen binnen Amsterdam is inbegrepen; verder weg spreek ik dat vooraf met je af.</p>
    </section>

{contact("Vertel me over jullie dag.", "nl")}"""

NL_ATELIER = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Atelier</p>
      <h1 class="display" id="h-t">Langzaam gemaakt, <em>om te houden</em>.</h1>
      <p class="lede">Hulpmiddelen, prints en geschenken uit hetzelfde huis. E&eacute;n is vandaag open. De rest is in de maak, en dat zeg ik liever dan dat ik doe alsof.</p>
    </section>

    <section class="sec" aria-labelledby="il-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Open &middot; gratis</p>
      <h2 class="h2" id="il-t">Illuminated Life</h2>
      <div class="prose">
        <p>E&eacute;n Meester vertrouwt &eacute;&eacute;n rentmeester twaalf velden toe, in drie ringen: Persoon, Huishouden en Wereld. De app bewaart je leefregel, je dagboek en het kerkelijk jaar. Ze geeft je nooit een score, vergeeft een gemiste dag meteen, en alles blijft op je eigen toestel.</p>
        <p>Erbij hoort het boek <i>Illuminated: The Image of God, Embodied</i>. App en boek zijn in het Engels.</p>
      </div>
      <div class="row"><a class="btn" href="{APP}" rel="noopener">Open Illuminated Life</a></div>
    </section>

    <section class="sec" id="digital" aria-labelledby="d-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In de maak</p>
      <h2 class="h2" id="d-t">Digitale producten</h2>
      <dl class="terms">
        <dt>Catholicity OS</dt><dd>Een Notion-werkruimte voor het geheel van een katholiek leven, gebouwd op dezelfde drie ringen. De winst gaat naar het bouwfonds van Family of Pure Grace.</dd>
        <dt>Catholic Healing Arts</dt><dd>Meer volgt.</dd>
      </dl>
    </section>

    <section class="sec" id="apps" aria-labelledby="a-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In de maak</p>
      <h2 class="h2" id="a-t">Apps</h2>
      <dl class="terms">
        <dt>Global Holy Rosary</dt><dd>Bid de Rozenkrans voor elk land in zijn eigen taal en zie de wereldkaart goud kleuren.</dd>
        <dt>Beatitude</dt><dd>Een katholieke sociale app die liefde beloont in plaats van populariteit. Een ongebruikelijk verdienmodel, dat geef ik toe.</dd>
        <dt>Eternal Camino</dt><dd>Een reisgezel met een pagina voor elk land.</dd>
      </dl>
    </section>

    <section class="sec" id="prints" aria-labelledby="pr-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In de maak</p>
      <h2 class="h2" id="pr-t">Kunstprints</h2>
      <p class="prose">Tekeningen in gouden fijne lijn op natuurlijk papier.</p>
    </section>

    <section class="sec" id="gifts" aria-labelledby="gf-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">In de maak</p>
      <h2 class="h2" id="gf-t">Geschenken</h2>
      <p class="prose">Ethisch en duurzaam geproduceerde kleding.</p>
    </section>

{contact("Vraag me een seintje als er iets opengaat.", "nl")}"""

NL_LETTER = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">De Brief &middot; wekelijks &middot; gratis</p>
      <h1 class="display" id="h-t">E&eacute;n brief per week, voor <em>heel</em> de mens.</h1>
      <p class="lede">Kort genoeg voor &eacute;&eacute;n kop koffie. Drie delen, elke week, voor lichaam, geest en ziel. De Brief is voorlopig in het Engels.</p>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="w-t">Wat er aankomt</h2>
      <ol class="steps">
        <li><b>Het lichaam</b><span>E&eacute;n praktijk uit de wereld van het biohacken, eerlijk bekeken: wat het bewijs ondersteunt, wat hype is, en wat je grootmoeder allang wist.</span></li>
        <li><b>De geest</b><span>Een korte overweging uit de katholieke theologie van gezondheid en bloei. Het lichaam als gave, rust als gehoorzaamheid, en waarom heiligheid en welzijn vrienden zijn.</span></li>
        <li><b>Het verhaal</b><span>E&eacute;n Bijbelverhaal gelezen met de blik van een psycholoog, uit de boeken die ik schrijf. De Schrift leest ons al heel lang.</span></li>
      </ol>
    </section>

    <section class="sec" aria-labelledby="s-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="s-t">Aanmelden</h2>
      <div class="panel">
        <p class="lede">Stuur &eacute;&eacute;n e-mail met het woord <i>Aanmelden</i>, en je bent erbij.</p>
        <p class="addr">{EMAIL}</p>
        <div class="row"><a class="btn" href="{ABONNEER}">Aanmelden per e-mail</a></div>
        <p class="small">Ik bewaar je e-mailadres en verder niets, en gebruik het alleen voor deze brief. Stoppen? Antwoord <i>stop</i> op een willekeurige brief. Geen trucs, geen verkoop van lijsten.</p>
      </div>
      <p class="small">De Brief deelt idee&euml;n voor gezond leven en is geen medisch advies. Overleg met je arts voordat je iets verandert aan behandeling, vasten of supplementen.</p>
    </section>

{contact("Of zeg gewoon gedag.", "nl")}"""

NL_ABOUT = f"""    <section class="sec" aria-labelledby="h-t">
      <p class="eyebrow">Over mij</p>
      <h1 class="display" id="h-t">De kunst van de <em>liefde</em>, beoefend.</h1>
      <p class="lede">Ik ben Wietske: gezondheids- en leefstijlcoach, fotograaf, en levenslang leerling van het menselijk hart. Ik ben niet af, en dat ben ik als goed nieuws gaan zien.</p>
    </section>

    <section class="sec" aria-labelledby="l-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Een leven in beweging</p>
      <h2 class="h2" id="l-t">Zesenvijftig landen, en nog steeds nieuwsgierig.</h2>
      <div class="prose">
        <p>Ik heb door meer dan 56 landen gereisd en kunstenaars uit de hele wereld gefotografeerd. Wat ik mee naar huis nam is eenvoudig. Mensen willen overal dezelfde paar dingen: gezien worden, ergens bij horen, en leven voor iets goeds.</p>
        <p>Ik ben het gelukkigst buiten en in beweging. Ik ben skilerares, en ik houd van de sporten die je hele aandacht vragen: kitesurfen, surfen en trailrunnen. De zee en de berg zijn uitstekende leermeesters in nederigheid; ze geven geen punten voor inzet. Ze leerden mij wat ik nu doorgeef: het lichaam is een gave om in te wonen, en moed is een gewoonte.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="w-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Werk en studie</p>
      <h2 class="h2" id="w-t">Dicht bij mensen, in hun eigen huis.</h2>
      <div class="prose">
        <p>Door de jaren heen heb ik voor meer dan 35 gezinnen gewerkt, waarvan veel in de schijnwerpers staan. Binnen een huishouden leer je hoe een leven werkelijk loopt: zijn ritmes, zijn spanningen, en de stille dingen die het bijeenhouden. Je leert er ook discretie, en dat is liefde met de mond dicht.</p>
      </div>
      <dl class="terms">
        <dt>Coaching</dt><dd>Gecertificeerd holistisch gezondheidscoach (Institute for Integrative Nutrition).</dd>
        <dt>Studie</dt><dd>Bachelor Psychologie, in opleiding.</dd>
        <dt>Fotografie</dt><dd>Bruiloften, gezinnen, portretten, en kunstenaars uit de hele wereld.</dd>
        <dt>Bergen</dt><dd>Skilerares.</dd>
        <dt>Talen</dt><dd>Nederlands en Engels.</dd>
        <dt>Vrijwilligerswerk</dt><dd>Effeta Amsterdam, de Onze Lieve Vrouwekerk, Look Up Amsterdam en Family of Pure Grace.</dd>
        <dt>Gebouwd</dt><dd>Payag Experience, Siargao.</dd>
      </dl>
    </section>

    <section class="sec" aria-labelledby="f-t">
      <span class="rule" aria-hidden="true"></span>
      <p class="eyebrow">Naastenliefde</p>
      <h2 class="h2" id="f-t">Family of Pure Grace</h2>
      <div class="panel">
        <p class="lede">Een thuis voor weeskinderen in Bugiri, Oeganda.</p>
        <div class="prose">
          <p>Family of Pure Grace geeft weeskinderen zorg, onderdak, eten en onderwijs. Ik help geld in te zamelen om een huis te bouwen voor de 28 kinderen, en de winst van de Catholicity OS-template gaat naar het bouwfonds.</p>
          <p>Een leus over liefde hoort haar schrijver iets te kosten. Giften gaan rechtstreeks naar Family of Pure Grace, via hun eigen pagina.</p>
        </div>
        <div class="row"><a class="btn" href="{DONATE}" rel="noopener">Doneer aan Family of Pure Grace</a><a href="{FOPG}" rel="noopener">Ontmoet de kinderen</a></div>
      </div>
    </section>

    <section class="sec" aria-labelledby="b-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="b-t">Wat ik geloof</h2>
      <div class="prose">
        <p>Ieder mens draagt een waardigheid die gegeven is, nooit verdiend. Geen succes voegt eraan toe en geen mislukking neemt haar weg. Een goed leven is &eacute;&eacute;n leven, waarin lichaam, geest, hart, huis en werk hetzelfde doel dienen.</p>
        <p>De liefde is de kroon van dat leven. Alles wat in dit huis gemaakt wordt, wil iemand helpen een beetje beter lief te hebben: een uur coaching, een foto van de mensen van wie je houdt, een hulpmiddel dat je dag op orde houdt. In het donker vormt God goud. Ik heb gemerkt dat het waar is, en van daaruit werk ik.</p>
      </div>
    </section>

    <section class="sec" aria-labelledby="v-t">
      <span class="rule" aria-hidden="true"></span>
      <h2 class="h2" id="v-t">Missie, visie en waarden</h2>
      <div class="panel">
        <p class="eyebrow">Missie</p>
        <p class="lede">L&rsquo;arte dell&rsquo;amore begeleidt mensen in het gewetensonderzoek en de vorming van deugd, zodat ieder mens zijn hele leven kan richten op de liefde: de Liefde*, de naaste en het algemeen welzijn.</p>
        <p>Dat doe ik met persoonlijke coaching, fotografie die menselijke relaties eert, digitale hulpmiddelen voor het dagelijks leven en kunstwerken.</p>
        <p class="eyebrow">Visie</p>
        <p class="lede">Een wereld waarin ieder mens wordt ontvangen als drager van een onschendbare waardigheid, zijn gaven kent, en de gewoonten en de vrijheid heeft om zijn leven te besteden aan het welzijn van anderen. Ik geloof dat dit het fundament is van blijvende vreugde, en van vrede.</p>
        <p class="small">* God.</p>
      </div>
      <dl class="terms">
        <dt>Menselijke waardigheid</dt><dd>Ieder mens heeft een waarde die gegeven is, niet verdiend, en die geen omstandigheid kan wegnemen.</dd>
        <dt>Liefde</dt><dd>Liefde die handelt voor het goede van de ander is de maat van alles wat ik maak. De liefde is de kroon van het leven.</dd>
        <dt>Waarheid</dt><dd>Ik begin met eerlijk zelfonderzoek en zeg mensen de waarheid met zachtheid.</dd>
        <dt>Integrale ontwikkeling</dt><dd>Ik dien de hele mens: lichaam, geest, hart, huis, werk en ziel.</dd>
        <dt>Solidariteit met de armen</dt><dd>Mijn werk is niet af zolang het de mensen die het minst hebben niet bereikt.</dd>
        <dt>Nederigheid</dt><dd>Ik word volmaakt, ik ben het niet. Ik dien &eacute;&eacute;n mens tegelijk en begin opnieuw zo vaak als nodig is.</dd>
        <dt>Schoonheid</dt><dd>Wat ik maak moet de mensen die het dient waardig zijn, want schoonheid wekt het verlangen naar het goede.</dd>
      </dl>
    </section>

{contact("Schrijf mij.", "nl")}"""

PAGES = [
    ("index.html", "L'arte dell'amore", "Coaching, photography and tools for a life ordered to love. Amsterdam.", "L&rsquo;arte dell&rsquo;amore &nbsp;&middot;&nbsp; <b>Amsterdam</b>", HOME, "en"),
    ("coaching.html", "Coaching · L'arte dell'amore", "One-to-one holistic health and lifestyle coaching, online or in Amsterdam. From 95 euros a session.", "Coaching &nbsp;&middot;&nbsp; <b>one to one</b>", COACHING, "en"),
    ("photography.html", "Photography · L'arte dell'amore", "Wedding, engagement, family and portrait photography from Amsterdam.", "Photography &nbsp;&middot;&nbsp; <b>natural light</b>", PHOTO, "en"),
    ("atelier.html", "Atelier · L'arte dell'amore", "Illuminated Life, digital products, apps, art prints and gifts.", "Atelier &nbsp;&middot;&nbsp; <b>made slowly</b>", ATELIER, "en"),
    ("letter.html", "The Letter · L'arte dell'amore", "A free weekly letter for body, mind and soul.", "The Letter &nbsp;&middot;&nbsp; <b>weekly</b>", LETTER, "en"),
    ("about.html", "About · L'arte dell'amore", "Wietske, holistic health coach and photographer in Amsterdam.", "About &nbsp;&middot;&nbsp; <b>Wietske</b>", ABOUT, "en"),
    ("index.html", "L'arte dell'amore", "Coaching, fotografie en hulpmiddelen voor een leven gericht op liefde. Amsterdam.", "L&rsquo;arte dell&rsquo;amore &nbsp;&middot;&nbsp; <b>Amsterdam</b>", NL_HOME, "nl"),
    ("coaching.html", "Coaching · L'arte dell'amore", "Holistische gezondheids- en leefstijlcoaching, één op één, online of in Amsterdam. Vanaf 95 euro per sessie.", "Coaching &nbsp;&middot;&nbsp; <b>&eacute;&eacute;n op &eacute;&eacute;n</b>", NL_COACHING, "nl"),
    ("photography.html", "Fotografie · L'arte dell'amore", "Bruidsfotografie, verlovings-, gezins- en portretfotografie vanuit Amsterdam.", "Fotografie &nbsp;&middot;&nbsp; <b>natuurlijk licht</b>", NL_PHOTO, "nl"),
    ("atelier.html", "Atelier · L'arte dell'amore", "Illuminated Life, digitale producten, apps, kunstprints en geschenken.", "Atelier &nbsp;&middot;&nbsp; <b>langzaam gemaakt</b>", NL_ATELIER, "nl"),
    ("letter.html", "De Brief · L'arte dell'amore", "Een gratis wekelijkse brief voor lichaam, geest en ziel.", "De Brief &nbsp;&middot;&nbsp; <b>wekelijks</b>", NL_LETTER, "nl"),
    ("about.html", "Over mij · L'arte dell'amore", "Wietske, holistisch gezondheidscoach en fotograaf in Amsterdam.", "Over mij &nbsp;&middot;&nbsp; <b>Wietske</b>", NL_ABOUT, "nl"),
]

(ROOT / "nl").mkdir(exist_ok=True)
for slug, title, desc, rail, body, lang in PAGES:
    out = ROOT / slug if lang == "en" else ROOT / "nl" / slug
    out.write_text(page(slug, title, desc, rail, body, lang), encoding="utf-8")

# A body-only copy of the home page with the stylesheet inlined, for previewing outside GitHub.
css = (ROOT / "css/site.css").read_text(encoding="utf-8").replace('url("../assets/', 'url("assets/')
home = (ROOT / "index.html").read_text(encoding="utf-8")
inner = re.search(r"<body>(.*)</body>", home, re.S).group(1)
(ROOT / "tools/preview.html").write_text(f"<title>L'arte dell'amore</title>\n<style>\n{css}\n</style>\n{inner}", encoding="utf-8")
print("built", len(PAGES), "pages")
