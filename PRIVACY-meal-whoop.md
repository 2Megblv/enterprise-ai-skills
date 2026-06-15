# Privacy Policy — Meal-Whoop Tracker

**Effective date:** May 23, 2026
**Last updated:** May 23, 2026

This privacy policy describes how the **Meal-Whoop Tracker** application ("the App") accesses, uses, stores, and protects data from the Whoop API.

---

## About the App

Meal-Whoop Tracker is a **personal-use, single-user application** developed by Sruthi Reddy Chintakunta to correlate her own food intake with her own Whoop recovery data. It runs entirely on the developer's local computer. It is not a commercial product, has no external users, and is not distributed as a hosted service.

The source code is open-source and available for inspection at:
https://github.com/sruthir28/enterprise-ai-skills (related skills and tooling)

---

## Data accessed via the Whoop API

The App requests the following Whoop API scopes:

- `read:recovery` — daily recovery score, HRV (RMSSD), resting heart rate, SpO2, skin temperature
- `read:cycles` — daily strain, average and max heart rate, kilojoules
- `read:sleep` — sleep duration, efficiency, performance, sleep stages, respiratory rate
- `read:workout` — workout summaries (not required for current functionality, requested for future use)
- `read:profile` — basic profile information
- `read:body_measurement` — body measurements

The App accesses **only the authenticated user's own data** (the developer's personal Whoop account).

---

## How data is used

Data retrieved from the Whoop API is used solely to:
1. Store daily recovery, sleep, and cycle metrics in a local SQLite database on the developer's computer.
2. Compute correlations between the developer's logged meals and her next-day Whoop recovery / HRV / RHR metrics.
3. Generate personal reports (e.g., "top 3 foods associated with lowest recovery") for the developer's own review.

Data is not used for advertising, marketing, profiling, training of any machine learning model, or any commercial purpose.

---

## How data is stored

- All Whoop data is stored **locally** in a SQLite database file (`tracker.db`) on the developer's personal computer.
- OAuth access tokens and refresh tokens are stored locally in a JSON file (`.whoop_token.json`).
- API credentials (client_id, client_secret) are stored locally in a JSON file (`config.json`).
- These files are excluded from version control and are never uploaded to any cloud service or remote server.

---

## Data sharing

**No data accessed via the Whoop API is shared with any third party.** It is not transmitted to any remote server, not sold, not licensed, and not made available to other users (because there are no other users).

---

## Data retention

Data is retained on the developer's local computer until the developer manually deletes the local database file or revokes the application's access via the Whoop user dashboard. The developer may delete all stored data at any time by removing the `tracker.db`, `.whoop_token.json`, and `config.json` files.

---

## User rights

As a single-user personal application, the only user is the developer herself. She has full control to:
- Revoke the application's access at any time via the Whoop user dashboard.
- Delete all locally-stored data at any time.
- Inspect the open-source code that processes the data.

If the application were ever expanded to additional users (it is not currently), an updated privacy policy with appropriate user-rights provisions would be published at this URL before any additional user's data is accessed.

---

## Security

- The application runs locally and does not expose any endpoints over the network during normal operation, except a temporary `http://localhost:1234` callback used during the initial OAuth authorization (which closes immediately after).
- OAuth tokens are stored in plain text on the local machine. Users running the application are responsible for the physical and digital security of their own computer.
- HTTPS is used for all Whoop API requests.

---

## Changes to this policy

If material changes are made to this privacy policy, the "Last updated" date at the top of this document will be revised, and a brief summary of changes will be added in a `## Change log` section below.

---

## Contact

Questions about this privacy policy can be sent to:

**Sruthi Reddy Chintakunta**
sru281@gmail.com

---

## Change log
- 2026-05-23 — Initial publication.
