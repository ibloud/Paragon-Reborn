# Teams + Planner Collaboration Layer

## Purpose

Teams is the collaboration surface for people, meetings, reviews, and hackathon coordination. Planner is the execution surface for sprint tasks, owners, milestones, and workload.

The canonical project record remains split by responsibility:

| System | Canonical responsibility |
|---|---|
| GitHub | Code, issues/PRs, schemas, tests, architecture contracts, roadmap, published project docs |
| SharePoint / OneDrive | Research corpus, source files, working documents, rights/provenance records, review packets |
| Teams | Conversation, meetings, collaboration, review sessions |
| Planner | Sprint/hackathon execution, tasks, owners, milestones, workload |
| Azure | Preview/staging/production runtime |

Teams and Planner must link back to GitHub and SharePoint rather than silently becoming a second source of truth.

## Paragon-Reborn Teams workspace

Recommended Team name: **Return to the Void — Paragon-Reborn**

Channels:

- `00-announcements` — project-wide notices and milestone changes
- `01-brief` — current sprint/hackathon brief and acceptance criteria
- `02-ideas` — proposals and design discussion
- `03-build` — implementation coordination
- `04-demo` — demos, captures, and review sessions
- `05-review` — structured review and decisions
- `06-shipping` — release readiness and deployment coordination

Each channel should contain links/tabs to the relevant GitHub views and SharePoint folders. Files that become canonical project documentation should be promoted back into GitHub.

## Planner execution model

Use a Planner plan named **Paragon-Reborn Delivery**.

Default buckets:

1. Backlog
2. Ready
3. In Progress
4. Review
5. Done
6. Blocked

Task conventions:

- **Title:** action-oriented task
- **Description:** acceptance criteria + links to GitHub issue/PR and supporting SharePoint material
- **Owner:** responsible contributor
- **Due date:** sprint commitment
- **Labels:** `engineering`, `research`, `design`, `review`, `release`, `blocked`
- **Checklist:** concrete completion steps

For premium Planner capabilities, sprints/dependencies/custom fields can be used where the tenant/license supports them.

## Sprint flow

```
Backlog
  -> Ready
  -> In Progress
  -> Review
  -> Done
```

Blocked work moves to **Blocked** with the blocking dependency recorded in the task and the corresponding GitHub issue.

A completed Planner task should normally point to a merged PR, closed issue, published document, or other durable artifact. Planner is the execution ledger, not the permanent technical record.

## Hackathon mode

A hackathon can reuse the same Team with a dedicated channel set or use a separate Team when membership/security requires isolation.

Suggested flow:

```
Brief
  -> Ideas
  -> Build
  -> Integration
  -> QA
  -> Demo
  -> Ship
```

Recommended hackathon task fields:

- owner/team
- track
- repository
- GitHub issue/PR
- acceptance criteria
- demo status
- deployment target
- reviewer
- ship/no-ship decision

The **Loptr-Lab/duet-solo-hackathon** repository is a natural later pilot for this reusable hackathon template.

## GitHub ↔ Teams operating pattern

1. Work is proposed or tracked in a GitHub issue.
2. The issue becomes a Planner task when it is committed to a sprint/hackathon.
3. Discussion happens in Teams.
4. Code changes happen in GitHub.
5. Research/evidence stays in SharePoint.
6. The Planner task links the relevant GitHub and SharePoint artifacts.
7. Review occurs in Teams and GitHub.
8. Completion is recorded in GitHub and Planner.
9. Release/deployment status is surfaced in Teams; Azure remains the runtime authority.

## Automation candidates

A later Power Automate / Microsoft Graph layer can automate:

- GitHub issue -> Planner task creation
- GitHub PR opened -> Teams review notification
- PR merged -> Planner task completion
- blocked GitHub issue -> Teams alert
- sprint start/end -> Teams summary
- hackathon deadline -> Teams reminders
- SharePoint research item classified -> linked Planner research task
- release candidate -> Teams shipping checklist

Automation should create links and notifications, not duplicate the underlying canonical content.

## Provisioning status

The current ChatGPT-connected Microsoft surface exposes SharePoint/OneDrive operations, but not Team or Planner provisioning operations. Therefore this document defines the implementation contract without falsely claiming that a Team or Planner plan has been created.

When Teams/Planner write access is connected, the first provisioning pass should create the Paragon-Reborn Team/channel structure and the Planner execution board described above.

## Security boundary

Do not place restricted/proprietary source material in public GitHub merely to make it visible in Teams. Use SharePoint permissions for document access, GitHub permissions for source access, and Teams membership/channel permissions for collaboration access.

No secrets, credentials, or private source assets belong in this repository.
