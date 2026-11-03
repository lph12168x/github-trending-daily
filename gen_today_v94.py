#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-03 (v94).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain-DNS direct
connection: rc=0, 589,844 bytes, complete document ending in </html>,
exactly 15 Box-row articles. Freshness verified: saved-file mtime
12:31:44 > pre-fetch time 12:31:17.
Cross-check: independent WebFetch (?since=daily) returned the SAME 15
repos, SAME order, SAME stars-today values. Total raw = +14,586 on both
views. Cumulative star counts: report uses the curl values (freshest).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks is NOT on today's list (no action needed).
p-e-w/heretic (+420 today, raw #15) is EXCLUDED: its README states the
DEFAULT action is "Suppress refusals / remove censorship" -- a tool
whose primary purpose is bypassing AI safety guardrails, same family
as the jailbreak prompt collections excluded 10-28..11-02. No political-
sensitivity issues among the rest. Included: 14 repos, +14,166 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (11/14):
  * pingdotgg/t3code               -- agent harness control surface.
  * vercel-labs/agent-desktop      -- Computer use CLI for AI agents.
  * thedotmack/claude-mem          -- persistent memory layer for agents.
  * Donchitos/Claude-Code-Game-Studios -- 49 AI agents game studio.
  * mattpocock/skills              -- personal agent-skills library.
  * shiyu-coder/Kronos             -- foundation model for financial markets.
  * JustVugg/colibri               -- local MoE inference engine (pure C).
  * FlashML-org/FreeToken          -- local LLM serving on desktop.
  * max-sixty/worktrunk            -- worktree CLI designed FOR parallel
                                      AI agent workflows (agent-ecosystem
                                      tooling, ponytail precedent).
  * paperclipai/paperclip          -- app to manage agents at work.
  * karpathy/nanochat              -- full ChatGPT stack (train+serve).
Not counted (3): Scrapling (web-scraping framework), Hyprland (Wayland
compositor), kornia (CV library; "Spatial AI" marketing but classical
CV toolset -- counted NO conservatively, same as 11-02).

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-03"
TODAY_FMT = "2026年11月3日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass), minus the excluded heretic.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("vercel-labs/agent-desktop", "https://github.com/vercel-labs/agent-desktop", "Rust", 10391, 2275,
     "agent-desktop：面向 AI 智能体的 Computer use CLI——让智能体直接操控你的电脑桌面。Vercel 官方实验室出品，新面孔首次登榜即位居 GitHub 原始榜单首位（但涨幅列第二，按新增重排），累计 Star 10,391。"),
    ("thedotmack/claude-mem", "https://github.com/thedotmack/claude-mem", "TypeScript", 110937, 1803,
     "claude-mem：为每个智能体提供跨会话持久记忆——捕获会话中的全部操作、用 AI 压缩，并在未来会话中注入相关上下文；兼容 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流工具。智能体记忆层明星项目连续第三日在榜，累计 Star 达 110,937（11 万+）。"),
    ("D4Vinci/Scrapling", "https://github.com/D4Vinci/Scrapling", "Python", 93183, 706,
     "Scrapling：自诩「最强」的 Python 网页抓取框架——从单个请求到全站爬取一站式搞定（handles everything from a single request to a full-scale crawl）。新面孔首次登榜，累计 Star 93,183、逼近 10 万。"),
    ("hyprwm/Hyprland", "https://github.com/hyprwm/Hyprland", "C++", 40021, 509,
     "Hyprland：独立、高度可定制的动态平铺 Wayland 合成器（dynamic tiling Wayland compositor），颜值与功能兼得。Linux 桌面生态明星项目连续第二日在榜，累计 Star 40,021。"),
    ("Donchitos/Claude-Code-Game-Studios", "https://github.com/Donchitos/Claude-Code-Game-Studios", "Shell", 33766, 1379,
     "Claude-Code-Game-Studios：把 Claude Code 变成完整的游戏开发工作室——49 个 AI 智能体、72 个工作流技能，外加一套对标真实工作室层级的完整协作系统。「智能体组织化」方向连续第三日在榜，累计 Star 33,766。"),
    ("FlashML-org/FreeToken", "https://github.com/FlashML-org/FreeToken", "Python", 16206, 653,
     "FreeToken：把数据中心级模型服务搬上桌面（datacenter-scale model serving to your desktop）——在本地快速高效地运行大模型。端侧本地化方向连续第二日在榜，累计 Star 16,206。"),
    ("pingdotgg/t3code", "https://github.com/pingdotgg/t3code", "TypeScript", 42327, 3229,
     "t3code：T3 Code「智能体 harness 控制面」（agent harness control surface）——用 iOS/Android App、Web 与桌面端远程操控你电脑上的 Claude Code、Codex、Cursor、OpenCode 等编程智能体；官方强调「不卖任何东西、方向跑偏随时可 fork」。Theo（t3dotgg）出品，连续第二日在榜并蝉联今日涨幅榜首（唯一破三千；榜单无官方简介，简介取自项目 README），累计 Star 42,327。"),
    ("shiyu-coder/Kronos", "https://github.com/shiyu-coder/Kronos", "Python", 46070, 857,
     "Kronos：金融市场语言的基础模型（A Foundation Model for the Language of Financial Markets）——把 K 线等金融时序当作一门「语言」建模的开源基座模型。连续第二日在榜，累计 Star 46,070。"),
    ("kornia/kornia", "https://github.com/kornia/kornia", "Python", 12183, 412,
     "kornia：面向空间 AI（Spatial AI）的几何计算机视觉库——可微 CV 算法层，服务于三维重建、SLAM 等空间智能场景。连续第二日在榜，累计 Star 12,183。"),
    ("JustVugg/colibri", "https://github.com/JustVugg/colibri", "C", 46694, 675,
     "colibri：用纯 C、零依赖在你已有的硬件上运行前沿 MoE 模型——专家权重直接从磁盘流式加载（experts streamed from disk），小引擎跑大模型（Tiny engine, immense model）。新面孔首次登榜，累计 Star 46,694。"),
    ("mattpocock/skills", "https://github.com/mattpocock/skills", "Shell", 310400, 858,
     "skills：Matt Pocock（TypeScript 教育领域知名作者）开源的个人智能体技能库——Skills for Real Engineers，直接来自他的 .agents 目录。新面孔首次登榜，累计 Star 已达 310,400（30 万+）。"),
    ("max-sixty/worktrunk", "https://github.com/max-sixty/worktrunk", "Rust", 10116, 77,
     "worktrunk：面向并行 AI 智能体工作流设计的 Git worktree 管理 CLI——为多智能体并行开发而生的工作树切换与管理工具。新面孔首次登榜，累计 Star 破万（10,116）。"),
    ("paperclipai/paperclip", "https://github.com/paperclipai/paperclip", "TypeScript", 110512, 412,
     "paperclip：开源的工作智能体管理应用（The open-source app everyone uses to manage agents at work）——把团队日常使用的各类智能体集中到一个界面统一管理。新面孔首次登榜，累计 Star 110,512（11 万）。"),
    ("karpathy/nanochat", "https://github.com/karpathy/nanochat", "Python", 59984, 321,
     "nanochat：Andrej Karpathy 出品的「100 美元能买到的最好的 ChatGPT」——覆盖预训练、微调到推理服务的完整 ChatGPT 复刻教学栈。新面孔首次登榜，累计 Star 59,984、逼近 6 万。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体控制面与记忆": ["t3code", "claude-mem"],
    "给智能体一台电脑": ["agent-desktop"],
    "金融 AI": ["Kronos"],
    "端侧/本地化 AI": ["FreeToken", "colibri", "nanochat"],
    "智能体组织与工作流": ["Game-Studios", "paperclip", "worktrunk", "mattpocock/skills"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"pingdotgg/t3code", "vercel-labs/agent-desktop", "thedotmack/claude-mem",
            "Donchitos/Claude-Code-Game-Studios", "mattpocock/skills", "shiyu-coder/Kronos",
            "JustVugg/colibri", "FlashML-org/FreeToken", "max-sixty/worktrunk",
            "paperclipai/paperclip", "karpathy/nanochat"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（唯一破三千）；而 GitHub 原始榜单首位是 agent-desktop（+{rank1[4]:,}，涨幅列第二）——<b>两者不一致</b>。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 以 {maxc}/{len(repos)} 居首</b>：Python（Scrapling、FreeToken、Kronos、kornia、nanochat）独占鳌头；其余分布：{others}，共 {len(lang_stats)} 种语言。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：t3code（+{top[4]:,}）、agent-desktop（+{second[4]:,}）与 claude-mem（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 worktrunk 的 +77 收尾。</li>')

    delta_pct = int(round(abs(total_today - 12940) / 12940 * 100))
    ins.append(f'<li><b>热度续升、榜单小幅收窄</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-02（+12,940 / 16 个仓库）回升约 <b>{delta_pct}%</b>，仓库数减少 2 个——增量更高但更集中于头部。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 3 个为 Scrapling（网页抓取框架）、Hyprland（Wayland 合成器）、kornia（几何 CV 库，从保守口径不计入）。另注：原始榜单第 15 位的 p-e-w/heretic（+420）README 自述默认动作即「移除模型安全拒绝/审查」，属绕过 AI 安全防护类，与 jailbreaks 同口径剔除、不予收录。</li>')

    ins.append('<li><b>新面孔 7 个、延续 7 个、掉榜 9 个</b>：新进 <b>vercel-labs/agent-desktop</b>（Computer use CLI，首次登榜即原始榜单首位）、<b>D4Vinci/Scrapling</b>（网页抓取框架）、<b>JustVugg/colibri</b>（纯 C 本地 MoE 引擎）、<b>mattpocock/skills</b>（个人智能体技能库）、<b>max-sixty/worktrunk</b>（面向智能体工作流的 worktree CLI）、<b>paperclipai/paperclip</b>（工作智能体管理）、<b>karpathy/nanochat</b>（Karpathy 完整 ChatGPT 教学栈）；延续：t3code、claude-mem、Claude-Code-Game-Studios、Kronos、FreeToken、kornia、Hyprland。较上期掉榜 9 个：ai-engineering-hub、hex、ziwei-doushu、OpenMausBot、lightpanda、AiSOC、Handy、public-apis、CopilotKit/OpenBot。</li>')

    ins.append('<li><b>主题观察：「智能体运行时」继续补全 + 端侧本地化三连</b>——控制面（t3code）、记忆层（claude-mem）、电脑（agent-desktop 的 Computer use）、组织化（Game-Studios 连续第三日）、工作管理（paperclip、worktrunk、mattpocock/skills 的技能层）同日或连日在榜，「智能体运行时」栈愈发完整；另一条主线是<b>端侧本地化</b>：FreeToken（桌面级模型服务）、colibri（纯 C 磁盘流式 MoE）、nanochat（Karpathy 亲民版完整 ChatGPT 栈）同时登榜——「在自己的硬件上跑自己的模型」成为与云端智能体并行的第二叙事。Kronos 则代表金融 AI 基座模型的持续热度。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：mattpocock/skills 累计 Star 达 <b>310,400</b>（30 万+）、claude-mem 站上 <b>11.1 万</b>（110,937）、paperclip <b>11 万</b>（110,512）、Scrapling 9.3 万逼近 10 万、nanochat 逼近 6 万、worktrunk 破万；而新面孔 worktrunk（10,116）体量最小，「新老兵共存」格局延续。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 3)
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
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today (excl. heretic +420)")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
