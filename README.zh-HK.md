# IELTS Writing Skills

[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文（香港）](README.zh-HK.md)

這是一套為 IELTS 寫作備考而設的 Agent Skills，可安裝到 Claude Code、Codex、Cursor、OpenCode，以及 [skills.sh](https://skills.sh) 支援的其他智能代理。

項目包括 Task 1、Task 2、詞彙判斷和診斷式學習計劃四個 Skill。重點不是堆砌模板，而是準確回應題目、說清楚邏輯、控制語言錯誤，並提供學生能夠執行的修改建議。

## 包含的 Skills

| Skill | 用途 |
|---|---|
| [`ielts-writing-task1`](skills/ielts-writing-task1/) | 輔導 Academic Task 1 圖表、表格、流程圖和地圖，以及 General Training 書信。支援教學、範文、批改和限時練習。 |
| [`ielts-writing-task2`](skills/ielts-writing-task2/) | 輔導主要 Task 2 題型。支援拆題、論點發展、範文、批改，以及使用 359 道題目的專項練習。 |
| [`ielts-band8-vocabulary`](skills/ielts-band8-vocabulary/) | 提供語料輔助的搭配系統，包括 193 個核心詞組和 252 個動詞句型。用於檢查 Lexical Resource、判斷語域和改善籠統表達。 |
| [`ielts-band8-study-plan`](skills/ielts-band8-study-plan/) | 根據重複錯誤、題型弱項和限時表現制定學習計劃。包括可調整的八星期框架，以及背甚麼、怎樣背的指引。 |

## 安裝

安裝全部四個 Skill：

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills
```

只安裝一個 Skill：

```bash
npx skills add CHEUKFUNGWU/ielts-writing-skills --skill ielts-writing-task2
```

從本機副本安裝：

```bash
git clone https://github.com/CHEUKFUNGWU/ielts-writing-skills.git
npx skills add ./ielts-writing-skills
```

亦可以手動複製。把需要的 Skill 資料夾放進智能代理使用的技能目錄，例如 `.claude/skills/` 或 `.agents/skills/`。

## 使用例子

- 「這是我的 Academic Task 1 圖表和作文，請評分，並告訴我下一篇最先要改善甚麼。」
- 「幫我拆解這道 Discuss Both Views 題，並發展兩個有邏輯的論點。」
- 「這裏可以寫 `curb emissions` 嗎？有沒有更自然的說法？」
- 「我的寫作大約是 6.5，請根據最近兩篇作文制定學習計劃。」

## 教學方法

- **評分必須有證據。** 批改採用估計區間，引用學生原文，並說明甚麼限制了下一級分數。缺少題目或圖表時，不猜測 Task Response 或 Task Achievement。
- **先教修改，再給範文。** 批改協議優先作出最少而且可模仿的修改。除非使用者要求，否則不用一篇全新的範文取代學生作文。
- **準確比生僻重要。** 常見詞用得準確，比孤立的「高級詞」更可靠。語料頻次只是內部觀察，不是 IELTS 官方統計。
- **先診斷，再計劃。** 學習計劃會考慮錯誤頻率、錯誤是否重複出現，以及會否影響理解，不會把錯誤數量直接換算成 Band。
- **策略不是硬規則。** 四段式、建議字數和句型模板都是教學選項，最終以官方評分標準為準。

## 程式碼庫結構

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

每個 `SKILL.md` 負責工作流程和資料路由。詳細內容放在 `references/`，只會在任務需要時載入。

## 重要說明

- 本項目是非官方學習材料，與 IELTS、Cambridge University Press & Assessment、British Council 或 IDP 沒有關聯，亦未獲得其認可。
- 考試規則和 Band 描述符應以 IELTS 官方最新資料為準。
- 詞彙頻次來自內部參考語料，不是官方詞頻，也不能證明某個表達對應特定分數。
- 題庫保留了原材料中的題目標籤。目前程式碼庫沒有提供逐題來源和授權記錄。

## 授權條款

[MIT](LICENSE)
