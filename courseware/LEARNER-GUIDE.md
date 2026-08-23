# Learner Guide - AI Agents with Gemini Spark

**Course code:** TGS-2026064173  
**Version:** v1.0  
**Duration:** 8 hours, including assessment

## Course learning outcomes

- LO1: Determine an AI-agent strategy by translating a web-design goal into bounded tasks, permissions, risks and human approval points.
- LO2: Develop web content and a responsive website through a controlled vibe-coding loop using Claude Code, Codex or Antigravity, with Gemini Spark supporting research and reusable skills.
- LO3: Develop an implementation plan for Gemini Spark tasks, skills, schedules and connected tools, including responsibilities, timelines and rollback controls.
- LO4: Evaluate agent and website performance using evidence, acceptance criteria, incident signals and iterative improvement decisions.

## Before you start

Use a supported Google account where Gemini Spark is available, a modern browser, Git, Python 3, and one coding agent: Claude Code, Codex, or Antigravity. Use only supplied training data. Keep personal data, payment details, credentials, and private API keys out of prompts and files.

## Topic concepts

### Topic 01 - Agent Strategy and Gemini Spark Runtime

Autonomy is safe only when the goal, permission boundary, evidence and stop conditions are explicit.

- **Task thread:** Holds the goal, instructions, files and task state.
- **Planner:** Decomposes the goal into observable steps and revises when blocked.
- **Skills:** Reusable how-to instructions and context, selected explicitly or automatically.
- **Connected tools:** Workspace apps, websites, local or remote browser, and code execution.
- **Human control:** Review, confirm, take over, stop, pause schedules and inspect changed files.

### Topic 02 - Vibe Coding a Responsive Website

Vibe coding is rapid co-creation with an AI coding agent, disciplined by small changes, executable evidence and human review.

- **Design brief:** Audience, job-to-be-done, content, constraints and acceptance tests.
- **Coding agent:** Claude Code, Codex or Antigravity edits the repository from natural-language intent.
- **Local project:** HTML, CSS, JavaScript, assets, README and version history.
- **Test loop:** Open in a browser, check responsive layouts, links, form states and accessibility.
- **Reviewer:** Accepts, rejects or redirects each meaningful change before release.

### Topic 03 - Skills, Schedules and Implementation Governance

A reusable agent workflow is an operating procedure with versioned instructions, scoped tools, owners and measurable completion evidence.

- **Task:** The what: a complete project or objective managed in a thread.
- **Skill:** The how: reusable instructions, context, tools and quality rules.
- **Schedule:** The when: a time-based or event-based trigger for a task.
- **Connected apps:** The where: Gmail, Calendar, Drive, Docs, Sheets, Slides, Search and approved third parties.
- **Runbook:** Owner, approvals, logs, exception handling, rollback and review cadence.

### Topic 04 - Monitoring, Incident Control and Optimisation

An agent is not successful because it completed a run; it is successful when the output is correct, safe, useful and recoverable.

- **Progress panel:** Planned, current and completed steps reveal runtime state.
- **Files panel:** Shows which files were read or updated and supports evidence review.
- **Schedules panel:** Pause or resume recurring work and inspect the active trigger.
- **Takeover/Stop:** Human interrupts browsing, supplies sensitive data directly, or cancels the task.
- **Scorecard:** Quality, safety, efficiency and business-result indicators drive the next change.

## Hands-on labs - detailed procedures

### Lab 1 - Create the Agent Strategy and Approval Map

**Goal:** Translate a website goal into a bounded Gemini Spark task with permissions, risk tiers, approval gates and acceptance evidence.  
**Build:** A strategy brief, task contract, permission matrix, risk register and human-approval map for the Northstar Studio website.  
**Assessment alignment:** A1, K1

#### Step 1 - Open the supplied business brief and identify the audience, primary action, required pages and prohibited claims.

**Work with:** `brief-template.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 2 - Write one measurable outcome using the pattern: deliverable + audience + quality threshold + deadline.

**Work with:** `agent-task-contract.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 3 - Decompose the outcome into research, content, design, build, test and release work packages.

**Work with:** `agent-task-contract.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 4 - Mark which work package belongs to Gemini Spark, the coding agent or the human owner.

**Work with:** `responsibility-map.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 5 - Select only the minimum data sources and tools needed for each work package.

**Work with:** `permission-matrix.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 6 - Classify each proposed action as observe, draft, modify, communicate, publish or transact.

**Work with:** `risk-register.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 7 - Require human approval for every communicate, publish or transact action and for changes to sensitive data.

**Work with:** `approval-map.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 8 - Add stop rules for credential requests, unexpected sites, sensitive data, new dependencies and unsupported claims.

**Work with:** `approval-map.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 9 - Define acceptance evidence: filenames, source links, screenshots, test results and owner sign-off.

