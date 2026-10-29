#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-10-29 (v91).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on its first (plain-DNS) route: rc=0,
575,088 bytes, complete document ending in </html>, exactly 14 Box-row
articles -> today's list is really 14 repos, not a truncation artifact.
Freshness verified: saved-file mtime 12:31:59 > pre-fetch time 12:31:34.
Cross-check: independent WebFetch (?since=daily) returned the SAME 14
repos, SAME order, SAME stars-today values
(1,068 / 2,139 / 1,095 / 2,371 / 117 / 2,110 / 1,472 / 728 / 1,054 /
1,477 / 1,616 / 90 / 557 / 148). Total = +16,042 on both views.
Cumulative star counts: report uses the curl values (freshest source).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks (+1,477 today, raw list #10) is EXCLUDED again
(second consecutive day): it is a curated collection of jailbreak
prompts targeting 25+ models (system prompts / persona locks designed
to bypass model safety guardrails). Per the content policy (same
family as circumvention / access-evasion tools) it is dropped from the
report. Included: 13 repos, +14,565 today.
No political-sensitivity issues among the rest.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (11/13):
  * JetBrains/thinkrail          -- JetBrains vibe-coding AI IDE (pi).
  * elayadesign/ai-design-skills -- design skills for AI coding tools.
  * obra/superpowers             -- agentic skills framework & methodology.
  * HKUDS/DeepTutor              -- lifelong personalized AI tutoring.
  * macro-inc/macro              -- team workspace with shared AI memory.
  * Nutlope/hallmark             -- anti-AI-slop design skill.
  * pbakaus/impeccable           -- design vocabulary for coding agents.
  * makecindy/cindy              -- open-source out-of-the-box AI Agent.
  * nightly-labs/openbot         -- desktop workspace for AI teammates.
  * expo/skills                  -- AI agent skills for Expo projects.
  * ruvnet/RuView                -- WiFi sensing ML (deep learning).
Not AI (2): hmjz100/LinkSwift (netdisk direct-link downloader),
xiaolai/the-craft-of-selfteaching (self-teaching open book).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-10-29"
TODAY_FMT = "2026年10月29日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass), minus the excluded jailbreaks.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("JetBrains/thinkrail", "https://github.com/JetBrains/thinkrail", "TypeScript", 5267, 1068,
     "thinkrail：JetBrains 官方「与 pi 一起 vibe coding」轻量级真实 IDE——围绕你的工作方式自适应定制（The Vibe You Need）。老牌 IDE 巨头入局 vibe coding 赛道，发布后连续多日在榜，且今日位居 GitHub 原始榜单首位，累计 Star 5,267。"),
    ("elayadesign/ai-design-skills", "https://github.com/elayadesign/ai-design-skills", "", 11324, 2139,
     "ai-design-skills：面向 AI 编程工具（Claude Code、Cursor、Codex、Windsurf 等）的设计技能合集——每个技能是自包含文件夹、按需安装，首个技能 landing-page-design 覆盖需求访谈、页面结构、转化文案与完整视觉系统。设计技能赛道领军项目连续第二日在榜且持续高速涨星，累计 Star 11,324。"),
    ("obra/superpowers", "https://github.com/obra/superpowers", "Shell", 307584, 1095,
     "superpowers：obra 的智能体技能框架与软件开发方法论——「An agentic skills framework & software development methodology that works」。智能体方法论的元老级项目，回归后连续第二日在榜，累计 Star 已突破 30 万（307,584），今日榜单体量第一。"),
    ("HKUDS/DeepTutor", "https://github.com/HKUDS/DeepTutor", "Python", 48360, 2371,
     "DeepTutor：终身个性化 AI 导师（Lifelong Personalized Tutoring）——港大 HKUDS 团队的智能辅导产品，官网 deeptutor.info 可直接使用。回归后连续第三日在榜并登顶今日涨幅榜，AI 教育线持续走热，累计 Star 48,360。"),
    ("macro-inc/macro", "https://github.com/macro-inc/macro", "Rust", 5501, 117,
     "macro：团队统一工作区——邮件、聊天、文档、任务、智能体、通话与 CRM @-linked 打通，并共享 AI 记忆（shared AI memory）。「AI 记忆驱动的团队协作」方向新品，时隔约两个半月（上次在榜 8-14）回归，累计 Star 5,501。"),
    ("Nutlope/hallmark", "https://github.com/Nutlope/hallmark", "CSS", 40939, 2110,
     "hallmark：面向 Claude Code、Cursor 与 Codex 的「反 AI 味」设计技能——专治 AI 生成界面的千篇一律（AI-slop）。让智能体生成的 UI 拥有真正的设计质感，连续多日位居涨幅榜前三，累计 Star 40,939。"),
    ("pbakaus/impeccable", "https://github.com/pbakaus/impeccable", "Rust", 93174, 1472,
     "impeccable：「让你的 AI harness 更懂设计的设计词汇」——用 polish 与更大胆的版本引导、用 critique 与 audit 审查、在上线前拦截 AI 味产出。与 hallmark、ai-design-skills 组成设计技能赛道「三连击」，累计 Star 93,174。"),
    ("makecindy/cindy", "https://github.com/makecindy/cindy", "TypeScript", 8230, 728,
     "cindy：「Consider it done. 想到，就能做到。」开源、开箱即用的通用 AI Agent——无需复杂配置，装上就能干活（中英双语简介）。通用型开源 Agent 的「开箱即用化」趋势延续，累计 Star 8,230。"),
    ("nightly-labs/openbot", "https://github.com/nightly-labs/openbot", "TypeScript", 3379, 1054,
     "openbot：本地优先（local-first）的桌面工作区，用于持久的 AI 队友——为 Codex、Claude、Grok 提供专属工作区、任务队列、文件共享、浏览器控制与智能体间协作。「多智能体协作工作台」方向延续快速成长，累计 Star 3,379。"),
    ("hmjz100/LinkSwift", "https://github.com/hmjz100/LinkSwift", "JavaScript", 35286, 1616,
     "LinkSwift：基于 JavaScript 的网盘文件下载地址获取工具——基于「网盘直链下载助手」修改，支持百度网盘 / 阿里云盘 / 中国移动云盘 / 天翼云盘 / 迅雷云盘 / 夸克网盘 / UC网盘 / 123云盘 八大网盘。实用工具类新面孔，为本自动化有记录以来首次登榜，累计 Star 35,286。"),
    ("expo/skills", "https://github.com/expo/skills", "Shell", 3637, 90,
     "expo/skills：Expo 官方出品的 AI 智能体技能合集——用于处理 Expo 项目与 Expo Application Services（EAS）的开发任务。框架官方下场建设智能体技能生态的又一例证，新面孔首次登榜，累计 Star 3,637。"),
    ("ruvnet/RuView", "https://github.com/ruvnet/RuView", "Rust", 101193, 557,
     "RuView：把普通 WiFi 信号变成实时空间智能——呼吸/生命体征监测与在场感知，全程无需一个像素的视频（隐私友好感知）。深度学习 + WiFi CSI 感知方向明星项目，时隔约一个半月（上次在榜 9-15）回归，累计 Star 破十万（101,193）。"),
    ("xiaolai/the-craft-of-selfteaching", "https://github.com/xiaolai/the-craft-of-selfteaching", "Jupyter Notebook", 18630, 148,
     "the-craft-of-selfteaching：李笑来的开源自学教程《自学是门手艺》——「One has no future if one couldn't teach themself.」以 Python 为载体的自学方法论长销书，老牌经典项目新面孔首次进入本自动化记录，累计 Star 18,630。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "设计技能赛道": ["hallmark", "impeccable", "ai-design-skills"],
    "智能体方法论与 harness": ["superpowers"],
    "多智能体协作工作台": ["openbot"],
    "AI 教育": ["DeepTutor"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"JetBrains/thinkrail", "elayadesign/ai-design-skills", "obra/superpowers",
            "HKUDS/DeepTutor", "macro-inc/macro", "Nutlope/hallmark",
            "pbakaus/impeccable", "makecindy/cindy", "nightly-labs/openbot",
            "expo/skills", "ruvnet/RuView"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars；而 GitHub 原始榜单首位是 thinkrail（+{rank1[4]:,}）——<b>两者不一致</b>，且原始首位本身并非涨幅冠军。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    ins.append(f'<li><b>{" 与 ".join(top_langs)} 并列第一（各 {maxc} 席）</b>：TypeScript（thinkrail、cindy、openbot）与 Rust（macro、impeccable、RuView）平分秋色；其余席位分布：{"、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)}，共 {len(lang_stats)} 种语言/无语言标注。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：{top[0].split("/")[-1]}（+{top[4]:,}）、{second[0].split("/")[-1]}（+{second[4]:,}）与 {third[0].split("/")[-1]}（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>，与上期 44% 大体持平；且本期三强全部为 AI 教育与设计技能类项目。</li>')

    ins.append(f'<li><b>热度温和回升</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（13 个仓库），较上期 10-28（+13,451 / 10 个仓库）回升约 {abs(int(round((total_today-13451)/13451*100)))}%，维持在近期中等偏上水位。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>——明确计入 AI 的是：{ai_list}。非 AI 仅 2 个：LinkSwift（网盘直链下载工具）与 the-craft-of-selfteaching（自学方法论开源书）。另注：原始榜单第 10 位的 togg53192-cmd/jailbreaks（+1,477）为「针对 25+ 模型的越狱提示词合集」，属绕过 AI 安全防护类内容，连续第二日按内容口径剔除、不予收录。</li>')

    ins.append('<li><b>新面孔 3 个、回归 2 个、延续 8 个</b>：新进 <b>hmjz100/LinkSwift</b>（八大网盘直链下载工具）、<b>expo/skills</b>（Expo 官方智能体技能合集）、<b>xiaolai/the-craft-of-selfteaching</b>（《自学是门手艺》开源书）；回归项：<b>ruvnet/RuView</b>（WiFi 感知，上次在榜 9-15）、<b>macro-inc/macro</b>（AI 记忆团队工作区，上次在榜 8-14）；延续项：thinkrail、ai-design-skills、superpowers、DeepTutor、hallmark、impeccable、cindy、openbot。较上期掉榜 2 个：postiz-app、ECC。</li>')

    ins.append('<li><b>主题观察：设计赛道「三连击」第二天 + 智能体技能生态持续扩容</b>——设计线 ai-design-skills、hallmark、impeccable 连续两日同日在榜，「给智能体装审美」已成稳定赛道；技能/框架官方生态再添重磅玩家：Expo 官方 skills 上场（此前已有 Android/skills、NVIDIA、JetBrains 先例）；体量上 superpowers 突破 30 万 Star、RuView 破 10 万，两个巨型项目与一众新兴智能体项目同榜，榜单「新老兵共存」。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 10, 29)
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
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today (excl. jailbreaks +1,477)")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
