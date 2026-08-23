# Lab 3: Design a Reusable Spark Content Skill and Schedule

**Course:** AI Agents with Gemini Spark (TGS-2026064173)  
**Learning objective:** Turn the approved content workflow into a reusable skill and a scheduled draft-only operation with ownership and rollback controls.  
**Assessment alignment:** A3, K3, K5  
**Tools:** Gemini Spark skills, schedules, Drive, Docs, Sheets, Gmail notification

## Scenario

Northstar Studio is a small Singapore design business preparing a responsive website and a governed content workflow. You are the human owner of the outcome. Gemini Spark may research, organise or draft within the approved boundary; Claude Code, Codex or Antigravity may edit the local website repository. Publishing, sending, purchases, credential entry and sensitive-data changes always require human control.

## Deliverable

A versioned website-content skill, output schema, schedule specification, trigger deduplication rule and implementation plan.

## Before you start

1. Work only with the supplied mock data and project folder.
2. Never paste passwords, payment details, live customer data or API keys into an agent task.
3. Read the requested plan and inspect every file diff before accepting a change.
4. Stop if the agent requests a new tool, site, permission or consequential action outside the approved contract.

## Detailed procedure

### Step 1 - Review the approved content inventory and mark each source as allowed, blocked or approval-required.

**Work with:** `content-inventory.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 2 - Open the supplied SKILL.md template and rewrite the description as a precise trigger contract.

**Work with:** `skill/SKILL.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 3 - Define required inputs, freshness window, exclusions and the exact output schema.

**Work with:** `skill/SKILL.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 4 - Add a source-verification step that records the URL, publication date and claim supported.

**Work with:** `skill/source-log-template.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 5 - Add a draft-only rule: save to Review/Drafts and never publish or send externally.

**Work with:** `skill/SKILL.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 6 - Add a human checkpoint requiring an APPROVED.txt file before a coding change request is created.

**Work with:** `skill/SKILL.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 7 - Define a safe failure route for missing sources, ambiguous claims and unavailable folders.

**Work with:** `skill/SKILL.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 8 - Create a schedule specification for Monday 09:00 Asia/Singapore with a unique run key.

**Work with:** `schedule-spec.yaml`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 9 - Add a concurrency rule so a new run is skipped when a prior run is active.

**Work with:** `schedule-spec.yaml`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 10 - Assign the workflow owner, reviewer, backup reviewer and incident contact.

**Work with:** `implementation-plan.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 11 - Set target timings and evidence for research, draft, review, approved change and closure.

**Work with:** `implementation-plan.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 12 - Ask Spark to create the skill conversationally, then compare the created instructions with the local template.

> Create a website-content-draft skill from this approved SKILL.md. Do not connect apps or schedule it yet.

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 13 - Review the requested connected-app permissions and enable only the agreed project folder and notification path.

**Work with:** `permission-review.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 14 - Run one supervised dry run, verify the draft and logs, then pause the schedule until trainer sign-off.

**Work with:** `evidence/dry-run-checklist.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

## Acceptance test

The skill produces the specified draft and source log, the schedule cannot overlap, publication is impossible without human approval, and every stage has an owner, target time and evidence artifact.

## Evidence checklist

- [ ] All required working files are present.
- [ ] The permission boundary was followed.
- [ ] Human approval is recorded at every required gate.
- [ ] The acceptance test was run and the result captured.
- [ ] Any failure or limitation is recorded honestly.
- [ ] No secret, live personal data or answer key is present.

## Clean-up / rollback

Pause any schedule created for the lab, stop unfinished tasks, disconnect unnecessary apps, and restore the recorded baseline or rollback commit if the final evidence does not pass.
