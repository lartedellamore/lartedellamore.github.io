# L'arte dell'amore

The house site: coaching, photography, the atelier. Plain HTML and CSS, no build step needed to serve it.

- `index.html`, `coaching.html`, `photography.html`, `atelier.html`, `about.html`: the pages
- `css/site.css`: the design (rice paper, sumi ink, one gold fine line; light and dark)
- `assets/`: the crest and the fonts (Cormorant Garamond, Inter), hosted here
- `tools/build.py`: all the words live here. Edit, run `python3 tools/build.py`, commit.

## Put it online
1. Create a public repository `lartedellamore/lartedellamore.com` and upload everything in this folder.
2. Settings, Pages: deploy from branch `main`, folder `/ (root)`.
3. For the domain: rename `CNAME.example` to `CNAME`, then add the DNS records GitHub shows at your domain provider.

## Still to add
- Portfolio photographs: put them in `assets/photos/` and replace each `<span>` inside a `.mount` with an `<img>`.
- Coaching fees and a booking link, once chosen.
- Privacy statement and business details before taking payments.
