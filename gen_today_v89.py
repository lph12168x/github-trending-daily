#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-10-27 (v89).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on its first (plain-DNS) route: rc=0,
614,638 bytes, complete document ending in </html>, exactly 14 Box-row
articles -> today's list is really 14 repos, not a truncation artifact.
Freshness verified: saved-file mtime 12:31 > pre-fetch time.
Cross-check: independent WebFetch (?since=daily) returned the SAME 14
repos, SAME order, SAME stars-today values
(2,244 / 1,395 / 1,173 / 1,296 / 896 / 1,506 / 214 / 843 / 176 / 746 /
2,297 / 188 / 251 / 638). Total = +13,863 on both views.
Cumulative star counts: report uses the curl values (freshest source).

CONTENT NOTE
------------
No political-sensitivity issues and no circumvention / access-evasion tool
on today's list -- all 14 repos are reported, nothing dropped.
(Agent-Reach is an agent web-content reading/search CLI, not an
access-evasion tool; per the 09-30 criteria it is included.)

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (13/14):
  * Nutlope/hallmark                  -- anti-AI-slop design skill.
  * TauricResearch/TradingAgents      -- multi-agent LLM trading framework.
  * JetBrains/thinkrail               -- JetBrains vibe-coding AI IDE (pi).
  * makecindy/cindy                   -- open-source out-of-the-box AI Agent.
  * affaan-m/ECC                      -- agent harness optimization system.
  * pbakaus/impeccable                -- design language for AI harnesses.
  * NVIDIA/SkillSpector               -- security scanner for AI agent skills.
  * nightly-labs/openbot              -- desktop workspace for AI teammates.
  * Panniantong/Agent-Reach           -- agent internet-content access CLI.
  * debpalash/VoiceStudio             -- fully-local AI voice product.
  * gitroomhq/postiz-app              -- agentic social media scheduling.
  * alchaincyf/huashu-design          -- HTML-native design skill for agents.
  * multica-ai/andrej-karpathy-skills -- CLAUDE.md skill from Karpathy's
                                         LLM coding-pitfall observations.

NOT counted (1/14):
  * pollen-robotics/microduck -- biped duck robot (hardware/robotics).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-10-27"
