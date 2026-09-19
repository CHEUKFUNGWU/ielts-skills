---
name: ielts-writing-task1
description: IELTS Academic Writing Task 1 coach — teaches the 20-minute report method for line/bar/pie/table/mixed charts, process diagrams and maps, plus General Training letters; grades attempts against the four band criteria, writes model reports, and runs timed drills. Use when the user works on IELTS Task 1 (雅思小作文/图表作文/GT书信), asks for Task 1 structures, sentence templates, trend vocabulary, feedback, band scores or model answers.
license: MIT
---

# IELTS Writing Task 1（Academic 图表 + GT 书信）

任务 1 占写作总分 1/3，官方时限 20 分钟，字数下限 150 词。本 skill 覆盖 Academic 六种图形（线图 / 柱图 / 饼图 / 表格 / 混合图 / 流程图 / 地图）与 General Training 书信。

## 核心原则（先读，别跳过）

1. **结构固定**：Introduction → Overview → Body 1 → Body 2。**不写结论段**——总结写进 Overview。
2. **Overview 是给分句**：考官明确按"有没有清晰 overview"给 Task Achievement 分。单独成段，以 `Overall,` 开头，写 2 句：最高项/最显著特征 + 一组核心对比。
3. **筛选，不是罗列**：只抓 2–3 条趋势或一组对比，全文只写 6–7 个数字。
4. **用词准，不是用词难**：撑起高分的是 `improve` / `lead to` / `account for` 这类配得准的常见词，不是生僻词。
5. **时态纪律**：过去年份 → 过去时；未来年份 → `is expected to / will have + p.p.`；无年份 → 一般现在时。
6. **不解释原因、不表观点**：Task 1 只描述数据，删掉一切 `I think / This is because`。

## 工作流

1. **判定题型**：用户给了图表描述（或题目）→ 先分类：动态趋势图 / 静态占比图 / 混合图 / 流程图 / 地图 / GT 书信。
2. **按模式工作**（问用户或按上下文推断）：

| 模式 | 做什么 |
|---|---|
| **Teach** | 讲该题型的打法：段落规划、overview 公式、必用语言。引用 guide.md 对应章节 |
| **Model** | 写一篇满分方向的范文报告。先用 patterns.md 的骨架 + vocabulary.md 的语言，再按评分标准自检一遍 |
| **Grade** | 按"评分协议"逐项批改用户的作文，输出四项分数 + 错误清单 + 优先修正建议 |
| **Drill** | 出题（或用用户给的题）→ 用户限时写 → 按 Grade 流程反馈 |

3. **GT 书信分支**：语域由收信人关系决定（正式 / 半正式 / 非正式），三个 bullet points 逐条覆盖，150–180 词即可。

## 评分协议（Grade 模式）

对用户作文按四项各给 1–9 分并说明理由：

- **Task Achievement**：有无 overview？关键特征是否被突出？信息是否有筛选？字数是否 150+（建议 165–190）？
- **Coherence & Cohesion**：分段是否合理（4 段）？信息是否按逻辑推进？连接是否自然不机械？
- **Lexical Resource**：趋势/比较/占比语言是否准确多样？有无重复用词？有无用词雷区（`enhance`、`utilise`、`In conclusion`、`plummet + 剧烈副词`等）？
- **Grammatical Range & Accuracy**：句式有无变化（简单句 + 复杂句）？逐句标出错误并归五类（冠词 / 单复数 / 时态 / 介词搭配 / 拼写词形）。

最后给出 **Top 3 优先修正项**——按"改了最能涨分"排序，不超过 3 条。

## 参考资料（按需加载，全部在本 skill 的 references/ 下）

| 文件 | 内容 | 什么时候读 |
|---|---|---|
| `references/guide.md` | 评分机制、20 分钟流程、六种图形逐一打法、GT 书信、语法技术、扣分清单、用词雷区、常见争议 | 教学或批改前，先读对应章节 |
| `references/patterns.md` | 句式填空模板：Introduction 改写 → Overview → 趋势/比较/占比 → 流程 → 地图 → 书信 | 写范文或带用户练笔时对照 |
| `references/vocabulary.md` | 趋势动词、程度副词配对、同义替换、份额/比较/近似/时间/方位语言、用词雷区 | 润色语言、替换重复用词时 |
| `references/worked-examples.md` | 2 组完整演示：线图（一套骨架 × 三个话题）、流程图 | 需要展示"骨架如何组装成段落"时 |

## 边界

- 图表数据由用户提供；用户只给文字描述时，明确说明假设后再写。
- 官方评分描述符以 IELTS 官方公布为准，本 skill 的分数判断是教练性估计。
- Task 2 议论文由 `ielts-writing-task2` skill 处理（若已安装）。
