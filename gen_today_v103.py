"""Generate GitHub Trending report for 2026-11-16 (v103).

DATA SOURCE (all facts below verified this run)
-----------------------------------------------
fetch_trending_curl.py succeeded via plain-DNS direct connection:
rc=0, 549,750 bytes, complete document ending in </html>, exactly
12 Box-row articles. Freshness verified: saved-file mtime 12:32 >
pre-fetch start 12:31. NOTE: the fetch script's TSV columns are
name / lang / total_stars / forks / today_stars (forks before today).
Cross-check: independent WebFetch (?since=daily) returned the SAME 12
repos, SAME order, SAME stars-today values (988/355/247/866/717/691/
423/43/98/1219/706/122). Total = +6,475 on both views.
Cumulative star counts: report uses the curl values (freshest).

CONTENT JUDGMENT
----------------
jailbreaks and p-e-w/heretic: NOT on the list today (both absent).
No political-sensitivity issues. No circumvention tools of any kind
on the list. All 12 repos included, +6,475 today.

Counted as AI / Agent related (10/12):
  * GoogleChrome/modern-web-guidance-src -- coding-agent skills pack
        (11-12/11-13/11-14/11-15 precedent).
  * dream-num/univer                     -- NOT counted (see below).
  * ag-ui-protocol/ag-ui                 -- Agent-User Interaction
        Protocol (11-15 precedent).
  * google-labs-code/stitch-skills       -- Google Labs official Agent
        Skills library for the Stitch MCP server.
  * backnotprop/plannotator              -- annotation workspace for
        coding agents (11-14/11-15 precedent).
  * ChromeDevTools/chrome-devtools-mcp   -- MCP for coding agents.
  * alibaba/open-code-review             -- LLM Agent integral to the
        product (11-14/11-15 precedent).
  * Tencent/LoopForge                    -- orchestration of coding-
        agent delivery (CodeBuddy/Codex/Claude Code), 11-15 precedent.
  * elementalsouls/Claude-BugHunter      -- Claude Code skill bundle
        for bug hunting / red-team work.
  * tradermonty/claude-trading-skills    -- Claude Code skills for
        traders (11-14/11-15 precedent).
  * NVIDIA/SkillEvaluator                -- framework for evaluating
        AI agent skills (quality gates, live agent evaluation).

NOT counted (2):
  * dream-num/univer -- Office SDK at its core; AI office is the
        positioning, the body is a document engine (dbx precedent,
        re-verified against 11-15 judgment).
  * ggml-org/ggml    -- general-purpose tensor library for ML
        (kornia precedent: ML infra library without agent/AI product
        identity is not counted).

NEW / RETURNING / DROPPED (vs 2026-11-15, v102)
-----------------------------------------------
Continuations (8): dream-num/univer, ag-ui-protocol/ag-ui,
  backnotprop/plannotator, ChromeDevTools/chrome-devtools-mcp,
  alibaba/open-code-review, Tencent/LoopForge,
  GoogleChrome/modern-web-guidance-src,
  tradermonty/claude-trading-skills.
Returning (0).
New faces (4): google-labs-code/stitch-skills, ggml-org/ggml,
  elementalsouls/Claude-BugHunter, NVIDIA/SkillEvaluator
  (all first appearance in this automation's records).
Dropped (7): QwenLM/qwen-code, ashhart/TensorFold,
  JuliusBrussee/caveman, louislam/uptime-kuma, we-promise/sure,
  Likely7/Veyra-NRVideo, martin-olivier/airgorah.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-16"
TODAY_FMT = "2026年11月16日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 12 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("dream-num/univer", "https://github.com/dream-num/univer", "TypeScript", 26464, 988,
     "univer：Univer Office SDK——开源办公套件引擎，以 Sheets/Docs 为核心，把编辑、计算、协作与文件处理能力嵌入自家产品，官方定位「为你和 AI 智能体打造 AI 办公」；本体是可扩展的文档/表格引擎。连续第二日在榜并今日跃居 GitHub 原始榜单首位，累计 Star 26,464。"),
    ("ag-ui-protocol/ag-ui", "https://github.com/ag-ui-protocol/ag-ui", "TypeScript", 18068, 355,
     "ag-ui：Agent-User Interaction Protocol——把 AI 智能体接入前端应用的标准化交互协议，为智能体 UI 提供事件流状态同步与渲染契约。连续第二日在榜，累计 Star 18,068。"),
    ("google-labs-code/stitch-skills", "https://github.com/google-labs-code/stitch-skills", "TypeScript", 9409, 247,
     "stitch-skills：Google Labs 官方出品的 Agent Skills 技能库——为 Stitch MCP 服务器设计，每个技能均遵循 Agent Skills 开放标准，可兼容 Antigravity、Gemini CLI、Claude Code、Cursor 等编码智能体。新面孔首次登榜，累计 Star 9,409。"),
    ("backnotprop/plannotator", "https://github.com/backnotprop/plannotator", "TypeScript", 11982, 866,
     "plannotator：编码智能体的「批注工作台」——收件箱统一跟进智能体动态，可对计划/规格/Markdown/HTML 等工件划词批注，审查 diff 与 PR，一键把反馈发回智能体；原生支持 Claude Code、Codex、Copilot CLI、Gemini CLI 等。连续第三日在榜，累计 Star 11,982。"),
    ("ChromeDevTools/chrome-devtools-mcp", "https://github.com/ChromeDevTools/chrome-devtools-mcp", "TypeScript", 57132, 717,
     "chrome-devtools-mcp：Chrome DevTools 官方 MCP 服务器——让编码智能体直接驱动浏览器进行调试、性能分析与页面检查。回归后连续第三日在榜，累计 Star 57,132。"),
    ("alibaba/open-code-review", "https://github.com/alibaba/open-code-review", "Go", 52285, 691,
     "open-code-review：阿里巴巴出品的混合架构代码评审工具——确定性流水线 + LLM Agent 双引擎，行级精确评论，内置多语言规则集（NPE、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic 接口，在阿里规模上久经考验。回归后连续第三日在榜，累计 Star 52,285。"),
    ("Tencent/LoopForge", "https://github.com/Tencent/LoopForge", "Go", 1734, 423,
     "LoopForge：腾讯官方出品的编码智能体交付工作流引擎——自托管编排 CodeBuddy、Codex 与 Claude Code，以脚本与人工审批门（human approval gates）串起智能体交付流水线，并为本地编码助手提供本地 workflow。连续第二日在榜、今日 +423 位列涨幅榜第七，累计 Star 1,734。"),
    ("ggml-org/ggml", "https://github.com/ggml-org/ggml", "C++", 15969, 43,
     "ggml：ggml-org 官方主仓的机器学习张量库——llama.cpp 背后的同门底层引擎，为端侧与边缘推理提供轻量张量计算原语。新面孔首次登榜，累计 Star 15,969。"),
    ("elementalsouls/Claude-BugHunter", "https://github.com/elementalsouls/Claude-BugHunter", "Python", 6628, 98,
     "Claude-BugHunter：面向漏洞挖掘与外部红队工作的 Claude Code 技能包——82 个技能、15 个斜杠命令，横跨 24 类核心漏洞 curated 出 681 个已公开漏洞报告模式，并附企业身份 + 基础设施攻击矩阵。新面孔首次登榜，累计 Star 6,628。"),
    ("GoogleChrome/modern-web-guidance-src", "https://github.com/GoogleChrome/modern-web-guidance-src", "TypeScript", 7358, 1219,
     "modern-web-guidance-src：Google Chrome 团队出品的「Web 最佳实践」智能体技能包——Chrome/Edge/Firefox/MDN 四方联合，把最新 Web 平台最佳实践整理成编码智能体可直接消费的技能源数据，让 AI 编码助手始终跟上 Web 标准。连续第五日在榜、连续第三日蝉联涨幅榜首（+1,219），累计 Star 7,358。"),
    ("tradermonty/claude-trading-skills", "https://github.com/tradermonty/claude-trading-skills", "Python", 5699, 706,
     "claude-trading-skills：面向股票投资者与交易员的 Claude Code 技能集——市场分析、技术图表、经济日历、选股筛选器等专业技能包，把编码智能体改造成投研助手。连续第三日在榜，累计 Star 5,699。"),
    ("NVIDIA/SkillEvaluator", "https://github.com/NVIDIA/SkillEvaluator", "Python", 1856, 122,
     "SkillEvaluator：NVIDIA 官方出品的 AI 智能体技能评测框架——多层评测体系，含质量门（quality gates）、语义重叠检测、合成评测数据集生成，以及可量化「技能对智能体行为影响」的在线评测。新面孔首次登榜，累计 Star 1,856。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体技能层（生产→评测）": ["stitch-skills", "SkillEvaluator", "modern-web-guidance-src"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"GoogleChrome/modern-web-guidance-src",
            "ag-ui-protocol/ag-ui", "google-labs-code/stitch-skills",
            "backnotprop/plannotator", "ChromeDevTools/chrome-devtools-mcp",
            "alibaba/open-code-review", "Tencent/LoopForge",
            "elementalsouls/Claude-BugHunter",
            "tradermonty/claude-trading-skills", "NVIDIA/SkillEvaluator"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top (modern-web) != raw #1 (univer).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第五日在榜、连续第三日蝉联涨幅榜首。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，重排后今日第 2）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：TypeScript 包揽 univer、ag-ui、stitch-skills、plannotator、chrome-devtools-mcp、modern-web-guidance-src 六席；其余分布：{others}，共 {len(lang_stats)} 种语言，无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：modern-web-guidance-src（+{top[4]:,}）、univer（+{second[4]:,}）与 plannotator（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 ggml 的 +{repos[-1][4]:,} 收尾。</li>')

    delta_pct = int(round(abs(total_today - 6393) / 6393 * 100))
    ins.append(f'<li><b>热度企稳，连续两日站稳 6K 档</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-15（+6,393 / 15 个仓库）微升约 <b>{delta_pct}%</b>、仓库数减 3；三日走势 11-14 +4,996 → 11-15 +6,393 → 今日 +6,475，仍是 11-10 高水位（+13,136）的约一半。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'Office SDK 本体，AI 为定位非核心' if 'univer' in r[0] else '通用 ML 张量库'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 2 个为 {non_ai_txt}。口径说明：univer 沿用 11-15 判定（本体文档引擎、AI 办公仅为定位，参照 dbx 先例）；ggml 为通用 ML 张量库、无智能体产品身份，参照 kornia 先例不计入；NVIDIA/SkillEvaluator 因评测对象即 AI 智能体技能而计入。</li>')

    ins.append('<li><b>新面孔 4 个、延续 8 个、掉榜 7 个（无回归）</b>：新进 <b>stitch-skills</b>（Google Labs 官方技能库）、<b>ggml</b>（llama.cpp 同门张量库）、<b>Claude-BugHunter</b>（82 技能红队包）、<b>SkillEvaluator</b>（NVIDIA 技能评测框架）；延续 univer、ag-ui、plannotator、chrome-devtools-mcp、open-code-review、LoopForge、modern-web-guidance-src、claude-trading-skills。上期掉榜：qwen-code、TensorFold、caveman、uptime-kuma、sure、Veyra-NRVideo、airgorah，换手率 47%。</li>')

    ins.append('<li><b>主题观察：「智能体技能层」从生产走向评测</b>——技能类仓库今日密集同榜：上游有 <b>modern-web-guidance-src</b>（Web 最佳实践）与 <b>stitch-skills</b>（Google Labs 官方）持续供给，垂直领域 <b>claude-trading-skills</b>（投研）与 <b>Claude-BugHunter</b>（安全红队）各守一摊，而 <b>NVIDIA/SkillEvaluator</b> 首次把「技能质量」本身做成可评测对象（质量门 + 语义重叠检测 + 在线评测）——技能生态完成「生产 → 消费 → 评测」闭环。大厂阵营同样密集：Google Labs、GoogleChrome、ChromeDevTools、alibaba、Tencent、NVIDIA 六家同榜，其中 LoopForge 编排对象正包括 CodeBuddy。</li>')

    ins.append('<li><b>里程碑观察</b>：今日无 10 万+ 星仓库；chrome-devtools-mcp <b>57,132</b> 与 open-code-review <b>52,285</b> 双双站稳 5 万档；univer <b>26,464</b> 逼近 3 万；ggml 上榜首日即 <b>15,969</b> 星（老牌底层的迟来曝光）；LoopForge <b>1,734</b> 与 SkillEvaluator <b>1,856</b> 为今日两个微型体量新跟踪对象。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 16)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).
    # Today's languages: TypeScript / Go / Python / C++ -- all present.

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
