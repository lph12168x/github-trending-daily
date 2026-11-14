#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-14 (v101).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded via --resolve 140.82.116.3 fallback:
rc=0, 551,685 bytes, complete document ending in </html>, exactly
12 Box-row articles. Freshness verified: saved-file mtime 12:35 >
pre-fetch start 12:35:0x.
Cross-check: independent WebFetch (?since=daily) returned the SAME 12
repos, SAME order, SAME stars-today values (215/1925/751/256/925/108/
71/97/69/256/256/67). Total raw = +4,996 on both views. Cumulative
star counts: report uses the curl values (freshest).

CONTENT NOTE
------------
No political-sensitivity issues. No circumvention tools: tailscale/
tailcat is a netcat-style network utility over Tailscale's own
WireGuard data plane (open-source plumbing, not an access-
circumvention product), included. All 12 repos included, +4,996 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (8/12):
  * GoogleChrome/modern-web-guidance-src -- coding-agent skill pack
        (11-12/11-13 precedent).
  * openai/codex-security                -- OpenAI official AI security
        CLI/SDK.
  * ZhuLinsen/daily_stock_analysis       -- LLM-driven stock analysis.
  * alibaba/open-code-review             -- code review tool whose core
        is "deterministic pipelines + LLM Agent" (LLM integral to the
        product, not an incidental mention).
  * backnotprop/plannotator              -- annotation/review workspace
        for coding agents (Claude Code/Codex/Copilot/Gemini).
  * block/buzz                           -- self-hostable workspace
        where humans and AI agents build together (README verified).
  * tradermonty/claude-trading-skills    -- Claude Code skills for
        traders.
  * ChromeDevTools/chrome-devtools-mcp   -- Chrome DevTools MCP for
        coding agents.
NOT counted (4):
  * we-promise/sure       -- personal finance app.
  * tailscale/tailcat     -- netcat-style network utility, no AI.
  * Likely7/Veyra-NRVideo -- Windows video player/enhancer (AI super
        resolution is a bundled feature, not the core; astryx/dbx
        precedent).
  * louislam/uptime-kuma  -- self-hosted monitoring, no AI.

NEW / RETURNING / DROPPED (vs 2026-11-13, v100)
-----------------------------------------------
Continuations (4): modern-web-guidance-src, codex-security, sure,
  daily_stock_analysis.
Returning (3): alibaba/open-code-review (last 10-10), block/buzz
  (last 08-24), ChromeDevTools/chrome-devtools-mcp (last 09-03).
New faces (5): backnotprop/plannotator, louislam/uptime-kuma,
  tradermonty/claude-trading-skills, tailscale/tailcat,
  Likely7/Veyra-NRVideo (all first appearance in this automation's
  records; uptime-kuma at 93.9k stars is the most notable first-timer).
Dropped (9): meta/astryx, addyosmani/agent-skills,
  Alishahryar1/free-claude-code, CopilotKit/OpenBot,
  pookjw/HermesEnabler, QwenLM/qwen-code, ashhart/TensorFold,
  nodejs/node, ggml-org/llama.cpp.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-14"
