---
name: wechat-viral-topic
displayName: wechat-viral-topic
slug: wechat-viral-topic
author: 诺声(Logos)@SynomosAI
copyright: 赵兴华 / Steven Zhao·China
version: 2.1.4
license: LicenseRef-AllRightsReserved
license_scope: 理论文本保留所有权利（见文末「License」）；tools/*.py、tests/*.py、demo/*.py 等脚本文件单独以 MIT 许可提供，便于他人复跑与审计
allowed-tools: Read, Glob, Grep, Edit, Bash
description: "Topic-selection assistant for WeChat public accounts, short-video creators, comic authors and H5 planners that turns a raw trend into a defensible topic card: extracts verifiable signals (figures, time windows, platform fit, hashtags, conflict lines, reader pain points), screens drafts against compliance red lines (medical claims, absolute wording, income promises, incentivised sharing, unsourced assertions), and grades headlines for length, formula type and red-line risk. Ships a zero-dependency offline toolchain (scan / riskcheck / titlecheck) plus an 11-case golden set with a re-executable runner and a demo proving both the block path and the no-false-positive path. Progressive disclosure: frameworks live in references/. Triggers: topic selection, topic ideas, content ideas, what to write, viral topic, viral content, hit article, trending topic, trend analysis, hot take, headline, headline writing, title check, title grading, click through rate, open rate, 100k read, 10w+, WeChat public account, WeChat article, official account, short video script, douyin, xiaohongshu, comic script, H5 planning, content calendar, compliance check, content compliance, red line, medical claims, absolute wording, advertising law, 选题, 选题策划, 写什么, 爆款, 10万+, 公众号, 公众号选题, 标题, 起标题, 标题党, 打开率, 内容合规, 广告法, 医疗宣称, 绝对化用语, 短视频脚本, 漫画选题."
description_zh: "把热点变成可交付的选题卡：素材信号抽取、合规红线筛查、标题四维体检，全部可复跑；工具脚本以 MIT 许可提供，理论文本保留权利。 触发词：选题 爆款 10万+ 公众号 标题 内容合规 广告法 短视频脚本。"
description_en: "Topic-selection assistant for WeChat public accounts, short-video creators, comic authors and H5 planners that turns a raw trend into a defensible topic card: extracts verifiable signals (figures, time windows, platform fit, hashtags, conflict lines, reader pain points), screens drafts against compliance red lines (medical claims, absolute wording, income promises, incentivised sharing, unsourced assertions), and grades headlines for length, formula type and red-line risk. Ships a zero-dependency offline toolchain (scan / riskcheck / titlecheck) plus an 11-case golden set with a re-executable runner and a demo proving both the block path and the no-false-positive path. Progressive disclosure: frameworks live in references/. Triggers: topic selection, topic ideas, content ideas, what to write, viral topic, viral content, hit article, trending topic, trend analysis, hot take, headline, headline writing, title check, title grading, click through rate, open rate, 100k read, 10w+, WeChat public account, WeChat article, official account, short video script, douyin, xiaohongshu, comic script, H5 planning, content calendar, compliance check, content compliance, red line, medical claims, absolute wording, advertising law."
tags:
- 选题策划
- 爆款
- 自媒体运营
- 内容创作
- wechat-viral-topic
display_name: 10万+爆款选题制造机
display_name_en: Viral Topic Maker
agent_created: true
visibility: public
category: 内容创作
updated: 2026-11-18
fingerprint: FP-MX-838BFC6F758F
languages:
- zh-CN
- en
- ja
- ko
- es
- fr
- de
- ar
aliases:
- 热点选题
- 爆款策划
- viral topic
brand: SynomosAI
discoverable_by_ai: true
ambassador: 诺声
trigger_keywords:
- wechat
- viral
- topic
- 选题
- 爆款
- 热点
- 标题
- 策划
- 公众号
---

# wechat-viral-topic · 精简版（v2.2.0-slim）

原 284 行 / 18 个 H2 / 9 份 references → 本页 60 行 / 2 模块 / 1 份 `references/details.md`。
依据 SkillsBench（arXiv 2602.12670）：聚焦型胜全面型。

## 1 用法：只决定一件事——这条选题凭什么值得写

三步：**扫描素材信号 → 过合规红线 → 体检标题**。任一步不过，不进入写作。

```bash
python tools/topicguard.py scan --file 素材.md --out ./out --json
python tools/topicguard.py riskcheck --file 选题卡.md --json
python tools/topicguard.py titlecheck --file 标题清单.txt --json
python tests/run_golden.py
```

## 2 纪律：不可妥协（逐条满足，缺一即返工）

- **MUST** 每个选题附**来源与时间**，无出处的说法不写。
- **MUST** 素材如实：不编造用户案例、不美化数据（faithful reporting），引用需可回溯。
- **MUST** 发布前跑 `riskcheck`，红线项必须清零或改写。
- **MUST** 标题与正文承诺一致，标题不超出正文能兑现的范围。
- **MUST** 涉及医疗、金融、法律的内容只做科普口径，附「不构成建议」。
- **MUST** 引用数据标明口径（样本量、时间窗、来源）。
- **NEVER** 使用「最/第一/唯一/国家级」等绝对化用语，除非有可查依据。
- **NEVER** 蹭灾难、事故、伤亡类热点做流量。
- **NEVER** 承诺效果（涨粉数、转化率、阅读量）。
- **NEVER** 编造用户案例、对话截图或数据。

示例（输入残句 → 输出选题卡字段）：

```text
输入：某厂把交付周期从 6 周压到 3 周
输出：信号=交付周期减半｜来源=原文｜可写角度=流程改造｜风险=需核实是否个例
      标题A=「6 周压到 3 周，他们改的不是工具」 合规=通过（无绝对化用语）
```

## 3 边界与降级

- 不代运营账号、不承诺传播结果；选题价值判断留给作者。
- 素材<3 条信号时：只出「还缺什么素材」清单，不硬凑选题。
- 平台规则变动频繁：以发布当日平台公示为准，本包不替代平台规则。
- 全量规范（信号词典、红线清单、标题公式、模板）见 `references/details.md`。
- 同系列：`summarize-pro`（纪要）→ `debug-pro`（排障）→ 本包（选题）。

零依赖 · 零联网 · 零凭据 ｜ MIT ｜ 诺声(Logos)@SynomosAI

## Hand-off

- 需要把讨论出成纪要 → `summarize-pro`
- 需要定位故障根因 → `debug-pro`
- 需要对外证明本包质量 → `lgd-skill-review`（六维评审，`--focus` 附加聚焦度报告）