TODAY_FMT = "2026年10月27日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass).
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("Nutlope/hallmark", "https://github.com/Nutlope/hallmark", "CSS", 36843, 2244,
     "hallmark：面向 Claude Code、Cursor 与 Codex 的「反 AI 味」设计技能——专治 AI 生成界面的千篇一律（AI-slop）。让智能体生成的 UI 拥有真正的设计质感，今日 GitHub 原始榜单首位，累计 Star 36,843。"),
    ("TauricResearch/TradingAgents", "https://github.com/TauricResearch/TradingAgents", "Python", 116395, 1395,
     "TradingAgents：多智能体 LLM 金融交易框架——用基本面、情绪、技术面等多个分析师智能体协作模拟真实交易团队的决策流程。金融 + 多智能体交叉方向的代表项目，连续多期在榜，累计 Star 116,395。"),
    ("JetBrains/thinkrail", "https://github.com/JetBrains/thinkrail", "TypeScript", 3114, 1173,
     "thinkrail：JetBrains 官方「与 pi 一起 vibe coding」轻量级真实 IDE——围绕你的工作方式自适应定制。老牌 IDE 巨头入局 vibe coding 赛道的标志性产品，发布次日继续冲榜，累计 Star 3,114。"),
    ("makecindy/cindy", "https://github.com/makecindy/cindy", "TypeScript", 6722, 1296,
     "cindy：「Consider it done. 想到，就能做到。」开源、开箱即用的通用 AI Agent——无需复杂配置，装上就能干活（中英双语简介）。通用型开源 Agent 的「开箱即用化」趋势延续，累计 Star 6,722。"),
    ("affaan-m/ECC", "https://github.com/affaan-m/ECC", "JavaScript", 289994, 896,
     "ECC：智能体 harness 性能优化系统——涵盖技能、直觉（instincts）、记忆、安全与研究优先开发，适配 Claude Code、Codex、Opencode、Cursor 等。今日榜单上体量最大的项目，累计 Star 已达 289,994，时隔约十一天重返榜单。"),
    ("pbakaus/impeccable", "https://github.com/pbakaus/impeccable", "Rust", 89407, 1506,
     "impeccable：「让你的 AI harness 更懂设计的设计语言」。与 hallmark 同处一条赛道——给 AI 编码智能体注入设计规范与审美约束，让智能体产出的界面不再廉价，累计 Star 89,407。"),
    ("NVIDIA/SkillSpector", "https://github.com/NVIDIA/SkillSpector", "Python", 22363, 214,
     "SkillSpector：NVIDIA 官方推出的 AI 智能体技能安全扫描器——在安装前检测 Claude Code、Codex 与 MCP 技能中的漏洞、恶意模式、提示注入、数据外泄与供应链风险。英伟达官方下场「智能体技能安全」赛道，为本自动化有记录以来首次登榜，累计 Star 22,363。"),
    ("pollen-robotics/microduck", "https://github.com/pollen-robotics/microduck", "Rust", 12505, 843,
     "microduck：Pollen Robotics（Hugging Face 旗下）开源的迷你双足鸭子机器人——用 Rust 编写，是具身智能/机器人方向罕见的「萌系」硬件项目。今日唯一非 AI 相关项目，图形/硬件方向读者可关注，累计 Star 12,505。"),
    ("nightly-labs/openbot", "https://github.com/nightly-labs/openbot", "TypeScript", 1608, 176,
     "openbot：本地优先（local-first）的桌面工作区，用于持久的 AI 队友——为 Codex、Claude、Grok 提供专属工作区、任务队列、文件共享、浏览器控制与智能体间协作。「多智能体协作工作台」方向的早期项目，累计 Star 仅 1,608，值得关注其成长。"),
    ("Panniantong/Agent-Reach", "https://github.com/Panniantong/Agent-Reach", "Python", 103916, 746,
     "Agent-Reach：给你的 AI 智能体「看整个互联网的眼睛」——一个 CLI 即可读取与搜索 Twitter、Reddit、YouTube、GitHub、B站、小红书，零 API 费用。智能体「内容触达层」的代表项目，累计 Star 103,916，为本自动化有记录以来首次登榜。"),
    ("debpalash/VoiceStudio", "https://github.com/debpalash/VoiceStudio", "Python", 89638, 2297,
     "VoiceStudio：开源、完全本地的 ElevenLabs 替代品——支持 646 种语言的语音克隆、音色设计、视频配音、听写、转写与有声书制作。本地 AI 语音赛道的标杆项目，今日涨星最快，累计 Star 89,638。"),
    ("gitroomhq/postiz-app", "https://github.com/gitroomhq/postiz-app", "TypeScript", 38600, 188,
     "postiz-app：终极 agentic 社交媒体定时发布工具——一个工具管理多平台内容排期。「智能体化（agentic）」正在吞噬各类工具品类，社媒运营也不例外，累计 Star 38,600，为本自动化有记录以来首次登榜。"),
    ("alchaincyf/huashu-design", "https://github.com/alchaincyf/huashu-design", "HTML", 27107, 251,
     "huashu-design：花叔的 HTML-native 设计技能（Claude Code / Codex / Cursor 及任意智能体可用）——在 agent 里打一句话，拿回能交付的设计：网页 / App 原型 / 可编辑 PPTX / 动画 / 信息图，六个候选挑三个方向、84 种带样张的风格库，越用越懂你的外观账本与设计体检。国产智能体设计技能的头部项目，累计 Star 27,107，为本自动化有记录以来首次登榜。"),
    ("multica-ai/andrej-karpathy-skills", "https://github.com/multica-ai/andrej-karpathy-skills", "", 224806, 638,
     "andrej-karpathy-skills：单个 CLAUDE.md 文件改进 Claude Code 行为——提炼自 Andrej Karpathy 对 LLM 编码陷阱（coding pitfalls）的观察。「Karpathy 方法论」被产品化为开箱即用的智能体配置，借大佬之名自带传播力，累计 Star 224,806，为本自动化有记录以来首次登榜。"),
]

