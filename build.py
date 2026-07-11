#!/usr/bin/env python3
"""Static site generator for booboosketch.com — minimal, designer-register."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).parent
os.chdir(ROOT)

data = json.load(open("data.json"))
projects = data["projects"]
site = data["site"]

# Ensure projects/ dir exists
(ROOT / "projects").mkdir(exist_ok=True)


# CSS
CSS = r""":root {
  --ink: #0a0a0a;
  --bg: #ffffff;
  --muted: #6e6e6e;
  --rule: #ececec;
  --max: 1400px;
  --gutter: clamp(18px, 4vw, 56px);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.5;
  color: var(--ink);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

a { color: var(--ink); text-decoration: none; }
a:hover { opacity: 0.6; }

.wrap { max-width: var(--max); margin: 0 auto; padding: 0 var(--gutter); }

/* Header */
.site-head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding: 32px var(--gutter);
  border-bottom: 1px solid var(--rule);
  position: sticky;
  top: 0;
  background: var(--bg);
  z-index: 10;
}
.site-head .brand {
  font-weight: 500;
  font-size: 13px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  font-feature-settings: 'ss01';
  display: inline-flex;
  align-items: center;
  gap: 12px;
}
.site-head .brand .mark {
  height: 42px;
  width: auto;
  display: inline-block;
  opacity: 0.95;
}

/* Mascot accent — section divider charm */
.mascot-divider {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 64px 0 32px;
  border-top: 1px solid var(--rule);
}
.mascot-divider img {
  height: 88px;
  width: auto;
  opacity: 0.9;
}

/* About page mascot signature */
.mascot-signature {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  margin-top: 64px;
  padding-top: 32px;
  border-top: 1px solid var(--rule);
}
.mascot-signature img {
  height: 220px;
  width: auto;
  opacity: 0.95;
}
@media (max-width: 720px) {
  .mascot-signature img { height: 160px; }
  .site-head .brand .mark { height: 26px; }
}
.site-head nav {
  display: flex;
  gap: 32px;
  font-size: 13px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.site-head nav a { font-weight: 400; }

/* Hero image (homepage banner) */
.hero-image {
  position: relative;
  width: 100%;
  margin: 0;
  padding: 0;
  border-bottom: 1px solid var(--rule);
  overflow: hidden;
}
.hero-image img {
  display: block;
  width: 100%;
  height: clamp(520px, 82vh, 920px);
  object-fit: cover;
}
.hero-image .hero-overlay {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: clamp(36px, 6vw, 72px);
  padding-top: clamp(80px, 14vw, 180px);
  background: linear-gradient(to top, rgba(0,0,0,0.78) 0%, rgba(0,0,0,0.55) 35%, rgba(0,0,0,0.15) 75%, rgba(0,0,0,0) 100%);
  color: #fff;
}
.hero-image .hero-overlay h1,
.hero-image .hero-overlay p {
  text-shadow: 0 1px 24px rgba(0,0,0,0.45);
}
.hero-image .hero-overlay h1 {
  font-size: clamp(28px, 4.2vw, 54px);
  line-height: 1.1;
  font-weight: 500;
  letter-spacing: -0.01em;
  max-width: 22ch;
  margin: 0;
  color: #fff;
}
.hero-image .hero-overlay p {
  margin: 14px 0 0;
  max-width: 60ch;
  font-size: clamp(14px, 1.1vw, 16px);
  color: rgba(255,255,255,0.92);
  line-height: 1.5;
}

/* Hero (text fallback when no hero image) */
.hero {
  padding: clamp(120px, 18vw, 240px) var(--gutter);
  max-width: 1100px;
  margin: 0 auto;
}
.hero h1 {
  font-weight: 500;
  font-size: clamp(28px, 5.5vw, 72px);
  line-height: 1.05;
  letter-spacing: -0.025em;
  word-wrap: break-word;
  overflow-wrap: break-word;
  hyphens: auto;
}
.hero .sub {
  margin-top: 32px;
  font-size: 15px;
  color: var(--muted);
  max-width: 540px;
  line-height: 1.6;
}

/* Section labels */
.section-label {
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 24px;
}

/* Work label (above grid) */
.work-label {
  max-width: var(--max);
  margin: 0 auto;
  padding: 64px var(--gutter) 0;
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 12px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}
.work-label .label-text {
  color: var(--ink);
  font-weight: 500;
}

/* Work grid */
.work-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 80px;
  padding: 40px var(--gutter) 160px;
  max-width: var(--max);
  margin: 0 auto;
}
@media (min-width: 800px) {
  .work-grid {
    grid-template-columns: 1fr 1fr;
    gap: 100px 60px;
  }
}
@media (min-width: 1180px) {
  .work-grid {
    grid-template-columns: 1fr 1fr 1fr;
    gap: 80px 56px;
  }
}
.project-card {
  display: block;
  cursor: pointer;
}
.project-card .thumb {
  display: block;
  width: 100%;
  aspect-ratio: 4 / 3;
  background: #f5f5f5;
  overflow: hidden;
  margin-bottom: 18px;
}
.project-card .thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}
.project-card:hover .thumb img {
  transform: scale(1.02);
}
.project-card .name {
  font-size: 16px;
  font-weight: 500;
  letter-spacing: -0.01em;
}

