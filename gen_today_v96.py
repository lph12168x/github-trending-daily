#!/usr/bin/env python3
"""Generate GitHub Trending report for 2026-11-09 (v96).

Data source: https://github.com/trending.

HOW THE DATA WAS OBTAINED
-------------------------
fetch_trending_curl.py succeeded on the FIRST pass via plain-DNS direct
connection: rc=0, 517,546 bytes, complete document ending in </html>,
exactly 9 Box-row articles. Freshness verified: saved-file mtime
09:49:31 > pre-fetch start 09:49:05.
Cross-check: independent WebFetch (?since=daily) returned the SAME 9
repos, SAME order, SAME stars-today values (2373/345/1439/32/815/875/
792/41/460). Total raw = +7,172 on both views. Cumulative star counts:
report uses the curl values (freshest).

CONTENT NOTE
------------
togg53192-cmd/jailbreaks and p-e-w/heretic are NOT on today's list
(no action needed). No political-sensitivity issues, no circumvention
tools among the 9. sherlock-project/sherlock is a well-known OSINT
username-reconnaissance tool -- legitimate, included. All 9 repos
included, +7,172 today.

AI / AGENT JUDGEMENT
--------------------
Explicit whitelist (not keyword scanning), per the 2026-09-29 lesson.
Counted as AI / Agent related (5/9):
  * milind-soni/OpenMausBot          -- open-source Grok Bot alternative
                                        (VM for bots), AI by nature.
  * anthropics/claude-quickstarts    -- official Claude API starter apps.
  * vercel-labs/agent-browser        -- browser automation CLI FOR AI
                                        agents (sibling of agent-desktop).
  * anthropics/skills                -- official public repo for Agent
                                        Skills (SKILL.md standard).
  * ranxianglei/billion-context      -- LLM context-compression plugin.
NOT counted (4), with precedent:
  * sherlock-project/sherlock        -- OSINT username hunting tool,
                                        no AI component.
  * dsx-ai-factory/nvke              -- NVIDIA Kubernetes Engine: GPU K8s
                                        management plane, infra product
                                        (coolify/supabase precedent), AI-
                                        adjacent only.
  * meta/astryx                      -- design system at its core; "agent
                                        ready" is a property, same family
                                        as dbx (built-in AI mentions, not
                                        an AI product). README verified.
  * google-deepmind/mujoco           -- physics simulator, no AI.

meta/astryx README verified via Contents API: Meta-internal design system
of 8 years powering 13,000+ apps, 150+ accessible components, React 19 +
StyleX, APIs/docs/CLI "designed so a person and an AI assistant build the
same way".

Reuses the polished light/dark HTML + MD + index generation engine from
gen_today_v26 by overriding its module globals.
"""

from datetime import date

import gen_today_v26 as base
import nav_utils

TODAY_STR = "2026-11-09"
TODAY_FMT = "2026年11月9日"

