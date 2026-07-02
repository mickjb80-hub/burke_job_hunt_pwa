CareerConsole v13.5 — iPhone Comfort Plus
==========================================
A profile-driven job-search console PWA, tuned for iPhone daily use.
Build: v13.5.0  |  Schema: 13

WHAT CHANGED FROM v13.4
-----------------------
- Larger base text across the app for iPhone readability.
- Larger tap targets: main buttons are now designed around 44–48px+ touch height.
- Larger job cards with more spacing and clearer metadata.
- Bigger bottom navigation labels and touch areas.
- Larger chips / filters so they are easier to tap.
- Larger sheets, close buttons, form fields, warning boxes and import-result messages.
- Mobile layout rules: cramped two-column areas collapse more cleanly on iPhone.
- Version cleanup: title, manifest and service worker all now identify v13.5.
- Cache bumped to careerconsole-v13-5-0.

WHAT CHANGED FROM v13.3
-----------------------
- Search bars on Jobs and Contacts.
- Phone back / swipe-back closes sheets first instead of exiting immediately.
- App remembers last tab and filter during the session.
- Backup reminder added.
- Pipeline stats strip added on Today.

WHAT CHANGED FROM v13.2
-----------------------
- Import latest verified applications into the active profile.
- Duplicate-safe matching by reference or employer + role.
- Application Log sorted newest first.
- Jobs filters: Newest applied, Applications, Need chasing, High priority.
- Chase-date calculation and CSV export for Excel.

UPLOAD TO GITHUB PAGES
----------------------
Upload the files inside this zip, not the zip itself:
- index.html
- manifest.webmanifest
- sw.js
- README.txt

Optional:
- icons/
- icons-alt-mycareer/
- make_icons.py

After upload, GitHub should show "now" beside index.html, manifest.webmanifest, sw.js and README.txt.
Then open the app in Safari and refresh twice. Top-right should show v13.5.0.

IMPORTANT
---------
CareerConsole stores your profile data in the browser/PWA local storage. Updating the app files does not automatically delete or replace your saved jobs. Use More -> Quick actions -> Import latest applications to merge verified application updates into your active profile.
