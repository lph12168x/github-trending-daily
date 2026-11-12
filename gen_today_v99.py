#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-12 (v99).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain DNS (direct
connection worked today): rc=0, 526,971 bytes, complete document ending in
</html>, exactly 10 Box-row articles. Freshness verified: saved-file mtime
12:31 > pre-fetch start.
Cross-check: independent WebFetch returned the SAME 10 repos, SAME order,
SAME stars-today values (2776/278/159/361/787/708/1078/645/52/51).
Total raw = +6,895 on both views. Cumulative star counts: report uses the
curl values (freshest).

CONTENT NOTE
------------
No political-sensitivity issues, no circumvention tools among the 10.
All 10 repos included, +6,895 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
README-verified today:
  * GoogleChrome/modern-web-guidance-src -- jointly stewarded by the
    Chrome/Edge/Firefox/MDN teams; a set of installable AGENT SKILLS that
    embed web-platform expertise into coding agents (AI-native by purpose).
  * shadcn/improve -- agent skill: strong model audits + writes plans,
    cheaper models execute (AI-native workflow).
Counted as AI / Agent related (7/10):
  * ZhuLinsen/daily_stock_analysis     -- LLM-driven stock analysis system.
  * addyosmani/agent-skills            -- engineering skills FOR AI agents.
  * vercel-labs/agent-browser          -- browser automation FOR AI agents.
  * homeassistant-ai/ha-mcp            -- Home Assistant MCP server.
  * openai/codex-security              -- OpenAI Codex Security CLI/SDK.
  * GoogleChrome/modern-web-guidance-src (above).
  * shadcn/improve (above).
NOT counted (3), with precedent:
  * meta/astryx      -- design system at its core; "agent ready" is a
                        property (dbx / 11-11 precedent).
  * we-promise/sure  -- personal finance app.
  * TheAlgorithms/Java -- classic algorithms teaching collection, no AI.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-12"
