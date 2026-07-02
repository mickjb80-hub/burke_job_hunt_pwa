CareerConsole v13.2
===================
A profile-driven, reusable job-search console PWA.
Build: v13.2.0  |  Schema: 13


WHAT CHANGED FROM v13.1
-----------------------
- Added a Michael Burke current-profile seed using the verified application list from Gmail/project history.
- Added job fields for Applied Date, Source/Platform, Reference, Evidence URL and Priority.
- Job cards now show application evidence metadata, not just company/role/score.
- Export-for-AI now includes application date, source, reference and priority for each job.
- Cache bumped to careerconsole-v13-2-0 so GitHub Pages does not serve the old build.

WHAT CHANGED FROM v13.0
-----------------------
The app is no longer hard-coded around one person. It is now PROFILE-DRIVEN:
- First launch shows a Welcome screen: Start blank / Import my backup /
  Use sample engineering profile.
- More > Profile Setup defines who the profile is for. Those answers drive
  scoring, dashboard priorities, generators, and reminders.
- You can hold MULTIPLE profiles (e.g. you and your brother Lee), switch
  between them, export/import a single profile, or restore a full backup.
- The original engineering profile (Michael Burke) is included only as the
  "sample engineering profile" you can load and edit, not baked-in default data.

PACKAGE CONTENTS
----------------
index.html               The whole app (HTML + CSS + JS).
manifest.webmanifest     PWA manifest.
sw.js                    Service worker (offline + cache versioning).
README.txt               This file.
make_icons.py            Script that generated the default icons.
icons/icon-180/192/512   Default icon: clean "CC" monogram with gear accent.
icons-alt-mycareer/      Your uploaded "MyCareer" icon, as an OPTIONAL swap.

ABOUT THE ICON
--------------
Default is a clean CC monogram. It reads at iPhone home-screen size, which is
the whole point of an app icon.
Your uploaded "MyCareer" icon (in icons-alt-mycareer/) is a spanner-shaped C
with the words "My CAREER" inside it. Two honest problems with it:
  1. It is the spanner-C your original brief told me to avoid.
  2. Text inside an icon turns to mush at small sizes.
If you want it anyway, copy the three files from icons-alt-mycareer/ into
icons/ (overwriting), keep the names identical, and redeploy. No code change needed.

DEPLOY TO GITHUB PAGES
----------------------
1. Upload index.html, manifest.webmanifest, sw.js and the icons/ folder to the
   repo root (mickjb80-hub/burke_job_hunt_pwa), replacing the old files.
2. Commit. Pages publishes to:
   https://mickjb80-hub.github.io/burke_job_hunt_pwa/
3. On iPhone, open that URL in Safari first (not the old home-screen icon).
   You should see "New version ready. Reload". Tap it.
4. Install: Safari share sheet -> "Add to Home Screen".

WHY THE CACHE WON'T GET STUCK
-----------------------------
The service worker serves the app shell network-first, so a new deploy is always
fetched fresh when online. Each release bumps the cache name
(careerconsole-v13-2-0) which purges old caches. Build version shows top-right
and under More > Admin. When you ship a new build, change BUILD in index.html
AND the CACHE string in sw.js.

SETTING UP A PROFILE
--------------------
Required (these drive scoring): name, postcode, salary minimum, max commute,
driving available yes/no. Everything else (target roles, sectors, skills, key
experience, qualifications, restrictions, tone, disclosure notes, work
preference, preferred salary, travel limit) is optional and editable any time.
Letters and prep sheets fill from these fields, so the more you add the better
the generated drafts.

BRINGING DATA ACROSS
--------------------
- v12 JSON: More > Admin > "Import v12 JSON". Imports into the CURRENT profile.
  Maps common v12 field names; originals preserved under "_raw". Spot-check a few.
- A v13.0 backup or a single-profile export: use "Restore from backup" or
  "Import a profile". The app detects the shape automatically.
- Full v13.1 backup (all profiles): "Restore from backup" replaces everything.

DATA SAFETY
-----------
- localStorage is a cache. Your JSON backup is the source of truth.
- Back up weekly: More > Admin > "Backup my data" (saves ALL profiles).
- "Export this profile" saves just the active profile to share or move.
- Disclosure / clearance notes are stored on-device only, like everything else.
- Generators produce DRAFTS only. Nothing is ever sent automatically.

SCORING (priority order, highest weight first)
-----------------------------------------------
1. Driving         - if the profile has driving switched off, a driving-required
                     role is capped at 2.5/10 and auto-decided "Reject".
2. Technical fit   - your 0-10 rating on the job.
3. Commute         - green <=60m, amber <= your max, red+capped over your max.
4. Salary          - full marks at/above the profile minimum.
5. Work-life/travel- travel over the profile max % is flagged.
