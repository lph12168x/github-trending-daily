#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-04 (v95).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain-DNS direct
connection: rc=0, 568,391 bytes, complete document ending in </html>,
exactly 13 Box-row articles. Freshness verified: saved-file mtime
12:31:25 > pre-fetch time 12:31:02.
Cross-check: independent WebFetch (?since=daily) returned the SAME 13
repos, SAME order, SAME stars-today values. Total raw = +12,589 on both
views. Cumulative star counts: report uses the curl values (freshest).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks is NOT on today's list (no action needed).
p-e-w/heretic (+701 today, raw #6) is EXCLUDED again: its README states
the DEFAULT action is "Suppress refusals / remove censorship" -- a tool
whose primary purpose is bypassing AI safety guardrails, same family as
the jailbreak prompt collections excluded 10-28..11-03. No political-
sensitivity issues among the rest. Included: 12 repos, +11,888 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (10/12):
  * thedotmack/claude-mem          -- persistent memory layer for agents.
  * vercel-labs/agent-desktop      -- Computer use CLI for AI agents.
  * max-sixty/worktrunk            -- worktree CLI designed FOR parallel
                                      AI agent workflows (ponytail precedent).
  * JustVugg/colibri               -- local MoE inference engine (pure C).
  * mattpocock/skills              -- personal agent-skills library.
  * spotify/portal-ai-plugins      -- Spotify official plugins that bring
                                      the Portal developer portal into
                                      Claude Code / Codex / Cursor.
  * Usagi-org/ai-goofish-monitor   -- AI-powered Xianyu monitoring.
  * anomalyco/hex                  -- local AI voice dictation (counted
                                      AI per the 11-02 precedent).
  * shiyu-coder/Kronos             -- foundation model for financial markets.
  * Donchitos/Claude-Code-Game-Studios -- 49 AI agents game studio.
Not counted (2): Scrapling (web-scraping framework), floci (AWS local
emulator, PaaS-family precedent like coolify/supabase).

spotify/portal-ai-plugins has no description on the trending card; its
README (fetched via Contents API) describes it as Spotify Portal plugins
for coding agents -- description derived from that README.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-04"
TODAY_FMT = "2026年11月4日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass), minus the excluded heretic.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("thedotmack/claude-mem", "https://github.com/thedotmack/claude-mem", "TypeScript", 112103, 1139,
     "claude-mem：为每个智能体提供跨会话持久记忆——捕获会话中的全部操作、用 AI 压缩，并在未来会话中注入相关上下文；兼容 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等主流工具。智能体记忆层明星项目连续第四日在榜，并位居 GitHub 原始榜单首位（但涨幅列第五，按新增重排），累计 Star 达 112,103（11.2 万）。"),
    ("vercel-labs/agent-desktop", "https://github.com/vercel-labs/agent-desktop", "Rust", 13178, 3791,
     "agent-desktop：面向 AI 智能体的 Computer use CLI——让智能体直接操控你的电脑桌面。Vercel 官方实验室出品，连续第二日在榜并蝉联今日涨幅榜首（唯一破三千），累计 Star 13,178。"),
    ("max-sixty/worktrunk", "https://github.com/max-sixty/worktrunk", "Rust", 10598, 438,
     "worktrunk：面向并行 AI 智能体工作流设计的 Git worktree 管理 CLI——为多智能体并行开发而生的工作树切换与管理工具。连续第二日在榜，累计 Star 10,598、站稳万级。"),
    ("JustVugg/colibri", "https://github.com/JustVugg/colibri", "C", 47343, 802,
     "colibri：面向前沿 MoE 模型的分层推理引擎——热专家驻 GPU（CUDA、Vulkan）、温专家驻内存、冷专家从 NVMe 流式加载；用纯 C 编写、跑在你已有的硬件上。连续第二日在榜，累计 Star 47,343。"),
    ("mattpocock/skills", "https://github.com/mattpocock/skills", "Shell", 311664, 1164,
     "skills：Matt Pocock（TypeScript 教育领域知名作者）开源的个人智能体技能库——Skills for Real Engineers，直接来自他的 .agents 目录。连续第二日在榜，累计 Star 达 311,664（31 万+）。"),
    ("spotify/portal-ai-plugins", "https://github.com/spotify/portal-ai-plugins", "TypeScript", 3082, 91,
     "portal-ai-plugins：Spotify 官方出品的 Portal AI 插件——把 Spotify Portal 开发者门户接入 Claude Code、Codex、Cursor、pi 等编程智能体：自然语言检索软件目录与技术文档、生成服务简报、运行诊断、安全调用 Portal 动作；另附 shunt 插件，把批量读文件/样板代码等 I/O 密集型智能体工作路由到更便宜的 worker 模型以省 token。大厂官方入场智能体插件生态的新面孔首次登榜，累计 Star 3,082（榜单无官方简介，简介取自项目 README）。"),
    ("floci-io/floci", "https://github.com/floci-io/floci", "Java", 28949, 482,
     "floci：轻量、免费、开箱即用的 AWS 本地模拟器（The AWS Local Emulator alternative）——在本地完整模拟 AWS 服务用于开发与测试。新面孔首次登榜，累计 Star 28,949。"),
    ("Usagi-org/ai-goofish-monitor", "https://github.com/Usagi-org/ai-goofish-monitor", "Python", 16672, 228,
     "ai-goofish-monitor：基于 Playwright 与 AI 实现的闲鱼多任务实时/定时监控与智能分析系统——配备功能完善的后台管理 UI，帮助用户从闲鱼海量商品中找到心仪产品。新面孔首次登榜，累计 Star 16,672。"),
    ("anomalyco/hex", "https://github.com/anomalyco/hex", "Rust", 4690, 410,
     "hex：本地语音听写工具（Local voice dictation）——支持 macOS、Windows 与 Linux，语音转文字全程在本地完成、数据不出设备。回归项目（上次 11-02），累计 Star 4,690。"),
    ("D4Vinci/Scrapling", "https://github.com/D4Vinci/Scrapling", "Python", 95138, 1658,
     "Scrapling：自诩「最强」的 Python 网页抓取框架——从单个请求到全站爬取一站式搞定（handles everything from a single request to a full-scale crawl）。连续第二日在榜，累计 Star 95,138、逼近 10 万。"),
    ("shiyu-coder/Kronos", "https://github.com/shiyu-coder/Kronos", "Python", 46584, 503,
     "Kronos：金融市场语言的基础模型（A Foundation Model for the Language of Financial Markets）——把 K 线等金融时序当作一门「语言」建模的开源基座模型。连续第三日在榜，累计 Star 46,584。"),
    ("Donchitos/Claude-Code-Game-Studios", "https://github.com/Donchitos/Claude-Code-Game-Studios", "Shell", 34807, 1182,
     "Claude-Code-Game-Studios：把 Claude Code 变成完整的游戏开发工作室——49 个 AI 智能体、72 个工作流技能，外加一套对标真实工作室层级的完整协作系统。「智能体组织化」方向连续第四日在榜，累计 Star 34,807。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体控制面与记忆": ["claude-mem"],
    "给智能体一台电脑": ["agent-desktop"],
    "金融 AI": ["Kronos"],
    "端侧/本地化 AI": ["colibri", "hex"],
    "智能体组织与工作流": ["Game-Studios", "worktrunk", "mattpocock/skills", "portal-ai-plugins"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"thedotmack/claude-mem", "vercel-labs/agent-desktop", "max-sixty/worktrunk",
            "JustVugg/colibri", "mattpocock/skills", "spotify/portal-ai-plugins",
            "Usagi-org/ai-goofish-monitor", "anomalyco/hex", "shiyu-coder/Kronos",
            "Donchitos/Claude-Code-Game-Studios"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（唯一破三千，连续第二日登顶）；而 GitHub 原始榜单首位是 claude-mem（+{rank1[4]:,}，涨幅列第五）——<b>两者不一致</b>。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 各以 {maxc}/{len(repos)} 并列居首</b>：Rust（agent-desktop、worktrunk、hex）与 Python（ai-goofish-monitor、Scrapling、Kronos）平分秋色；其余分布：{others}，共 {len(lang_stats)} 种语言。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：agent-desktop（+{top[4]:,}）、Scrapling（+{second[4]:,}）与 Game-Studios（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 portal-ai-plugins 的 +91 收尾。</li>')

    delta_pct = int(round(abs(total_today - 14166) / 14166 * 100))
    ins.append(f'<li><b>热度回落</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-03（+14,166 / 14 个仓库）回落约 <b>{delta_pct}%</b>，仓库数减少 2 个。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 2 个为 Scrapling（网页抓取框架）、floci（AWS 本地模拟器，按 coolify/supabase 先例不计）。另注：原始榜单第 6 位的 p-e-w/heretic（+701）README 自述默认动作即「移除模型安全拒绝/审查」，属绕过 AI 安全防护类，与 jailbreaks 同口径剔除、不予收录（连续第二日）。</li>')

    ins.append('<li><b>新面孔 3 个、回归 1 个、延续 8 个、掉榜 6 个</b>：新进 <b>spotify/portal-ai-plugins</b>（Spotify 官方智能体插件，大厂入场）、<b>floci-io/floci</b>（AWS 本地模拟器）、<b>Usagi-org/ai-goofish-monitor</b>（AI 闲鱼监控）；回归 <b>anomalyco/hex</b>（上次 11-02）；延续：claude-mem、agent-desktop、worktrunk、colibri、skills、Game-Studios、Kronos、Scrapling。较上期掉榜 6 个：t3code、FreeToken、Hyprland、kornia、paperclip、nanochat。</li>')

    ins.append('<li><b>主题观察：「智能体生态」全线延续 + 大厂官方入场</b>——记忆层（claude-mem 连续第四日）、电脑（agent-desktop 连续第二日登顶涨幅榜）、组织化（Game-Studios 连续第四日）、工作管理（worktrunk、mattpocock/skills）热度不减；本日最大新意是 <b>Spotify 官方 portal-ai-plugins</b>：把内部开发者门户接入 Claude Code/Codex/Cursor，并附 shunt 插件把 I/O 密集工作路由到便宜模型——「企业门户 × 编程智能体」成为新叙事。另一条主线仍是<b>端侧本地化</b>：colibri（纯 C 分层 MoE 推理）与 hex（本地语音听写）分别代表「本地跑模型」与「本地传数据」两个层面；floci 则把「本地化」延伸到云服务模拟。ai-goofish-monitor 展示 AI 监控类应用的持续人气。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：mattpocock/skills 累计 Star 达 <b>311,664</b>（31 万+）、claude-mem 站上 <b>11.2 万</b>（112,103）、Scrapling 9.5 万逼近 10 万、Game-Studios 破 3.4 万、colibri 逼近 4.8 万；新面孔 portal-ai-plugins（3,082）体量最小。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 4)
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
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today (excl. heretic +701)")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
