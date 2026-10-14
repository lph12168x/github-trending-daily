# GitHub Trending 每日简报 · 2026年10月14日

> 数据来源：[GitHub Trending](https://github.com/trending) · 生成时间：2026-10-14
> 共 9 个热门仓库，今日新增 67,642 Stars

---

## #1 [morluto/rea](https://github.com/morluto/rea)

> REA（Reverse Engineer Anything）：面向逆向工程的统一 MCP 服务，让智能体从应用行为一路分析到原生二进制——覆盖原生二进制、JavaScript / Electron 应用、.NET 程序集与网站，「看到一个喜欢的功能，就顺着理解到二进制级别」。它能在没有源码的情况下检查应用、解释功能如何实现、给出证据，并在你自己的项目里复刻一版；分析全部在本地运行，每条结论都附带证据与局限性说明。原生分析可复用本机已装的 Hopper 或 Ghidra，纯静态 JavaScript 分析则不需要任何反汇编引擎。MIT 许可，要求 Node.js 22+。

- **语言**：TypeScript
- **总 Stars**：214,568
- **今日新增**：+54,679 ⭐

## #2 [storytold/artcraft](https://github.com/storytold/artcraft)

> ArtCraft：自称「艺术家的 IDE」，面向交互式 AI 图像与视频创作，主张「先搭场景，再生成」。在 2D 画布上做图层合成与蒙版重绘、在 3D 场景里布景打机位，把提示词变成可精确复现的「crafting」：文生图、提示词图像编辑（Nano Banana Pro、GPT Image 等）、图生 3D 网格、角色姿态与身份迁移、背景移除、图生视频，并允许在工作流内自由选择图像 / 视频模型。Rust 实现，提供桌面端下载与开源构建。

- **语言**：Rust
- **总 Stars**：26,168
- **今日新增**：+4,081 ⭐

## #3 [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view)

> gods-eye-view（上帝视角）：运行在浏览器里的「间谍卫星模拟器」，但数据是真的——在逼真的三维地球上做实时开源空间情报。项目把公开卫星轨道与遥感数据接进可自由漫游的 3D 场景，让读者直观看到「卫星此刻在看哪里」，对图形 / 可视化方向的读者直接可参考。

- **语言**：JavaScript
- **总 Stars**：55,685
- **今日新增**：+1,961 ⭐

## #4 [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

> diagram-design：面向 Claude Code、Codex、GitHub Copilot、Cursor、Factory Droid 与 Pi 的「编辑部级」示意图设计技能。内置 44 种图表类型，产出零依赖、自包含的 HTML + SVG——无阴影，也没有千篇一律的 Mermaid 味。

- **语言**：HTML
- **总 Stars**：54,460
- **今日新增**：+1,815 ⭐

## #5 [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

> VoiceStudio：开源、完全本地化的 ElevenLabs 替代方案——语音克隆、音色设计、视频配音、听写、转写与有声书制作，支持 646 种语言。全部推理在本地完成，隐私不出设备，是本地语音 AI 方向功能覆盖最全的开源实现之一。

- **语言**：Python
- **总 Stars**：63,874
- **今日新增**：+1,748 ⭐

## #6 [xtool-org/xtool](https://github.com/xtool-org/xtool)

> xtool：跨平台 Xcode 替代方案——在 Linux / WSL / macOS 上用开放标准复刻 Xcode 核心能力：把 SwiftPM 包构建成 iOS 应用、签名并安装到设备、以编程方式对接 Apple Developer Services，配套 xtool new / dev / devices / install / launch 等完整 CLI 与可嵌入的 XKit 库。让 iOS 开发摆脱「必须有 Mac + Xcode」的束缚，对 CI 与异构开发环境尤其友好。

- **语言**：Swift
- **总 Stars**：9,632
- **今日新增**：+1,198 ⭐

## #7 [lyogavin/airllm](https://github.com/lyogavin/airllm)

> AirLLM：用单张 4GB 显存 GPU 跑 70B 大模型的推理方案。核心思路是分层流式加载——把一个上百 GB 的模型按层切分，推理时逐层载入显存、算完即释放，从而把显存占用从「装下整个模型」降到「装下最大的一层」，无需量化、无需多卡即可在消费级硬件上完成大模型推理。

- **语言**：Jupyter Notebook
- **总 Stars**：38,433
- **今日新增**：+1,001 ⭐

## #8 [mksglu/context-mode](https://github.com/mksglu/context-mode)

> Context Mode：面向 AI 编码智能体的上下文窗口优化 MCP 服务。每次 MCP 工具调用的原始返回（一个 Playwright 快照 56 KB、20 个 GitHub issue 59 KB）会把上下文窗口迅速吃满，压缩对话时智能体又会忘记正在编辑的文件与进行中的任务。Context Mode 用沙箱工具把原始数据挡在上下文之外（实测 315 KB 压到 5.4 KB、缩减 98%），跨会话持久化任务记忆，并通过 MCP + hooks 在 17 个平台上强制路由。曾登 Hacker News 第一（570+ 分）。

- **语言**：TypeScript
- **总 Stars**：28,403
- **今日新增**：+969 ⭐

## #9 [vercel-labs/skills](https://github.com/vercel-labs/skills)

> vercel-labs/skills：开放智能体技能（Agent Skills）生态的官方 CLI——一条 `npx skills add owner/repo` 即可把技能装进 OpenCode、Claude Code、Codex、Cursor 等 75+ 种编码智能体；`npx skills use` 无需安装即可生成技能提示词并拉起对应智能体，支持 GitHub / GitLab / Azure Repos / 任意 git URL / 本地路径等来源，MIT 许可。技能生态正成为智能体工具链的事实标准，这个 CLI 是它的「包管理器」。

- **语言**：TypeScript
- **总 Stars**：34,659
- **今日新增**：+190 ⭐