# (name, url, lang, total_stars, today_stars, desc_zh)
# Raw order below == order shown on github.com/trending today (verified
# against an independent WebFetch pass). All 9 included, no exclusions.
# The report itself is regenerated sorted by today's star gain.
REPOS = [
    ("sherlock-project/sherlock", "https://github.com/sherlock-project/sherlock", "Python", 103706, 2373,
     "sherlock：跨社交网络按用户名侦查社交账号的开源 OSINT 工具——输入一个用户名，即可在数百个社交平台上并行查找同名账号。开源情报领域最知名的项目之一，本自动化记录中首次登榜并直接登顶涨幅榜，累计 Star 达 103,706（10 万+）。"),
    ("dsx-ai-factory/nvke", "https://github.com/dsx-ai-factory/nvke", "Go", 870, 345,
     "nvke：NVIDIA Kubernetes Engine（NVKE）——英伟达官方出品、Preview 阶段的 GPU Kubernetes 管理面：平台团队把它装在自有裸金属 GPU 基础设施上，即可为客户创建并运营托管的 K8s 集群（每集群独立控制面与 etcd）。AI 算力基础设施新面孔首次登榜，累计 Star 870。"),
    ("milind-soni/OpenMausBot", "https://github.com/milind-soni/OpenMausBot", "TypeScript", 18321, 1439,
     "OpenMausBot：开源的 Grok Bot 替代品——自带一台供 Bot 使用的虚拟机（a virtual machine that bots can use），让 AI 机器人拥有可安全操作的完整运行环境。「给智能体一台电脑」赛道延续在榜，回归项目（上次 10-30），累计 Star 18,321。"),
    ("anthropics/claude-quickstarts", "https://github.com/anthropics/claude-quickstarts", "Python", 19457, 32,
     "claude-quickstarts：Anthropic 官方的 Claude API 快速上手项目集——一系列帮助开发者用 Claude API 快速构建可部署应用（含智能体应用）的官方示例库。官方新面孔首次登榜（今日 +32 为涨幅垫底，但原始榜单列第 4），累计 Star 19,457。"),
    ("vercel-labs/agent-browser", "https://github.com/vercel-labs/agent-browser", "Rust", 47653, 815,
     "agent-browser：面向 AI 智能体的浏览器自动化 CLI——Vercel Labs 出品，让智能体像操控桌面一样操控浏览器。与上周登榜的 agent-desktop 同门，「给智能体一台电脑/浏览器」赛道继续扩张，新面孔首次登榜，累计 Star 47,653。"),
    ("meta/astryx", "https://github.com/meta/astryx", "TypeScript", 16947, 875,
     "astryx：Meta 开源的设计系统——在 Meta 内部生长八年、支撑 13,000+ 应用后走向开源（Beta）；提供 150+ 无障碍组件、品牌级主题、暗色模式与 CLI，基于 React 19 + StyleX 构建，API 与文档专为「人和 AI 智能体用同一套工具协同开发」而设计。Meta 官方新面孔首次登榜，累计 Star 16,947。"),
    ("anthropics/skills", "https://github.com/anthropics/skills", "Python", 189699, 792,
     "skills：Anthropic 官方的智能体技能（Agent Skills）公共仓库——SKILL.md 开放标准的官方实现与示例集合，供 Claude 等智能体安装使用。继 mattpocock/skills（31 万）等社区技能库之后，「技能层」的官方源头仓库首次登榜，累计 Star 达 189,699（19 万）。"),
    ("google-deepmind/mujoco", "https://github.com/google-deepmind/mujoco", "C++", 16445, 41,
     "MuJoCo：Multi-Joint dynamics with Contact——DeepMind 维护的通用多关节接触动力学物理仿真引擎，机器人学与强化学习研究的标准工具，对图形/仿真方向的读者亦有参考价值。老牌项目本自动化记录中首次登榜，累计 Star 16,445。"),
    ("ranxianglei/billion-context", "https://github.com/ranxianglei/billion-context", "TypeScript", 5191, 460,
     "billion-context：LLM 上下文压缩插件——面向「月级长会话」（数十亿 token）设计：让 100K 的小上下文窗口撑起超长会话，并节省约 5 倍 token，「billion-context is all you need」。来自中国开发者的新面孔首次登榜，累计 Star 5,191。"),
]

# Categories for the "主题观察" auto-matching (matched against desc/name).
CATS = {
    "给智能体一台电脑": ["OpenMausBot", "agent-browser"],
    "上下文工程": ["billion-context"],
}

# Repos judged AI / Agent related today. Set explicitly rather than by keyword
# (the 2026-09-29 lesson: descriptions that merely mention AI would be
# mis-classified by a keyword scan).
AI_NAMES = {"milind-soni/OpenMausBot", "anthropics/claude-quickstarts",
            "vercel-labs/agent-browser", "anthropics/skills",
            "ranxianglei/billion-context"}


