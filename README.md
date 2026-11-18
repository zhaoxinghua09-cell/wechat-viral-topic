# wechat-viral-topic · 公众号选题专家

选题时把「真信号」与「标题党猜测」分开，并在动笔前先过合规红线。给出候选选题的证据强度分级，而不是热度数字。

Separates a real signal from a clickbait guess when choosing topics, and applies compliance red lines before any draft is written.

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

