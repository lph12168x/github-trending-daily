#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-13 (v100).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain-DNS direct
connection: rc=0, 561,718 bytes, complete document ending in </html>,
exactly 13 Box-row articles. Freshness verified: saved-file mtime
12:31:19 > pre-fetch start 12:31:0x.
Cross-check: independent WebFetch (?since=daily) returned the SAME 13
repos, SAME order, SAME stars-today values (739/643/63/218/967/151/54/
62/816/1830/298/415/176). Total raw = +6,432 on both views. Cumulative
star counts: report uses the curl values (freshest).

CONTENT NOTE
------------
jailbreaks and heretic are NOT on today's list (no action needed). No
political-sensitivity issues, no circumvention tools among the 13.
Alishahryar1/free-claude-code README re-verified via Contents API raw:
it is a multi-harness -> 61-provider model ROUTER that explicitly
"follows provider TOS and removes integrations if they stop being
allowed" -- NOT a circumvention tool (10-13 precedent), included.
pookjw/HermesEnabler is Apple Watch face customization (device feature
enablement, not access circumvention), included.
All 13 repos included, +6,432 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (8/13):
  * GoogleChrome/modern-web-guidance-src -- Chrome/Edge/Firefox/MDN
        joint skill pack FOR coding agents (11-12 precedent: judged AI).
  * openai/codex-security                -- OpenAI official AI security
        CLI/SDK for finding & fixing vulnerabilities.
  * QwenLM/qwen-code                     -- Qwen official AI coding
        agent CLI.
  * ashhart/TensorFold                   -- LLM-dedicated inference
        engine (BitNet/tokenspeed precedent: LLM-specific inference
        counts, unlike general tensor frameworks such as PyTorch).
  * addyosmani/agent-skills              -- production-grade skills for
        AI coding agents.
  * CopilotKit/OpenBot                   -- AI coworkers, each agent
        gets its own computer.
  * Alishahryar1/free-claude-code        -- coding-agent model router
        (10-13 precedent: counted as Agent ecosystem).
  * ggml-org/llama.cpp                   -- LLM-dedicated inference
        engine (BitNet/tokenspeed precedent).
NOT counted (5), with precedent:
  * nvm-sh/nvm            -- Node version manager, no AI.
  * pookjw/HermesEnabler  -- Apple Watch face enabler, no AI.
  * we-promise/sure       -- personal finance app, no AI.
  * nodejs/node           -- JS runtime, no AI.
  * meta/astryx           -- design system at its core; "agent ready"
                             is a property (dbx precedent, 11-09/11-11/
                             11-12).

NEW / RETURNING / DROPPED (vs 2026-11-12, v99)
----------------------------------------------
Continuations (5): modern-web-guidance-src, codex-security, sure,
  addyosmani/agent-skills, meta/astryx (3rd day).
Returning (3): nvm-sh/nvm (last 10-15), CopilotKit/OpenBot (last
  11-02), Alishahryar1/free-claude-code (last 10-13).
