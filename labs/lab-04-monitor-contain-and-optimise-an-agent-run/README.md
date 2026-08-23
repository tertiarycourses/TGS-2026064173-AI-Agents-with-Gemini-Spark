# Lab 4: Monitor, Contain and Optimise an Agent Run

**Course:** AI Agents with Gemini Spark (TGS-2026064173)  
**Learning objective:** Evaluate a Spark-supported website workflow, respond to a simulated incident and implement one controlled improvement.  
**Assessment alignment:** A4, K2, K6  
**Tools:** Gemini Spark task panels, schedule controls, website QA, evidence review, incident playbook

## Scenario

Northstar Studio is a small Singapore design business preparing a responsive website and a governed content workflow. You are the human owner of the outcome. Gemini Spark may research, organise or draft within the approved boundary; Claude Code, Codex or Antigravity may edit the local website repository. Publishing, sending, purchases, credential entry and sensitive-data changes always require human control.

## Deliverable

A completed KPI scorecard, incident timeline, containment record, root-cause analysis and verified improvement proposal.

## Before you start

1. Work only with the supplied mock data and project folder.
2. Never paste passwords, payment details, live customer data or API keys into an agent task.
3. Read the requested plan and inspect every file diff before accepting a change.
4. Stop if the agent requests a new tool, site, permission or consequential action outside the approved contract.

## Detailed procedure

### Step 1 - Open the simulated run log and mark planned, completed, failed and approval-waiting steps.

**Work with:** `simulation/run-log.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 2 - Compare the reported file list with the actual files in simulation/output/.

**Work with:** `simulation/output/`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 3 - Score accuracy, completeness, safety, accessibility and owner acceptance from 0 to 100.

**Work with:** `qa-scorecard.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 4 - Calculate failed-run rate, retry count, intervention minutes and cycle time.

**Work with:** `qa-scorecard.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 5 - Identify the prompt-injection message embedded in the supplied source and stop the run.

**Work with:** `simulation/tainted-source.html`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 6 - Pause the schedule and record the time, actor and reason in the incident timeline.

**Work with:** `incident-timeline.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 7 - Remove the tainted source from the allow-list and disconnect any unnecessary app permission.

**Work with:** `containment-checklist.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 8 - Restore the website content from the recorded rollback commit.

**Work with:** `git -C ../lab-02-vibe-code-website/working-site log --oneline -5`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 9 - Draft a public correction only if the bad content was published; require owner approval before sending.

**Work with:** `correction-draft.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 10 - Use five whys to identify the missing control that allowed the unsafe source into the workflow.

**Work with:** `root-cause-analysis.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 11 - Propose one smallest effective control: source allow-list, evidence rule or approval gate.

**Work with:** `improvement-proposal.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 12 - Run the simulation again with the control and record before/after KPI values.

**Work with:** `qa-scorecard.csv`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 13 - Approve the improvement only if it reduces risk without blocking the legitimate workflow.

**Work with:** `review-signoff.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

### Step 14 - Set the next review date and owner for the skill, schedule and permissions.

**Work with:** `review-signoff.md`

**Review before continuing**

- Confirm the result serves the stated objective.
- Confirm only approved files, data and tools were used.
- Capture the named evidence artifact or note why the step stopped.

## Acceptance test

The learner detects the unsafe instruction, stops and contains the run, restores the approved state, explains the root cause, and proves one control improvement with before/after evidence.

## Evidence checklist

- [ ] All required working files are present.
- [ ] The permission boundary was followed.
- [ ] Human approval is recorded at every required gate.
- [ ] The acceptance test was run and the result captured.
- [ ] Any failure or limitation is recorded honestly.
- [ ] No secret, live personal data or answer key is present.

## Clean-up / rollback

Pause any schedule created for the lab, stop unfinished tasks, disconnect unnecessary apps, and restore the recorded baseline or rollback commit if the final evidence does not pass.