TODAY_FMT = "2026年11月12日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 10 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("meta/astryx", "https://github.com/meta/astryx", "TypeScript", 25317, 2776,
     "astryx：Meta 开源的设计系统——在 Meta 内部生长八年、支撑 13,000+ 应用后走向开源（Beta）；提供 150+ 无障碍组件、品牌级主题、暗色模式与 CLI，API 与文档专为「人和 AI 智能体用同一套工具协同开发」而设计。连续第四日在榜且今日继续登顶涨幅榜，累计 Star 25,317。"),
    ("ZhuLinsen/daily_stock_analysis", "https://github.com/ZhuLinsen/daily_stock_analysis", "Python", 70504, 278,
     "daily_stock_analysis：LLM 驱动的多市场股票智能分析系统——多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。回归项目（上次 11-10），累计 Star 70,504（7 万+）。"),
    ("GoogleChrome/modern-web-guidance-src", "https://github.com/GoogleChrome/modern-web-guidance-src", "TypeScript", 1913, 159,
     "modern-web-guidance-src：Chrome、Edge、Firefox 与 MDN 四方团队联合维护的「现代 Web 指南」源仓库——把 Web 平台专业知识、最佳实践与浏览器兼容性数据打包成可安装的智能体技能（npx 一键安装），纠正编程智能体因训练数据充满遗留代码而默认生成过时模式的问题。浏览器厂商联合下场做智能体技能的新面孔，首次登榜，累计 Star 1,913。"),
    ("shadcn/improve", "https://github.com/shadcn/improve", "", 11053, 361,
     "improve：shadcn（shadcn/ui 作者）出品的智能体技能——用你最强的模型审计代码库、判断什么值得做、写出实现规格，再把执行交给更便宜的模型；「技能本身不实现任何东西，计划就是产品」。兼容 Agent Skills 开放标准，产出纯 markdown 计划可被任意智能体接手。新面孔首次登榜，累计 Star 11,053（trending 页未标注语言）。"),
    ("addyosmani/agent-skills", "https://github.com/addyosmani/agent-skills", "JavaScript", 116066, 787,
     "agent-skills：Addy Osmani（Google Chrome 团队工程负责人、《Learning JavaScript Design Patterns》作者）开源的面向 AI 编程智能体的生产级工程技能集——把资深工程师的代码审查、测试、架构等工程实践封装成可安装的智能体技能。连续第三日在榜，累计 Star 116,066（11 万+）。"),
    ("vercel-labs/agent-browser", "https://github.com/vercel-labs/agent-browser", "Rust", 49983, 708,
     "agent-browser：Vercel Labs 出品的面向 AI 智能体的浏览器自动化 CLI——让智能体像操控桌面一样操控浏览器。「给智能体一台浏览器」赛道连续第四日在榜，累计 Star 49,983——距 5 万里程碑仅差 17 星。"),
    ("we-promise/sure", "https://github.com/we-promise/sure", "Ruby", 13102, 1078,
     "sure：「属于所有人、由所有人构建」的社区驱动个人理财应用——开源记账与财务规划工具。连续第二日在榜且今日冲至涨幅第二，累计 Star 13,102。"),
    ("homeassistant-ai/ha-mcp", "https://github.com/homeassistant-ai/ha-mcp", "Python", 7465, 645,
     "ha-mcp：Home Assistant MCP 服务器——用 Claude、ChatGPT 等 AI 助手配置和自动化智能家居，提供 87 个工具，基于 FastMCP 构建。智能家居 × AI 官方组织仓库连续第三日在榜，累计 Star 7,465。"),
    ("openai/codex-security", "https://github.com/openai/codex-security", "TypeScript", 11856, 52,
     "codex-security：OpenAI 出品的 Codex Security CLI 与 TypeScript SDK——用 AI 查找、验证并修复代码中的安全漏洞，npm 提供 @openai/codex-security 包。AI 安全工具链新面孔首次登榜，累计 Star 11,856。"),
    ("TheAlgorithms/Java", "https://github.com/TheAlgorithms/Java", "Java", 67096, 51,
     "TheAlgorithms/Java：经典开源算法教学仓库——Java 实现的全套算法与数据结构集合（TheAlgorithms 组织旗下）。111 期简报以来的新面孔首次登榜（经典长青项目回暖），累计 Star 67,096。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体技能生态": ["agent-skills", "improve", "modern-web-guidance"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"ZhuLinsen/daily_stock_analysis", "GoogleChrome/modern-web-guidance-src",
            "shadcn/improve", "addyosmani/agent-skills", "vercel-labs/agent-browser",
            "homeassistant-ai/ha-mcp", "openai/codex-security"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer vs raw #1 (today they AGREE again).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（Meta 设计系统连续第四日在榜、连续两日登顶涨幅榜）。GitHub 原始榜单首位同样是 meta/astryx（+{top[4]:,}）——<b>今日两者再次一致</b>；但仍提醒：GitHub 榜单排序并非按当日涨幅（如原始第 7 位 sure 有 +1,078，而原始第 9 位 codex-security 仅 +52），本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{top_langs[0]} 以 {maxc}/{len(repos)} 居首</b>：astryx、modern-web-guidance-src 与 codex-security 三席；其余分布：{others}，共 {len(lang_stats)} 类（shadcn/improve 未标注语言，trending 页语言栏为空），全部已内置色表，无 #888888 缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：astryx（+{top[4]:,}）、sure（+{second[4]:,}）与 agent-skills（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；astryx 单仓库即占 <b>{int(round(top[4] / total_today * 100))}%</b>，长尾由 TheAlgorithms/Java 的 +51 收尾。</li>')

    delta_pct = int(round(abs(total_today - 12153) / 12153 * 100))
    ins.append(f'<li><b>热度明显回落</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-11（+12,153 / 12 个仓库）回落约 <b>{delta_pct}%</b>，为 11 月以来较低水位；除 astryx 一枝独秀外整体增量分布平缓（无其他单日 +1,500 以上项目）。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'设计系统本体，dbx 先例' if 'astryx' in r[0] else '个人理财应用' if '/sure' in r[0] else '算法教学集合'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 3 个为 {non_ai_txt}（modern-web-guidance-src 经 README 核对：Chrome/Edge/Firefox/MDN 联合出品、面向编程智能体的技能包，判为 AI；improve 为「强模型规划、便宜模型执行」的智能体技能）。</li>')

    ins.append('<li><b>新面孔 4 个、回归 1 个、延续 5 个、掉榜 7 个</b>：新进 <b>modern-web-guidance-src</b>（浏览器四厂商联合的智能体 Web 技能）、<b>shadcn/improve</b>（审计出计划的智能体技能）、<b>openai/codex-security</b>（OpenAI 安全 CLI）、<b>TheAlgorithms/Java</b>（111 期以来首现的经典算法库）；回归 <b>daily_stock_analysis</b>（上次 11-10，LLM 股票分析）；上期 12 个仓库中 5 个延续（astryx、sure、agent-skills、agent-browser、ha-mcp），掉榜 sherlock、anthropics/skills、mattpocock/skills、claude-quickstarts、mujoco、billion-context、topcoat。</li>')

    ins.append('<li><b>主题观察：「智能体技能层」从社区扩散到厂商官方</b>——① <b>厂商下场</b>：modern-web-guidance-src 由 Chrome、Edge、Firefox、MDN 四方团队联合 steward，把 Web 平台最佳实践直接装进编程智能体，标志「智能体技能」正式成为浏览器厂商的一等交付物；② <b>个人范式</b>：shadcn/improve 确立「聪明模型做规划、便宜模型做执行」的分工哲学——计划即产品；③ <b>安全工具链</b>：openai/codex-security 代表 AI 从写代码走向审计与修复代码；④ <b>生活应用</b>：sure（理财）与 ha-mcp（智能家居 × AI）延续「开源走进日常」主线；⑤ <b>经典回暖</b>：TheAlgorithms/Java 作为教学常青树首现榜单。</li>')

    ins.append('<li><b>里程碑与体量</b>：addyosmani/agent-skills 达 <b>116,066</b>（11 万+）为今日全榜体量之最；daily_stock_analysis 站上 <b>70,504</b>（7 万+）；agent-browser <b>49,983</b> 距 5 万里程碑仅差 17 星，明日大概率破线；astryx 25,317 四日在榜翻倍节奏；TheAlgorithms/Java 以 67,096 展示经典项目的长青热度。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 12)
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
