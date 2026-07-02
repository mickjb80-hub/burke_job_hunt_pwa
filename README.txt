CareerConsole v15.0.1 — Daily Driver Patch

This is the generic public build. It contains no personal application history and no real recruiter email addresses.

What changed in v15.0.1:
- Trimmed job-card pill density: state pill stays; decision pill is removed from cards and remains in the detail sheet.
- Prep state is no longer red. Red is reserved for overdue/risk signals.
- Today screen is less repetitive: removed the duplicate Weekly Review section and capped "What should I do now" to three items.
- Preserved the v15.0 command-centre structure, guided Review Today flow and profile/backup banner.

Retained from v14.x:
- Privacy split: real data lives in localStorage and private JSON backups, not the public GitHub Pages file.
- Weekly Summary export with UC journal, Personal review and Recruiter update styles.
- Completed weekly activity from job logs and contact timelines.
- .gitignore patterns to reduce accidental private JSON uploads.
- Card clarity patch: less visual noise on job cards and colour reserved for real urgency/risk.

Retained from v13.x:
- Paste-advert quick add with full advert storage.
- Driving-negation guard and fixed-site override.
- Hourly-rate handling and role-title cleanup.
- Transit deep link to Google Maps.
- Interview prep workspace.
- Contacts with follow-up dates, timelines and undo.
- iPhone comfort sizing, light/dark theme, motion and app badge support.

Upload these files to GitHub Pages:
- index.html
- manifest.webmanifest
- sw.js
- README.txt
- .gitignore

Do not upload private profile JSON backups to the public repo. Import them inside the app from your own device.

After upload, refresh Safari twice and confirm v15.0.1.1 in the top-right build badge.
