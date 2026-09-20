# IELTS Writing Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文（香港）](README.zh-HK.md)

这是一个面向雅思写作备考的 Agent Skills 合集，可以安装到 Claude Code、Codex、Cursor、OpenCode，以及 [skills.sh](https://skills.sh) 支持的其他智能体中。

项目包含 Task 1、Task 2、词汇判断和诊断式学习计划四个 Skill。重点不是堆模板，而是准确完成任务、讲清逻辑、控制语言错误，并给出学生能够执行的修改建议。

## 包含的 Skills

| Skill | 用途 |
|---|---|
| [`ielts-writing-task1`](skills/ielts-writing-task1/) | 辅导 Academic Task 1 图表、表格、流程图和地图，以及 General Training 书信。支持教学、范文、批改和限时训练。 |
| [`ielts-writing-task2`](skills/ielts-writing-task2/) | 辅导主要 Task 2 题型。支持拆题、论点展开、范文、批改，以及使用 359 道题目的专项训练。 |
| [`ielts-band8-vocabulary`](skills/ielts-band8-vocabulary/) | 提供语料辅助的搭配系统，包含 193 个核心词块和 252 个动词句型。用于检查 Lexical Resource、判断语域和改进笼统表达。 |
| [`ielts-band8-study-plan`](skills/ielts-band8-study-plan/) | 根据重复错误、任务弱项和限时表现制定学习计划。包含可调整的八周框架，以及背什么、怎么背的指导。 |

## 安装

安装全部四个 Skill：

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills
```

只安装一个 Skill：

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills --skill ielts-writing-task2
```

从本地副本安装：

```bash
git clone https://github.com/CHEUKFUNGWU/ielts-writing-skills.git
npx skills add ./ielts-writing-skills
```

也可以手动复制。把需要的 Skill 文件夹放进智能体使用的技能目录，例如 `.claude/skills/` 或 `.agents/skills/`。

## 使用示例

- “这是我的 Academic Task 1 图表和作文，请评分，并告诉我下一篇最先改什么。”
- “帮我拆解这道 Discuss Both Views 题，并展开两个有逻辑的论点。”
- “这里可以写 `curb emissions` 吗？有没有更自然的说法？”
- “我的写作大约 6.5，请根据最近两篇作文制定学习计划。”

## 教学方法

- **评分必须有证据。** 批改采用估计区间，引用学生原文，并说明是什么限制了下一档分数。缺少题目或图表时，不猜测 Task Response 或 Task Achievement。
- **先教修改，再给范文。** 批改协议优先做最小、可模仿的修改。除非用户要求，不用一篇全新的范文替换学生作文。
- **准确比生僻重要。** 常见词用得准确，比孤立的“高级词”更可靠。语料频次只是内部观察，不是 IELTS 官方统计。
- **先诊断，再计划。** 学习计划关注错误频率、是否重复出现，以及是否影响理解，不把错误数量直接换算成 Band。
- **策略不是硬规则。** 四段式、建议词数和句型模板都是教学选项，最终以官方评分标准为准。

## 仓库结构

```text
skills/
  ielts-writing-task1/
    SKILL.md
    references/guide.md
    references/grading-protocol.md
    references/patterns.md
    references/vocabulary.md
    references/worked-examples.md
  ielts-writing-task2/
    SKILL.md
    references/guide.md
    references/grading-protocol.md
    references/patterns.md
    references/prompt-bank.md
    references/vocabulary.md
    references/worked-examples.md
  ielts-band8-vocabulary/
    SKILL.md
    references/collocations.md
    references/methodology.md
  ielts-band8-study-plan/
    SKILL.md
    references/
```

每个 `SKILL.md` 负责工作流程和资料路由。详细内容放在 `references/` 中，只在任务需要时加载。

## 重要说明

- 本项目是非官方学习材料，与 IELTS、Cambridge University Press & Assessment、British Council 或 IDP 没有关联，也未获得其背书。
- 考试规则和 Band 描述符应以 IELTS 官方最新资料为准。
- 词汇频次来自内部参考语料，不是官方词频，也不能证明某个表达对应特定分数。
- 题库保留了原材料中的题目标签。目前仓库没有提供逐题来源和授权记录。

## 许可证

[MIT](LICENSE)
