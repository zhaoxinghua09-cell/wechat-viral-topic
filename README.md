# wechat-viral-topic · 公众号选题专家

[![skills.sh](https://skills.sh/b/zhaoxinghua09-cell/wechat-viral-topic)](https://skills.sh/zhaoxinghua09-cell/wechat-viral-topic) [![LobeHub](https://img.shields.io/badge/LobeHub-Skills%20Market-6f42c1)](https://lobehub.com/skills/zhaoxinghua09-cell-wechat-viral-topic)

## Install

```bash
npx skills add zhaoxinghua09-cell/wechat-viral-topic
```

One command, no sign-in. Works with Claude Code, Codex, Cursor, Windsurf, Gemini CLI, VS Code, Zed and any agent that reads `SKILL.md`.

**Use when**
- you need topic ideas for a WeChat public account, short video or comic
- you want a trend turned into a defensible topic card with real signals
- you need a headline graded for length, formula and red-line risk
- you must screen a draft for medical claims, absolute wording or income promises
- you are planning a content calendar and need angles that survive compliance

<!-- LGD-ECOSYSTEM -->
[![verifiability](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fzhaoxinghua09-cell%2Flgd-skill-review%2Fmain%2Fbench%2Fbadge.json)](https://zhaoxinghua09-cell.github.io/lgd-skill-review/benchmark.html)

**同系列 / Ecosystem** — 本包属于同一套可验证技能，共用一把尺子：
[`summarize-pro`](https://github.com/zhaoxinghua09-cell/summarize-pro) ｜ [`debug-pro`](https://github.com/zhaoxinghua09-cell/debug-pro) ｜ [`lgd-skill-review`](https://github.com/zhaoxinghua09-cell/lgd-skill-review)

- 评分口径与公开基准：https://zhaoxinghua09-cell.github.io/lgd-skill-review/rubric.html ｜ 榜单：https://zhaoxinghua09-cell.github.io/lgd-skill-review/benchmark.html
- 把自己的技能丢进来比，不用联系我们：[提交评测](https://github.com/zhaoxinghua09-cell/lgd-skill-review/issues/new?template=review-request.yml)
- 机器入口：`https://zhaoxinghua09-cell.github.io/lgd-skill-review/llms.txt` （全量语料：`llms-full.txt`）
<!-- /LGD-ECOSYSTEM -->

<!-- LGD-DIFF -->
**Compliance hits quote the source draft — every flagged phrase is auditable.**

合规命中项一律摘回原文片段，可逐句核对；没有原文依据的风险点不报。
复现：`python demo/run_demo.py`，见 `demo/SAMPLE-IO.md`。
<!-- /LGD-DIFF -->


**想知道自己的技能多少分？/ Get your own skill scored:** [一键提交评测 / submit for review](https://github.com/zhaoxinghua09-cell/lgd-skill-review/issues/new?template=review-request.yml) — 静态分析、不执行你的代码。

**skills.sh 页面**: https://skills.sh/zhaoxinghua09-cell/wechat-viral-topic ｜ `npx skills add zhaoxinghua09-cell/wechat-viral-topic`


选题时把「真信号」与「标题党猜测」分开，并在动笔前先过合规红线。给出候选选题的证据强度分级，而不是热度数字。

Separates a real signal from a clickbait guess when choosing topics, and applies compliance red lines before any draft is written.

## 一步安装 / Install in one line

```bash
# LobeHub 市场 / LobeHub marketplace
npx -y @lobehub/market-cli skills install zhaoxinghua09-cell-wechat-viral-topic --agent codex

# 直接从 GitHub 源安装 / install from source
npx -y skills add zhaoxinghua09-cell/wechat-viral-topic --skill wechat-viral-topic --agent codex
```

[![verify](https://github.com/zhaoxinghua09-cell/wechat-viral-topic/actions/workflows/verify.yml/badge.svg)](https://github.com/zhaoxinghua09-cell/wechat-viral-topic/actions/workflows/verify.yml)

- 市场页 / Marketplace page: https://lobehub.com/skills/zhaoxinghua09-cell-wechat-viral-topic
- 标识符 / Identifier: `zhaoxinghua09-cell-wechat-viral-topic`
- 自检 / Verify: `python tests/run_golden.py`（零依赖、离线，退出码即结论）
- 审计报告 / Audit: [`AUDIT-REPORT.md`](AUDIT-REPORT.md)（命令生成，重跑可推翻）

### 同族技能 / Same family

- [`summarize-pro`](https://github.com/zhaoxinghua09-cell/summarize-pro)
- [`debug-pro`](https://github.com/zhaoxinghua09-cell/debug-pro)
- [`lgd-skill-review`](https://github.com/zhaoxinghua09-cell/lgd-skill-review)
- [`lgd-hit-list`](https://github.com/zhaoxinghua09-cell/lgd-hit-list) — 爆款清单登记 / hit-list registry

## 快速开始 / Quick start

```bash
git clone https://github.com/zhaoxinghua09-cell/wechat-viral-topic.git
cd wechat-viral-topic
python tools/topicguard.py score --file candidates.md --out ./out --json
python tools/topicguard.py redline --file draft.md --json
python tests/run_golden.py
```

## 为什么可信 / Why it is checkable

- 黄金集 11 cases，`python tests/run_golden.py` 会真实执行并给出退出码（不靠自述）。
- 差异化点：title overreach detection。
- 零依赖、离线、零凭据：仅标准库，不发网络请求。

## AI 发现层 / AI discovery layer

- `llms.txt` — 面向 AI Agent 的能力与触发条件说明（双语）。
- `AI-INDEX.json` — 机器可读索引（schema `lgd.ai-index/1`）。
- 六维审计通过后登记于爆款清单：https://github.com/zhaoxinghua09-cell/lgd-hit-list

## 同族技能 / Family

- [summarize-pro](https://github.com/zhaoxinghua09-cell/summarize-pro) — 会议纪要专家
- [debug-pro](https://github.com/zhaoxinghua09-cell/debug-pro) — 排障专家
- [lgd-skill-review](https://github.com/zhaoxinghua09-cell/lgd-skill-review) — 技能审计官

---