New faces (5): pookjw/HermesEnabler, QwenLM/qwen-code,
  ashhart/TensorFold, nodejs/node, ggml-org/llama.cpp (all first
  appearance in this automation's records).
Dropped (5): improve, TheAlgorithms/Java, daily_stock_analysis,
  ha-mcp, vercel-labs/agent-browser.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-13"
TODAY_FMT = "2026年11月13日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 13 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("GoogleChrome/modern-web-guidance-src", "https://github.com/GoogleChrome/modern-web-guidance-src", "TypeScript", 3378, 739,
     "modern-web-guidance-src：Google Chrome 团队出品的「Web 最佳实践」智能体技能包——Chrome/Edge/Firefox/MDN 四方联合，把最新 Web 平台最佳实践整理成编码智能体可直接消费的技能源数据，让 AI 编码助手始终跟上 Web 标准。延续在榜（昨日首登），累计 Star 3,378。"),
    ("openai/codex-security", "https://github.com/openai/codex-security", "TypeScript", 12576, 643,
     "codex-security：OpenAI 官方的 Codex Security CLI 与 TypeScript SDK——用 AI 帮助发现、验证并修复代码安全漏洞，npm 包 @openai/codex-security 一键安装。官方安全工具延续在榜，累计 Star 12,576。"),
    ("nvm-sh/nvm", "https://github.com/nvm-sh/nvm", "Shell", 96041, 63,
     "nvm：Node Version Manager——POSIX 兼容的 bash 脚本，管理多个活跃的 node.js 版本，Node 生态最经典的基础设施。老牌项目回归（上次 10-15），累计 Star 96,041，距 10 万里程碑仅差约 4 千。"),
    ("pookjw/HermesEnabler", "https://github.com/pookjw/HermesEnabler", "Objective-C", 1604, 218,
     "HermesEnabler：在任意 Apple Watch 设备上启用爱马仕（Hermès）官方表盘——Objective-C 小工具，让未购联名款手表也能用上奢侈品牌表盘。小而美的苹果生态新面孔首次登榜，累计 Star 1,604。"),
    ("we-promise/sure", "https://github.com/we-promise/sure", "Ruby", 14074, 967,
     "sure：人人共建的个人财务 App（The personal finance app for everyone, by everyone）——Ruby on Rails 自托管开源理财应用，社区驱动开发。延续在榜（11-11 首登），今日 +967 位居榜单第二，累计 Star 14,074。"),
    ("QwenLM/qwen-code", "https://github.com/QwenLM/qwen-code", "TypeScript", 29915, 151,
     "qwen-code：阿里 Qwen 团队的开源 AI 编码智能体——常驻终端的编码 CLI，Qwen 大模型官方命令行工具。本自动化记录中首次登榜，累计 Star 29,915。"),
    ("ashhart/TensorFold", "https://github.com/ashhart/TensorFold", "Zig", 1992, 54,
     "TensorFold：面向 Metal、CUDA 与 Vulkan 的 LLM 推理引擎——Zig 编写的新生推理框架，一套实现同时覆盖苹果、英伟达与跨厂商三大计算后端。新面孔首次登榜，累计 Star 1,992。"),
    ("nodejs/node", "https://github.com/nodejs/node", "JavaScript", 123626, 62,
     "Node.js：全球最知名的 JavaScript 服务端运行时本体——标杆级开源基础设施罕见登榜。本自动化记录中首次上榜，累计 Star 123,626。"),
    ("addyosmani/agent-skills", "https://github.com/addyosmani/agent-skills", "JavaScript", 116783, 816,
     "agent-skills：Addy Osmani（Google Chrome 工程领导）维护的生产级 AI 编码智能体工程技能集——为 AI 编码智能体提供可安装的实战技能包。智能体技能层延续在榜，累计 Star 116,783。"),
    ("meta/astryx", "https://github.com/meta/astryx", "TypeScript", 26761, 1830,
     "astryx：Meta 官方开源设计系统——内部生长八年、支撑 13,000+ 应用后开源（Beta），150+ 无障碍组件、品牌级主题与暗色模式，API 与文档专为「人和 AI 智能体协同开发」设计。连续第三日在榜且今日涨星登顶（+1,830），累计 Star 26,761。"),
    ("CopilotKit/OpenBot", "https://github.com/CopilotKit/OpenBot", "TypeScript", 11746, 298,
     "OpenBot：CopilotKit 出品的开源「AI 同事」——每个智能体分到一台属于自己的电脑：浏览器、文件与工具，每步操作先决策后执行并全程留痕，支持接入任意 AG-UI 智能体。「给智能体一台电脑」赛道项目回归（上次 11-02），累计 Star 11,746。"),
    ("Alishahryar1/free-claude-code", "https://github.com/Alishahryar1/free-claude-code", "Python", 69449, 415,
     "free-claude-code：把 Claude Code、Codex、Antigravity、VSCode 等 12 种 AI 编码 harness 路由到 61 家模型供应商——每月 1.3B+ 免费 token，覆盖终端/桌面/IDE/手机/浏览器全场景，遵循各供应商 TOS。回归项目（上次 10-13），累计 Star 69,449。"),
    ("ggml-org/llama.cpp", "https://github.com/ggml-org/llama.cpp", "C++", 134637, 176,
     "llama.cpp：最经典的本地大模型推理引擎——纯 C/C++ 无依赖、跨平台跑 LLM，本地 AI 生态的基石项目。老牌巨头本自动化记录中首次登榜，累计 Star 134,637，为今日全榜最高。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "给智能体一台电脑": ["OpenBot"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"GoogleChrome/modern-web-guidance-src", "openai/codex-security",
            "QwenLM/qwen-code", "ashhart/TensorFold",
            "addyosmani/agent-skills", "CopilotKit/OpenBot",
            "Alishahryar1/free-claude-code", "ggml-org/llama.cpp"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top (astryx) != raw #1 (modern-web).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第三日在榜且首次登顶涨幅榜。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，今日第 4）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：TypeScript 包揽 modern-web-guidance-src、codex-security、qwen-code、astryx、OpenBot 五席；其余分布：{others}，共 {len(lang_stats)} 种语言。Objective-C 与 Zig 为今日新触发语言（脚本已补色），无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：astryx（+{top[4]:,}）、sure（+{second[4]:,}）与 agent-skills（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 TensorFold 的 +54 收尾，整体分布较前两日（astryx 单仓占四成）更均衡。</li>')

    delta_pct = int(round(abs(total_today - 6895) / 6895 * 100))
    ins.append(f'<li><b>热度持续低位</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-12（+6,895 / 10 个仓库）再回落约 <b>{delta_pct}%</b>，连续两日处于 11 月的 6K 档低水位（对比 11-10 的 +13,136 与 11-11 的 +12,153）。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'Node 版本管理器' if 'nvm' in r[0] else 'Apple Watch 表盘工具' if 'Hermes' in r[0] else '个人理财 App' if 'sure' in r[0] else 'JS 运行时' if 'nodejs/node' in r[0] else '设计系统本体，dbx 先例'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 5 个为 {non_ai_txt}。口径说明：TensorFold 与 llama.cpp 为 LLM 专用推理引擎故计入（BitNet/tokenspeed 先例，区别于 PyTorch 类通用框架）。另注：越狱提示词合集 jailbreaks 与 p-e-w/heretic 今日均未上榜（剔除口径无需触发）。</li>')

    ins.append('<li><b>新面孔 5 个、回归 3 个、延续 5 个、掉榜 5 个</b>：新进 <b>HermesEnabler</b>（Apple Watch 爱马仕表盘）、<b>qwen-code</b>（Qwen 官方编码智能体 CLI）、<b>TensorFold</b>（Zig 三后端 LLM 推理引擎）、<b>nodejs/node</b>（Node.js 运行时本体）、<b>llama.cpp</b>（本地 LLM 推理基石）；回归 <b>nvm</b>（上次 10-15）、<b>OpenBot</b>（上次 11-02）、<b>free-claude-code</b>（上次 10-13）；延续 modern-web-guidance-src、codex-security、sure、agent-skills、astryx。上期掉榜：improve、TheAlgorithms/Java、daily_stock_analysis、ha-mcp、agent-browser。</li>')

    ins.append('<li><b>主题观察：巨头官方基础设施「集中点名」日</b>——① <b>GoogleChrome 的智能体技能包连续第二日在榜</b>，浏览器厂商为编码智能体供料成为常态；② <b>OpenAI 官方安全 CLI codex-security</b> 把「AI 找漏洞、AI 修漏洞」产品化；③ <b>Qwen 官方 qwen-code</b> 补齐国亠大模型的终端编码智能体入口；④ <b>三大老牌基建罕见同榜</b>：nodejs/node（12.3 万）、llama.cpp（13.4 万）、nvm（9.6 万）——通用基础设施与 LLM 基础设施同日汇聚；⑤ <b>「给智能体一台电脑」赛道</b>：OpenBot 回归（AI 同事分电脑），free-claude-code 回归（12 种 harness × 61 家供应商路由）；⑥ <b>astryx 连庄三日</b>且今日以 +1,830 登顶，Meta 设计系统成为本周最稳的流量入口。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：今日三座 10 万+ 同榜——llama.cpp <b>134,637</b>（13.4 万，全榜最高）、nodejs/node <b>123,626</b>（12.3 万）、agent-skills <b>116,783</b>（11.6 万）；nvm 96,041 逼近 10 万大关；free-claude-code 69,449 稳居 7 万档。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 13)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).
    base.LANG_COLORS.update({"Zig": "#EC915C", "Objective-C": "#438EFF"})

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
