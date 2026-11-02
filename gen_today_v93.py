#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-02 (v93).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
The sandbox could NOT reach github.com directly on the first pass this
morning: every edge IP timed out (rc=56 / connect timeout) except
20.27.177.113, which returned HTTP 200 but throttled the body to 0 bytes
within 280 s. Public CORS proxies (codetabs 522 / allorigins 408 /
r.jina.ai unreachable) all failed too. A background retry of
fetch_trending_curl.py then succeeded via `--resolve 140.82.113.3`:
rc=0, 615,592 bytes, complete document ending in </html>, exactly
17 Box-row articles -> today's list is really 17 repos, NOT a truncation
artifact. Freshness verified: saved-file mtime 09:57:46 > pre-fetch time.
Cross-check: two independent WebFetch passes returned the SAME 17 repos,
SAME order, SAME stars-today values. Total raw = +13,666 on both views.
Cumulative star counts: report uses the curl values (freshest source).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks (+726 today, raw list #14) is EXCLUDED again
(fourth consecutive day): curated jailbreak prompt collection, same
family as circumvention / access-evasion content. No political-
sensitivity issues among the rest. Included: 16 repos, +12,940 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (11/16):
  * pingdotgg/t3code               -- agent harness control surface (README).
  * thedotmack/claude-mem          -- persistent memory layer for agents.
  * patchy631/ai-engineering-hub   -- LLM / RAG / agent tutorials.
  * anomalyco/hex                  -- local voice dictation (AI org; see note).
  * Donchitos/Claude-Code-Game-Studios -- 49 AI agents game studio.
  * milind-soni/OpenMausBot        -- open-source Grok Bot alt (VM for bots).
  * lightpanda-io/browser          -- headless browser designed FOR AI.
  * shiyu-coder/Kronos             -- foundation model for financial markets.
  * beenuar/AiSOC                  -- AI security operations center.
  * CopilotKit/OpenBot             -- open-source AI coworkers (AG-UI).
  * FlashML-org/FreeToken          -- local LLM serving on desktop.
Not counted (5): public-apis (API list), Handy (offline STT app),
kornia (CV library; "Spatial AI" marketing but a classical CV toolset --
counted NO to stay conservative), ziwei-doushu (fortune-chart engine),
Hyprland (Wayland compositor).
NOTE on hex/Handy: both are local voice-dictation / STT apps; hex is by
anomalyco (the org behind opencode) so counted AI, Handy is not agent-
ecosystem, counted NO. kornia counted NO conservatively.

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-02"
TODAY_FMT = "2026年11月2日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against two independent WebFetch passes), minus the excluded jailbreaks.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("thedotmack/claude-mem", "https://github.com/thedotmack/claude-mem", "TypeScript", 109366, 1526,
     "claude-mem：为每个智能体提供跨会话持久记忆——捕获会话中的全部操作、用 AI 压缩，并在未来会话中注入相关上下文；兼容 Claude Code、OpenClaw、Codex、Gemini、Copilot 等主流工具。智能体记忆层明星项目连续第二日在榜并位居 GitHub 原始榜单首位（但涨幅列第二，按新增重排），累计 Star 109,366。"),
    ("lightpanda-io/browser", "https://github.com/lightpanda-io/browser", "Zig", 40205, 825,
     "lightpanda：为 AI 与自动化而生的无头浏览器（the headless browser designed for AI and automation）——性能优先的浏览器基础设施，专为智能体抓取与自动化场景设计。时隔近两个月（上次在榜 09-08）回归，累计 Star 破 4 万（40,205）。"),
    ("shiyu-coder/Kronos", "https://github.com/shiyu-coder/Kronos", "Python", 45427, 630,
     "Kronos：金融市场语言的基础模型（A Foundation Model for the Language of Financial Markets）——把 K 线等金融时序当作一门「语言」建模的开源基座模型。时隔约两周（上次在榜 10-21）回归，累计 Star 45,427。"),
    ("pingdotgg/t3code", "https://github.com/pingdotgg/t3code", "TypeScript", 38152, 3094,
     "t3code：T3 Code「智能体 harness 控制面」（agent harness control surface）——用 iOS/Android App、Web 与桌面端远程操控你电脑上的 Claude Code、Codex、Cursor、Grok Build、OpenCode、Antigravity 等编程智能体；官方强调「不卖任何东西、方向跑偏随时可 fork」。Theo（t3dotgg）出品，时隔近三个月（上次在榜 08-11）回归并直接登顶今日涨幅榜（唯一破三千；榜单无官方简介，简介取自项目 README），累计 Star 38,152。"),
    ("milind-soni/OpenMausBot", "https://github.com/milind-soni/OpenMausBot", "TypeScript", 10586, 922,
     "OpenMausBot：开源的 Grok Bot 替代品——自带一台可供 bot 使用的虚拟机（a virtual machine that bots can use）。「给智能体一台电脑」方向延续在榜，累计 Star 10,586。"),
    ("public-apis/public-apis", "https://github.com/public-apis/public-apis", "Python", 494663, 324,
     "public-apis：免费 API 大全（A collective list of free APIs）——GitHub 史上最著名的聚合仓库之一。老牌巨型仓库时隔两个半月（上次在榜 08-19）回归，累计 Star 已达 494,663、逼近 50 万。"),
    ("cjpais/Handy", "https://github.com/cjpais/Handy", "Rust", 36604, 339,
     "Handy：免费、开源、可扩展的完全离线语音转文字应用（a speech-to-text application that works completely offline）——本地运行、隐私优先。新面孔首次登榜，累计 Star 36,604。"),
    ("Donchitos/Claude-Code-Game-Studios", "https://github.com/Donchitos/Claude-Code-Game-Studios", "Shell", 32357, 967,
     "Claude-Code-Game-Studios：把 Claude Code 变成完整的游戏开发工作室——49 个 AI 智能体、72 个工作流技能，外加一套对标真实工作室层级的完整协作系统。「智能体组织化」方向连续第二日在榜，累计 Star 32,357。"),
    ("kornia/kornia", "https://github.com/kornia/kornia", "Python", 11820, 101,
     "kornia：面向空间 AI（Spatial AI）的几何计算机视觉库——可微 CV 算法层，服务于三维重建、SLAM 等空间智能场景。老牌 CV 库新面孔首次登榜，累计 Star 11,820。"),
    ("beenuar/AiSOC", "https://github.com/beenuar/AiSOC", "Python", 6258, 446,
     "AiSOC：开源 AI 安全运营中心（Security Operations Center）——告警融合、LLM 智能体分诊、MITRE ATT&CK 调查，每个智能体步骤都有可回放的决策账本；自托管、无需 API Key、MIT 协议，自带 MCP server。新面孔首次登榜，累计 Star 6,258。"),
    ("Renhuai123/ziwei-doushu", "https://github.com/Renhuai123/ziwei-doushu", "TypeScript", 13190, 941,
     "ziwei-doushu：紫微斗数开源排盘引擎——基于倪海厦《天纪》体系，含完整排盘算法、四化系统、格局知识库与古籍原文数据。传统文化 + 开源工程结合的中文项目时隔一周（上次在榜 10-26）回归，累计 Star 13,190。"),
    ("anomalyco/hex", "https://github.com/anomalyco/hex", "Rust", 3335, 1179,
     "hex：anomalyco 出品的本地语音听写工具（Local voice dictation for mac, windows and linux）——完全本地运行、隐私优先；该组织此前曾以 anomalyco/opencode 登榜，本次为 hex 本体新面孔首次登榜，累计 Star 3,335。"),
    ("CopilotKit/OpenBot", "https://github.com/CopilotKit/OpenBot", "TypeScript", 9551, 175,
     "OpenBot：开源 AI 同事（AI coworkers）——每个智能体分到一台自己的电脑：浏览器、文件与工具，每步操作先决定后执行、全程留痕；支持接入任意 AG-UI 智能体。CopilotKit 官方出品，连续第二日在榜，累计 Star 9,551。"),
    ("patchy631/ai-engineering-hub", "https://github.com/patchy631/ai-engineering-hub", "Jupyter Notebook", 40303, 1191,
     "ai-engineering-hub：LLM、RAG 与真实世界 AI 智能体应用的深度教程合集（In-depth tutorials on LLMs, RAGs and real-world AI agent applications）——AI 工程学习型仓库的常青树。新面孔首次登榜，累计 Star 40,303。"),
    ("FlashML-org/FreeToken", "https://github.com/FlashML-org/FreeToken", "Python", 15437, 242,
     "FreeToken：把数据中心级模型服务搬上桌面（datacenter-scale model serving to your desktop）——在本地快速高效地运行大模型。新面孔首次登榜，累计 Star 15,437。"),
    ("hyprwm/Hyprland", "https://github.com/hyprwm/Hyprland", "C++", 39399, 38,
     "Hyprland：独立、高度可定制的动态平铺 Wayland 合成器（dynamic tiling Wayland compositor），颜值与功能兼得。Linux 桌面生态明星项目时隔三个多月（上次在榜 07-23）回归，累计 Star 39,399。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "智能体控制面与记忆": ["t3code", "claude-mem"],
    "给智能体一台电脑": ["OpenMausBot", "OpenBot"],
    "金融 AI": ["Kronos"],
    "端侧/本地化 AI": ["hex", "Handy", "FreeToken"],
    "AI 安防": ["AiSOC"],
    "传统文化开源": ["ziwei-doushu"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"pingdotgg/t3code", "thedotmack/claude-mem", "patchy631/ai-engineering-hub",
            "anomalyco/hex", "Donchitos/Claude-Code-Game-Studios", "milind-soni/OpenMausBot",
            "lightpanda-io/browser", "shiyu-coder/Kronos", "beenuar/AiSOC",
            "CopilotKit/OpenBot", "FlashML-org/FreeToken"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars（唯一破三千）；而 GitHub 原始榜单首位是 claude-mem（+{rank1[4]:,}，涨幅列第二）——<b>两者不一致</b>。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 各 {maxc}/16 并列居首</b>：TypeScript（t3code、OpenMausBot、ziwei-doushu、claude-mem、OpenBot）与 Python（Kronos、public-apis、kornia、AiSOC、FreeToken）平分秋色；其余分布：{others}，共 {len(lang_stats)} 种语言。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：t3code（+{top[4]:,}）、claude-mem（+{second[4]:,}）与 ai-engineering-hub（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾跨度极大——从 +1,179 一直到 Hyprland 的 +38。</li>')

    delta_pct = int(round(abs(total_today - 10982) / 10982 * 100))
    ins.append(f'<li><b>热度回升、榜单扩容</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（16 个仓库），较上期 10-30（+10,982 / 10 个仓库，中间隔两日）回升约 <b>{delta_pct}%</b>，仓库数增加 6 个，为近期最热闹的一天。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 5 个为 public-apis（API 清单）、Handy（离线语音转写 App）、kornia（几何 CV 库，从保守口径不计入）、ziwei-doushu（紫微斗数排盘引擎）、Hyprland（Wayland 合成器）。另注：原始榜单第 14 位的 togg53192-cmd/jailbreaks（+726）为越狱提示词合集，连续第四日按内容口径剔除、不予收录。</li>')

    ins.append('<li><b>新面孔 6 个、回归 6 个、延续 4 个</b>：新进 <b>patchy631/ai-engineering-hub</b>（LLM/RAG/智能体教程合集）、<b>anomalyco/hex</b>（本地听写；组织曾以 opencode 登榜）、<b>cjpais/Handy</b>（离线语音转写）、<b>kornia/kornia</b>（几何 CV 库）、<b>beenuar/AiSOC</b>（AI 安全运营中心）、<b>FlashML-org/FreeToken</b>（桌面级模型服务）；回归：<b>t3code</b>（08-11）、<b>lightpanda</b>（09-08）、<b>Kronos</b>（10-21）、<b>public-apis</b>（08-19）、<b>ziwei-doushu</b>（10-26）、<b>Hyprland</b>（07-23）；延续：claude-mem、OpenMausBot、Claude-Code-Game-Studios、CopilotKit/OpenBot。较上期掉榜 6 个：impeccable、DeepTutor、ai-design-skills、thinkrail、superpowers、openbot。</li>')

    ins.append('<li><b>主题观察：智能体基础设施「全家桶」日</b>——t3code（远程控制面）、claude-mem（记忆层）、lightpanda（为 AI 而生的浏览器）、OpenMausBot / CopilotKit/OpenBot（给智能体一台电脑，连续第二日）、Claude-Code-Game-Studios（智能体组织化）同日或连日在榜，「智能体运行时」从单一工具走向完整基础设施栈；另一条暗线是<b>端侧本地化</b>：hex（本地听写）、Handy（离线转写）、FreeToken（桌面级模型服务）同时登榜。Kronos 把金融市场当作一门语言建模， ziwei-doushu 则代表中文传统文化 + 开源工程的独特路线。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：public-apis 累计 Star 达 <b>494,663</b>、逼近 50 万，claude-mem 站上 <b>10.9 万</b>（109,366），lightpanda 破 4 万；而新面孔 hex（3,335）与 AiSOC（6,258）体量最小，「新老兵共存」格局延续。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 2)
    base.TODAY_STR = TODAY_STR
    base.TODAY_FMT = TODAY_FMT
    base.REPOS = REPOS
    base.build_insights = build_insights  # gen_html looks this up in base's namespace
    # The TeX lesson: missing colors fall back to #888888. v26 lacks Zig.
    base.LANG_COLORS.update({"Zig": "#EC915C"})

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
    print(f"\nSummary: {len(REPOS)} repos, +{total_stars:,} stars today (excl. jailbreaks +726)")
    print("Top 3 by today stars:")
    for i, r in enumerate(sorted(REPOS, key=lambda x: -x[4])[:3], 1):
        print(f"  #{i} {r[0]} (+{r[4]:,} stars)")
    # Language color sanity check (the TeX lesson: missing colors fall back to #888888).
    missing = sorted({r[2] for r in REPOS if r[2] and r[2] not in base.LANG_COLORS})
    print("Languages missing color:", missing if missing else "none")
