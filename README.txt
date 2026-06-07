CareerConsole v13
=================

This is a clean replacement package for your PWA job-search app.

Files to upload to GitHub Pages:
- index.html
- manifest.webmanifest
- sw.js
- icons/icon-180.png
- icons/icon-192.png
- icons/icon-512.png

Do NOT upload your private backup JSON to GitHub.
Your job/contact data should stay in browser storage or your iCloud backup file.

Install / update steps
----------------------
1. Open your GitHub repository.
2. Upload the full contents of this folder, keeping the same file names.
3. Commit changes.
4. Wait 2 minutes for GitHub Pages to update.
5. Open your site with a cache-busting URL, for example:
   https://mickjb80-hub.github.io/burke_job_hunt_pwa/index.html?v=13
6. On iPhone, open in Safari, tap Share, then Add to Home Screen.

Data migration
--------------
CareerConsole v13 can import:
- CareerConsole v13 backup JSON
- v12/v11 Job Hunt Console snapshot JSON

Use:
More -> Restore from backup

If the old v12 app already stored data in the same browser/origin, v13 will try to migrate it automatically.

Main features
-------------
- Today screen with top-5 action engine
- Best-first Jobs view with scoring and filters
- Contacts auto-linked from jobs
- Contact timeline
- Prep generators for emails, cover letters, LinkedIn messages and interview sheets
- Backup / restore / ChatGPT review export
- Calendar .ics reminder export
- PWA install and offline support

Privacy note
------------
GitHub Pages public repositories expose your app code. Keep private job/contact data in local browser storage and JSON backups only.
