# Über GitHub veröffentlichen

## Einzelschritte

1. In GitHub unter {menuselection}`Settings --> Pages` für die `Source` den Wert `GitHub Actions` auswählen.
2. Im μEditor einen neuen Branch anlegen.
3. Im Wurzelverzeichnis einen neuen Ordner {file}`.github` anlegen.
4. Im {file}`.github` Ordner einen neuen Ordner {file}`workflows` anlegen.
5. Im {file}`.github/workflows` Ordner eine neue Datei {file}`pages.yml` anlegen.
6. Folgenden Inhalt in die neue Datei einfügen:

   :::{code-block} yaml
   name: Publish the site

   on:
     push:
       branches:
         - main

     workflow_dispatch:

   concurrency:
     group: "pages"
     cancel-in-progress: true

   jobs:
     # Build the site
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Setup python
           uses: actions/setup-python@v5
           with:
             python-version: "3.11"

         - name: Install Base Dependencies
           run: |
             sudo pip install hatch

         - name: Build the pages
           run: |
             hatch run build

         - name: Setup Pages
           uses: actions/configure-pages@v4

         - name: Upload artifact
           uses: actions/upload-pages-artifact@v3
           with:
             path: "site"

     # Deploy the site
     deploy:
       runs-on: ubuntu-latest

       needs: build

       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}

       permissions:
         contents: read
         pages: write
         id-token: write

       steps:
         - name: Deploy to GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v4
   :::
7. Die Datei speichern. Sie wird automatisch zu GitHub gepushed und started dort den Buildvorgang.
