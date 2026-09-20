# IELTS Writing Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文（香港）](README.zh-HK.md)

Four installable [Agent Skills](https://agentskills.io) for IELTS writing practice. They work with Claude Code, Codex, Cursor, OpenCode, and other agents supported by [skills.sh](https://skills.sh).

The collection covers Task 1, Task 2, vocabulary decisions, and diagnostic study planning. It focuses on accurate task handling, clear reasoning, controlled language, and feedback that students can act on.

## Skills

| Skill | Purpose |
|---|---|
| [`ielts-writing-task1`](skills/ielts-writing-task1/) | Coaches Academic Task 1 charts, tables, process diagrams and maps, plus General Training letters. Supports teaching, model answers, grading and timed drills. |
| [`ielts-writing-task2`](skills/ielts-writing-task2/) | Coaches the main Task 2 prompt types. Supports prompt analysis, argument development, model essays, grading and drills using a 359-prompt bank. |
| [`ielts-band8-vocabulary`](skills/ielts-band8-vocabulary/) | Provides a corpus-informed collocation system with 193 core chunks and 252 verb patterns. Audits lexical resource, checks register and helps replace vague wording without forcing rare words. |
| [`ielts-band8-study-plan`](skills/ielts-band8-study-plan/) | Builds a diagnostic study plan around recurring errors, task weaknesses and timed performance. Includes an adaptable eight-week framework and guidance on what to memorise. |

## Install

Install all four skills:

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills
```

Install one skill:

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills --skill ielts-writing-task2
```

Install from a local checkout:

```bash
git clone https://github.com/CHEUKFUNGWU/ielts-writing-skills.git
npx skills add ./ielts-writing-skills
```

Manual installation also works. Copy a skill folder into the skills directory used by your agent, such as `.claude/skills/` or `.agents/skills/`.

## Example prompts

- "Here is my Academic Task 1 report and the chart. Grade it and tell me what to fix first."
- "Break down this Discuss Both Views question and help me build two developed arguments."
- "Is `curb emissions` appropriate here, or is there a more natural alternative?"
- "My writing is around Band 6.5. Build a study plan from my last two essays."

## Teaching approach

- **Evidence before scores.** Grading uses estimated ranges, quotes the student's text and explains what limits the next band. Missing prompts or charts are reported instead of guessed.
- **Revision before replacement.** The grading protocols prioritise small, teachable corrections. They do not replace the student's essay with a polished model unless requested.
- **Precision before rarity.** Common words used accurately are more useful than isolated "advanced" vocabulary. Corpus counts are internal observations, not official IELTS statistics.
- **Diagnosis before planning.** Error frequency, repeated patterns and impact on meaning guide the study plan. Error counts are not converted directly into Band scores.
- **Strategies are defaults, not rules.** Four-paragraph structures, word-count ranges and template phrases are teaching options. Official scoring criteria remain the authority.

## Repository layout

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

Each `SKILL.md` contains the workflow and routes the agent to the relevant reference file. Detailed material is loaded only when the task needs it.

## Important notes

- This is unofficial study material. It is not affiliated with or endorsed by IELTS, Cambridge University Press & Assessment, the British Council, or IDP.
- Check current test rules and Band descriptors against official IELTS sources.
- Vocabulary frequencies describe the internal reference corpus. The repository does not present them as official frequency data or proof of a Band score.
- The prompt bank retains the labels used by its source material. The repository does not currently include a question-by-question source and rights record.

## License

[MIT](LICENSE)
