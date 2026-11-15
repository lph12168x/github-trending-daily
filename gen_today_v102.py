#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-15 (v102).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded via plain-DNS direct connection:
rc=0, 584,991 bytes, complete document ending in </html>, exactly
15 Box-row articles. Freshness verified: saved-file mtime 12:31:57 >
pre-fetch start 12:31. NOTE: the fetch script's TSV columns are
name / lang / total_stars / forks / today_stars (forks before today).
Cross-check: independent WebFetch (?since=daily) returned the SAME 15
repos, SAME order, SAME stars-today values (408/1231/553/664/893/64/
495/9/37/227/430/659/33/420/270). Total = +6,393 on both views.
Cumulative star counts: report uses the curl values (freshest).

CONTENT NOTE
------------
No political-sensitivity issues. No circumvention tools: airgorah is a
WiFi security-auditing tool for authorized pentesting (sherlock
precedent), included. All 15 repos included, +6,393 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (10/15):
  * backnotprop/plannotator            -- annotation workspace for coding
        agents (11-14 precedent).
  * GoogleChrome/modern-web-guidance-src -- coding-agent skill pack
        (11-12/11-13/11-14 precedent).
  * tradermonty/claude-trading-skills  -- Claude Code skills for traders.
  * ChromeDevTools/chrome-devtools-mcp -- MCP for coding agents.
  * alibaba/open-code-review           -- LLM Agent integral to the
        product (11-14 precedent).
  * QwenLM/qwen-code                   -- Qwen official AI coding agent
        CLI (11-13 precedent).
  * ag-ui-protocol/ag-ui               -- Agent-User Interaction Protocol.
  * ashhart/TensorFold                 -- LLM inference engine (11-13
        precedent: LLM-dedicated engines count).
  * JuliusBrussee/caveman              -- token-cutting skill + proxy for
        coding agents.
  * Tencent/LoopForge                  -- orchestration of coding-agent
        delivery (CodeBuddy/Codex/Claude Code) with human approval gates.
NOT counted (5):
  * dream-num/univer       -- Office SDK (Sheets/Docs engine) at its
        core; README verified: "Build your own AI office ... connect
        your own application or agent". AI is the positioning, the body
        is a document engine (dbx precedent).
  * louislam/uptime-kuma   -- self-hosted monitoring, no AI.
  * we-promise/sure        -- personal finance app.
  * Likely7/Veyra-NRVideo  -- Windows video player/enhancer (AI super
        resolution is a bundled feature, not the core; astryx/dbx
        precedent).
  * martin-olivier/airgorah -- WiFi security auditing, no AI.

NEW / RETURNING / DROPPED (vs 2026-11-14, v101)
-----------------------------------------------
Continuations (8): plannotator, modern-web-guidance-src,
  claude-trading-skills, chrome-devtools-mcp, open-code-review,
  uptime-kuma, sure, Veyra-NRVideo.
Returning (2): QwenLM/qwen-code (last 11-13), ashhart/TensorFold
  (last 11-13).
