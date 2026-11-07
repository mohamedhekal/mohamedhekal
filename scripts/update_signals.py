#!/usr/bin/env python3
"""Refreshes the 'GitHub signals' table in README.md from the public GitHub API.

Standard library only. Reads public data; GITHUB_TOKEN is optional and only raises the rate limit.
Rewrites the block between the signals markers and nothing else.
"""
import datetime
import json
import os
import re
import sys
import urllib.request

USER = "mohamedhekal"
README = os.path.join(os.path.dirname(__file__), "..", "README.md")
START, END = "<!-- signals:start -->", "<!-- signals:end -->"


def api(path):
    req = urllib.request.Request(f"https://api.github.com{path}", headers={
        "Accept": "application/vnd.github+json", "User-Agent": "profile-signals"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def own_public_repos():
    out, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?type=owner&per_page=100&page={page}")
        out += batch
        if len(batch) < 100:
            return [r for r in out if not r["fork"]]
        page += 1


def main():
    repos = own_public_repos()
    release = api(f"/repos/{USER}/agentproof/releases/latest")
    runs = api(f"/repos/{USER}/agentproof/actions/workflows/ci.yml/runs?branch=main&per_page=1")["workflow_runs"]
    today = datetime.date.today().isoformat()
    if runs:
        run = runs[0]
        ci = f"last run on main: **{run['conclusion'] or run['status']}** ({run['created_at'][:10]})"
    else:
        ci = "no runs found"
    block = "\n".join([
        START,
        "| Signal | Value |",
        "|:--|:--|",
        f"| Original public repositories | {len(repos)} |",
        f"| Latest AgentProof release | [{release['tag_name']}]({release['html_url']}) (explainer videos in EN and AR) |",
        f"| AgentProof CI (tests and reliability gate) | {ci} |",
        "| Open-source Laravel packages | indexed in [oss-portfolio](https://github.com/mohamedhekal/oss-portfolio) |",
        "",
        f"<sub>Refreshed automatically from the GitHub API on {today}. No third-party stat services.</sub>",
        END,
    ])
    text = open(README, encoding="utf-8").read()
    new, n = re.subn(re.escape(START) + r".*?" + re.escape(END), lambda _m: block, text, flags=re.S)
    if n != 1:
        sys.exit("signals markers not found exactly once")
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
    print(f"repos={len(repos)} release={release['tag_name']} ci={ci}")


if __name__ == "__main__":
    main()
