#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-10-26 (v88).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on its first (plain-DNS) route: rc=0,
581,951 bytes, complete document ending in </html>, exactly 11 Box-row
articles -> today's list is really 11 repos, not a truncation artifact.
Freshness verified: saved-file mtime 09:37:24 > pre-fetch 09:37:18.
Cross-check: independent WebFetch (?since=daily) returned the SAME 11
repos, SAME order, SAME stars-today values
(675 / 1,317 / 1,592 / 1,092 / 647 / 381 / 199 / 51 / 152 / 2,878 / 197).
Total = +9,181.
Cumulative star counts: report uses the curl values (freshest source).

CONTENT NOTE
------------
No political-sensitivity issues and no circumvention / access-evasion tool
on today's list -- all 11 repos are reported, nothing dropped.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (8/11):
  * makecindy/cindy                 -- open-source out-of-the-box AI Agent.
  * Nutlope/hallmark                -- anti-AI-slop design skill for Claude
                                       Code / Cursor / Codex (agent skill).
  * debpalash/VoiceStudio           -- fully-local AI voice product.
  * pbakaus/impeccable              -- design language for AI harnesses.
  * TauricResearch/TradingAgents    -- multi-agent LLM trading framework.
  * JetBrains/thinkrail             -- JetBrains' vibe-coding AI IDE (pi).
  * cloudflare/security-audit-skill -- coding-agent security audit skill.
  * AgriciDaniel/claude-seo         -- universal SEO skill for Claude Code.

NOT counted (3/11):
  * pollen-robotics/microduck -- biped duck robot (hardware/robotics).
  * Renhuai123/ziwei-doushu   -- Zi Wei Dou Shu chart engine (traditional
                                 Chinese astrology, not AI).
  * coollabsio/coolify        -- self-hostable PaaS (mentions AI apps but
                                 the product itself is a PaaS; per the
                                 dbx/openship/supabase precedent).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-10-26"
TODAY_FMT = "2026年10月26日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass).
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("makecindy/cindy", "https://github.com/makecindy/cindy", "TypeScript", 4911, 675,
     "cindy：「Consider it done. 想到，就能做到。」开源、开箱即用的通用 AI Agent——无需复杂配置，装上就能干活。今日 GitHub 原始榜单首位；通用型开源 Agent 在消费侧的「开箱即用化」正在成为新趋势，累计 Star 4,911。"),
    ("Nutlope/hallmark", "https://github.com/Nutlope/hallmark", "CSS", 33858, 1317,
     "hallmark：面向 Claude Code、Cursor 与 Codex 的「反 AI 味」设计技能——专治 AI 生成界面的千篇一律（AI-slop）。让智能体生成的 UI 拥有真正的设计质感：当「会写代码」卷完之后，「有审美」成为智能体技能层的新战场，累计 Star 33,858。"),
    ("debpalash/VoiceStudio", "https://github.com/debpalash/VoiceStudio", "Python", 86894, 1592,
     "VoiceStudio：开源、完全本地的 ElevenLabs 替代品——支持 646 种语言的语音克隆、音色设计、视频配音、听写、转写与有声书制作。本地 AI 语音赛道的标杆项目，累计 Star 已达 86,894，重返榜单即位列第二。"),
    ("pbakaus/impeccable", "https://github.com/pbakaus/impeccable", "Rust", 87740, 1092,
     "impeccable：「让你的 AI harness 更懂设计的设计语言」。与 hallmark 同处一条赛道——给 AI 编码智能体注入设计规范与审美约束，让智能体产出的界面不再廉价。设计质量正在成为智能体生态的独立技能层，累计 Star 87,740。"),
    ("pollen-robotics/microduck", "https://github.com/pollen-robotics/microduck", "Rust", 11675, 647,
     "microduck：Pollen Robotics（Hugging Face 旗下）开源的迷你双足鸭子机器人——用 Rust 编写，是具身智能/机器人方向罕见的「萌系」硬件项目。今日唯一非软件类项目，图形/硬件方向读者可关注，累计 Star 11,675。"),
    ("TauricResearch/TradingAgents", "https://github.com/TauricResearch/TradingAgents", "Python", 114656, 381,
     "TradingAgents：多智能体 LLM 金融交易框架——用基本面、情绪、技术面等多个分析师智能体协作模拟真实交易团队的决策流程。金融 + 多智能体交叉方向的代表项目，累计 Star 114,656，时隔一个月回归榜单。"),
    ("Renhuai123/ziwei-doushu", "https://github.com/Renhuai123/ziwei-doushu", "TypeScript", 7616, 199,
     "ziwei-doushu：紫微斗数开源排盘引擎——基于倪海厦《天纪》体系，含完整排盘算法、四化系统、格局知识库与古籍原文数据。传统文化数字化的有意思案例，今日最「本土」的项目，累计 Star 7,616。"),
    ("JetBrains/thinkrail", "https://github.com/JetBrains/thinkrail", "TypeScript", 1781, 51,
     "thinkrail：JetBrains 官方新推出的「与 pi 一起 vibe coding」轻量级真实 IDE——围绕你的工作方式自适应定制。老牌 IDE 巨头正式入局 vibe coding 赛道的标志性产品，发布即登 Trending，累计 Star 1,781。"),
    ("coollabsio/coolify", "https://github.com/coollabsio/coolify", "PHP", 64424, 152,
     "coolify：开源、可自托管的 PaaS——Vercel/Heroku/Netlify 的平替，一键部署静态站、数据库、全栈应用与 360+ 一键服务到自己的服务器。自托管基础设施赛道的老牌项目，累计 Star 64,424，为本自动化有记录以来首次登榜。"),
    ("cloudflare/security-audit-skill", "https://github.com/cloudflare/security-audit-skill", "JavaScript", 46974, 2878,
     "security-audit-skill：Cloudflare 官方的编码智能体安全审计技能——对代码库执行多阶段安全审计，产出经独立验证、机器可读的审计发现。连续第二期位居涨星榜首，今日 +2,878：智能体「安全审计」技能的热度仍在攀升，累计 Star 46,974。"),
    ("AgriciDaniel/claude-seo", "https://github.com/AgriciDaniel/claude-seo", "Python", 20927, 197,
     "claude-seo：Claude Code 的通用 SEO 技能——26 个子技能 + 19 个子代理，覆盖技术 SEO、E-E-A-T、Schema、GEO/AEO、智能体就绪度（Lighthouse Agentic Browsing、WebMCP、llms.txt）、外链、本地/电商/国际 SEO 与 Google API、PDF/Excel 报告，另附 9 个可选扩展。「智能体技能垂直专业化」的代表：SEO 这类营销工种也拥有了专属技能包，累计 Star 20,927。"),
]

