# Wonder Nanny

A room in the house of L'arte dell'amore. Plain HTML and CSS; inherits `../css/site.css`.

- `index.html` — the English page (packages A/B/C, add-ons, nannies, hotels, the gift, request form, FAQ)
- `nl/index.html` — the same page in Dutch
- `app/index.html` — the Planner: plan a day, run the day, write the handover card, keep a log. Everything stays in the browser (localStorage); nothing is sent unless you press Send. Add it to your iPhone home screen from Safari (Share → Add to Home Screen).
- `css/wonder.css` — the cloud ground, gold frames, the three columns

## Before you publish
Search the pages for `class="confirm"` — every yellow-dashed phrase is a figure or claim Wietske must confirm (prices, VAT, the quarterly charity report). Remove the class once confirmed.

## Launch
Merge the `wonder-nanny` branch into `main`. GitHub Pages serves the folder automatically at
`https://lartedellamore.github.io/wonder-nanny/` (and `/wonder-nanny/nl/`, `/wonder-nanny/app/`).
To link it from the house: add `<a href="wonder-nanny/index.html">Wonder Nanny</a>` to the nav in `tools/build.py` (both languages) and run the build.
