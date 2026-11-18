"""Generate GitHub Trending report for 2026-11-18 (v105).

DATA SOURCE (all facts below verified this run)
-----------------------------------------------
fetch_trending_curl.py succeeded via plain-DNS direct connection:
rc=0, 583,825 bytes, complete document ending in </html>, exactly
15 Box-row articles. Freshness verified: saved-file mtime 12:31:35 >
pre-fetch time 12:31:08. NOTE: the fetch script's TSV columns are
name / lang / total_stars / forks / today_stars (forks before today).
Cross-check: independent WebFetch returned the SAME 15 repos, SAME
order, SAME stars-today values (1005/696/763/591/1774/618/350/201/
1917/1445/691/477/883/192/1072). Total = +12,675 on both views.
Cumulative star counts: report uses the curl values (freshest).

CONTENT JUDGMENT
----------------
jailbreaks and p-e-w/heretic: NOT on the list today (both absent).
No political-sensitivity issues. No circumvention tools of any kind.
All 15 repos included, +12,675 today.
cursor/plugins: README fetched via Contents API (raw) -- it is Cursor's
official agent plugin/skill/context ecosystem (skills, subagents,
orchestration, third-party integrations) => counted as AI.

Counted as AI / Agent related (12/15):
  * elementalsouls/Claude-BugHunter -- Claude Code red-team skill bundle.
  * mvanhorn/last30days-skill       -- AI agent research skill.
  * alibaba/open-code-review        -- LLM Agent integral to product.
  * Tencent/LoopForge               -- coding-agent delivery orchestration.
  * google-labs-code/stitch-skills  -- Google Labs Agent Skills library.
  * cursor/plugins                  -- Cursor official agent plugin ecosystem.
  * obra/superpowers                -- agentic skills framework (verified).
  * ag-ui-protocol/ag-ui            -- Agent-User Interaction Protocol.
  * backnotprop/plannotator         -- agent annotation workspace.
  * affaan-m/ECC                    -- agent harness optimization system.
  * jingyaogong/minimind            -- train-an-LLM-from-scratch project
        (nanochat 11-03 precedent: LLM training education counts as AI).
  * google-research/paper-orchestra -- multi-agent paper-writing framework.

NOT counted (3):
  * dream-num/univer  -- Office SDK at its core; AI office is the
        positioning, the body is a document engine (dbx precedent,
        re-verified against 11-15/11-16/11-17 judgment).
  * getarcaneapp/arcane -- Docker management UI, no agent/AI identity.
  * sveltejs/svelte     -- frontend framework, no AI identity.

NEW / RETURNING / DROPPED (vs 2026-11-17, v104)
-----------------------------------------------
Continuations (10): Claude-BugHunter, last30days-skill, open-code-review,
  univer, arcane, stitch-skills, ag-ui, plannotator, svelte, paper-orchestra.
Returning (5): Tencent/LoopForge (last 11-16), cursor/plugins (last 10-19),
  obra/superpowers (last 10-30), affaan-m/ECC (last 10-28),
  jingyaogong/minimind (last 09-02).
New faces (0): none -- a rare "all old-timers" day; every repo has a
  prior appearance (verified via grep over all historical md reports).
Dropped (5): claude-trading-skills, jiangshan-map, SkillEvaluator,
  chrome-devtools-mcp, ffmpeg-skill. Turnover 5/15 = 33%.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-18"
TODAY_FMT = "2026年11月18日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 15 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("elementalsouls/Claude-BugHunter", "https://github.com/elementalsouls/Claude-BugHunter", "Python", 9629, 1005,
     "Claude-BugHunter：面向漏洞挖掘与外部红队工作的 Claude Code 技能包——82 个技能、15 个斜杠命令，横跨 24 类核心漏洞，curated 出 681 个已公开漏洞报告模式，并附企业身份 + 基础设施攻击矩阵。连续第二日在榜，今日位列 GitHub 原始榜单首位（+1,005，与涨幅冠军不一致，已按新增重排），累计 Star 9,629。"),
    ("mvanhorn/last30days-skill", "https://github.com/mvanhorn/last30days-skill", "Python", 69250, 696,
     "last30days-skill：AI 智能体研究技能——跨 Reddit、X、YouTube、HN、Polymarket 与全网检索任意主题近 30 天动态，并合成有据可查的摘要。连续第二日在榜，累计 Star 69,250，逼近 7 万。"),
    ("alibaba/open-code-review", "https://github.com/alibaba/open-code-review", "Go", 53862, 763,
     "open-code-review：阿里巴巴出品的混合架构代码评审工具——确定性流水线 + LLM Agent 双引擎，行级精确评论，内置多语言规则集（NPE、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic 接口，在阿里规模上久经考验。连续第五日在榜，累计 Star 53,862，站稳 5 万档。"),
    ("Tencent/LoopForge", "https://github.com/Tencent/LoopForge", "Go", 3404, 591,
     "LoopForge：腾讯开源的自托管「编码智能体交付」工作流平台——用脚本与人工审批关卡编排 CodeBuddy、Codex 与 Claude Code，内含面向编码助手的本地工作流。回归登榜（上次 11-16），累计 Star 3,404。"),
    ("dream-num/univer", "https://github.com/dream-num/univer", "TypeScript", 29054, 1774,
     "univer：Univer Office SDK——开源办公套件引擎，以 Sheets/Docs 为核心，把编辑、计算、协作与文件处理能力嵌入自家产品，官方定位「为你和 AI 智能体打造 AI 办公」；本体是可扩展的文档/表格引擎。连续第四日在榜、今日涨幅第二（+1,774），累计 Star 29,054，逼近 3 万。"),
    ("getarcaneapp/arcane", "https://github.com/getarcaneapp/arcane", "Go", 9411, 618,
     "arcane：Modern Docker Management, Designed for Everyone——面向所有人的现代化 Docker 管理工具，简化容器、镜像与卷的日常运维。连续第二日在榜，累计 Star 9,411。"),
    ("google-labs-code/stitch-skills", "https://github.com/google-labs-code/stitch-skills", "TypeScript", 10165, 350,
     "stitch-skills：Google Labs 官方出品的 Agent Skills 技能库——为 Stitch MCP 服务器设计，每个技能均遵循 Agent Skills 开放标准，可兼容 Antigravity、Gemini CLI、Claude Code、Cursor 等编码智能体。连续第三日在榜，累计 Star 10,165，站稳 1 万。"),
    ("cursor/plugins", "https://github.com/cursor/plugins", "TypeScript", 16953, 201,
     "cursor/plugins：Cursor 官方插件规范与官方插件集合——按 README，涵盖智能体技能、子智能体、并行云端智能体编排、代码审查，以及 Gmail/Drive/Salesforce/GitHub 等第三方集成；是 Cursor 编码智能体的官方扩展生态。回归登榜（上次 10-19），累计 Star 16,953。"),
    ("obra/superpowers", "https://github.com/obra/superpowers", "Shell", 319462, 1917,
     "superpowers：久经考验的智能体技能框架与软件开发方法论——把 TDD、代码评审、子智能体协作等实践固化为可组合技能，供 Claude Code、Codex、Cursor 等编码智能体调用。回归登榜（上次 10-30）、今日首登涨幅榜首（+1,917），累计 Star 319,462，逼近 32 万。"),
    ("ag-ui-protocol/ag-ui", "https://github.com/ag-ui-protocol/ag-ui", "TypeScript", 20096, 1445,
     "ag-ui：Agent-User Interaction Protocol——把 AI 智能体接入前端应用的标准化交互协议，为智能体 UI 提供事件流、状态同步与渲染契约。连续第四日在榜、今日涨幅第三（+1,445），累计 Star 20,096，刚破 2 万。"),
    ("backnotprop/plannotator", "https://github.com/backnotprop/plannotator", "TypeScript", 13131, 691,
     "plannotator：编码智能体的「批注工作台」——收件箱统一跟进智能体动态，可对计划/规格/Markdown/HTML 等工件划词批注，审查 diff 与 PR，一键把反馈发回智能体；原生支持 Claude Code、Codex、Copilot CLI、Gemini CLI 等。连续第五日在榜，累计 Star 13,131。"),
    ("sveltejs/svelte", "https://github.com/sveltejs/svelte", "JavaScript", 89639, 477,
     "svelte：Svelte 官方主仓——「为其余人准备的 Web 开发」，编译时框架的代表，把组件编译为极小、无虚拟 DOM 的原生 JS。连续第二日在榜，累计 Star 89,639，逼近 9 万。"),
    ("affaan-m/ECC", "https://github.com/affaan-m/ECC", "JavaScript", 305682, 883,
     "ECC：智能体 harness 性能优化系统——为 Claude Code、Codex、Opencode、Cursor 等提供技能、直觉（instincts）、记忆、安全与研究优先的开发范式。回归登榜（上次 10-28），累计 Star 305,682，站稳 30 万档。"),
    ("jingyaogong/minimind", "https://github.com/jingyaogong/minimind", "Python", 66140, 192,
     "minimind：🧠 用 2 小时从零训练一个 6400 万参数的 LLM——中文社区广受欢迎的 LLM 入门实战项目，覆盖数据处理、预训练、SFT 到部署全流程。回归登榜（上次 09-02），累计 Star 66,140。"),
    ("google-research/paper-orchestra", "https://github.com/google-research/paper-orchestra", "Python", 3239, 1072,
     "paper-orchestra：Google Research 出品的多智能体框架——用于自动化 AI 研究论文写作，多个智能体协同完成文献调研与论文产出。连续第二日在榜、今日涨幅第四（+1,072），累计 Star 3,239。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"elementalsouls/Claude-BugHunter", "mvanhorn/last30days-skill",
            "alibaba/open-code-review", "Tencent/LoopForge",
            "google-labs-code/stitch-skills", "cursor/plugins",
            "obra/superpowers", "ag-ui-protocol/ag-ui",
            "backnotprop/plannotator", "affaan-m/ECC",
            "jingyaogong/minimind", "google-research/paper-orchestra"}

NON_AI_REASON = {
    "dream-num/univer": "Office SDK 本体，AI 为定位非核心（dbx 先例）",
    "getarcaneapp/arcane": "Docker 管理工具，无智能体身份",
    "sveltejs/svelte": "前端框架，无 AI 身份",
}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top (superpowers) != raw #1 (Claude-BugHunter).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，回归登榜即登顶涨幅榜。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，重排后今日第 5）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：TypeScript 包揽 univer、stitch-skills、cursor/plugins、ag-ui、plannotator 五席；其余分布：{others}，共 {len(lang_stats)} 种语言（Python 4 / Go 3 / JavaScript 2 / Shell 1），无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：superpowers（+{top[4]:,}）、univer（+{second[4]:,}）与 ag-ui（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；15 个仓库中 14 个单日涨幅破 190，长尾由 minimind 的 +{repos[-1][4]:,} 收尾，分布较为均衡。</li>')

    delta_pct = int(round(abs(total_today - 9704) / 9704 * 100))
    ins.append(f'<li><b>热度回升约 {delta_pct}%，重返 1.2 万档</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-17（+9,704 / 15 个仓库）回升约 <b>{delta_pct}%</b>，仓库数持平；五日走势 11-14 +4,996 → 11-15 +6,393 → 11-16 +6,475 → 11-17 +9,704 → 今日 +12,675，回到 11-10（+13,136）附近的活跃水位。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{NON_AI_REASON.get(r[0], '无 AI 身份')}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 3 个为 {non_ai_txt}。口径说明：cursor/plugins 经 README 核实为 Cursor 官方智能体插件/技能生态，计入 AI；minimind 为「从零训练 LLM」教学实战项目，沿用 11-03 nanochat 先例计入；univer 沿用 dbx 先例（本体文档引擎、AI 办公仅为定位）不计入。</li>')

    ins.append('<li><b>新面孔 0 个、回归 5 个、延续 10 个、掉榜 5 个</b>：今日<b>无首次登榜项目</b>，为罕见的「全老面孔」日——回归 <b>LoopForge</b>（上次 11-16）、<b>cursor/plugins</b>（10-19）、<b>superpowers</b>（10-30）、<b>ECC</b>（10-28）、<b>minimind</b>（09-02）；延续 Claude-BugHunter、last30days-skill、open-code-review、univer、arcane、stitch-skills、ag-ui、plannotator、svelte、paper-orchestra；上期掉榜：claude-trading-skills、jiangshan-map、SkillEvaluator、chrome-devtools-mcp、ffmpeg-skill，换手率 33%。</li>')

    ins.append('<li><b>主题观察：「智能体技能/ harness 基础设施」集体回归</b>——今日 5 个回归项目几乎全是智能体底座层：<b>superpowers</b>（技能框架，涨星冠军）、<b>ECC</b>（harness 性能优化，30 万星）、<b>cursor/plugins</b>（Cursor 官方插件/技能生态）、<b>LoopForge</b>（腾讯编码智能体交付编排）叠加新入榜的 ag-ui（交互协议），构成「技能→编排→交互」的智能体基础设施闭环。与此同时 univer 的「AI 办公」与 minimind 的「从零训 LLM」分别代表落地应用与底层教育两条支线。中文阵营四席同榜：腾讯 LoopForge、阿里 open-code-review、dream-num/univer、jingyaogong/minimind。</li>')

    ins.append('<li><b>里程碑观察</b>：今日有 <b>2 个 30 万+ 星仓库</b>——<b>superpowers 319,462</b>（逼近 32 万）与 <b>ECC 305,682</b>（站稳 30 万）；<b>svelte 89,639</b> 逼近 9 万；<b>last30days-skill 69,250</b> 逼近 7 万；open-code-review <b>53,862</b> 站稳 5 万档；ag-ui <b>20,096</b> 刚破 2 万；paper-orchestra <b>3,239</b> 为今日最小体量跟踪对象。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 18)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).
    # Today's languages: Python / Go / TypeScript / Shell / JavaScript -- all present.

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