/* Project page */
.project-head {
  padding: clamp(80px, 12vw, 160px) var(--gutter) 60px;
  max-width: 1100px;
  margin: 0 auto;
}
.project-head h1 {
  font-weight: 500;
  font-size: clamp(28px, 4.5vw, 56px);
  letter-spacing: -0.02em;
  line-height: 1.05;
}
.project-head .crumb {
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 18px;
}
.gallery {
  display: grid;
  grid-template-columns: 1fr;
  gap: 40px;
  padding: 40px var(--gutter) 120px;
  max-width: var(--max);
  margin: 0 auto;
}
.gallery img {
  display: block;
  width: 100%;
  height: auto;
  background: #f5f5f5;
}
.project-nav {
  display: flex;
  justify-content: space-between;
  padding: 60px var(--gutter) 120px;
  max-width: var(--max);
  margin: 0 auto;
  font-size: 13px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  border-top: 1px solid var(--rule);
}

/* About / Contact */
.copy {
  max-width: 720px;
  margin: 0 auto;
  padding: clamp(120px, 18vw, 200px) var(--gutter) 160px;
}
.copy h1 {
  font-weight: 500;
  font-size: clamp(28px, 4vw, 48px);
  letter-spacing: -0.02em;
  margin-bottom: 32px;
  line-height: 1.1;
}
.copy p {
  font-size: 17px;
  line-height: 1.6;
  margin-bottom: 1.2em;
  color: #1a1a1a;
}
.copy a {
  border-bottom: 1px solid var(--ink);
  padding-bottom: 1px;
}

/* Footer */
.site-foot {
  padding: 60px var(--gutter);
  border-top: 1px solid var(--rule);
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}
@media (max-width: 600px) {
  .site-foot { flex-direction: column; gap: 12px; align-items: flex-start; }
  .site-head { padding: 20px var(--gutter); flex-wrap: wrap; gap: 16px; }
  .site-head nav { gap: 20px; }
}
"""

(ROOT / "style.css").write_text(CSS)


def head(title, root=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Booboosketch Fine Art</title>
<meta name="description" content="{site['tagline']}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<header class="site-head">
  <a href="{root}index.html" class="brand"><img src="{root}images/_brand/logo-200.png" alt="" class="mark"><span>Booboosketch</span></a>
  <nav>
    <a href="{root}work.html">Work</a>
    <a href="{root}about.html">About</a>
    <a href="{root}contact.html">Contact</a>
  </nav>
</header>"""


FOOT = f"""<section class="mascot-divider">
  <img src="images/_brand/logo-200.png" alt="">
</section>
<footer class="site-foot">
  <span>© Booboosketch Fine Art</span>
  <a href="mailto:{site['email']}">{site['email']}</a>
</footer>
</body></html>"""

FOOT_PROJECT = f"""<section class="mascot-divider">
  <img src="../images/_brand/logo-200.png" alt="">
</section>
<footer class="site-foot">
  <span>© Booboosketch Fine Art</span>
  <a href="mailto:{site['email']}">{site['email']}</a>
</footer>
</body></html>"""


def get_images(slug):
    """Return sorted list of image and video filenames for a project slug."""
    folder = ROOT / "images" / slug
    if not folder.exists():
        return []
    files = []
    for ext in ('*.jpg', '*.jpeg', '*.png', '*.MOV', '*.mov', '*.mp4', '*.avi', '*.webm'):
        files.extend([p.name for p in folder.glob(ext)])
    return sorted(files)


def cover(slug, project=None):
    """Return cover image path. If project has explicit 'cover' field, use it."""
    if project and project.get("cover"):
        return f"images/{slug}/{project['cover']}"
    imgs = get_images(slug)
    return f"images/{slug}/{imgs[0]}" if imgs else None


