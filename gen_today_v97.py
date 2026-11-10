#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-10 (v97).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain-DNS direct
connection: rc=0, 538,336 bytes, complete document ending in </html>,
exactly 11 Box-row articles. Freshness verified: saved-file mtime
12:31:27 > pre-fetch start, file starts fresh this run.
Cross-check: independent WebFetch (?since=daily) returned the SAME 11
repos, SAME order, SAME stars-today values (1038/3278/4267/574/551/216/
916/172/506/31/1587). Total raw = +13,136 on both views. Cumulative star
counts: report uses the curl values (freshest).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks and p-e-w/heretic are NOT on today's list
(no action needed). No political-sensitivity issues, no circumvention
tools among the 11. All 11 repos included, +13,136 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (7/11):
  * anthropics/skills                -- official Agent Skills repo.
  * anthropics/claude-quickstarts    -- official Claude API starter apps.
  * vercel-labs/agent-browser        -- browser automation CLI FOR AI agents.
  * milind-soni/OpenMausBot          -- open-source Grok Bot alternative (VM for bots).
  * ZhuLinsen/daily_stock_analysis   -- LLM-driven multi-market stock analysis
                                        system (LLM is the core engine, not a
                                        mention).
  * garrytan/gbrain                  -- agent memory/brain by Garry Tan (YC CEO):
                                        README verified, "Give the agent you
                                        already use a memory you control", MCP
                                        exposed, knowledge graph. AI by nature.
  * homeassistant-ai/ha-mcp          -- Home Assistant MCP Server (87 tools),
                                        README verified: control HA with
                                        Claude/ChatGPT etc. AI by nature.
NOT counted (4), with precedent:
  * sherlock-project/sherlock        -- OSINT username hunting tool (11-09 precedent).
  * google-deepmind/mujoco           -- physics simulator, no AI (11-09 precedent).
  * ruvnet/RuView                    -- WiFi-sensing spatial intelligence, no AI.
  * meta/astryx                      -- design system at its core; "agent ready"
                                        is a property (dbx precedent, 11-09).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-10"
