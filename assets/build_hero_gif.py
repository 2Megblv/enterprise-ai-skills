"""Build the README hero GIF for enterprise-ai-skills.

The GIF tells a 30-second story: take a relatable personal question
("Which sport should I pick up?"), run it through the toolkit, end with
a deck and a chart.

Each "scene" is a static PNG rendered with Pillow, then assembled into
an animated GIF with a per-scene duration.

Usage:
    python3 build_hero_gif.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------------
# Canvas + palette (matches mckinsey-charts conventions)
# ----------------------------------------------------------------------
W, H = 1280, 720
WHITE = (255, 255, 255)
NAVY = (5, 28, 44)
HIGHLIGHT = (0, 110, 182)
DARK_GREY = (85, 85, 85)
GREY = (191, 191, 191)
LIGHT_GREY = (217, 217, 217)
SOURCE_GREY = (128, 128, 128)


def _font(size, bold=False):
    """Try Inter, then SF, then Helvetica, then default."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Inter-Regular.ttf" if not bold else "/System/Library/Fonts/Supplemental/Inter-Bold.ttf",
        "/Library/Fonts/Inter-Regular.ttf" if not bold else "/Library/Fonts/Inter-Bold.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def _new_canvas():
    return Image.new("RGB", (W, H), WHITE)


