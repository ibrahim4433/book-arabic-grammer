# Project TODO: 

1. implement the new cli-headless way of using batch jules sessions ?
"┌──(saito㉿Saito)-[~]
└─$ jules --help
A CLI for Jules, the asynchronous coding agent from Google.

Usage:
  jules [flags]
  jules [command]

Examples:
jules # Launch the TUI

# Create a session (defaults to current working directory's repository)
jules new "write unit tests"

# Create a session for a specific repository
jules new --repo torvalds/linux "write unit tests"

# Create 3 parallel sessions for the same task
jules new --repo torvalds/linux --parallel 3 "write unit tests"

# List all sessions
jules remote list --session

# List all repos
jules remote list --repo

# Pull the result of a session
jules remote pull --session 123456

# Pull and apply the patch to the local repository
jules remote pull --session 123456 --apply

# Teleport to a session (clone repo + checkout branch + apply patch, or apply to existing repo)
jules teleport 123456

# Create multiple sessions for each task in TODO.md
cat TODO.md | while IFS= read -r line; do\
  jules new "$line";\
done

# Create a session based on the first issue assigned to @me
gh issue list --assignee @me --limit 1 --json title | jq -r '.[0].title' | jules new

# Use Gemini CLI to analyze GitHub issues and send the hardest one to Jules
gemini -p "find the most tedious issue, print it verbatim\n$(gh issue list --assignee @me)" | jules new

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  login       Login your Google account to use Jules
  logout      Logout your Google account
  new         Assign a new session to Jules (defaults to current working directory)
  remote      Interact with remote sessions, e.g. new/list/pull
  teleport    Clone repository and apply session changes (or apply to existing repo)
  version     Show the version

Flags:
  -h, --help           help for jules
      --theme string   Which theme to use, dark/light (default "dark")

Use "jules [command] --help" for more information about a command.
"

## Jules API Implementation Plan

Based on the API documentation, here is a full plan on how to update the current workflow of the tools using Jules batch sessions to ensure correct implementation, fix mistakes, and adopt a proper architecture:

### Architecture & Workflow Updates:

1. **Authentication & Setup (API Keys instead of UI/Headless hacks)**
   - Remove any manual session cookie passing or brittle headless browser logins.
   - Transition to using formal API Keys generated via the Jules Web App settings.
   - Use the `X-Goog-Api-Key` header for all requests to `https://jules.googleapis.com/v1alpha/...`.

2. **Source Discovery (`v1alpha/sources`)**
   - Use `GET /v1alpha/sources` to dynamically retrieve the correct GitHub repository source ID (e.g., `sources/github/owner/repo`) rather than hardcoding repository references.

3. **Session Creation Workflow (`POST /v1alpha/sessions`)**
   - Create batch sessions asynchronously using `POST /v1alpha/sessions`.
   - Provide the prompt, sourceContext, and use `automationMode: AUTO_CREATE_PR` directly in the JSON payload.
   - Instead of maintaining complex browser state, immediately store the returned `name` (e.g., `sessions/12345`) in the `state_manager` for monitoring.

4. **Activity Monitoring & Polling (`v1alpha/sessions.activities`)**
   - Replace complex web scraping or unstable polling with `GET /v1alpha/sessions/{SESSION_ID}/activities`.
   - Implement an intelligent polling mechanism (with backoff) to iterate through the activities feed and track state changes (`planGenerated`, `progressUpdated`, `sessionCompleted`).

5. **Headless Agent Q&A (`POST /v1alpha/sessions/{SESSION_ID}:sendMessage`)**
   - During the polling cycle, if an activity indicates Jules is blocked or requires input, use the headless Gemini client to formulate a response and post it back to the session using the `sendMessage` endpoint.

6. **Plan Approval Handling**
   - While the API defaults to auto-approving plans, you can enforce strict quality control by setting `requirePlanApproval: true` on creation.
   - Automatically trigger `POST /v1alpha/sessions/{SESSION_ID}:approvePlan` via the script *only* after reviewing the plan output.

7. **PR Pulling and Result Extraction**
   - Wait for the activity containing `sessionCompleted`.
   - The completed activity payload will reliably contain the `pullRequest` URL and `changeSet` info. This allows the script to directly fetch the patch or merge the PR locally via the `gh` CLI, eliminating the need to search through branches and guess file names (like in `jules_page_generator.py`).

### CLI Alternative Option:
The `jules` CLI commands can act as an immediate drop-in replacement for bash-level orchestration (e.g., using `jules new` in a loop from `TODO.md` alongside `jules remote pull`). However, the REST API approach detailed above is recommended for deeper Python integration inside `jules_planner.py` and `jules_page_generator.py`.