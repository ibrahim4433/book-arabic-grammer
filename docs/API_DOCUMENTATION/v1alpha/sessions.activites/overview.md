\# REST Resource: sessions.activities



\- \[Resource: Activity](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Activity)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Activity.SCHEMA\_REPRESENTATION)

\- \[AgentMessaged](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#AgentMessaged)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#AgentMessaged.SCHEMA\_REPRESENTATION)

\- \[UserMessaged](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#UserMessaged)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#UserMessaged.SCHEMA\_REPRESENTATION)

\- \[PlanGenerated](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanGenerated)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanGenerated.SCHEMA\_REPRESENTATION)

\- \[Plan](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Plan)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Plan.SCHEMA\_REPRESENTATION)

\- \[PlanStep](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanStep)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanStep.SCHEMA\_REPRESENTATION)

\- \[PlanApproved](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanApproved)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanApproved.SCHEMA\_REPRESENTATION)

\- \[ProgressUpdated](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ProgressUpdated)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ProgressUpdated.SCHEMA\_REPRESENTATION)

\- \[SessionCompleted](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionCompleted)

\- \[SessionFailed](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionFailed)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionFailed.SCHEMA\_REPRESENTATION)

\- \[Artifact](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Artifact)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Artifact.SCHEMA\_REPRESENTATION)

\- \[ChangeSet](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ChangeSet)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ChangeSet.SCHEMA\_REPRESENTATION)

\- \[GitPatch](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#GitPatch)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#GitPatch.SCHEMA\_REPRESENTATION)

\- \[Media](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Media)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Media.SCHEMA\_REPRESENTATION)

\- \[BashOutput](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#BashOutput)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#BashOutput.SCHEMA\_REPRESENTATION)

\- \[Methods](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#METHODS\_SUMMARY)



\## Resource: Activity



An activity is a single unit of work within a session.



| JSON representation |

|---|

| ``` { "name": string, "id": string, "description": string, "createTime": string, "originator": string, "artifacts": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Artifact`) } ], // Union field `activity` can be only one of the following: "agentMessaged": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#AgentMessaged`) }, "userMessaged": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#UserMessaged`) }, "planGenerated": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanGenerated`) }, "planApproved": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanApproved`) }, "progressUpdated": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ProgressUpdated`) }, "sessionCompleted": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionCompleted`) }, "sessionFailed": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionFailed`) } // End of list of possible types for union field `activity`. } ``` |



| Fields ||

|---|---|

| `name` | `string` Identifier. The full resource name (e.g., "sessions/{session}/activities/{activity}"). |

| `id` | `string` Output only. The id of the activity. This is the same as the "{activity}" part of the resource name (e.g., "sessions/{session}/activities/{activity}"). |

| `description` | `string` Output only. A description of this activity. |

| `createTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. The time at which this activity was created. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

| `originator` | `string` The entity that this activity originated from (e.g. "user", "agent", "system"). |

| `artifacts\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Artifact`)`` Output only. The artifacts produced by this activity. |

| Union field `activity`. The activity content. `activity` can be only one of the following: ||

| `agentMessaged` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#AgentMessaged`)`` The agent posted a message. |

| `userMessaged` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#UserMessaged`)`` The user posted a message. |

| `planGenerated` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanGenerated`)`` A plan was generated. |

| `planApproved` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanApproved`)`` A plan was approved. |

| `progressUpdated` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ProgressUpdated`)`` There was a progress update. |

| `sessionCompleted` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionCompleted`)`` The session was completed. |

| `sessionFailed` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#SessionFailed`)`` The session failed. |



\## AgentMessaged



The agent posted a message.



| JSON representation |

|---|

| ``` { "agentMessage": string } ``` |



| Fields ||

|---|---|

| `agentMessage` | `string` The message the agent posted. |



\## UserMessaged



The user posted a message.



| JSON representation |

|---|

| ``` { "userMessage": string } ``` |



| Fields ||

|---|---|

| `userMessage` | `string` The message the user posted. |



\## PlanGenerated



A plan was generated.



| JSON representation |

|---|

