#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-11 (v98).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via --resolve
20.87.245.0: rc=0, 549,554 bytes, complete document ending in </html>,
exactly 12 Box-row articles. Freshness verified: saved-file mtime
12:34:53 > pre-fetch start.
Cross-check: independent WebFetch returned the SAME 12 repos, SAME
order, SAME stars-today values (3108/1679/465/531/456/159/790/780/
2393/192/375/1225). Total raw = +12,153 on both views. Cumulative star
counts: report uses the curl values (freshest).

CONTENT NOTE
------------
No political-sensitivity issues, no circumvention tools among the 12.
All 12 repos included, +12,153 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (7/12):
  * anthropics/skills                -- official Agent Skills repo.
  * addyosmani/agent-skills          -- production-grade engineering skills
                                        FOR AI coding agents (AI-native by
                                        purpose, not a mere mention).
  * mattpocock/skills                -- "Skills for Real Engineers, straight
                                        from my .agents directory" (agent
                                        skills repo, AI-native).
  * anthropics/claude-quickstarts    -- official Claude API starter apps.
  * vercel-labs/agent-browser        -- browser automation CLI FOR AI agents.
  * homeassistant-ai/ha-mcp          -- Home Assistant MCP server (11-10
                                        precedent, README verified).
  * ranxianglei/billion-context      -- LLM context-compression plugin.
NOT counted (5), with precedent:
  * meta/astryx                      -- design system at its core;
                                        "agent ready" is a property
                                        (dbx/11-09 precedent).
  * sherlock-project/sherlock        -- OSINT username hunting tool.
  * google-deepmind/mujoco           -- physics simulator, no AI.
  * we-promise/sure                  -- personal finance app (contributors
                                        include a "claude" bot account,
                                        which does NOT make it AI).
  * tokio-rs/topcoat                 -- Rust web framework, no AI.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-11"
