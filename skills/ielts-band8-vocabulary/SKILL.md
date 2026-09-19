---
name: ielts-band8-vocabulary
description: IELTS Band 8 lexical decisions — a corpus-verified collocation system (193 core chunks + 252 verb patterns) proving band 8 needs precise common words, not rare ones; audits essays for lexical resource, upgrades vague words, flags high-risk "advanced" vocabulary, and distinguishes writing vs spoken register. Use when the user asks about IELTS vocabulary (雅思词汇/搭配/lexical resource), whether a phrase suits an essay, word upgrades, or building topic word lists for writing or speaking.
license: MIT
---

# IELTS Band 8 词汇系统（搭配优先）

官方 Lexical Resource 描述符里，band 8 的关键词是 **precise meanings**——并且**明确允许** occasional inaccuracies in word choice and collocation。也就是说：**8 分不要求零错误，也不要求生僻词，要求"配得准"**。

本 skill 的知识基础是一组反直觉的实测结论：

- 在约 17.5 万词的雅思范文中实测核验的 68 个"必备高级动词块"（`curb` / `safeguard` / `strike a balance` / `impose stricter standards on`…）**全部 0 命中**；
- 真正撑起范文论证的是 `improve`、`lead to`、`enhance`、`contribute to`、`result in` 这类常见词——**配得准，而不是用得难**；
- 一批被词汇书标为"高级"的词（`bolster` / `exacerbate` 级）约 40 个在雅思作文里用出来是**风险而不是加分**。

## 条目标记（读 references 前先懂这套记号）

| 标记 | 含义 | 怎么用 |
|---|---|---|
| **A** | 范文实证高频（≥5 次），写作口语通用 | 必背 |
| **B** | 范文实证（2–4 次）或语域偏正式 | 写作必背，口语选背 |
| **C** | 学术语域较窄 | 认得出，慎主动用 |
| **📕 范文语料 0 次** | 词典级词汇，非范文实际用法 | 不是错，但别当"范文同款" |
| **[词典]** | 词条来自学术词表而非范文 | 用前自查搭配与语域 |

## 工作流（按用户意图分模式）

| 模式 | 触发语 | 做法 |
|---|---|---|
| **Audit** | "看看我作文的词汇" | 逐段标注：搭配准确度、重复用词、笼统词（important / good / problem / thing）、雷区词；给升级替换表；按 Lexical Resource 打分 |
| **Upgrade** | "这个词能不能换得更高级" | 先给 1–2 个**更精确**的常见说法，再给 1 个进阶选项（说明语域风险）；反对无语境的难词替换 |
| **Decide** | "essay 里能写 X 吗" | 查 references 中的语料结论：有没有真实用例、语域是否偏口语、是否在高风险清单里；给结论 + 替代 |
| **Topic list** | "给我教育话题的词块" | 从 task2 vocabulary 附二（若安装 ielts-writing-task2）或 collocations.md 分组中取该话题搭配 + 论点句模板 |
| **Drill** | "考我词汇" | 抽 10 条搭配做中英互测或改错（搭配错误四形态：介词错配 / 名词错配 / 语域错配 / 中式直译） |

## 搭配自查四形态（Audit 模式必查）

1. **介词错配**：`depend on` 不是 `depend of`；`investment in` 不是 `investment to`；
2. **名词错配**：`heavy traffic` 不是 `crowded traffic`；
3. **语域错配**：`kids / a lot of / get` 进不了学术写作；
4. **中式直译**：`learn knowledge` → `acquire knowledge`；`open the TV` → `turn on the TV`。

## 参考资料

| 文件 | 内容 | 什么时候读 |
|---|---|---|
| `references/collocations.md` | 全部知识本体：A. 实证高频搭配与正误对照、语域对照表；B. 193 条搭配与 chunks；D. 高风险"高级词"反向清单；E–G. 使用方法、边界、方法与局限；H. 252 条动词句型表 + 坑位清单 | 按目录定位到对应小节再读，不要整读 |

话题级词汇（教育 / 环境 / 科技等 21 话题的搭配与论点句）在 `ielts-writing-task2` skill 的 `vocabulary.md`（若已安装）；图表语言在 `ielts-writing-task1` 的 `vocabulary.md`（若已安装）。

## 边界

- "语料 0 次"只表示不在这批范文的用词范围内，不表示英语里不存在；判断时把这条边界讲清楚。
- 频次来自范文语料统计，不是官方词频；用于教学判断，不用于打分承诺。