| ``` { "plan": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Plan`) } } ``` |



| Fields ||

|---|---|

| `plan` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Plan`)`` The plan that was generated. |



\## Plan



A plan is a sequence of steps that the agent will take to complete the task.



| JSON representation |

|---|

| ``` { "id": string, "steps": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanStep`) } ], "createTime": string } ``` |



| Fields ||

|---|---|

| `id` | `string` Output only. ID for this plan; unique within a session. |

| `steps\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#PlanStep`)`` Output only. The steps in the plan. |

| `createTime` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` Output only. Time when the plan was created. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |



\## PlanStep



A step in a plan.



| JSON representation |

|---|

| ``` { "id": string, "title": string, "description": string, "index": integer } ``` |



| Fields ||

|---|---|

| `id` | `string` Output only. ID for this step; unique within a plan. |

| `title` | `string` Output only. The title of the step. |

| `description` | `string` Output only. The description of the step. |

| `index` | `integer` Output only. 0-based index into the plan.steps. |



\## PlanApproved



A plan was approved.



| JSON representation |

|---|

| ``` { "planId": string } ``` |



| Fields ||

|---|---|

| `planId` | `string` The ID of the plan that was approved. |



\## ProgressUpdated



There was a progress update.



| JSON representation |

|---|

| ``` { "title": string, "description": string } ``` |



| Fields ||

|---|---|

| `title` | `string` The title of the progress update. |

| `description` | `string` The description of the progress update. |



\## SessionCompleted



This type has no fields.

The session was completed.



\## SessionFailed



The session failed.



| JSON representation |

|---|

| ``` { "reason": string } ``` |



| Fields ||

|---|---|

| `reason` | `string` The reason the session failed. |



\## Artifact



An artifact is a single unit of data produced by an activity step.



| JSON representation |

|---|

| ``` { // Union field `content` can be only one of the following: "changeSet": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ChangeSet`) }, "media": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Media`) }, "bashOutput": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#BashOutput`) } // End of list of possible types for union field `content`. } ``` |



| Fields ||

|---|---|

| Union field `content`. The artifact content. `content` can be only one of the following: ||

| `changeSet` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#ChangeSet`)`` A change set was produced (e.g. code changes). |

| `media` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Media`)`` A media file was produced (e.g. image, video). |

| `bashOutput` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#BashOutput`)`` A bash output was produced. |



\## ChangeSet



A set of changes to be applied to a source.



| JSON representation |

|---|

| ``` { "source": string, // Union field `changes` can be only one of the following: "gitPatch": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#GitPatch`) } // End of list of possible types for union field `changes`. } ``` |



| Fields ||

|---|---|

| `source` | `string` The name of the source this change set applies to. Format: sources/{source} |

| Union field `changes`. The changes to be applied to the source. `changes` can be only one of the following: ||

| `gitPatch` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#GitPatch`)`` A patch in Git format. |



\## GitPatch



A patch in Git format.



| JSON representation |

|---|

| ``` { "unidiffPatch": string, "baseCommitId": string, "suggestedCommitMessage": string } ``` |



| Fields ||

|---|---|

| `unidiffPatch` | `string` The patch in unidiff format. |

| `baseCommitId` | `string` The base commit id of the patch. This is the id of the commit that the patch should be applied to. |

| `suggestedCommitMessage` | `string` A suggested commit message for the patch, if one is generated. |



\## Media



A media output.



| JSON representation |

|---|

| ``` { "data": string, "mimeType": string } ``` |



| Fields ||

|---|---|

| `data` | `string (https://developers.google.com/discovery/v1/type-format format)` The media data. A base64-encoded string. |

| `mimeType` | `string` The media mime type. |



\## BashOutput



A bash output.



| JSON representation |

|---|

| ``` { "command": string, "output": string, "exitCode": integer } ``` |



| Fields ||

|---|---|

| `command` | `string` The bash command. |

| `output` | `string` The bash output. Includes both stdout and stderr. |

| `exitCode` | `integer` The bash exit code. |



| ## Methods ||

|---|---|

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/get` | Gets a single activity. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list` | Lists activities for a session. |

