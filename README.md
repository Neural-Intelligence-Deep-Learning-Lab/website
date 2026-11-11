# NIDL — Neural Intelligence & Deep Learning Lab

This is a deliberately simple, database-free Django site. All lab information, publications, team members, and page content live directly in the templates under `main/lab/templates/lab/`. CSS and JavaScript live under `main/lab/static/lab/`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd main
python manage.py runserver
```

There are no models, migrations, admin pages, database settings, seed commands, API clients, or network sync jobs. Edit the HTML files directly to update content. Publication search and year filtering are lightweight client-side JavaScript enhancements and the pages remain readable without JavaScript.

The interface uses Ubuntu for body text and a warm editorial serif for headings. The paper/dark theme toggle is persisted in local storage.