TODAY_FMT = "2026年11月14日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 12 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("alibaba/open-code-review", "https://github.com/alibaba/open-code-review", "Go", 50771, 215,
     "open-code-review：阿里巴巴出品的混合架构代码评审工具——确定性流水线 + LLM Agent 双引擎，行级精确评论，内置多语言规则集（NPE、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic 接口，在阿里规模上久经考验。回归项目（上次 10-10），今日恰为 GitHub 原始榜单首位，累计 Star 50,771。"),
    ("GoogleChrome/modern-web-guidance-src", "https://github.com/GoogleChrome/modern-web-guidance-src", "TypeScript", 5006, 1925,
     "modern-web-guidance-src：Google Chrome 团队出品的「Web 最佳实践」智能体技能包——Chrome/Edge/Firefox/MDN 四方联合，把最新 Web 平台最佳实践整理成编码智能体可直接消费的技能源数据，让 AI 编码助手始终跟上 Web 标准。连续第三日在榜，今日以 +1,925 首次登顶涨幅榜，累计 Star 5,006。"),
    ("openai/codex-security", "https://github.com/openai/codex-security", "TypeScript", 13215, 751,
     "codex-security：OpenAI 官方的 Codex Security CLI 与 TypeScript SDK——用 AI 帮助发现、验证并修复代码安全漏洞，npm 包 @openai/codex-security 一键安装。官方安全工具延续在榜，累计 Star 13,215。"),
    ("ZhuLinsen/daily_stock_analysis", "https://github.com/ZhuLinsen/daily_stock_analysis", "Python", 71770, 256,
     "daily_stock_analysis：LLM 驱动的多市场股票智能分析系统——多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。延续在榜（回归后连续第三日），累计 Star 71,770；Fork 57,339，Fork/Star 比高达 0.80 依旧异常（疑似刷量延续观察）。"),
    ("we-promise/sure", "https://github.com/we-promise/sure", "Ruby", 14836, 925,
     "sure：人人共建的个人财务 App（The personal finance app for everyone, by everyone）——Ruby on Rails 自托管开源理财应用，社区驱动开发。延续在榜（11-11 首登），今日 +925 位居涨幅榜第二，累计 Star 14,836。"),
    ("backnotprop/plannotator", "https://github.com/backnotprop/plannotator", "TypeScript", 10527, 108,
     "plannotator：编码智能体的「批注工作台」——收件箱统一跟进智能体动态，可对计划/规格/Markdown/HTML 等工件划词批注，审查 diff 与 PR，一键把反馈发回智能体；原生支持 Claude Code、Codex、Copilot CLI、Gemini CLI 等。新面孔首次登榜，累计 Star 10,527。"),
    ("louislam/uptime-kuma", "https://github.com/louislam/uptime-kuma", "JavaScript", 93922, 71,
     "uptime-kuma：最流行的自托管监控工具——界面精美、支持 HTTP/TCP/DNS 等多种探测方式的开源 Uptime 监控。老牌明星项目在本自动化全部记录中首次登榜，累计 Star 93,922，距 10 万里程碑仅差约 6 千。"),
    ("block/buzz", "https://github.com/block/buzz", "Rust", 37331, 97,
     "buzz：Block（Jack Dorsey 旗下）出品的「蜂群」协作平台——人类与 AI 智能体在同一房间共建的自托管工作区，跑在你自有的中继上，频道/线程里人与智能体协同推进项目。回归项目（上次 08-24），累计 Star 37,331。"),
    ("tradermonty/claude-trading-skills", "https://github.com/tradermonty/claude-trading-skills", "Python", 4256, 69,
     "claude-trading-skills：面向股票投资者与交易员的 Claude Code 技能集——市场分析、技术图表、经济日历、选股筛选器等专业技能包，把编码智能体改造成投研助手。新面孔首次登榜，累计 Star 4,256。"),
    ("tailscale/tailcat", "https://github.com/tailscale/tailcat", "Go", 9528, 256,
     "tailcat：Tailscale 官方出品的 netcat 网络瑞士军刀——复用 Tailscale 开源数据平面（magicsock），在两台机器间建立 WireGuard 加密的点对点隧道（DERP 打洞兜底），但完全不依赖 Tailscale 控制平面，连接元数据带外交换。纯网络工具（非访问规避类），新面孔首次登榜，累计 Star 9,528。"),
    ("Likely7/Veyra-NRVideo", "https://github.com/Likely7/Veyra-NRVideo", "C++", 1683, 256,
     "Veyra-NRVideo：Windows 视频播放与采集增强工具——实时预览、AI 超分辨率、DLSS 5 帧生成，主打「把 PS5 上的 GTA6 提到 120FPS」。新面孔首次登榜，累计 Star 1,683。"),
    ("ChromeDevTools/chrome-devtools-mcp", "https://github.com/ChromeDevTools/chrome-devtools-mcp", "TypeScript", 55582, 67,
     "chrome-devtools-mcp：Chrome DevTools 官方 MCP 服务器——让编码智能体直接驱动浏览器进行调试、性能分析与页面检查。回归项目（上次 09-03），累计 Star 55,582。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "给智能体一块可视化工作台": ["plannotator", "buzz", "chrome-devtools-mcp"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"GoogleChrome/modern-web-guidance-src", "openai/codex-security",
            "ZhuLinsen/daily_stock_analysis", "alibaba/open-code-review",
            "backnotprop/plannotator", "block/buzz",
            "tradermonty/claude-trading-skills", "ChromeDevTools/chrome-devtools-mcp"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top (modern-web) != raw #1 (open-code-review).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第三日在榜且首次登顶涨幅榜。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，今日第 7）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：TypeScript 包揽 modern-web-guidance-src、codex-security、plannotator、chrome-devtools-mcp 四席；其余分布：{others}，共 {len(lang_stats)} 种语言。均为常见语言，无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：modern-web-guidance-src（+{top[4]:,}）、sure（+{second[4]:,}）与 codex-security（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 chrome-devtools-mcp 的 +67 收尾，与 +256 的三连并列形成中间梯队。</li>')

    delta_pct = int(round(abs(total_today - 6432) / 6432 * 100))
    ins.append(f'<li><b>热度跌破 5K，创 11 月新低</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-13（+6,432 / 13 个仓库）回落约 <b>{delta_pct}%</b>，连续第三日下行（11-12 +6,895 → 11-13 +6,432 → 今日 +4,996），仅为 11-10 高水位（+13,136）的约 38%。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'个人理财 App' if 'sure' in r[0] else 'netcat 类网络工具' if 'tailcat' in r[0] else 'Windows 视频工具' if 'Veyra' in r[0] else '自托管监控'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 4 个为 {non_ai_txt}。口径说明：open-code-review 的 LLM Agent 是产品核心引擎而非附带提及，故计入；Veyra-NRVideo 的 AI 超分辨率是捆绑功能而非本体，参照 astryx/dbx 先例不计入。</li>')

    ins.append('<li><b>新面孔 5 个、回归 3 个、延续 4 个、掉榜 9 个</b>：新进 <b>plannotator</b>（智能体批注工作台）、<b>uptime-kuma</b>（9.4 万星老牌监控，全记录首次登榜）、<b>claude-trading-skills</b>（交易员 Claude 技能集）、<b>tailcat</b>（Tailscale 版 netcat）、<b>Veyra-NRVideo</b>（DLSS 5 视频增强）；回归 <b>open-code-review</b>（上次 10-10）、<b>buzz</b>（上次 08-24）、<b>chrome-devtools-mcp</b>（上次 09-03）；延续 modern-web-guidance-src、codex-security、sure、daily_stock_analysis。上期 13 个仓库中多达 9 个掉榜（astryx、agent-skills、free-claude-code、OpenBot、HermesEnabler、qwen-code、TensorFold、nodejs/node、llama.cpp），换手率 75% 为近期最高。</li>')

    ins.append('<li><b>主题观察：智能体的「工作界面」从终端走向可视化工作台</b>——① <b>plannotator</b> 把智能体的计划/规格/PR 变成可划词批注的工件，一键回传反馈；② <b>buzz</b>（Block 官方）让人与智能体在同一房间频道里共建项目；③ <b>chrome-devtools-mcp</b> 回归，官方把浏览器调试能力交给智能体。三者共同指向：智能体协作正在长出自己的 GUI 层。另一条支线是<b>金融 AI 双仓库同榜</b>：daily_stock_analysis（多市场股票分析系统）与 claude-trading-skills（交易员技能集），LLM 投研工具持续升温；基础设施侧则由 tailcat（官方开源数据平面玩具）与 uptime-kuma（老牌监控首登）镇场。</li>')

    ins.append('<li><b>里程碑观察</b>：今日无 10 万+ 星仓库同榜（昨日三座盛况不再）；uptime-kuma <b>93,922</b> 逼近 10 万大关；daily_stock_analysis <b>71,770</b> 稳居 7 万档但 Fork/Star 比 0.80 的异常依旧；chrome-devtools-mcp <b>55,582</b>、open-code-review <b>50,771</b> 双双站上 5 万档。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 14)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).

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