**Work with:** `acceptance-checklist.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 10 - Ask Gemini Spark to interview you about missing constraints; do not authorize execution yet.

**Prompt:** Interview me to find missing scope, permissions, evidence and stop conditions for this website project.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 11 - Review Spark's proposed plan and remove any step that exceeds the permission matrix.

**Work with:** `review-checklist.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 12 - Save the approved strategy package and capture the final review decision.

**Work with:** `evidence/strategy-approval.txt`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

**Acceptance and evidence:** The task can be executed without guessing: every step has an owner, allowed tools, a risk tier, approval rule, stop condition and observable completion evidence.

**Lab folder:** `labs/lab-01-create-the-agent-strategy-and-approval-map/`

### Lab 2 - Vibe Code the Northstar Studio Website

**Goal:** Create and test a responsive website through a bounded vibe-coding loop using Claude Code, Codex or Antigravity.  
**Build:** A working one-page HTML/CSS/JavaScript website, responsive at three widths, with accessible navigation, an evidence log and a rollback commit.  
**Assessment alignment:** A2, K4, K5

#### Step 1 - Copy starter/ to working-site/ and open the folder in your chosen coding agent.

**Work with:** `cp -R starter working-site`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 2 - Initialize version control and create a baseline commit before the agent edits files.

**Work with:** `cd working-site && git init && git add index.html styles.css script.js && git commit -m 'chore: baseline starter'`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 3 - Give the agent the design brief, acceptance checklist and guardrails; ask for a plan only.

**Prompt:** Read ../design-brief.md and ../acceptance-checklist.md. Propose a five-step plan. Do not edit files yet.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 4 - Review the plan and approve only the first thin slice: semantic page structure and navigation.

**Prompt:** Implement only step 1. Preserve existing filenames and use no external framework.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 5 - Inspect the diff and reject unrelated changes before opening the site.

**Work with:** `git diff -- index.html styles.css script.js`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 6 - Run a local server and open the site in a browser.

**Work with:** `python3 -m http.server 8000`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 7 - Ask for the visual system: spacing scale, type scale, color tokens and reusable card/button styles.

**Prompt:** Implement the visual system only. Keep contrast at WCAG AA and explain the tokens you add.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 8 - Review the diff and test at 1440 px, 768 px and 390 px widths.

**Work with:** `Open http://localhost:8000 and use responsive device mode.`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 9 - Ask for the contact form interaction with client-side validation and clear success/error states.

**Prompt:** Add accessible client-side validation. Do not send data or add a backend.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 10 - Use keyboard-only navigation to test the menu, links and form controls.

**Work with:** `Tab through every interactive element; verify a visible focus indicator.`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 11 - Run the supplied checks and record results in evidence/test-results.md.

**Work with:** `python3 ../scripts/check_site.py working-site`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 12 - Ask the agent to fix only failed checks; re-run tests after each small change.

**Prompt:** Fix only the failures listed in ../evidence/test-results.md. Explain each change.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 13 - Review all claims against content-inventory.csv and remove invented facts.

**Work with:** `content-inventory.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 14 - Commit the approved website and record the commit hash as the rollback point.

**Work with:** `git add index.html styles.css script.js && git commit -m 'feat: build reviewed responsive site'`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

**Acceptance and evidence:** The website renders without errors, passes the supplied structural checks, works at desktop/tablet/mobile widths, is keyboard navigable, contains only approved claims, and has an identifiable rollback commit.

**Lab folder:** `labs/lab-02-vibe-code-the-northstar-studio-website/`

### Lab 3 - Design a Reusable Spark Content Skill and Schedule

**Goal:** Turn the approved content workflow into a reusable skill and a scheduled draft-only operation with ownership and rollback controls.  
**Build:** A versioned website-content skill, output schema, schedule specification, trigger deduplication rule and implementation plan.  
**Assessment alignment:** A3, K3, K5

#### Step 1 - Review the approved content inventory and mark each source as allowed, blocked or approval-required.

**Work with:** `content-inventory.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 2 - Open the supplied SKILL.md template and rewrite the description as a precise trigger contract.

**Work with:** `skill/SKILL.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 3 - Define required inputs, freshness window, exclusions and the exact output schema.

**Work with:** `skill/SKILL.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 4 - Add a source-verification step that records the URL, publication date and claim supported.

**Work with:** `skill/source-log-template.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 5 - Add a draft-only rule: save to Review/Drafts and never publish or send externally.

**Work with:** `skill/SKILL.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 6 - Add a human checkpoint requiring an APPROVED.txt file before a coding change request is created.

**Work with:** `skill/SKILL.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 7 - Define a safe failure route for missing sources, ambiguous claims and unavailable folders.

**Work with:** `skill/SKILL.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 8 - Create a schedule specification for Monday 09:00 Asia/Singapore with a unique run key.