TODAY_FMT = "2026年11月10日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 11 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("anthropics/skills", "https://github.com/anthropics/skills", "Python", 191255, 1038,
     "skills：Anthropic 官方的智能体技能（Agent Skills）公共仓库——SKILL.md 开放标准的官方实现与示例集合，供 Claude 等智能体安装使用。「技能层」官方源头仓库连续第二日在榜，累计 Star 达 191,255（19 万）。"),
    ("meta/astryx", "https://github.com/meta/astryx", "TypeScript", 20581, 3278,
     "astryx：Meta 开源的设计系统——在 Meta 内部生长八年、支撑 13,000+ 应用后走向开源（Beta）；提供 150+ 无障碍组件、品牌级主题、暗色模式与 CLI，基于 React 19 + StyleX 构建，API 与文档专为「人和 AI 智能体用同一套工具协同开发」而设计。连续第二日在榜，累计 Star 20,581。"),
    ("sherlock-project/sherlock", "https://github.com/sherlock-project/sherlock", "Python", 107488, 4267,
     "sherlock：跨社交网络按用户名侦查社交账号的开源 OSINT 工具——输入一个用户名，即可在数百个社交平台上并行查找同名账号。开源情报领域最知名的项目之一，连续第二日在榜且今日登顶涨幅榜，累计 Star 达 107,488（10 万+）。"),
    ("google-deepmind/mujoco", "https://github.com/google-deepmind/mujoco", "C++", 17007, 574,
     "MuJoCo：Multi-Joint dynamics with Contact——DeepMind 维护的通用多关节接触动力学物理仿真引擎，机器人学与强化学习研究的标准工具，对图形/仿真方向的读者亦有参考价值。连续第二日在榜，累计 Star 17,007。"),
    ("anthropics/claude-quickstarts", "https://github.com/anthropics/claude-quickstarts", "Python", 20114, 551,
     "claude-quickstarts：Anthropic 官方的 Claude API 快速上手项目集——一系列帮助开发者用 Claude API 快速构建可部署应用（含智能体应用）的官方示例库。连续第二日在榜，累计 Star 20,114。"),
    ("garrytan/gbrain", "https://github.com/garrytan/gbrain", "TypeScript", 32257, 216,
     "gbrain：Y Combinator 总裁兼 CEO Garry Tan 开源的智能体记忆/知识库（Agent Brain）——「给你已在用的智能体一个由你掌控的记忆」：以来源可溯的显式事实存储为核心，支持更正与撤回、跨智能体共享，经 MCP 暴露给 Grok Bot/Claude Code/ChatGPT 等客户端，内置综合问答层与类型化知识图谱；其本人生产环境承载 15.6 万页面、2.4 万人物、5,340 公司，66 个 cron 自主运行。Garry Tan 个人新面孔首次登榜，累计 Star 32,257。"),
    ("vercel-labs/agent-browser", "https://github.com/vercel-labs/agent-browser", "Rust", 48627, 916,
     "agent-browser：面向 AI 智能体的浏览器自动化 CLI——Vercel Labs 出品，让智能体像操控桌面一样操控浏览器。与 agent-desktop 同门，「给智能体一台电脑/浏览器」赛道连续在榜，累计 Star 48,627。"),
    ("ruvnet/RuView", "https://github.com/ruvnet/RuView", "Rust", 103584, 172,
     "RuView：把普通 WiFi 信号变成实时空间智能、生命体征监测与存在感知——无需任何摄像头视频。回归项目（上次 10-29），累计 Star 103,584（10 万+）。"),
    ("ZhuLinsen/daily_stock_analysis", "https://github.com/ZhuLinsen/daily_stock_analysis", "Python", 69102, 506,
     "daily_stock_analysis：LLM 驱动的多市场股票智能分析系统——多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。来自中国开发者的新面孔首次登榜，累计 Star 69,102、Fork 数高达 56,444（Fork/Star 比罕见地接近 0.82，社区复用热度极高）。"),
    ("homeassistant-ai/ha-mcp", "https://github.com/homeassistant-ai/ha-mcp", "Python", 6099, 31,
     "ha-mcp：Home Assistant MCP 服务器——用 Claude、ChatGPT 等 AI 助手配置和自动化智能家居，提供 87 个工具，基于 FastMCP 构建。智能家居生态官方组织新面孔首次登榜，累计 Star 6,099。"),
    ("milind-soni/OpenMausBot", "https://github.com/milind-soni/OpenMausBot", "TypeScript", 19937, 1587,
     "OpenMausBot：开源的 Grok Bot 替代品——自带一台供 Bot 使用的虚拟机（a virtual machine that bots can use），让 AI 机器人拥有可安全操作的完整运行环境。「给智能体一台电脑」赛道连续第三日在榜，累计 Star 19,937。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "给智能体一台电脑": ["OpenMausBot", "agent-browser"],
    "智能体记忆": ["gbrain"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"anthropics/skills", "anthropics/claude-quickstarts",
            "vercel-labs/agent-browser", "milind-soni/OpenMausBot",
            "ZhuLinsen/daily_stock_analysis", "garrytan/gbrain",
            "homeassistant-ai/ha-mcp"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer vs raw #1 (today they differ).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（OSINT 工具连续第二日在榜并登顶）。GitHub 原始榜单首位则是 anthropics/skills（+1,038）——<b>与涨幅冠军不一致</b>，注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>Python 以 {maxc}/{len(repos)} 居首</b>：sherlock、anthropics/skills、claude-quickstarts、daily_stock_analysis 与 ha-mcp 五席；其余分布：{others}，共 {len(lang_stats)} 种语言，全部已内置色表，无 #888888 缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：sherlock（+{top[4]:,}）、astryx（+{second[4]:,}）与 OpenMausBot（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 ha-mcp 的 +31 收尾。</li>')

    delta_pct = int(round(abs(total_today - 7172) / 7172 * 100))
    ins.append(f'<li><b>热度大幅回升</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-09（+7,172 / 9 个仓库）回升约 <b>{delta_pct}%</b>，重返 10-27~10-29 的水位区间（+13.4K~+14.6K）。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'OSINT 侦查工具' if 'sherlock' in r[0] else '物理仿真引擎' if 'mujoco' in r[0] else 'WiFi 感知空间智能' if 'RuView' in r[0] else '设计系统本体，dbx 先例'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 4 个为 {non_ai_txt}。另注：越狱提示词合集 jailbreaks 与 p-e-w/heretic 今日均未上榜（剔除口径无需触发）。</li>')

    ins.append('<li><b>新面孔 3 个、回归 1 个、延续 7 个、掉榜 2 个</b>：新进 <b>gbrain</b>（YC CEO Garry Tan 亲力亲为的智能体记忆系统）、<b>daily_stock_analysis</b>（中国开发者 LLM 量化分析，5.6 万 Fork）、<b>ha-mcp</b>（智能家居 × MCP 服务器）；回归 <b>RuView</b>（上次 10-29，WiFi 感知）；上期 9 个仓库中 7 个延续（sherlock、astryx、OpenMausBot、skills、agent-browser、mujoco、claude-quickstarts），掉榜 nvke、billion-context。</li>')

    ins.append('<li><b>主题观察：「智能体的大脑与身体」双线并进</b>——① <b>记忆线</b>：gbrain 登榜把「智能体记忆」做成一等公民（显式事实+来源溯源+知识图谱+MCP 共享），与上期 billion-context 的上下文压缩互为补充，YC CEO 亲自下场为赛道背书；② <b>身体线</b>：OpenMausBot（虚拟机）+ agent-browser（浏览器）连续在榜，「给智能体一台电脑」赛道第三日延续；③ <b>技能层</b>：anthropics/skills（19 万）与 claude-quickstarts 连续第二日同榜，官方源头稳坐；④ <b>AI 落地应用</b>：daily_stock_analysis（LLM 量化分析）与 ha-mcp（智能家居 MCP，87 工具）代表 AI 从基础设施走向日常场景；⑤ sherlock 与 mujoco 则是两个经典老牌项目的连续在榜——OSINT 与物理仿真领域热度罕见延续。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：anthropics/skills 累计 Star 达 <b>191,255</b>（19 万）、sherlock <b>107,488</b> 与 RuView <b>103,584</b> 双双稳站 10 万+；agent-browser 4.9 万、daily_stock_analysis 6.9 万（Fork 5.6 万，Fork/Star 比 0.82 罕见）紧随；体量最小的新面孔是 ha-mcp（6,099）。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 10)
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
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