# Today's data-driven insight categories (keyword -> matched repos, computed at runtime).
CATS = {
    "智能体技能生态（设计 / 安全 / 方法论）": ["hallmark", "impeccable", "skills", "huashu-design"],
    "AI Agent 产品与协作工作台": ["cindy", "thinkrail", "openbot", "harness"],
    "智能体内容触达与社交媒体": ["Agent-Reach", "postiz"],
    "本地 AI 语音": ["VoiceStudio"],
    "金融多智能体": ["TradingAgents"],
    "硬件机器人": ["microduck"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"Nutlope/hallmark", "TauricResearch/TradingAgents", "JetBrains/thinkrail",
            "makecindy/cindy", "affaan-m/ECC", "pbakaus/impeccable",
            "NVIDIA/SkillSpector", "nightly-labs/openbot", "Panniantong/Agent-Reach",
            "debpalash/VoiceStudio", "gitroomhq/postiz-app",
            "alchaincyf/huashu-design", "multica-ai/andrej-karpathy-skills"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    max_cnt = max(lang_stats.values())
    top_langs = sorted([l for l, c in lang_stats.items() if c == max_cnt])
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins = []
    if top[0] == rank1[0]:
        ins.append(f'<li><b>{top[0]} 今日涨星最快、同时位居榜单首位</b>：单日新增 <b>+{top[4]:,}</b> Stars，为今日最高（GitHub 原始榜单首位与其一致，合并表述场景）。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')
    else:
        ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，但领先优势极小——GitHub 原始榜单首位 hallmark（+{rank1[4]:,}）仅落后 {top[4]-rank1[4]} 星，两位「设计/AI 语音」选手贴身缠斗。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    # language distribution
    if len(top_langs) > 1:
        lang_repos = [r[0].split("/")[-1] for r in repos if (r[2] or "无语言") in top_langs]
        ins.append(f'<li><b>多语言并驾齐驱</b>：{"、".join(top_langs)} 各占据 {max_cnt} 个 Trending 席位，并列第一（{"、".join(lang_repos)}）。</li>')
    else:
        lang_repos = [r[0].split("/")[-1] for r in repos if (r[2] or "无语言") in top_langs]
        others = "、".join(f"{l}（{lang_stats[l]}）" for l in sorted(lang_stats, key=lambda x: -lang_stats[x]) if l != top_langs[0])
        ins.append(f'<li><b>{top_langs[0]} 最为活跃</b>：占据 {max_cnt}/{len(repos)} 个 Trending 席位（{"、".join(lang_repos[:10])}），是今日绝对主力语言；其余席位分布：{others}。</li>')
    lang_line = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]))
    ins.append(f'<li><b>今日榜单覆盖 {len(lang_stats)} 种语言</b>：{lang_line}。其中 <b>CSS</b>（hallmark）与 <b>HTML</b>（huashu-design）各占一席——「设计技能」以样式语言登榜成为常态；另有无语言标注的 CLAUDE.md 技能仓（andrej-karpathy-skills）一席。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：{top[0].split("/")[-1]}（+{top[4]:,}）、{second[0].split("/")[-1]}（+{second[4]:,}）与 {third[0].split("/")[-1]}（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>，较上期 63% 继续回落；为本自动化近期分布最均衡的一期，无单一霸榜巨无霸。</li>')

    ins.append(f'<li><b>热度明显回升</b>：今日榜单新增合计 <b>+{total_today:,}</b> Stars，较上期 10-26（+9,181）回升约 {int(round((total_today-9181)/9181*100))}%，接近 10-21（+14,693）的水平。榜单规模 {len(repos)} 个（上期 11 个）。</li>')

    ai = [r for r in repos if r[0] in AI_NAMES]
    ai_names = "、".join(r[0].split("/")[-1] for r in ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(ai)}/{len(repos)}</b>：明确计入 AI 的是 {ai_names}。唯一不计入：microduck（双足鸭子机器人，硬件项目）。判定口径：本行已明示名单，读者可自行复算。</li>')

    ins.append('<li><b>新面孔 6 个、回归 1 个、延续 7 个</b>：新进 <b>NVIDIA/SkillSpector</b>（英伟达官方智能体技能安全扫描器，本自动化记录中首次登榜）、<b>Panniantong/Agent-Reach</b>（智能体互联网内容触达 CLI）、<b>gitroomhq/postiz-app</b>（agentic 社媒定时发布）、<b>alchaincyf/huashu-design</b>（花叔 HTML-native 设计技能）、<b>multica-ai/andrej-karpathy-skills</b>（Karpathy 方法论 CLAUDE.md）、<b>nightly-labs/openbot</b>（AI 队友桌面工作区）；回归项：ECC（上期 10-16）；延续项：hallmark、TradingAgents、thinkrail、cindy、impeccable、microduck、VoiceStudio。较上期掉榜 4 个：coolify、claude-seo、ziwei-doushu、security-audit-skill。</li>')

    ins.append('<li><b>主题观察：「设计 + 安全」双线包抄智能体技能层</b>——设计线三连：hallmark（反 AI 味）、impeccable（设计语言）、huashu-design（HTML-native 设计技能）同日登榜，「让智能体产出有设计感」已从隐含需求变成显性赛道；安全线由 NVIDIA 官方 SkillSpector 接棒（上期 security-audit-skill 恰好掉榜），大厂开始为「装技能」这一动作本身提供安全审计。另一看点：andrej-karpathy-skills 把 Karpathy 的 LLM 编码陷阱观察直接产品化成 CLAUDE.md，「名人方法论 → 智能体配置」成为新的内容变现形态。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 10, 27)
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