# === index.html (Home) ===
hero_img = site.get("hero")
parts = [head("Booboosketch Fine Art")]
if hero_img:
    parts.append(f"""
<section class="hero-image">
  <img src="{hero_img}" alt="" loading="eager">
  <div class="hero-overlay">
    <h1>Site-specific visual systems for architectural-scale environments.</h1>
    <p>The practice of Ben Heller — hard-edge, restraint-first work designed to read at scale and integrate with the architecture.</p>
  </div>
</section>
""")
else:
    parts.append(f"""
<section class="hero">
  <h1>Site-specific visual systems for architectural-scale environments.</h1>
  <p class="sub">The practice of Ben Heller. Hard-edge, restraint-first work designed to read at scale and integrate with the architecture, not sit on top of it.</p>
</section>
""")
parts.append(f"""
<section style="border-top:1px solid var(--rule)">
<div class="work-label">
  <span class="label-text">Selected Work</span>
  <span class="label-count">{len(projects)} Projects</span>
</div>
<div class="work-grid">
""")
for p in projects:
    c = cover(p["slug"], p)
    if c:
        parts.append(f"""  <a class="project-card" href="projects/{p['slug']}.html">
    <div class="thumb"><img src="{c}" alt="{p['name']}" loading="lazy"></div>
    <div class="name">{p['name']}</div>
  </a>
""")
parts.append("</div></section>")
parts.append(FOOT)
(ROOT / "index.html").write_text("".join(parts))


# === work.html ===
parts = [head("Work")]
parts.append("""
<section style="padding:clamp(80px,12vw,140px) var(--gutter) 0;max-width:var(--max);margin:0 auto">
  <div class="section-label">Selected Work</div>
  <h1 style="font-weight:500;font-size:clamp(28px,4.5vw,56px);letter-spacing:-0.02em;line-height:1.05">Selected projects across civic, commercial, transit, and educational environments.</h1>
</section>
<div class="work-grid">
""")
for p in projects:
    c = cover(p["slug"], p)
    if c:
        parts.append(f"""  <a class="project-card" href="projects/{p['slug']}.html">
    <div class="thumb"><img src="{c}" alt="{p['name']}" loading="lazy"></div>
    <div class="name">{p['name']}</div>
  </a>
""")
parts.append("</div>")
parts.append(FOOT)
(ROOT / "work.html").write_text("".join(parts))


# === project pages ===
n = len(projects)
for i, p in enumerate(projects):
    slug = p["slug"]
    name = p["name"]
    prev_p = projects[(i - 1) % n]
    next_p = projects[(i + 1) % n]
    imgs = get_images(slug)

    parts = [head(name, "../")]
    parts.append(f"""
<section class="project-head">
  <div class="crumb">Project</div>
  <h1>{name}</h1>
</section>
<div class="gallery">
""")
    # if cover is specified, hoist it to the top so it's the first/main image
    cover_img = p.get("cover")
    ordered = imgs[:]
    if cover_img and cover_img in ordered:
        ordered.remove(cover_img)
        ordered.insert(0, cover_img)
    for img in ordered:
        ext = img.lower().split('.')[-1]
        if ext in ('mov', 'mp4', 'avi', 'webm'):
            parts.append(f'  <video src="../images/{slug}/{img}" controls preload="metadata" style="width:100%;height:auto"></video>\n')
        else:
            parts.append(f'  <img src="../images/{slug}/{img}" alt="{name}" loading="lazy">\n')
    parts.append(f"""</div>
<nav class="project-nav">
  <a href="{prev_p['slug']}.html">← {prev_p['name']}</a>
  <a href="../work.html">All Work</a>
  <a href="{next_p['slug']}.html">{next_p['name']} →</a>
</nav>
""")
    parts.append(FOOT_PROJECT)
    (ROOT / "projects" / f"{slug}.html").write_text("".join(parts))


# === about.html ===
parts = [head("About")]
parts.append("""
<section class="copy">
  <h1>Booboosketch is the practice of Ben Heller.</h1>
  <p>Site-specific visual systems for architectural-scale environments. The work is hard-edge, restraint-first, and designed to read at scale — closer in register to architectural collaboration than traditional muralism.</p>
  <p>Recent and ongoing projects span civic, commercial, transit, and educational environments — including Brightline, 5th Third Bank, FAU Research Park, and Bridge Prep Academy.</p>
  <p>For project inquiries, <a href="contact.html">get in touch</a>.</p>
  <div class="mascot-signature"><img src="images/_brand/logo-400.png" alt=""></div>
</section>
""")
parts.append(FOOT)
(ROOT / "about.html").write_text("".join(parts))


# === contact.html ===
parts = [head("Contact")]
parts.append(f"""
<section class="copy">
  <h1>Inquiries.</h1>
  <p>For project inquiries, partnerships, or studio access:</p>
  <p style="font-size:22px;margin-top:32px"><a href="mailto:{site['email']}">{site['email']}</a></p>
</section>
""")
parts.append(FOOT)
(ROOT / "contact.html").write_text("".join(parts))


print("Build complete.")
print(f"Pages: {len(list(ROOT.glob('*.html')))} top-level + {len(list((ROOT / 'projects').glob('*.html')))} project")
