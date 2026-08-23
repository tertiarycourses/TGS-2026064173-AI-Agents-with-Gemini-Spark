# Lab 1: Create the Agent Strategy and Approval Map

**Course:** AI Agents with Gemini Spark (TGS-2026064173)  
**Learning objective:** Translate a website goal into a bounded Gemini Spark task with permissions, risk tiers, approval gates and acceptance evidence.  
**Assessment alignment:** A1, K1  
**Tools:** Gemini Spark task planning, browser research, Google Drive, human review

## Scenario

Northstar Studio is a small Singapore design business preparing a responsive website and a governed content workflow. You are the human owner of the outcome. Gemini Spark may research, organise or draft within the approved boundary; Claude Code, Codex or Antigravity may edit the local website repository. Publishing, sending, purchases, credential entry and sensitive-data changes always require human control.

## Deliverable

A strategy brief, task contract, permission matrix, risk register and human-approval map for the Northstar Studio website.

## Before you start

1. Work only with the supplied mock data and project folder.
2. Never paste passwords, payment details, live customer data or API keys into an agent task.
3. Read the requested plan and inspect every file diff before accepting a change.
4. Stop if the agent requests a new tool, site, permission or consequential action outside the approved contract.

## Detailed procedure

### Step 1 - Open the supplied business brief and identify the audience, primary action, required pages and prohibited claims.

**Work with:** `brief-template.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 2 - Write one measurable outcome using the pattern: deliverable + audience + quality threshold + deadline.

**Work with:** `agent-task-contract.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 3 - Decompose the outcome into research, content, design, build, test and release work packages.

**Work with:** `agent-task-contract.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 4 - Mark which work package belongs to Gemini Spark, the coding agent or the human owner.

**Work with:** `responsibility-map.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 5 - Select only the minimum data sources and tools needed for each work package.

**Work with:** `permission-matrix.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 6 - Classify each proposed action as observe, draft, modify, communicate, publish or transact.

**Work with:** `risk-register.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 7 - Require human approval for every communicate, publish or transact action and for changes to sensitive data.

**Work with:** `approval-map.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 8 - Add stop rules for credential requests, unexpected sites, sensitive data, new dependencies and unsupported claims.

**Work with:** `approval-map.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 9 - Define acceptance evidence: filenames, source links, screenshots, test results and owner sign-off.

**Work with:** `acceptance-checklist.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 10 - Ask Gemini Spark to interview you about missing constraints; do not authorize execution yet.

> Interview me to find missing scope, permissions, evidence and stop conditions for this website project.

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 11 - Review Spark's proposed plan and remove any step that exceeds the permission matrix.

**Work with:** `review-checklist.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 12 - Save the approved strategy package and capture the final review decision.

**Work with:** `evidence/strategy-approval.txt`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

## Acceptance test

The task can be executed without guessing: every step has an owner, allowed tools, a risk tier, approval rule, stop condition and observable completion evidence.

## Evidence checklist

- [ ] All required working files are present.
- [ ] The permission boundary was followed.
- [ ] Human approval is recorded at every required gate.
- [ ] The acceptance test was run and the result captured.
- [ ] Any failure or limitation is recorded honestly.
- [ ] No secret, live personal data or answer key is present.

## Clean-up / rollback

Pause any schedule created for the lab, stop unfinished tasks, disconnect unnecessary apps, and restore the recorded baseline or rollback commit if the final evidence does not pass.
