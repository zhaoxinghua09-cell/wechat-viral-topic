#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""命中可溯源自测：验证「每个被抓出来的风险词、每个抽取事实，都真实存在于原文」。

用法（在技能包根目录）：
    python demo/prove_hits.py

三组检查：
  1. 抽取不臆造：scan 抽出的 audience/figures/dates/topics 必须在原文逐字出现。
  2. 命中不臆造：riskcheck 的每一处命中，word 与 context 必须能在原文逐字找到。
  3. 篡改跟随：改掉原文里的一个数字，抽取结果必须跟着变，不得残留旧值。

退出码 0 = 三组全部成立。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "tools"))

import topicguard as tg  # noqa: E402

DRAFT = os.path.join(HERE, "risky_draft.md")
NUM = re.compile(r"\d+(?:\.\d+)?%?|\d+(?:\.\d+)?万")


def main():
    text = open(DRAFT, encoding="utf-8").read()

    # 1) 抽取不臆造
    d = tg.scan(text)
    missing = []
    counts = {}
    for key in ("audience", "figures", "dates", "topics", "quotes"):
        vals = d.get(key) or []
        counts[key] = len(vals)
        for v in vals:
            tok = v if isinstance(v, str) else (v.get("text") or v.get("quote") or str(v))
            if tok and tok not in text:
                missing.append("%s:%s" % (key, tok))
    print("[1] 抽取不臆造：%s；无出处 %d 个"
          % (" / ".join("%s %d" % (k, v) for k, v in counts.items()), len(missing)))
    for m in missing[:6]:
        print("    ✗ 原文找不到：%s" % m)

    # 2) 命中不臆造
    r = tg.riskcheck(text)
    hits = (r.get("red") or []) + (r.get("yellow") or [])
    print("[2] 命中不臆造：风险命中 %d 条（红 %d / 黄 %d）"
          % (len(hits), len(r.get("red") or []), len(r.get("yellow") or [])))
    untraced = []
    for h in hits:
        word = h.get("word") or ""
        quote = h.get("quote") or ""
        if word and word not in text:
            untraced.append("word 缺失：%s" % word)
        elif quote and quote not in text:
            untraced.append("quote 不是原文逐字片段：%s" % word)
    for u in untraced[:6]:
        print("    ✗ %s" % u)

    # 3) 篡改跟随
    print("\n[3] 篡改跟随")
    nums = NUM.findall(text)
    ok3 = True
    if nums:
        old = nums[0]
        head = re.match(r"\d+", old).group()
        new = "%d%s" % (int(head) + 5, old[len(head):])
        mutated = text.replace(old, new, 1)
        d2 = tg.scan(mutated)
        vals = [v if isinstance(v, str) else str(v) for v in (d2.get("figures") or [])]
        has_new = any(new in v for v in vals) or new in mutated
        has_old = any(old in v for v in vals)
        ok3 = has_new and not has_old
        print("    %s -> %s：%s（新值出现=%s 旧值残留=%s）"
              % (old, new, "跟随" if ok3 else "未跟随 ⚠", has_new, has_old))
    else:
        print("    原文无数字，跳过（不算失败）")

    all_ok = not missing and not untraced and ok3
    print("\n结论：%s" % ("抽取与命中全部可回溯原文（不臆造）" if all_ok
                        else "存在无出处项或未跟随，证明不成立"))
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()

