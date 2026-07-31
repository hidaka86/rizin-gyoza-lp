#!/usr/bin/env python3
"""index.html と Claude Design 用セクションプレビューを src/sections/ から生成する。

usage: python3 build.py
"""
import pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "sections"

# (fragment file, preview file, card title, ds group)
# 表示順はこのリストが正(ファイル名の番号は目安)
SECTIONS = [
    ("01-hero.html", "hero.html", "ファーストビュー", "セクション"),
    ("02-concept.html", "concept.html", "コンセプト", "セクション"),
    ("02-taste.html", "taste.html", "餃子としての良さ", "セクション"),
    ("03-protein.html", "protein.html", "成分ロジック", "セクション"),
    ("04-fighters.html", "fighters.html", "選手も愛用", "セクション"),
    ("05-single.html", "single.html", "通常購入", "セクション"),
    ("06-plans.html", "plans.html", "サブスクプラン", "セクション"),
    ("06b-oshi.html", "oshi.html", "推し選手サポート", "セクション"),
    ("07-tshirt.html", "tshirt.html", "Tシャツ特典", "セクション"),
    ("08-faq.html", "faq.html", "FAQ", "セクション"),
    ("09-footer.html", "footer.html", "フッター・法務", "セクション"),
]

HEAD = """<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="robots" content="noindex, nofollow" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Oswald:wght@500;600&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="styles.css" />
<script src="data.js"></script>"""

NAV = """<header class="nav" id="nav">
  <div class="nav__inner">
    <a href="#top" class="nav__brand"><img src="assets/rizin-logo.png" alt="RIZIN" /><span class="x">×</span><span>餃子</span></a>
    <button class="nav__toggle" id="navToggle" aria-label="メニュー" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav__links" id="navLinks">
      <a href="#concept">コンセプト</a>
      <a href="#taste">こだわり</a>
      <a href="#protein">成分</a>
      <a href="#fighters">選手</a>
      <a href="#single">単品</a>
      <a href="#oshi">推し活</a>
      <a href="#faq">FAQ</a>
      <a href="#plans" class="nav__cta">サブスクプラン</a>
    </nav>
  </div>
</header>"""


def build_index():
    body = "\n".join((SRC / f).read_text() for f, *_ in SECTIONS)
    html = f"""<!-- @dsCard group="LP全体" -->
<!DOCTYPE html>
<html lang="ja">
<head>
{HEAD}
<title>RIZIN餃子｜Fight. Eat. Repeat.</title>
<meta name="description" content="食べて、応援する。RIZIN公式 高タンパク餃子。選手は、食べて戦う。ファンは、食べて応援する。" />
</head>
<body>
{NAV}
<main>
{body}
</main>
<script src="main.js"></script>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html)


def build_previews():
    for frag, out, title, group in SECTIONS:
        body = (SRC / frag).read_text()
        html = f"""<!-- @dsCard group="{group}" -->
<!DOCTYPE html>
<html lang="ja">
<head>
{HEAD}
<title>{title}</title>
</head>
<body class="ds-preview">
{body}
<script src="main.js"></script>
</body>
</html>
"""
        (ROOT / out).write_text(html)


if __name__ == "__main__":
    build_index()
    build_previews()
    print(f"built index.html + {len(SECTIONS)} previews")