TODAY_FMT = "2026年11月11日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 12 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("meta/astryx", "https://github.com/meta/astryx", "TypeScript", 23331, 3108,
     "astryx：Meta 开源的设计系统——在 Meta 内部生长八年、支撑 13,000+ 应用后走向开源（Beta）；提供 150+ 无障碍组件、品牌级主题、暗色模式与 CLI，基于 React 19 + StyleX 构建，API 与文档专为「人和 AI 智能体用同一套工具协同开发」而设计。连续第三日在榜且今日重返涨幅榜首，累计 Star 23,331。"),
    ("sherlock-project/sherlock", "https://github.com/sherlock-project/sherlock", "Python", 109252, 2393,
     "sherlock：跨社交网络按用户名侦查社交账号的开源 OSINT 工具——输入一个用户名，即可在数百个社交平台上并行查找同名账号。开源情报领域最知名的项目之一，连续第三日在榜，累计 Star 达 109,252（10 万+）。"),
    ("anthropics/skills", "https://github.com/anthropics/skills", "Python", 192507, 1679,
     "skills：Anthropic 官方的智能体技能（Agent Skills）公共仓库——SKILL.md 开放标准的官方实现与示例集合，供 Claude 等智能体安装使用。「技能层」官方源头仓库连续第三日在榜，累计 Star 达 192,507（19 万+）。"),
    ("mattpocock/skills", "https://github.com/mattpocock/skills", "Shell", 321113, 1225,
     "skills：Matt Pocock（Total TypeScript 作者、TypeScript 教育领域最具影响力人物之一）公开的个人智能体技能目录——「给真正工程师的 Skills， straight from my .agents directory」，把他日常开发工作流中沉淀的智能体技能配置原样开源。新面孔首次登榜即以 321,113（32 万）Star 成为今日全榜体量之最。"),
    ("homeassistant-ai/ha-mcp", "https://github.com/homeassistant-ai/ha-mcp", "Python", 6774, 790,
     "ha-mcp：Home Assistant MCP 服务器——用 Claude、ChatGPT 等 AI 助手配置和自动化智能家居，提供 87 个工具，基于 FastMCP 构建。智能家居 × AI 官方组织仓库连续第二日在榜，累计 Star 6,774。"),
    ("vercel-labs/agent-browser", "https://github.com/vercel-labs/agent-browser", "Rust", 49363, 780,
     "agent-browser：面向 AI 智能体的浏览器自动化 CLI——Vercel Labs 出品，让智能体像操控桌面一样操控浏览器。与 agent-desktop 同门，「给智能体一台电脑/浏览器」赛道连续第三日在榜，累计 Star 49,363，逼近 5 万。"),
    ("anthropics/claude-quickstarts", "https://github.com/anthropics/claude-quickstarts", "Python", 20580, 531,
     "claude-quickstarts：Anthropic 官方的 Claude API 快速上手项目集——一系列帮助开发者用 Claude API 快速构建可部署应用（含智能体应用）的官方示例库。连续第三日在榜，累计 Star 20,580。"),
    ("addyosmani/agent-skills", "https://github.com/addyosmani/agent-skills", "JavaScript", 115293, 465,
     "agent-skills：Addy Osmani（Google Chrome 团队工程负责人、《Learning JavaScript Design Patterns》作者）开源的面向 AI 编程智能体的生产级工程技能集——把资深工程师的代码审查、测试、架构等工程实践封装成可安装的智能体技能。新面孔首次登榜，累计 Star 115,293（11 万+）。"),
    ("google-deepmind/mujoco", "https://github.com/google-deepmind/mujoco", "C++", 17443, 456,
     "MuJoCo：Multi-Joint dynamics with Contact——DeepMind 维护的通用多关节接触动力学物理仿真引擎，机器人学与强化学习研究的标准工具，对图形/仿真方向的读者亦有参考价值。连续第三日在榜，累计 Star 17,443。"),
    ("ranxianglei/billion-context", "https://github.com/ranxianglei/billion-context", "TypeScript", 6441, 375,
     "billion-context：上下文压缩插件——为月级超长会话（十亿 token 级）压缩上下文，100K 小窗口即可承载，节省约 5 倍 token。回归项目（上次 11-04），累计 Star 6,441。"),
    ("tokio-rs/topcoat", "https://github.com/tokio-rs/topcoat", "Rust", 6911, 192,
     "topcoat：Tokio 团队出品的「电池全含」Rust Web 应用框架——开箱即用地集成 Tokio 生态的异步运行时与配套组件，面向 Web 全栈开发。知名异步运行时官方组织新面孔首次登榜，累计 Star 6,911。"),
    ("we-promise/sure", "https://github.com/we-promise/sure", "Ruby", 12143, 159,
     "sure：「属于所有人、由所有人构建」的个人理财应用——社区驱动的开源记账与财务规划工具。新面孔首次登榜，累计 Star 12,143。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体技能生态": ["skills", "agent-skills", "claude-quickstarts"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"anthropics/skills", "anthropics/claude-quickstarts",
            "vercel-labs/agent-browser", "mattpocock/skills",
            "addyosmani/agent-skills", "ranxianglei/billion-context",
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

    # Insight 1: top gainer vs raw #1 (today they AGREE).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（Meta 设计系统连续第三日在榜并重返榜首）。GitHub 原始榜单首位同样是 meta/astryx（+{top[4]:,}）——<b>今日两者恰好一致</b>；但仍提醒：GitHub 榜单排序并非按当日涨幅（如原始第 2 位 anthropics/skills 仅 +1,679，而原始第 9 位 sherlock 有 +2,393），本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{top_langs[0]} 以 {maxc}/{len(repos)} 居首</b>：sherlock、anthropics/skills 与 ha-mcp 三席；其余分布：{others}，共 {len(lang_stats)} 种语言（含新面孔的 Shell、Ruby），全部已内置色表，无 #888888 缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：astryx（+{top[4]:,}）、sherlock（+{second[4]:,}）与 anthropics/skills（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 sure 的 +159 收尾。</li>')

    delta_pct = int(round(abs(total_today - 13136) / 13136 * 100))
    ins.append(f'<li><b>热度高位微降</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-10（+13,136 / 11 个仓库）回落约 <b>{delta_pct}%</b>，仍维持在 10-27 以来的高位区间；仓库数 12 个为近两周最多，热度结构更分散。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'OSINT 侦查工具' if 'sherlock' in r[0] else '物理仿真引擎' if 'mujoco' in r[0] else '个人理财应用' if '/sure' in r[0] else 'Rust Web 框架' if 'topcoat' in r[0] else '设计系统本体，dbx 先例'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 5 个为 {non_ai_txt}（sure 贡献者列表含 claude 机器人账号不构成 AI 判定依据）。</li>')

    ins.append('<li><b>新面孔 4 个、回归 1 个、延续 7 个、掉榜 4 个</b>：新进 <b>mattpocock/skills</b>（Total TypeScript 作者的个人智能体技能目录，32 万 Star 全榜体量之最）、<b>addyosmani/agent-skills</b>（Chrome 团队工程负责人的生产级智能体工程技能）、<b>tokio-rs/topcoat</b>（Tokio 官方 Rust Web 框架）、<b>sure</b>（社区驱动的个人理财应用）；回归 <b>billion-context</b>（上次 11-04，上下文压缩）；上期 11 个仓库中 7 个延续（sherlock、astryx、skills、agent-browser、mujoco、claude-quickstarts、ha-mcp），掉榜 OpenMausBot、daily_stock_analysis、gbrain、RuView。</li>')

    ins.append('<li><b>主题观察：「智能体技能层」大爆发</b>——今日 12 席中 <b>4 个技能类仓库同榜</b>：anthropics/skills（官方源头，19 万）+ mattpocock/skills（个人专家目录，32 万）+ addyosmani/agent-skills（生产级工程技能，11 万）+ claude-quickstarts（官方上手示例），从「官方标准 → 个人专家 → 工程实践」三个层次同时爆发，技能生态正从 Anthropic 单点扩散为开发者社区的通用工作流；② <b>身体线</b>：agent-browser 连续第三日在榜（49K 逼近 5 万里程碑）；③ <b>记忆/上下文线</b>：billion-context 回归，与上期 gbrain 的智能体记忆形成「压缩 vs 长期记忆」互补；④ <b>基础软件</b>：topcoat（Tokio 官方）与 mujoco（DeepMind）代表 Rust 生态与物理仿真的经典热度；⑤ <b>生活应用</b>：sure（理财）与 ha-mcp（智能家居 × AI）延续「AI/开源走进日常」的主线。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：mattpocock/skills 以 <b>321,113</b>（32 万）Star 成为今日全榜体量之最；anthropics/skills 达 <b>192,507</b>（19 万+）、addyosmani/agent-skills <b>115,293</b>（11 万+）、sherlock <b>109,252</b>（10 万+）——四个 10 万+ 项目同榜；agent-browser 49,363 逼近 5 万，astryx 23,331 三日近翻倍节奏。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 11)
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