def _wrap(draw, text, font, max_width):
    """Greedy word-wrap to fit max_width pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _draw_text(draw, x, y, text, font, color, max_width=None, line_spacing=8):
    """Draw possibly-wrapped text. Returns y after the last line."""
    if max_width:
        lines = _wrap(draw, text, font, max_width)
    else:
        lines = [text]
    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        bbox = draw.textbbox((0, 0), line, font=font)
        y += (bbox[3] - bbox[1]) + line_spacing
    return y


def _draw_caption_strip(draw):
    """Bottom-of-frame caption strip with the repo URL."""
    strip_h = 36
    draw.rectangle([(0, H - strip_h), (W, H)], fill=NAVY)
    f = _font(13, bold=False)
    txt = "github.com/sruthir28/enterprise-ai-skills"
    bbox = draw.textbbox((0, 0), txt, font=f)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, H - strip_h + 10), txt, font=f, fill=WHITE)


# ----------------------------------------------------------------------
# Scene renderers
# ----------------------------------------------------------------------
def scene_title():
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    # Big question
    f_big = _font(68, bold=True)
    f_sub = _font(28)
    f_kicker = _font(18)

    y = 220
    title = "Which sport should I pick up?"
    bbox = d.textbbox((0, 0), title, font=f_big)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) // 2, y), title, font=f_big, fill=NAVY)

    sub = "Pickleball  ·  Tennis  ·  Running"
    bbox = d.textbbox((0, 0), sub, font=f_sub)
    sw = bbox[2] - bbox[0]
    d.text(((W - sw) // 2, y + 110), sub, font=f_sub, fill=DARK_GREY)

    kicker = "Answered top-down with the Enterprise AI Skills toolkit · ~30 seconds"
    bbox = d.textbbox((0, 0), kicker, font=f_kicker)
    kw = bbox[2] - bbox[0]
    d.text(((W - kw) // 2, y + 200), kicker, font=f_kicker, fill=HIGHLIGHT)

    _draw_caption_strip(d)
    return img


def scene_issue_tree():
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_title = _font(28, bold=True)
    f_branch = _font(22, bold=True)
    f_leaf = _font(16)
    f_step = _font(14)

    d.text((60, 40), "Step 1 · Issue Tree", font=f_step, fill=HIGHLIGHT)
    _draw_text(
        d, 60, 70,
        "Decompose: Which sport sticks for 5+ years?",
        f_title, NAVY, max_width=W - 120,
    )

    # 3 branches in 3 columns
    col_w = (W - 120) // 3
    cols = [
        ("Time commitment", [
            "Hours to competence",
            "Weekly hours to maintain",
            "Scheduling flexibility",
        ]),
        ("Sustainability", [
            "Post-35 injury rate",
            "Repetitive stress profile",
            "Recovery time per session",
        ]),
        ("Social fit", [
            "% beginner-friendly courts",
            "Friends who already play",
            "League / drop-in structure",
        ]),
    ]
    y0 = 220
    for i, (branch, leaves) in enumerate(cols):
        x = 60 + i * col_w
        # branch header in highlight
        d.rectangle([(x, y0), (x + col_w - 30, y0 + 50)], fill=HIGHLIGHT)
        d.text((x + 16, y0 + 12), branch, font=f_branch, fill=WHITE)
        # leaves
        ly = y0 + 70
        for leaf in leaves:
            d.text((x + 16, ly), "•  " + leaf, font=f_leaf, fill=DARK_GREY)
            ly += 36

    _draw_caption_strip(d)
    return img


def scene_storyline():
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_title = _font(28, bold=True)
    f_step = _font(14)
    f_line = _font(17)

    d.text((60, 40), "Step 2 · Storyline (every line = a slide)", font=f_step, fill=HIGHLIGHT)
    _draw_text(d, 60, 70,
               "8 claim-shaped slide titles", f_title, NAVY)

    lines = [
        "1.  Adults at 30+ start 2.4 sports per decade — they stick with 0.4.",
        "2.  The three worth comparing: pickleball, tennis, running.",
        "3.  Pickleball's time-to-competence is ~6 hours; tennis's is ~40.",
        "4.  Post-35 injury rate: tennis 2.3x pickleball; running compounds.",
        "5.  Annual cost: pickleball $450, running $620, tennis $1,400.",
        "6.  60% of pickleball courts are beginner-friendly vs. 18% for tennis.",
        "7.  Running = flexibility. Tennis = intensity. Pickleball = durability.",
        "8.  Pick pickleball. Fastest to 'I have a sport.'",
    ]
    y = 180
    for i, line in enumerate(lines):
        color = HIGHLIGHT if i == 7 else DARK_GREY
        font = _font(18, bold=True) if i == 7 else f_line
        _draw_text(d, 80, y, line, font, color, max_width=W - 160, line_spacing=4)
        y += 50

    _draw_caption_strip(d)
    return img


def scene_chart_competence():
    """Mocked-up bar+callout chart frame."""
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_step = _font(14)
    f_title = _font(24, bold=True)
    f_axis = _font(13)
    f_bar = _font(15, bold=True)
    f_callout_big = _font(36, bold=True)
    f_callout_sub = _font(14)
    f_src = _font(11)

    d.text((60, 40), "Step 3 · Charts (native python-pptx, editable)", font=f_step, fill=HIGHLIGHT)
    _draw_text(d, 60, 70,
               "Pickleball's time-to-competence is ~6 hours; tennis's is ~40.",
               f_title, NAVY, max_width=W - 120)

    # Bar chart area
    chart_left, chart_top, chart_right, chart_bot = 200, 220, W - 120, 600
    chart_w = chart_right - chart_left
    chart_h = chart_bot - chart_top

    # baseline
    d.line([(chart_left, chart_bot), (chart_right, chart_bot)], fill=DARK_GREY, width=2)

    # 3 bars
    cats = ["Pickleball", "Running", "Tennis"]
    vals = [6, 10, 40]
    colors = [HIGHLIGHT, GREY, GREY]
    n = len(cats)
    bar_w = chart_w // (n * 2 + 1)
    max_v = max(vals)
    for i, (c, v, col) in enumerate(zip(cats, vals, colors)):
        x0 = chart_left + bar_w + i * bar_w * 2
        x1 = x0 + bar_w
        bar_h = int((v / max_v) * (chart_h - 60))
        y0 = chart_bot - bar_h
        d.rectangle([(x0, y0), (x1, chart_bot)], fill=col)
        # value label above bar
        label = str(v)
        bbox = d.textbbox((0, 0), label, font=f_bar)
        lw = bbox[2] - bbox[0]
        d.text((x0 + (bar_w - lw) // 2, y0 - 28), label, font=f_bar, fill=DARK_GREY)
        # category label
        bbox = d.textbbox((0, 0), c, font=f_axis)
        cw = bbox[2] - bbox[0]
        d.text((x0 + (bar_w - cw) // 2, chart_bot + 10), c, font=f_axis, fill=DARK_GREY)

    # Callout for pickleball
    cx = chart_left + bar_w + bar_w // 2 + 100
    cy = 250
    d.text((cx, cy), "6 hours", font=f_callout_big, fill=HIGHLIGHT)
    d.text((cx, cy + 50), "to enjoyable play", font=f_callout_sub, fill=DARK_GREY)

    # Y label
    d.text((60, 230), "Hours of practice to feel competent", font=f_axis, fill=DARK_GREY)
    # Source
    d.text((60, chart_bot + 60), "Source: synthesis of 14 beginner-onboarding studies; team analysis",
           font=f_src, fill=SOURCE_GREY)

    _draw_caption_strip(d)
    return img


def scene_chart_cost():
    """Mocked-up waterfall chart frame."""
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_step = _font(14)
    f_title = _font(22, bold=True)
    f_axis = _font(13)
    f_bar = _font(13, bold=True)
    f_src = _font(11)

    d.text((60, 40), "Step 3 · Charts", font=f_step, fill=HIGHLIGHT)
    _draw_text(d, 60, 70,
               "Pickleball's Year-1 all-in cost: $450 — gear + drop-in fees, not lessons.",
               f_title, NAVY, max_width=W - 120)

    # Waterfall data: bases + heights
    labels = ["Year 0", "Starter kit", "Lessons", "League", "Court time", "Year 1"]
    values = [0, 60, 120, 150, 120, 450]
    kinds = ["start", "pos", "pos", "pos", "pos", "total"]

    bases = []
    heights = []
    running = 0.0
    for v, k in zip(values, kinds):
        if k == "start":
            bases.append(0)
            heights.append(v)
            running = v
        elif k == "pos":
            bases.append(running)
            heights.append(v)
            running += v
        elif k == "total":
            bases.append(0)
            heights.append(v)

    chart_left, chart_top, chart_right, chart_bot = 120, 200, W - 80, 600
    chart_w = chart_right - chart_left
    chart_h = chart_bot - chart_top
    max_v = max([b + h for b, h in zip(bases, heights)] + [500])

    n = len(labels)
    bar_w = chart_w // (n * 2)
    d.line([(chart_left, chart_bot), (chart_right, chart_bot)], fill=DARK_GREY, width=2)

    for i, (lab, b, h, k) in enumerate(zip(labels, bases, heights, kinds)):
        x0 = chart_left + bar_w // 2 + i * bar_w * 2
        x1 = x0 + bar_w
        base_y = chart_bot - int((b / max_v) * (chart_h - 60))
        top_y = chart_bot - int(((b + h) / max_v) * (chart_h - 60))
        if k == "total":
            color = DARK_GREY
        elif k == "start":
            color = DARK_GREY
        else:
            color = HIGHLIGHT
        d.rectangle([(x0, top_y), (x1, base_y)], fill=color)
        # value label
        val_str = f"${int(b + h if k=='total' else h)}"
        bbox = d.textbbox((0, 0), val_str, font=f_bar)
        lw = bbox[2] - bbox[0]
        d.text((x0 + (bar_w - lw) // 2, top_y - 22), val_str, font=f_bar, fill=DARK_GREY)
        # cat label
        bbox = d.textbbox((0, 0), lab, font=f_axis)
        cw = bbox[2] - bbox[0]
        d.text((x0 + (bar_w - cw) // 2, chart_bot + 10), lab, font=f_axis, fill=DARK_GREY)

    d.text((60, 200), "Annual cost, USD", font=f_axis, fill=DARK_GREY)
    d.text((60, chart_bot + 60),
           "Source: 12 US metro pickleball clubs + rec-center lesson rates; team analysis",
           font=f_src, fill=SOURCE_GREY)

    _draw_caption_strip(d)
    return img


def scene_deck_recommendation():
    """The 'Pick pickleball' final slide preview."""
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_step = _font(14)
    f_huge = _font(96, bold=True)
    f_sub = _font(26)
    f_reason = _font(17)
    f_bottom = _font(15, bold=True)

    d.text((60, 40), "Step 4 · Deck (built end-to-end)", font=f_step, fill=HIGHLIGHT)

    # Hero claim
    d.text((60, 130), "Pick pickleball.", font=f_huge, fill=HIGHLIGHT)
    _draw_text(d, 60, 260,
               'Lowest start cost, highest social density, fastest to "I have a sport."',
               f_sub, NAVY, max_width=W - 120)

    # Three reasons
    reasons = [
        "1.  Time-to-fun: ~6 hours, vs. 40 for tennis.",
        "2.  Injury rate: ~half of tennis; no compounding joint wear.",
        "3.  Social access: 60% of US courts run beginner-friendly drop-in.",
    ]
    y = 400
    for r in reasons:
        d.text((80, y), r, font=f_reason, fill=DARK_GREY)
        y += 40

    d.text((60, 620),
           "8 slides · 3 native editable charts · built in one workflow",
           font=f_bottom, fill=DARK_GREY)

    _draw_caption_strip(d)
    return img


def scene_outro():
    img = _new_canvas()
    d = ImageDraw.Draw(img)
    f_big = _font(46, bold=True)
    f_mid = _font(22)
    f_url = _font(20, bold=True)
    f_small = _font(14)

    _draw_text(d, 60, 200,
               "Open-source consulting toolkit, in Claude.",
               f_big, NAVY, max_width=W - 120)

    _draw_text(d, 60, 320,
               "13 skills: Issue Tree, Synthesis, Hypothesis Tree, Stakeholder Map, "
               "Top-Down Memo, Workshop Designer, Decision Memo, Storyline, "
               "Charts, Deck Pipeline, McKinsey Critic, Prioritization, "
               "AI Use-Case Scorer.",
               f_mid, DARK_GREY, max_width=W - 120, line_spacing=10)

    d.text((60, 540), "github.com/sruthir28/enterprise-ai-skills",
           font=f_url, fill=HIGHLIGHT)
    d.text((60, 580), "Fork it. Try it on your own decision.",
           font=f_small, fill=DARK_GREY)

    _draw_caption_strip(d)
    return img


# ----------------------------------------------------------------------
# Assemble GIF
# ----------------------------------------------------------------------
# Per-scene durations in SECONDS. Slow enough to read; total ~33s.
SCENES = [
    (scene_title,                3.5),
    (scene_issue_tree,           6.0),
    (scene_storyline,            6.5),
    (scene_chart_competence,     5.0),
    (scene_chart_cost,           5.0),
    (scene_deck_recommendation,  5.0),
    (scene_outro,                3.0),
]


def build_gif():
    out_dir = Path(__file__).resolve().parent
    frames_dir = out_dir / "_gif_frames"
    frames_dir.mkdir(exist_ok=True)

    frames = []
    durations_ms = []
    for i, (renderer, duration_s) in enumerate(SCENES):
        img = renderer()
        # Save as PNG too — useful for the README static fallback / debugging
        png_path = frames_dir / f"scene_{i:02d}.png"
        img.save(png_path, "PNG", optimize=True)
        # Downsize for GIF (smaller file)
        gif_img = img.resize((960, 540), Image.LANCZOS).convert("P", palette=Image.ADAPTIVE, colors=128)
        frames.append(gif_img)
        durations_ms.append(int(duration_s * 1000))

    # Save the hero chart still for use as a fallback image / inline embed
    hero_still = scene_chart_competence()
    hero_still.save(out_dir / "hero-chart.png", "PNG", optimize=True)

    gif_path = out_dir / "hero.gif"
    # Pillow writes GIF directly. duration is per-frame in MILLISECONDS.
    # disposal=2 clears the previous frame so we don't get ghosting between scenes.
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations_ms,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"Wrote {gif_path}  ({gif_path.stat().st_size // 1024} KB, {len(frames)} scenes, "
          f"total {sum(durations_ms) / 1000:.1f}s)")
    print(f"Wrote {out_dir / 'hero-chart.png'}  ({(out_dir / 'hero-chart.png').stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build_gif()
