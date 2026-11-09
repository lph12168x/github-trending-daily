#!/usr/bin/env python3
"""Generate cloud-DB upsert SQL for the 2026-11-09 trending report."""
import json
from gen_today_v96 import REPOS

rows = sorted(REPOS, key=lambda r: (r[4], r[3]), reverse=True)
total_today = sum(r[4] for r in rows)
repos = [
    {
        "rank": i,
        "name": name,
        "url": url,
        "lang": lang,
        "total_stars": stars,
        "today_stars": today,
        "desc": desc,
    }
    for i, (name, url, lang, stars, today, desc) in enumerate(rows, 1)
]
repos_json = json.dumps(repos, ensure_ascii=False, indent=1)
title = "GitHub Trending 每日简报 · 2026-11-09"

sql = (
    "INSERT INTO trending_reports (report_date, title, total_today, repo_count, repos) VALUES\n"
    f"('2026-11-09', '{title}', {total_today}, {len(rows)}, $json${repos_json}$json$)\n"
    "ON CONFLICT (report_date) DO UPDATE SET\n"
    " title = EXCLUDED.title,\n"
    " total_today = EXCLUDED.total_today,\n"
    " repo_count = EXCLUDED.repo_count,\n"
    " repos = EXCLUDED.repos;\n"
)
with open("sync_trending_db_1109.sql", "w", encoding="utf-8") as f:
    f.write(sql)
print(f"written sync_trending_db_1109.sql: {len(sql)} chars, {len(rows)} repos, total_today={total_today}")
