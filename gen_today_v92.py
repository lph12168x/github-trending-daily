#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-10-30 (v92).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on its first (plain-DNS) route: rc=0,
546,093 bytes, complete document ending in </html>, exactly 11 Box-row
articles -> today's list is really 11 repos, not a truncation artifact.
Freshness verified: saved-file mtime 12:32:12 > pre-fetch time 12:31:52.
Cross-check: independent WebFetch (?since=daily) returned the SAME 11
repos, SAME order, SAME stars-today values
(1,930 / 1,034 / 2,870 / 1,117 / 1,199 / 709 / 1,187 / 336 / 247 /
1,594 / 353). Total = +12,576 on both views.
Cumulative star counts: report uses the curl values (freshest source).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks (+1,594 today, raw list #10) is EXCLUDED again
(third consecutive day): it is a curated collection of jailbreak
prompts targeting AI models. Per the content policy (same family as
circumvention / access-evasion tools) it is dropped from the report.
Included: 10 repos, +10,982 today.
No political-sensitivity issues among the rest.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (10/10, full coverage):
  * pbakaus/impeccable              -- design vocabulary for coding agents.
  * HKUDS/DeepTutor                 -- lifelong personalized AI tutoring.
  * milind-soni/OpenMausBot         -- open-source Grok Bot alternative (VM for bots).
  * elayadesign/ai-design-skills    -- design skills for AI coding tools.
  * JetBrains/thinkrail             -- JetBrains vibe-coding AI IDE (pi).
  * obra/superpowers                -- agentic skills framework & methodology.
  * nightly-labs/openbot            -- desktop workspace for AI teammates.
  * Donchitos/Claude-Code-Game-Studios -- 49 AI agents / 72 skills game studio.
  * thedotmack/claude-mem           -- persistent memory layer for agents.
  * CopilotKit/OpenBot              -- open-source AI coworkers (AG-UI).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-10-30"
TODAY_FMT = "2026年10月30日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass), minus the excluded jailbreaks.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("pbakaus/impeccable", "https://github.com/pbakaus/impeccable", "Rust", 95711, 2870,
     "impeccable：「让你的 AI harness 更懂设计的设计词汇」——用 polish 与更大胆的版本引导、用 critique 与 audit 审查、在上线前拦截 AI 味产出。设计技能赛道元老连续第四日在榜并首次登顶今日涨幅榜（唯一破两千），累计 Star 95,711。"),
    ("HKUDS/DeepTutor", "https://github.com/HKUDS/DeepTutor", "Python", 50515, 1930,
     "DeepTutor：终身个性化 AI 导师（Lifelong Personalized Tutoring）——港大 HKUDS 团队的智能辅导产品，官网 deeptutor.info 可直接使用。连续第四日在榜，今日位居 GitHub 原始榜单首位但涨幅列第二，AI 教育线持续走热，累计 Star 50,515。"),
    ("milind-soni/OpenMausBot", "https://github.com/milind-soni/OpenMausBot", "TypeScript", 7606, 1199,
     "OpenMausBot：开源的 Grok Bot 替代品——自带一台可供 bot 使用的虚拟机（a virtual machine that bots can use）。「给智能体一台电脑」方向新品，新面孔为本自动化有记录以来首次登榜，累计 Star 7,606。"),
    ("elayadesign/ai-design-skills", "https://github.com/elayadesign/ai-design-skills", "", 12349, 1187,
     "ai-design-skills：面向 AI 编程工具（Claude Code、Cursor、Codex、Windsurf 等）的设计技能合集——每个技能是自包含文件夹、按需安装，首个技能 landing-page-design 覆盖需求访谈、页面结构、转化文案与完整视觉系统。设计技能赛道领军项目连续第三日在榜，累计 Star 12,349。"),
    ("JetBrains/thinkrail", "https://github.com/JetBrains/thinkrail", "TypeScript", 6118, 1117,
     "thinkrail：JetBrains 官方「与 pi 一起 vibe coding」轻量级真实 IDE——围绕你的工作方式自适应定制（The Vibe You Need）。老牌 IDE 巨头入局 vibe coding 赛道，昨日曾位居原始榜单首位，今日继续在榜，累计 Star 6,118。"),
    ("obra/superpowers", "https://github.com/obra/superpowers", "Shell", 308733, 1034,
     "superpowers：obra 的智能体技能框架与软件开发方法论——「An agentic skills framework & software development methodology that works」。智能体方法论的元老级项目，连续第四日在榜，累计 Star 已达 308,733，今日榜单体量第一。"),
    ("nightly-labs/openbot", "https://github.com/nightly-labs/openbot", "TypeScript", 3970, 709,
     "openbot：本地优先（local-first）的桌面工作区，用于持久的 AI 队友——为 Codex、Claude、Grok 提供专属工作区、任务队列、文件共享、浏览器控制与智能体间协作。「多智能体协作工作台」方向延续快速成长，累计 Star 3,970。"),
    ("Donchitos/Claude-Code-Game-Studios", "https://github.com/Donchitos/Claude-Code-Game-Studios", "Shell", 29446, 353,
     "Claude-Code-Game-Studios：把 Claude Code 变成完整的游戏开发工作室——49 个 AI 智能体、72 个工作流技能，外加一套对标真实工作室层级的完整协作系统。「智能体团队模拟真实组织」方向新面孔首次登榜，累计 Star 29,446。"),
    ("thedotmack/claude-mem", "https://github.com/thedotmack/claude-mem", "TypeScript", 104971, 336,
     "claude-mem：为每个智能体提供跨会话持久记忆——捕获会话中的全部操作、用 AI 压缩，并在未来会话中注入相关上下文；兼容 Claude Code、Codex、Gemini、Copilot 等主流工具。智能体记忆层明星项目时隔约三周（上次在榜 10-08）回归，累计 Star 破十万（104,971）。"),
    ("CopilotKit/OpenBot", "https://github.com/CopilotKit/OpenBot", "TypeScript", 8249, 247,
     "OpenBot：开源 AI 同事（AI coworkers）——每个智能体都分到一台自己的电脑：浏览器、文件与工具，每一步操作先决定后执行、全程留痕；支持接入任意 AG-UI 智能体。CopilotKit 官方出品，「AI 员工」方向新面孔首次登榜，累计 Star 8,249。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "设计技能赛道": ["impeccable", "ai-design-skills"],
    "智能体方法论与 harness": ["superpowers"],
    "多智能体协作工作台": ["openbot", "OpenBot", "OpenMausBot"],
    "AI 教育": ["DeepTutor"],
    "游戏开发智能体": ["Game-Studios"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"pbakaus/impeccable", "HKUDS/DeepTutor", "milind-soni/OpenMausBot",
            "elayadesign/ai-design-skills", "JetBrains/thinkrail", "obra/superpowers",
            "nightly-labs/openbot", "Donchitos/Claude-Code-Game-Studios",
            "thedotmack/claude-mem", "CopilotKit/OpenBot"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（唯一破两千）；而 GitHub 原始榜单首位是 DeepTutor（+{rank1[4]:,}，仅列涨幅第二）——<b>两者不一致</b>。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    ins.append(f'<li><b>{top_langs[0]} {maxc}/10 居首</b>：TypeScript 包揽近半席位（OpenMausBot、thinkrail、openbot、claude-mem、OpenBot）；其余分布：{"、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)}，共 {len(lang_stats)} 种语言/无语言标注。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：{top[0].split("/")[-1]}（+{top[4]:,}）、{second[0].split("/")[-1]}（+{second[4]:,}）与 {third[0].split("/")[-1]}（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>，较上期 45% 回升；长尾相对分散，最小涨幅 +247。</li>')

    ins.append(f'<li><b>热度回落</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（10 个仓库），较上期 10-29（+14,565 / 13 个仓库）回落约 {abs(int(round((total_today-14565)/14565*100)))}%，降至近期中等水位。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)} 全覆盖</b>——今日收录的 10 个仓库全部与智能体生态相关：{ai_list}。另注：原始榜单第 10 位的 togg53192-cmd/jailbreaks（+1,594）为「针对 AI 模型的越狱提示词合集」，属绕过 AI 安全防护类内容，连续第三日按内容口径剔除、不予收录。</li>')

    ins.append('<li><b>新面孔 3 个、回归 1 个、延续 6 个</b>：新进 <b>milind-soni/OpenMausBot</b>（带虚拟机的开源 Grok Bot 替代品）、<b>CopilotKit/OpenBot</b>（每人一台电脑的 AI 同事）、<b>Donchitos/Claude-Code-Game-Studios</b>（49 智能体游戏工作室）；回归项：<b>thedotmack/claude-mem</b>（智能体记忆层，上次在榜 10-08）；延续项：impeccable、DeepTutor、ai-design-skills、thinkrail、superpowers、openbot。较上期掉榜 7 个：hallmark、LinkSwift、cindy、RuView、the-craft-of-selfteaching、macro、expo/skills。</li>')

    ins.append('<li><b>主题观察：「给智能体一台电脑」赛道三箭齐发 + 智能体组织化</b>——OpenMausBot（VM for bots）、CopilotKit/OpenBot（AI coworkers + AG-UI）、nightly-labs/openbot（AI 队友工作台）三个同方向项目同日登榜，「智能体运行时/工作台」成为今日最强主线；Claude-Code-Game-Studios 则把智能体组织成 49 人的「游戏工作室」，claude-mem 回归补上记忆层。设计赛道「三连击」中断：hallmark 掉榜，仅剩 impeccable 与 ai-design-skills 双雄延续。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：superpowers 累计 Star 达 <b>308,733</b>（30 万+，今日榜单体量第一），claude-mem 突破 <b>10 万</b>（104,971）；两个巨型老将与新一批累计不足 1 万的新面孔（openbot 3,970 / thinkrail 6,118 / OpenMausBot 7,606 / OpenBot 8,249）同榜，榜单「新老兵共存」格局延续。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 10, 30)
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
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today (excl. jailbreaks +1,594)")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