# Today's data-driven insight categories (keyword -> matched repos, computed at runtime).
CATS = {
    "智能体技能生态（安全审计 / SEO / 设计质量）": ["security-audit-skill", "claude-seo", "hallmark", "impeccable"],
    "AI Agent 产品与 IDE": ["cindy", "thinkrail"],
    "本地 AI 语音": ["VoiceStudio"],
    "金融多智能体": ["TradingAgents"],
    "硬件机器人": ["microduck"],
    "传统文化数字化": ["ziwei-doushu"],
    "自托管 PaaS": ["coolify"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"makecindy/cindy", "Nutlope/hallmark", "debpalash/VoiceStudio",
            "pbakaus/impeccable", "TauricResearch/TradingAgents",
            "JetBrains/thinkrail", "cloudflare/security-audit-skill",
            "AgriciDaniel/claude-seo"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    max_cnt = max(lang_stats.values())
    top_langs = sorted([l for l, c in lang_stats.items() if c == max_cnt])
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    if top[0] == rank1[0]:
        ins = [f'<li><b>{top[0]} 今日涨星最快、同时位居榜单首位</b>：单日新增 <b>+{top[4]:,}</b> Stars，为今日最高（GitHub 原始榜单首位与其一致，合并表述场景）。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>']
    else:
        ins = [f'<li><b>{top[0]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第二期位居涨星榜首；GitHub 原始榜单首位为 {rank1[0]}（+{rank1[4]:,}）——不一致。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>']

    # language distribution
    if len(top_langs) > 1:
        lang_repos = [r[0].split("/")[-1] for r in repos if (r[2] or "无语言") in top_langs]
        ins.append(f'<li><b>多语言并驾齐驱</b>：{"、".join(top_langs)} 各占据 {max_cnt} 个 Trending 席位，并列第一（{"、".join(lang_repos[:10])}）。</li>')
    else:
        lang_repos = [r[0].split("/")[-1] for r in repos if (r[2] or "无语言") in top_langs]
        others = "、".join(f"{l}（{lang_stats[l]}）" for l in sorted(lang_stats, key=lambda x: -lang_stats[x]) if l != top_langs[0])
        ins.append(f'<li><b>{top_langs[0]} 最为活跃</b>：占据 {max_cnt}/{len(repos)} 个 Trending 席位（{"、".join(lang_repos[:10])}），是今日绝对主力语言；其余席位分布：{others}。</li>')
    lang_line = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]))
    ins.append(f'<li><b>今日榜单覆盖 {len(lang_stats)} 种语言</b>：{lang_line}。其中 <b>CSS</b>（Nutlope/hallmark）与 <b>PHP</b>（coollabsio/coolify）各占一席——「设计技能」用 CSS 主语言登上 Trending，本身就是个信号。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：{top[0].split("/")[-1]}（+{top[4]:,}）、{second[0].split("/")[-1]}（+{second[4]:,}）与 {third[0].split("/")[-1]}（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>，较上期 79% 明显回落；本期没有单一霸榜巨无霸，增量分布相对均衡。</li>')

    ins.append(f'<li><b>热度小幅回升</b>：今日榜单新增合计 <b>+{total_today:,}</b> Stars，较上期 10-23（+8,015）回升约 {int(round((total_today-8015)/8015*100))}%，维持 9 月中旬以来的中等水位（10-24、10-25 无记录，自动化未触发，对比基准为 10-23）。榜单规模 {len(repos)} 个（上期 9 个）。</li>')

    ai = [r for r in repos if r[0] in AI_NAMES]
    ai_names = "、".join(r[0].split("/")[-1] for r in ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(ai)}/{len(repos)}</b>：明确计入 AI 的是 {ai_names}。口径说明：coolify 简介虽可搭 AI 应用，但本体是自托管 PaaS，按 dbx/openship/supabase 先例不计入 AI；microduck 是硬件机器人项目，ziwei-doushu 是紫微斗数排盘引擎，均不计入。判定口径：本行已明示名单，读者可自行复算。</li>')

    ins.append('<li><b>新面孔 5 个、回归 5 个、延续 1 个</b>：新进 <b>makecindy/cindy</b>（开源开箱即用 AI Agent）、<b>coollabsio/coolify</b>（自托管 PaaS，本自动化记录中首次登榜）、<b>JetBrains/thinkrail</b>（JetBrains 官方 vibe coding IDE）、<b>AgriciDaniel/claude-seo</b>（Claude Code 通用 SEO 技能）、<b>Renhuai123/ziwei-doushu</b>（紫微斗数排盘引擎）；回归项：VoiceStudio（上期 10-14）、TradingAgents（9-24）、impeccable（9-24）、microduck（9-01）、hallmark（7-18）；延续项（隔 10-24/10-25 无记录）：security-audit-skill。较上期掉榜 8 个：php-src、supabase、fastapi、PCL、claude-howto、knowledge-work-plugins、ponytail、graphify。</li>')

    ins.append('<li><b>主题观察：「AI 审美/设计质量」赛道成对出现</b>——hallmark（反 AI 味设计技能）与 impeccable（让 AI harness 更懂设计的设计语言）同日登榜且分列第 3、第 4，说明「让智能体产出有设计感的界面」正在从隐含需求变成显性技能层；加上 security-audit-skill（安全审计）与 claude-seo（SEO），今日智能体技能类项目占 4 席，「技能垂直专业化」仍是 Trending 主线。另一看点：JetBrains 官方推出 thinkrail 入局 vibe coding，老牌 IDE 厂商正式下场。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 10, 26)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace

    print(f"Generating GitHub Trending report for {TODAY_FMT}...")
    html = base.gen_html(REPOS)
    md = base.gen_md(REPOS)
    html_path = f"github-trending-{TODAY_STR}.html"
    md_path = f"github-trending-{TODAY_STR}.md"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Generated: {html_path}")
    print(f"Generated: {md_path}")

    import glob
    days = []
    for fname in sorted(glob.glob("github-trending-*.html"), reverse=True):
        ds = fname.replace("github-trending-", "").replace(".html", "")
        if ds == "index" or "-" not in ds:
            continue
        repos = base.parse_generic_for_index(open(fname, encoding="utf-8").read())
        if repos:
            days.append((ds, repos))
    days.sort(key=lambda x: x[0], reverse=True)
    index = base.render_index(days)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index)
    print(f"Updated:  index.html ({len(days)} issues)")

    nav_utils.inject_nav()

    total_stars = sum(r[4] for r in REPOS)
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
