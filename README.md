# Portfolio — María José Barney

Static, bilingual (EN at `/`, ES at `/es/`) portfolio. No framework, no build step on Vercel.

## Edit content
All text lives in `build/content_home.py` and `build/content_cases.py` (each string has `en` and `es`).
After editing, regenerate the HTML:

```
python3 build/build.py
```

Then commit and push; Vercel redeploys automatically.

## Structure
- `index.html`, `work/<case>/` — English
- `es/index.html`, `es/work/<case>/` — Spanish
- `assets/css`, `assets/js`, `assets/img/<case>/` — styles, lightbox script, anonymized images