New faces (5): dream-num/univer, ag-ui-protocol/ag-ui,
  JuliusBrussee/caveman, Tencent/LoopForge, martin-olivier/airgorah
  (all first appearance in this automation's records).
Dropped (4): openai/codex-security, ZhuLinsen/daily_stock_analysis,
  block/buzz, tailscale/tailcat.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-15"
TODAY_FMT = "2026年11月15日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 15 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("backnotprop/plannotator", "https://github.com/backnotprop/plannotator", "TypeScript", 11260, 408,
     "plannotator：编码智能体的「批注工作台」——收件箱统一跟进智能体动态，可对计划/规格/Markdown/HTML 等工件划词批注，审查 diff 与 PR，一键把反馈发回智能体；原生支持 Claude Code、Codex、Copilot CLI、Gemini CLI 等。连续第二日在榜，今日跃居 GitHub 原始榜单首位，累计 Star 11,260。"),
    ("GoogleChrome/modern-web-guidance-src", "https://github.com/GoogleChrome/modern-web-guidance-src", "TypeScript", 6208, 1231,
     "modern-web-guidance-src：Google Chrome 团队出品的「Web 最佳实践」智能体技能包——Chrome/Edge/Firefox/MDN 四方联合，把最新 Web 平台最佳实践整理成编码智能体可直接消费的技能源数据，让 AI 编码助手始终跟上 Web 标准。连续第四日在榜并蝉联涨幅榜首（+1,231），累计 Star 6,208。"),
    ("tradermonty/claude-trading-skills", "https://github.com/tradermonty/claude-trading-skills", "Python", 4925, 553,
     "claude-trading-skills：面向股票投资者与交易员的 Claude Code 技能集——市场分析、技术图表、经济日历、选股筛选器等专业技能包，把编码智能体改造成投研助手。连续第二日在榜，累计 Star 4,925。"),
    ("ChromeDevTools/chrome-devtools-mcp", "https://github.com/ChromeDevTools/chrome-devtools-mcp", "TypeScript", 56389, 664,
     "chrome-devtools-mcp：Chrome DevTools 官方 MCP 服务器——让编码智能体直接驱动浏览器进行调试、性能分析与页面检查。回归后连续第二日在榜，累计 Star 56,389。"),
    ("alibaba/open-code-review", "https://github.com/alibaba/open-code-review", "Go", 51514, 893,
     "open-code-review：阿里巴巴出品的混合架构代码评审工具——确定性流水线 + LLM Agent 双引擎，行级精确评论，内置多语言规则集（NPE、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic 接口，在阿里规模上久经考验。回归后连续第二日在榜，累计 Star 51,514。"),
    ("QwenLM/qwen-code", "https://github.com/QwenLM/qwen-code", "TypeScript", 30397, 64,
     "qwen-code：Qwen 官方开源的终端 AI 编码智能体——开源 CLI，原生驻留你的终端。回归项目（上次 11-13），累计 Star 30,397。"),
    ("dream-num/univer", "https://github.com/dream-num/univer", "TypeScript", 25013, 495,
     "univer：Univer Office SDK——开源办公套件引擎，以 Sheets/Docs 为核心，把编辑、计算、协作与文件处理能力嵌入自家产品，官方定位「为你和 AI 智能体打造 AI 办公」；本体是可扩展的文档/表格引擎。新面孔首次登榜，累计 Star 25,013。"),
    ("ag-ui-protocol/ag-ui", "https://github.com/ag-ui-protocol/ag-ui", "TypeScript", 17424, 9,
     "ag-ui：Agent-User Interaction Protocol——把 AI 智能体接入前端应用的标准化交互协议，为智能体 UI 提供事件流状态同步与渲染契约。新面孔首次登榜，累计 Star 17,424。"),
    ("ashhart/TensorFold", "https://github.com/ashhart/TensorFold", "Zig", 2185, 37,
     "TensorFold：面向 Metal、CUDA 与 Vulkan 的 LLM 推理引擎——Zig 编写的新生推理框架，一套实现同时覆盖苹果、英伟达与跨厂商三大计算后端。回归项目（上次 11-13），累计 Star 2,185。"),
    ("JuliusBrussee/caveman", "https://github.com/JuliusBrussee/caveman", "Go", 120136, 227,
     "caveman：「🪨 why use many token when few token do trick」——病毒式出圈的编码智能体技能 + 代理，让智能体改说「原始人语」以砍掉约 65% 的 token 开销。上榜即破 10 万星，累计 Star 120,136，为今日唯一 10 万+ 仓库。"),
    ("louislam/uptime-kuma", "https://github.com/louislam/uptime-kuma", "JavaScript", 94297, 430,
     "uptime-kuma：最流行的自托管监控工具——界面精美、支持 HTTP/TCP/DNS 等多种探测方式的开源 Uptime 监控。连续第二日在榜，累计 Star 94,297，距 10 万里程碑仅差约 5,700。"),
    ("we-promise/sure", "https://github.com/we-promise/sure", "Ruby", 15389, 659,
     "sure：人人共建的个人财务 App（The personal finance app for everyone, by everyone）——Ruby on Rails 自托管开源理财应用，社区驱动开发。连续第三日在榜，今日 +659 位居涨幅榜第四，累计 Star 15,389。"),
    ("Tencent/LoopForge", "https://github.com/Tencent/LoopForge", "Go", 976, 33,
     "LoopForge：腾讯官方出品的编码智能体交付工作流引擎——自托管编排 CodeBuddy、Codex 与 Claude Code，以脚本与人工审批门（human approval gates）串起智能体交付流水线，并为本地编码助手提供本地 workflow。新面孔首次登榜，累计 Star 976。"),
    ("Likely7/Veyra-NRVideo", "https://github.com/Likely7/Veyra-NRVideo", "C++", 2351, 420,
     "Veyra-NRVideo：Windows 视频播放与采集增强工具——实时预览、AI 超分辨率、DLSS 5 帧生成，主打「把 PS5 上的 GTA6 提到 120FPS」。连续第二日在榜，累计 Star 2,351。"),
    ("martin-olivier/airgorah", "https://github.com/martin-olivier/airgorah", "Rust", 5964, 270,
     "airgorah：WiFi 安全审计软件——Rust 编写的无线网络安全审计工具，面向授权渗透测试场景。新面孔首次登榜，累计 Star 5,964。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体交付流水线（编排/协议/界面/成本）": ["LoopForge", "ag-ui"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"backnotprop/plannotator", "GoogleChrome/modern-web-guidance-src",
            "tradermonty/claude-trading-skills", "ChromeDevTools/chrome-devtools-mcp",
            "alibaba/open-code-review", "QwenLM/qwen-code",
            "ag-ui-protocol/ag-ui", "ashhart/TensorFold",
            "JuliusBrussee/caveman", "Tencent/LoopForge"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top (modern-web) != raw #1 (plannotator).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第四日在榜、蝉联涨幅榜首。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，今日第 9）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：TypeScript 包揽 plannotator、modern-web-guidance-src、chrome-devtools-mcp、qwen-code、univer、ag-ui 六席；其余分布：{others}，共 {len(lang_stats)} 种语言。Zig 为 v26 引擎缺色语言，脚本内已补色（#EC915C），无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：modern-web-guidance-src（+{top[4]:,}）、open-code-review（+{second[4]:,}）与 chrome-devtools-mcp（+{third[4]:,}) 领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>，分布较前几日更均衡；长尾由 ag-ui 的 +9 收尾。</li>')

    delta_pct = int(round(abs(total_today - 4996) / 4996 * 100))
    ins.append(f'<li><b>热度回暖，重回 6K 档</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-14（+4,996 / 12 个仓库）回升约 <b>{delta_pct}%</b>；三日走势 11-13 +6,432 → 11-14 +4,996 → 今日 +6,393，止住连续下行，但仍是 11-10 高水位（+13,136）的约一半。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'Office SDK 本体，AI 为定位非核心' if 'univer' in r[0] else '自托管监控' if 'uptime' in r[0] else '个人理财 App' if 'sure' in r[0] else 'Windows 视频工具' if 'Veyra' in r[0] else 'WiFi 安全审计'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 5 个为 {non_ai_txt}。口径说明：TensorFold 沿用「LLM 专用推理引擎计入」（11-13 先例）；LoopForge 因编排对象即编码智能体（CodeBuddy/Codex/Claude Code）且设人工审批门而计入；univer 经 README 核对为本体文档引擎、AI 办公仅为定位，参照 dbx 先例不计入。</li>')

    ins.append('<li><b>新面孔 5 个、回归 2 个、延续 8 个、掉榜 4 个</b>：新进 <b>caveman</b>（病毒式 token 砍削技能，上榜即 12 万星）、<b>univer</b>（AI 办公 SDK）、<b>ag-ui</b>（智能体↔前端交互协议）、<b>LoopForge</b>（腾讯官方智能体编排）、<b>airgorah</b>（WiFi 安全审计）；回归 <b>qwen-code</b> 与 <b>TensorFold</b>（均上次 11-13）；延续 plannotator、modern-web-guidance-src、claude-trading-skills、chrome-devtools-mcp、open-code-review、uptime-kuma、sure、Veyra-NRVideo。上期掉榜：codex-security、daily_stock_analysis、buzz、tailcat，换手率 33%。</li>')

    ins.append('<li><b>主题观察：智能体「交付流水线」各层今日同榜</b>——① <b>LoopForge</b>（腾讯官方）做编排：串起 CodeBuddy/Codex/Claude Code 并设人工审批门；② <b>ag-ui</b> 做协议：定义智能体↔前端的事件流交互契约；③ <b>plannotator</b> 做界面：批注工作台一键回传反馈；④ <b>caveman</b> 管成本：号称砍 65% token。从编排、协议、界面到成本控制，智能体工程化栈一字排开。官方阵营同样密集：GoogleChrome、ChromeDevTools、alibaba、QwenLM、Tencent 五家大厂仓库同榜。</li>')

    ins.append('<li><b>里程碑观察</b>：caveman <b>120,136</b> 为今日唯一 10 万+ 星仓库（上榜即破 10 万的病毒式样本）；uptime-kuma <b>94,297</b> 距 10 万大关约 5,700；chrome-devtools-mcp <b>56,389</b> 与 open-code-review <b>51,514</b> 双双站稳 5 万档；LoopForge 上榜首日仅 <b>976</b> 星，为今日最小体量、值得跟踪的腾讯系新项。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 15)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).
    base.LANG_COLORS.update({"Zig": "#EC915C"})

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