def build_insights(repos):
    repos = sorted(repos, key=lambda r: (r[4], r[3]), reverse=True)
    ins = []
    lang_stats = {}
    for r in repos:
        lang_stats[r[2] or "无语言"] = lang_stats.get(r[2] or "无语言", 0) + 1
    total_today = sum(r[4] for r in repos)
    top, second, third = repos[0], repos[1], repos[2]
    rank1 = REPOS[0]

    # Insight 1: top gainer. Today: top == raw #1 (merged phrasing).
    ins.append(f'<li><b>{top[0].split("/")[-1]} 今日涨星最快</b>：单日新增 <b>+{top[4]:,}</b> Stars，<b>且同时位居 GitHub 原始榜单首位</b>（合并表述场景）。注意 GitHub 的榜单排序并非按当日涨幅，本报告统一按「今日新增 Star」重新排序；本日两者恰好一致。</li>')

    maxc = max(lang_stats.values())
    top_langs = [l for l, c in lang_stats.items() if c == maxc]
    others = "、".join(f"{l}（{c}）" for l, c in sorted(lang_stats.items(), key=lambda x: -x[1]) if l not in top_langs)
    ins.append(f'<li><b>{"与".join(top_langs)} 各以 {maxc}/{len(repos)} 并列居首</b>：Python（sherlock、claude-quickstarts、anthropics/skills）与 TypeScript（OpenMausBot、astryx、billion-context）平分秋色；其余分布：{others}，共 {len(lang_stats)} 种语言，无缺色回退。</li>')

    trio_pct = int(round((top[4] + second[4] + third[4]) / total_today * 100))
    ins.append(f'<li><b>头部三强贡献约 {trio_pct}% 增量</b>：sherlock（+{top[4]:,}）、OpenMausBot（+{second[4]:,}）与 astryx（+{third[4]:,}）领跑今日榜单，合计占今日总增量（+{total_today:,}）的 <b>{trio_pct}%</b>；长尾由 claude-quickstarts 的 +32 收尾。</li>')

    delta_pct = int(round(abs(total_today - 11888) / 11888 * 100))
    ins.append(f'<li><b>热度明显回落</b>：今日收录榜单新增合计 <b>+{total_today:,}</b> Stars（{len(repos)} 个仓库），较上期 11-04（+11,888 / 12 个仓库）回落约 <b>{delta_pct}%</b>，<b>为本自动化自 9-23（+4,169）以来最低单日增量</b>。另注：11-05 至 11-08 无记录（自动化未触发），本期对比基准即 11-04。</li>')

    ai_list = "、".join(r[0].split("/")[-1] for r in repos if r[0] in AI_NAMES)
    non_ai = [r for r in repos if r[0] not in AI_NAMES]
    non_ai_txt = "、".join(f"{r[0].split('/')[-1]}（{'OSINT 侦查工具' if 'sherlock' in r[0] else 'GPU K8s 管理面，基础设施先例' if 'nvke' in r[0] else '设计系统本体，dbx 先例' if 'astryx' in r[0] else '物理仿真引擎'}）" for r in non_ai)
    ins.append(f'<li><b>AI / Agent 相关 {len(AI_NAMES)}/{len(repos)}</b>：{ai_list}。非 AI 的 4 个为 {non_ai_txt}。另注：越狱提示词合集 jailbreaks 与 p-e-w/heretic 今日均未上榜（剔除口径无需触发）。</li>')

    ins.append('<li><b>新面孔 8 个、回归 1 个、掉榜 12 个（榜单规模收窄至 9 个）</b>：新进 <b>sherlock</b>（OSINT 老牌首次登榜即登顶）、<b>nvke</b>（英伟达官方 GPU K8s 管理面）、<b>agent-browser</b>（Vercel Labs 智能体浏览器 CLI）、<b>astryx</b>（Meta 官方设计系统开源）、<b>claude-quickstarts</b> 与 <b>anthropics/skills</b>（Anthropic 官方双仓库同日登榜）、<b>mujoco</b>（DeepMind 物理仿真）、<b>billion-context</b>（中国开发者上下文压缩插件）；回归 <b>OpenMausBot</b>（上次 10-30）。上期 12 个仓库全部掉榜：claude-mem、agent-desktop、worktrunk、colibri、mattpocock/skills、portal-ai-plugins、floci、Scrapling、Game-Studios、Kronos、hex、ai-goofish-monitor。</li>')

    ins.append('<li><b>主题观察：「官方源头」集中入场</b>——① <b>Anthropic 双仓库同日登榜</b>：官方技能仓库 anthropics/skills（19 万）+ 官方示例集 claude-quickstarts，技能层与生态入口被官方亲自接管；② <b>Vercel Labs 的「给智能体一台电脑」赛道从桌面延伸到浏览器</b>：agent-desktop 之后 agent-browser 登榜；③ <b>Meta 官方设计系统 astryx 开源</b>：八年内部打磨、13,000+ 应用验证，并为「人和智能体协同开发」专门设计 API/文档/CLI；④ <b>英伟达官方 nvke</b> 把 AI 算力基础设施（GPU K8s 管理面）带进榜单；⑤ <b>billion-context</b> 代表上下文工程（Context Engineering）方向的中国开发者声音；⑥ <b>mujoco</b> 与 <b>sherlock</b> 则是两个经典老牌项目的「初登榜」——AI 生态之外的仿真与 OSINT 领域难得上榜。</li>')

    ins.append('<li><b>巨型项目里程碑</b>：anthropics/skills 累计 Star 达 <b>189,699</b>（19 万）、sherlock 突破 <b>10 万</b>（103,706）——今日两项目双双站上十万量级；agent-browser 4.8 万、claude-quickstarts 1.9 万紧随；体量最小的新面孔是 nvke（870）。</li>')

    for label, kws in CATS.items():
        matched = [r for r in repos if any(k in (r[5] or "").lower() or k in r[0].lower() for k in kws)]
        if matched:
            names = "、".join(r[0].split("/")[-1] for r in matched)
            ins.append(f'<li><b>{label}</b>：{names} 上榜，成为今日看点。</li>')
    return ins


if __name__ == "__main__":
    # Override the v26 engine's module globals for today's run.
    base.TODAY = date(2026, 11, 9)
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
