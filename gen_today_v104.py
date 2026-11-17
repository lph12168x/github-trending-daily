"""Generate GitHub Trending report for 2026-11-17 (v104).

DATA SOURCE (all facts below verified this run)
-----------------------------------------------
fetch_trending_curl.py succeeded via plain-DNS direct connection:
rc=0, 582,912 bytes, complete document ending in </html>, exactly
15 Box-row articles. Freshness verified: saved-file mtime 12:31 >
pre-fetch start. NOTE: the fetch script's TSV columns are
name / lang / total_stars / forks / today_stars (forks before today).
Cross-check: independent WebFetch returned the SAME 15 repos, SAME
order, SAME stars-today values (791/696/1828/837/1094/46/288/529/
135/873/951/313/841/115/367). Total = +9,704 on both views.
Cumulative star counts: report uses the curl values (freshest).

CONTENT JUDGMENT
----------------
jailbreaks and p-e-w/heretic: NOT on the list today (both absent).
No political-sensitivity issues (jiangshan-map is a historical atlas
of Chinese dynasties, purely educational/cultural). No circumvention
tools of any kind. All 15 repos included, +9,704 today.

Counted as AI / Agent related (11/15):
  * ag-ui-protocol/ag-ui              -- Agent-User Interaction Protocol
        (11-15/11-16 precedent).
  * backnotprop/plannotator           -- annotation workspace for coding
        agents (11-14~11-16 precedent).
  * tradermonty/claude-trading-skills -- Claude Code skills for traders
        (11-14~11-16 precedent).
  * elementalsouls/Claude-BugHunter   -- Claude Code skill bundle for
        bug hunting / red-team work.
  * google-labs-code/stitch-skills    -- Google Labs official Agent
        Skills library.
  * mvanhorn/last30days-skill         -- AI agent research skill
        (multi-source research + grounded synthesis).
  * NVIDIA/SkillEvaluator             -- framework for evaluating AI
        agent skills.
  * alibaba/open-code-review          -- LLM Agent integral to the
        product (11-14~11-16 precedent).
  * google-research/paper-orchestra   -- multi-agent framework for
        automated AI research paper writing.
  * ChromeDevTools/chrome-devtools-mcp -- MCP for coding agents.
  * kajisho5/ffmpeg-skill             -- local video editor exposed to
        coding agents via MCP (42 FFmpeg tools).

NOT counted (4):
  * dream-num/univer    -- Office SDK at its core; AI office is the
        positioning, the body is a document engine (dbx precedent,
        re-verified against 11-15/11-16 judgment).
  * getarcaneapp/arcane -- Docker management UI, no agent/AI identity.
  * DeanChensj/jiangshan-map -- historical atlas web app
        (ziwei-doushu precedent: cultural/data product, not AI).
  * sveltejs/svelte     -- frontend framework, no AI identity.

NEW / RETURNING / DROPPED (vs 2026-11-16, v103)
-----------------------------------------------
Continuations (9): dream-num/univer, ag-ui-protocol/ag-ui,
  backnotprop/plannotator, tradermonty/claude-trading-skills,
  elementalsouls/Claude-BugHunter, google-labs-code/stitch-skills,
  NVIDIA/SkillEvaluator, alibaba/open-code-review,
  ChromeDevTools/chrome-devtools-mcp.
Returning (1): mvanhorn/last30days-skill (last seen 2026-08-31,
  verified via grep over all historical md reports).
New faces (5): getarcaneapp/arcane, DeanChensj/jiangshan-map,
  google-research/paper-orchestra, sveltejs/svelte, kajisho5/ffmpeg-skill
  (verified via grep: none of these names appear in any historical md).
Dropped (3): Tencent/LoopForge, ggml-org/ggml,
  GoogleChrome/modern-web-guidance-src.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-17"
TODAY_FMT = "2026年11月17日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 15 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("ag-ui-protocol/ag-ui", "https://github.com/ag-ui-protocol/ag-ui", "TypeScript", 19276, 791,
     "ag-ui：Agent-User Interaction Protocol——把 AI 智能体接入前端应用的标准化交互协议，为智能体 UI 提供事件流、状态同步与渲染契约。连续第三日在榜，今日以 +791 位列 GitHub 原始榜单首位（与涨幅冠军不一致，已按新增重排），累计 Star 19,276，逼近 2 万。"),
    ("backnotprop/plannotator", "https://github.com/backnotprop/plannotator", "TypeScript", 12697, 696,
     "plannotator：编码智能体的「批注工作台」——收件箱统一跟进智能体动态，可对计划/规格/Markdown/HTML 等工件划词批注，审查 diff 与 PR，一键把反馈发回智能体；原生支持 Claude Code、Codex、Copilot CLI、Gemini CLI 等。连续第四日在榜，累计 Star 12,697。"),
    ("dream-num/univer", "https://github.com/dream-num/univer", "TypeScript", 27934, 1828,
     "univer：Univer Office SDK——开源办公套件引擎，以 Sheets/Docs 为核心，把编辑、计算、协作与文件处理能力嵌入自家产品，官方定位「为你和 AI 智能体打造 AI 办公」；本体是可扩展的文档/表格引擎。连续第三日在榜、今日首登涨幅榜首（+1,828），累计 Star 27,934，逼近 3 万。"),
    ("tradermonty/claude-trading-skills", "https://github.com/tradermonty/claude-trading-skills", "Python", 6457, 837,
     "claude-trading-skills：面向股票投资者与交易员的 Claude Code 技能集——市场分析、技术图表、经济日历、选股筛选器等专业技能包，把编码智能体改造成投研助手。连续第四日在榜，累计 Star 6,457。"),
    ("elementalsouls/Claude-BugHunter", "https://github.com/elementalsouls/Claude-BugHunter", "Python", 7592, 1094,
     "Claude-BugHunter：面向漏洞挖掘与外部红队工作的 Claude Code 技能包——82 个技能、15 个斜杠命令，横跨 24 类核心漏洞 curated 出 681 个已公开漏洞报告模式，并附企业身份 + 基础设施攻击矩阵。连续第二日在榜、今日跃居涨幅第二，累计 Star 7,592。"),
    ("getarcaneapp/arcane", "https://github.com/getarcaneapp/arcane", "Go", 8859, 46,
     "arcane：Modern Docker Management, Designed for Everyone——面向所有人的现代化 Docker 管理工具，简化容器、镜像与卷的日常运维。新面孔首次登榜，累计 Star 8,859。"),
    ("DeanChensj/jiangshan-map", "https://github.com/DeanChensj/jiangshan-map", "JavaScript", 7095, 288,
     "jiangshan-map：江山时序——中国历史交互地图时间轴（公元前 403 年至今），横跨 18 个王朝、198 幅疆域快照，含古今地名谱系与古典诗词路线，支持交互式探索中国历史地理。新面孔首次登榜，累计 Star 7,095。"),
    ("google-labs-code/stitch-skills", "https://github.com/google-labs-code/stitch-skills", "TypeScript", 9798, 529,
     "stitch-skills：Google Labs 官方出品的 Agent Skills 技能库——为 Stitch MCP 服务器设计，每个技能均遵循 Agent Skills 开放标准，可兼容 Antigravity、Gemini CLI、Claude Code、Cursor 等编码智能体。连续第二日在榜，累计 Star 9,798，逼近 1 万。"),
    ("mvanhorn/last30days-skill", "https://github.com/mvanhorn/last30days-skill", "Python", 68272, 135,
     "last30days-skill：AI 智能体研究技能——跨 Reddit、X、YouTube、HN、Polymarket 与全网检索任意主题近 30 天动态，并合成有据可查的摘要。回归登榜（上次 08-31），累计 Star 68,272，逼近 7 万。"),
    ("NVIDIA/SkillEvaluator", "https://github.com/NVIDIA/SkillEvaluator", "Python", 2881, 873,
     "SkillEvaluator：NVIDIA 官方出品的 AI 智能体技能评测框架——多层评测体系，含质量门（quality gates）、语义重叠检测、合成评测数据集生成，以及可量化「技能对智能体行为影响」的在线评测。连续第二日在榜、今日升至涨幅第四，累计 Star 2,881。"),
    ("alibaba/open-code-review", "https://github.com/alibaba/open-code-review", "Go", 53084, 951,
     "open-code-review：阿里巴巴出品的混合架构代码评审工具——确定性流水线 + LLM Agent 双引擎，行级精确评论，内置多语言规则集（NPE、线程安全、XSS、SQL 注入），兼容 OpenAI 与 Anthropic 接口，在阿里规模上久经考验。连续第四日在榜，累计 Star 53,084。"),
    ("google-research/paper-orchestra", "https://github.com/google-research/paper-orchestra", "Python", 1708, 313,
     "paper-orchestra：Google Research 出品的多智能体框架——用于自动化 AI 研究论文写作，多个智能体协同完成文献调研与论文产出。新面孔首次登榜，累计 Star 1,708。"),
    ("ChromeDevTools/chrome-devtools-mcp", "https://github.com/ChromeDevTools/chrome-devtools-mcp", "TypeScript", 57778, 841,
     "chrome-devtools-mcp：Chrome DevTools 官方 MCP 服务器——让编码智能体直接驱动浏览器进行调试、性能分析与页面检查。连续第四日在榜，累计 Star 57,778。"),
    ("sveltejs/svelte", "https://github.com/sveltejs/svelte", "JavaScript", 89058, 115,
     "svelte：Svelte 官方主仓——「为其余人准备的 Web 开发」，编译时框架的代表，把组件编译为极小、无虚拟 DOM 的原生 JS。新面孔首次登榜，累计 Star 89,058，为今日榜单体量之最、逼近 9 万。"),
    ("kajisho5/ffmpeg-skill", "https://github.com/kajisho5/ffmpeg-skill", "Python", 7026, 367,
     "ffmpeg-skill：面向编码智能体的本地视频编辑器——42 个 FFmpeg 工具带机器可读契约与 MCP 服务器，供 Claude Code、Cursor 与 Codex 调用完成剪辑、字幕、重构图、响度与平台导出；无云端、无 API 密钥。新面孔首次登榜，累计 Star 7,026。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"ag-ui-protocol/ag-ui", "backnotprop/plannotator",
            "tradermonty/claude-trading-skills",
            "elementalsouls/Claude-BugHunter",
            "google-labs-code/stitch-skills",
            "mvanhorn/last30days-skill", "NVIDIA/SkillEvaluator",
            "alibaba/open-code-review",
            "google-research/paper-orchestra",
            "ChromeDevTools/chrome-devtools-mcp", "kajisho5/ffmpeg-skill"}

NON_AI_REASON = {
    "dream-num/univer": "Office SDK 本体，AI 为定位非核心（dbx 先例）",
    "getarcaneapp/arcane": "Docker 管理工具，无智能体身份",
    "DeanChensj/jiangshan-map": "历史地图文化产品（ziwei-doushu 先例）",
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

    # Insight 1: top gainer. Today: top (univer) != raw #1 (ag-ui).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，连续第三日在榜、今日首登涨幅榜首。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日 <b>GitHub 原始榜单首位为 {rank1[0].split("/")[-1]}（+{rank1[4]:,}，重排后今日第 7）</b>，两者不一致，已按新增重排并注明。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 席居首</b>：Python 包揽 claude-trading-skills、Claude-BugHunter、last30days-skill、SkillEvaluator、paper-orchestra、ffmpeg-skill 六席——技能类仓库清一色 Python；其余分布：{others}，共 {len(lang_stats)} 种语言，无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量，分布为近期最均匀</b>：univer（+{top[4]:,}）、Claude-BugHunter（+{second[4]:,}）与 open-code-review（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；15 个仓库中 14 个单日涨幅破百，长尾由 arcane 的 +{repos[-1][4]:,} 收尾。</li>')

    delta_pct = int(round(abs(total_today - 6475) / 6475 * 100))
    ins.append(f'<li><b>热度显著回升约 {delta_pct}%，重返 9K 档</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-16（+6,475 / 12 个仓库）回升约 <b>{delta_pct}%</b>；四日走势 11-14 +4,996 → 11-15 +6,393 → 11-16 +6,475 → 今日 +9,704，为 11-10 高水位（+13,136）的约 74%，且仓库数 15 为近两周最多。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{NON_AI_REASON.get(r[0], '无 AI 身份')}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 4 个为 {non_ai_txt}。口径说明：univer 沿用 11-15/11-16 判定（本体文档引擎、AI 办公仅为定位，参照 dbx 先例）；jiangshan-map 为历史文化数据产品，参照 ziwei-doushu 先例不计入；arcane 与 svelte 为纯基础设施/框架，无 AI 身份。</li>')

    ins.append('<li><b>新面孔 5 个、回归 1 个、延续 9 个、掉榜 3 个</b>：新进 <b>arcane</b>（Docker 管理）、<b>jiangshan-map</b>（中国历史交互地图）、<b>paper-orchestra</b>（Google Research 多智能体写论文）、<b>svelte</b>（编译时前端框架）、<b>ffmpeg-skill</b>（智能体视频剪辑）——均经全历史检索确认为首次登榜；回归 <b>last30days-skill</b>（上次 08-31）；延续 univer、ag-ui、plannotator、chrome-devtools-mcp、open-code-review、stitch-skills、SkillEvaluator、Claude-BugHunter、claude-trading-skills。上期掉榜：LoopForge、ggml、modern-web-guidance-src，换手率 40%。</li>')

    ins.append('<li><b>主题观察：「智能体技能层」扩容为榜单主力，并首次延伸到媒体处理</b>——技能类仓库今日多达 6 个同榜：投研（claude-trading-skills）、安全红队（Claude-BugHunter）、设计（stitch-skills）、评测（SkillEvaluator）、调研（last30days-skill）、视频剪辑（<b>ffmpeg-skill</b> 首次把视频编辑做成编码智能体技能，42 工具 + MCP、全程本地）；交互层双线延续（ag-ui 协议 + plannotator 工作台），研究自动化再添 <b>paper-orchestra</b>（Google Research 多智能体写论文）。大厂阵营五家同榜：Google Labs、NVIDIA、alibaba、ChromeDevTools、google-research；中文项目 jiangshan-map 以历史交互地图获 7 千星，为文化类项目（ziwei-doushu 之后）又一例。</li>')

    ins.append('<li><b>里程碑观察</b>：今日无 10 万+ 星仓库；<b>svelte 89,058</b> 为榜单体量之最、逼近 9 万；<b>last30days-skill 68,272</b> 逼近 7 万；chrome-devtools-mcp <b>57,778</b> 与 open-code-review <b>53,084</b> 双双站稳 5 万档；univer <b>27,934</b> 逼近 3 万；paper-orchestra <b>1,708</b> 与 SkillEvaluator <b>2,881</b> 为今日两个微型体量跟踪对象。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 17)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # Language colors missing from the v26 table (the TeX lesson: runtime
    # patches do not persist -- re-apply every time these languages appear).
    # Today's languages: TypeScript / Python / Go / JavaScript -- all present.

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