**Work with:** `schedule-spec.yaml`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 9 - Add a concurrency rule so a new run is skipped when a prior run is active.

**Work with:** `schedule-spec.yaml`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 10 - Assign the workflow owner, reviewer, backup reviewer and incident contact.

**Work with:** `implementation-plan.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 11 - Set target timings and evidence for research, draft, review, approved change and closure.

**Work with:** `implementation-plan.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 12 - Ask Spark to create the skill conversationally, then compare the created instructions with the local template.

**Prompt:** Create a website-content-draft skill from this approved SKILL.md. Do not connect apps or schedule it yet.

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 13 - Review the requested connected-app permissions and enable only the agreed project folder and notification path.

**Work with:** `permission-review.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 14 - Run one supervised dry run, verify the draft and logs, then pause the schedule until trainer sign-off.

**Work with:** `evidence/dry-run-checklist.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

**Acceptance and evidence:** The skill produces the specified draft and source log, the schedule cannot overlap, publication is impossible without human approval, and every stage has an owner, target time and evidence artifact.

**Lab folder:** `labs/lab-03-design-a-reusable-spark-content-skill-and-schedule/`

### Lab 4 - Monitor, Contain and Optimise an Agent Run

**Goal:** Evaluate a Spark-supported website workflow, respond to a simulated incident and implement one controlled improvement.  
**Build:** A completed KPI scorecard, incident timeline, containment record, root-cause analysis and verified improvement proposal.  
**Assessment alignment:** A4, K2, K6

#### Step 1 - Open the simulated run log and mark planned, completed, failed and approval-waiting steps.

**Work with:** `simulation/run-log.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 2 - Compare the reported file list with the actual files in simulation/output/.

**Work with:** `simulation/output/`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 3 - Score accuracy, completeness, safety, accessibility and owner acceptance from 0 to 100.

**Work with:** `qa-scorecard.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 4 - Calculate failed-run rate, retry count, intervention minutes and cycle time.

**Work with:** `qa-scorecard.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 5 - Identify the prompt-injection message embedded in the supplied source and stop the run.

**Work with:** `simulation/tainted-source.html`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 6 - Pause the schedule and record the time, actor and reason in the incident timeline.

**Work with:** `incident-timeline.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 7 - Remove the tainted source from the allow-list and disconnect any unnecessary app permission.

**Work with:** `containment-checklist.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 8 - Restore the website content from the recorded rollback commit.

**Work with:** `git -C ../lab-02-vibe-code-website/working-site log --oneline -5`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 9 - Draft a public correction only if the bad content was published; require owner approval before sending.

**Work with:** `correction-draft.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 10 - Use five whys to identify the missing control that allowed the unsafe source into the workflow.

**Work with:** `root-cause-analysis.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 11 - Propose one smallest effective control: source allow-list, evidence rule or approval gate.

**Work with:** `improvement-proposal.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 12 - Run the simulation again with the control and record before/after KPI values.

**Work with:** `qa-scorecard.csv`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 13 - Approve the improvement only if it reduces risk without blocking the legitimate workflow.

**Work with:** `review-signoff.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

#### Step 14 - Set the next review date and owner for the skill, schedule and permissions.

**Work with:** `review-signoff.md`

**Review before continuing:** confirm the objective, permission scope, expected evidence, and stop condition; pause when any is unclear.

**Acceptance and evidence:** The learner detects the unsafe instruction, stops and contains the run, restores the approved state, explains the root cause, and proves one control improvement with before/after evidence.

**Lab folder:** `labs/lab-04-monitor-contain-and-optimise-an-agent-run/`

## Assessment flow

1. Record assessment attendance through TRAQOM.
2. Complete the 60-minute Practical Performance covering A1-A4.
3. Complete the 20-minute Oral Questioning covering K1-K6.
4. Submit candidate papers and practical evidence on the LMS.
5. Review feedback and sign the Assessment Summary Record.

## References

- [Google Gemini Spark product overview](https://gemini.google/overview/agent/spark/)
- [Google Gemini Spark Help: tasks, workflows, safety and limits](https://support.google.com/gemini/answer/17094507?hl=en&co=GENIE.Platform=Android)
- [Google Gemini Spark release updates](https://support.google.com/gemini/answer/17171264?hl=en)
- [Google: next evolution of the Gemini app](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)
- [HardwareZone Singapore beginner guide](https://www.hardwarezone.com.sg/guides/how-to-use-gemini-spark-guide)
- [DataCamp: always-on agent explained](https://www.datacamp.com/blog/gemini-spark)
- [WIRED hands-on perspective](https://www.wired.com/story/google-gemini-spark-ai-agent-hands-on/)
