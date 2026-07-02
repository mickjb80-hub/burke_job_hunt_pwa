CareerConsole v14.2 — Privacy Split + Weekly Activity Summaries

This is the generic public build. It contains no personal application history and no real recruiter email addresses.

What changed in v14.2:
- Personal job/application seeds removed from index.html.
- Generic fictional demo profile only.
- Real data should live in localStorage and private JSON backups, not in the public GitHub Pages file.
- Added Weekly Summary export with three profile-driven styles: UC journal, Personal review and Recruiter update.
- Added nearby towns field in profile setup to improve pasted-advert location parsing outside the North West.
- Kept v13.9.1 parser fixes: driving-negation guard, hourly-rate handling, role-title cleanup, transit link correction and badge permission button.


Additional v14.1 fixes retained:
- Weekly summaries now include Actions completed this week from job logs and contact timelines.
- UC wording now separates completed activity from currently due follow-ups.
- Generic fallback next-step wording now follows the profile work preference instead of assuming fixed-site roles.
- Added .gitignore to reduce the risk of private JSON backups being uploaded accidentally.

Upload these files to GitHub Pages:
- index.html
- manifest.webmanifest
- sw.js
- README.txt

Do not upload private profile JSON backups to the public repo. Import them inside the app from your own device.

After upload, refresh Safari twice and confirm v14.2.0 in the top-right build badge.


Additional v14.2 fixes:
- Weekly outcome lines now print the closed decision rather than the job stage.
- Job cards are visually quieter: company, role, score, decision and only true risk/due pills are shown.
- Salary and commute detail stay in the job sheet/CSV instead of crowding every card.
- Score colour now carries quality signal: green high, amber medium, grey low.
- Jobs header now prioritises Paste advert and + Add; Application log remains available from More/Quick actions and the Applications filter.

After upload, refresh Safari twice and confirm v14.2.0 in the top-right build badge.
