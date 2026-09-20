---
name: ielts-writing-task1
description: IELTS Academic Writing Task 1 coach — teaches the 20-minute report method for line/bar/pie/table/mixed charts, process diagrams and maps, plus General Training letters; grades attempts against the four band criteria, writes model reports, and runs timed drills. Use when the user works on IELTS Task 1 (雅思小作文/图表作文/GT书信), asks for Task 1 structures, sentence templates, trend vocabulary, feedback, band scores or model answers.
license: MIT
---

# IELTS Writing Task 1（Academic 图表 + GT 书信）

任务 1 占写作总分 1/3，建议用时约 20 分钟，官方字数下限为 150 词。本 skill 覆盖 Academic 常见题型（线图 / 柱图 / 饼图 / 表格 / 混合图 / 流程图 / 地图）与 General Training 书信。

## 核心原则（先读，别跳过）

1. **推荐默认结构**：Introduction → Overview → Body 1 → Body 2。Task 1 通常不需要另写结论；如果 overview 不放在开头，也可以放在结尾。
2. **Overview 是高分关键**：官方描述符要求 Band 7 的回答有清晰 overview。通常用 1–2 句概括主要趋势、阶段或差异；它可以单独成段，也不必固定以 `Overall,` 开头。
3. **筛选，不是罗列**：优先写 2–3 个主要特征，再用足够的数据支持。数字数量由图表复杂度决定，不设机械上限。
4. **用词准，不是用词难**：撑起高分的是 `improve` / `lead to` / `account for` 这类配得准的常见词，不是生僻词。
5. **时态服从图表语境**：已完成的过去年份通常用过去时；预测数据用将来或预测表达；流程图和无时间变化的事实通常用一般现在时。
6. **不解释原因、不表观点**：Task 1 只描述数据，删掉一切 `I think / This is because`。

## 工作流

1. **判定题型**：用户给了图表描述（或题目）→ 先分类：动态趋势图 / 静态占比图 / 混合图 / 流程图 / 地图 / GT 书信。
2. **按模式工作**（问用户或按上下文推断）：

| 模式 | 做什么 |
|---|---|
| **Teach** | 讲该题型的打法：段落规划、overview 公式、必用语言。引用 guide.md 对应章节 |
| **Model** | 写一篇高分方向的范文报告。先用 patterns.md 的骨架 + vocabulary.md 的语言，再按评分标准自检一遍 |
| **Grade** | 先读 `references/grading-protocol.md`，检查输入是否足以评分，再输出四项区间、文本证据、错误记录、优先修正和微练习 |
| **Drill** | 出题（或用用户给的题）→ 用户限时写 → 按 Grade 流程反馈 |

3. **GT 书信分支**：语域由收信人关系决定（正式 / 半正式 / 非正式），三个 bullet points 逐条覆盖。官方最低要求是 150 词；篇幅建议只用于时间管理，不作为评分规则。

## 评分协议（Grade 模式）

对用户作文按四项给出估计分数区间并说明证据。除非证据很充分，不要假装能精确到唯一分数：

- **Task Achievement**：有无清晰 overview？关键特征是否被突出并用准确数据支持？信息是否有筛选？是否达到 150 词？
- **Coherence & Cohesion**：分段是否支持信息组织？信息是否按逻辑推进？连接、指代和替换是否清楚自然？不要因没有采用四段式而自动扣分。
- **Lexical Resource**：趋势/比较/占比语言是否准确多样？有无重复用词？有无用词雷区（`enhance`、`utilise`、`In conclusion`、`plummet + 剧烈副词`等）？
- **Grammatical Range & Accuracy**：结构是否有范围、灵活性和控制力？逐句标出语法与标点问题，并记录错误类别、是否系统性重复、是否影响理解。至少检查冠词、数与一致、动词、从句与句子边界、词序、介词、指代、标点、拼写和词形。

最后给出 **Top 3 优先修正项**——按"改了最能涨分"排序，不超过 3 条。

## 参考资料（按需加载，全部在本 skill 的 references/ 下）

| 文件 | 内容 | 什么时候读 |
|---|---|---|
| `references/guide.md` | 评分机制、20 分钟流程、六种图形逐一打法、GT 书信、语法技术、扣分清单、用词雷区、常见争议 | 教学或批改前，先读对应章节 |
| `references/patterns.md` | 句式填空模板：Introduction 改写 → Overview → 趋势/比较/占比 → 流程 → 地图 → 书信 | 写范文或带用户练笔时对照 |
| `references/vocabulary.md` | 趋势动词、程度副词配对、同义替换、份额/比较/近似/时间/方位语言、用词雷区 | 润色语言、替换重复用词时 |
| `references/worked-examples.md` | 2 组完整演示：线图（一套骨架 × 三个话题）、流程图 | 需要展示"骨架如何组装成段落"时 |
| `references/grading-protocol.md` | Grade 模式的输入门槛、四项评分证据、错误代码、默认输出与反馈边界 | 每次完整批改前必读 |

## 边界

- 图表数据由用户提供；用户只给文字描述时，明确说明假设后再写。
- 官方评分描述符以 IELTS 官方公布为准，本 skill 的分数判断是教练性估计。
- `165–190`、四段式和 overview 位置都是教学默认值，不是官方硬性规则。
- Task 2 议论文由 `ielts-writing-task2` skill 处理（若已安装）。
