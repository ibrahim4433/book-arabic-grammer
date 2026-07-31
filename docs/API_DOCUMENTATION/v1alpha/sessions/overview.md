\# REST Resource: sessions



\- \[Resource: Session](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#Session)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#Session.SCHEMA\_REPRESENTATION)

\- \[SourceContext](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SourceContext)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SourceContext.SCHEMA\_REPRESENTATION)

\- \[GitHubRepoContext](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#GitHubRepoContext)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#GitHubRepoContext.SCHEMA\_REPRESENTATION)

\- \[AutomationMode](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#AutomationMode)

\- \[State](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#State)

\- \[SessionOutput](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SessionOutput)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SessionOutput.SCHEMA\_REPRESENTATION)

\- \[PullRequest](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#PullRequest)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#PullRequest.SCHEMA\_REPRESENTATION)

\- \[Methods](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#METHODS\_SUMMARY)



\## Resource: Session



A session is a contiguous amount of work within the same context.



| JSON representation |

|---|

| ``` { "name": string, "id": string, "prompt": string, "sourceContext": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SourceContext`) }, "title": string, "requirePlanApproval": boolean, "automationMode": enum (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#AutomationMode`), "createTime": string, "updateTime": string, "state": enum (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#State`), "url": string, "outputs": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SessionOutput`) } ] } ``` |



| Fields ||

|---|---|

| `name` | `string` Output only. Identifier. The full resource name (e.g., "sessions/{session}"). |

| `id` | `string` Output only. The id of the session. This is the same as the "{session}" part of the resource name (e.g., "sessions/{session}"). |

| `prompt` | `string` Required. The prompt to start the session with. |

| `sourceContext` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SourceContext`)`` Required. The source to use in this session, with additional context. |

| `title` | `string` Optional. If not provided, the system will generate one. |

| `requirePlanApproval` | `boolean` Optional. Input only. If true, plans the agent generates will require explicit plan approval before the agent starts working. If not set, plans will be auto-approved. |

| `automationMode` | ``enum (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#AutomationMode`)`` Optional. Input only. The automation mode of the session. If not set, the default automation mode will be used. |

| `createTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time the session was created. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

| `updateTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time the session was last updated. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

| `state` | ``enum (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#State`)`` Output only. The state of the session. |

| `url` | `string` Output only. The URL of the session to view the session in the Jules web app. |

| `outputs\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#SessionOutput`)`` Output only. The outputs of the session, if any. |



\## SourceContext



Context for how to use a source in a session.



| JSON representation |

|---|

| ``` { "source": string, // Union field `context` can be only one of the following: "githubRepoContext": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#GitHubRepoContext`) } // End of list of possible types for union field `context`. } ``` |



| Fields ||

|---|---|

| `source` | `string` Required. The name of the source this context is for. To get the list of sources, use the ListSources API. Format: sources/{source} |

| Union field `context`. The context for how to use the source in a session. `context` can be only one of the following: ||

| `githubRepoContext` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#GitHubRepoContext`)`` Context to use a GitHubRepo in a session. |



\## GitHubRepoContext



Context to use a GitHubRepo in a session.



| JSON representation |

|---|

| ``` { "startingBranch": string } ``` |



| Fields ||

|---|---|

| `startingBranch` | `string` Required. The name of the branch to start the session from. |



\## AutomationMode



The automation mode of the session.



| Enums ||

|---|---|

| `AUTOMATION\_MODE\_UNSPECIFIED` | The automation mode is unspecified. Default to no automation. |

| `AUTO\_CREATE\_PR` | Whenever a final code patch is generated in the session, automatically create a branch and a pull request for it, if applicable. |



\## State



State of a session.



| Enums ||

|---|---|

| `STATE\_UNSPECIFIED` | The state is unspecified. |

| `QUEUED` | The session is queued. |

| `PLANNING` | The agent is planning. |

| `AWAITING\_PLAN\_APPROVAL` | The agent is waiting for plan approval. |

| `AWAITING\_USER\_FEEDBACK` | The agent is waiting for user feedback. |

| `IN\_PROGRESS` | The session is in progress. |

| `PAUSED` | The session is paused. |

| `FAILED` | The session has failed. |

| `COMPLETED` | The session has completed. |



\## SessionOutput



An output of a session.



| JSON representation |

|---|

| ``` { // Union field `output` can be only one of the following: "pullRequest": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#PullRequest`) } // End of list of possible types for union field `output`. } ``` |



| Fields ||

|---|---|

| Union field `output`. An output of the session. `output` can be only one of the following: ||

| `pullRequest` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#PullRequest`)`` A pull request created by the session, if applicable. |



\## PullRequest



A pull request.



| JSON representation |

|---|

| ``` { "url": string, "title": string, "description": string } ``` |



| Fields ||

|---|---|

| `url` | `string` The URL of the pull request. |

| `title` | `string` The title of the pull request. |

| `description` | `string` The description of the pull request. |



| ## Methods ||

|---|---|

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/approvePlan` | Approves a plan in a session. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/create` | Creates a new session. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/get` | Gets a single session. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list` | Lists all sessions. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage` | Sends a message from the user to a session. |

