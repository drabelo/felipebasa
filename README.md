# Felipe Sousa — Architecture Portfolio

Single-page portfolio site for Felipe Sousa, architect (São Paulo / Goiânia, Brazil), built from his 2026 architecture portfolio and CV.

Static site — plain HTML/CSS/JS, no build step or dependencies.

```
index.html
assets/
  css/style.css
  js/main.js
  img/            project photography, renders, and watercolor sketches
.github/workflows/deploy.yml   GitHub Pages deployment (GitHub Actions)
```

## Local preview

```
python3 -m http.server 8000
```

then open http://localhost:8000

## Deployment

Deploys automatically to GitHub Pages via GitHub Actions on every push to `main` or `claude/architect-portfolio-site-7u2498`. Repository setting **Settings → Pages → Build and deployment → Source** must be set to **GitHub Actions** once for the workflow to publish successfully.