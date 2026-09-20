# IELTS Writing Skills

[Agent Skills](https://agentskills.io) for IELTS writing preparation — a distilled, corpus-informed knowledge base packaged as four installable skills for Claude Code, Codex, Cursor, OpenCode and [70+ other agents](https://skills.sh).

> 雅思写作备考知识库,封装为 4 个可直接安装的 Agent Skills:Task 1 图表作文、Task 2 议论文、Band 8 词汇系统、备考方案。

## What's inside

| Skill | What it does |
|---|---|
| [`ielts-writing-task1`](skills/ielts-writing-task1/) | Coaches IELTS Academic Task 1 (line/bar/pie/table/mixed charts, process diagrams, maps) and General Training letters: teaching, model reports, band scoring, timed drills. |
| [`ielts-writing-task2`](skills/ielts-writing-task2/) | Coaches IELTS Task 2 essays across all five prompt types: argument generation, sentence skeletons, model essays, band scoring, prompt-deconstruction drills with a 359-prompt bank. |
| [`ielts-band8-vocabulary`](skills/ielts-band8-vocabulary/) | A corpus-informed collocation system (193 core chunks + 252 verb patterns) for lexical decisions: essay audits, word upgrades, risky vocabulary choices and register guidance. |
| [`ielts-band8-study-plan`](skills/ielts-band8-study-plan/) | A diagnostic-driven 8-week plan toward band 8 writing: error-zeroing loop, what-to-memorise framework, and transferring essay arguments to speaking. |

## Install

```bash
# All four skills
npx skills add CHEUKFUNGWU/ielts-skills

# Or just the ones you need
npx skills add CHEUKFUNGWU/ielts-skills --skill ielts-writing-task2
```

Local checkout:

```bash
git clone https://github.com/CHEUKFUNGWU/ielts-skills
npx skills add ./ielts-skills
```

Manual install also works: copy any skill folder into your agent's skills directory (e.g. `.claude/skills/` for Claude Code, `.agents/skills/` for Codex/Cursor).

## Try it

Once installed, just talk to your agent:

- "I'm preparing IELTS Task 1 — here's my line-graph report, grade it." → *ielts-writing-task1*
- "拆一下这道大作文:Many people believe that... Discuss both views." → *ielts-writing-task2*
- "Can I write 'curb emissions' in an IELTS essay?" → *ielts-band8-vocabulary*
- "我稳定 6.5,想要写作 7.5,帮我做一个 8 周计划" → *ielts-band8-study-plan*

## How the knowledge is organized

- **Structure first**: fixed skeletons with synonym slots and content slots — structure stays, content adapts to the prompt. Memorised whole essays are a trap; ten functional slots × 2–3 variants are not.
- **Collocations over rare words**: observations from an internal ~175k-word essay corpus show that common expressions such as `improve` and `lead to` appear more often than many phrases marketed as advanced. Zero hits describe this corpus, not the acceptability of an expression.
- **Evidence tiers**: vocabulary entries distinguish internal corpus frequency, register guidance and dictionary-sourced items. The repository does not present these frequencies as official IELTS statistics.
- **Diagnostics before plans**: the study-plan skill records error patterns, whether they are systematic and whether they affect understanding. It does not convert an error count directly into a Band score.

## Repository layout

```
skills/
  ielts-writing-task1/    SKILL.md + references/ (guide, patterns, vocabulary, worked examples)
  ielts-writing-task2/    SKILL.md + references/ (guide, patterns, vocabulary, prompt bank, worked examples)
  ielts-band8-vocabulary/ SKILL.md + references/ (collocations system)
  ielts-band8-study-plan/ SKILL.md + references/ (plan, memorisation, writing→speaking)
```

Each `SKILL.md` is a thin workflow layer; the depth lives in `references/`, loaded progressively as the agent needs it.

## Disclaimer

Unofficial study material. Not affiliated with or endorsed by IELTS, Cambridge Assessment English, the British Council or IDP. Band descriptors and test rules should always be checked against official IELTS sources. Frequency claims describe the internal reference corpus, not official statistics.

## License

[MIT](LICENSE)
