\# REST Resource: sources



\- \[Resource: Source](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#Source)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#Source.SCHEMA\_REPRESENTATION)

\- \[GitHubRepo](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubRepo)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubRepo.SCHEMA\_REPRESENTATION)

\- \[GitHubBranch](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch.SCHEMA\_REPRESENTATION)

\- \[Methods](https://developers.google.com/jules/api/reference/rest/v1alpha/sources#METHODS\_SUMMARY)



\## Resource: Source



An input source of data for a session.



| JSON representation |

|---|

| ``` { "name": string, "id": string, // Union field `source` can be only one of the following: "githubRepo": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubRepo`) } // End of list of possible types for union field `source`. } ``` |



| Fields ||

|---|---|

| `name` | `string` Identifier. The full resource name (e.g., "sources/{source}"). |

| `id` | `string` Output only. The id of the source. This is the same as the "{source}" part of the resource name (e.g., "sources/{source}"). |

| Union field `source`. The input data source. `source` can be only one of the following: ||

| `githubRepo` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubRepo`)`` A GitHub repo. |



\## GitHubRepo



A GitHub repo.



| JSON representation |

|---|

| ``` { "owner": string, "repo": string, "isPrivate": boolean, "defaultBranch": { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch`) }, "branches": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch`) } ] } ``` |



| Fields ||

|---|---|

| `owner` | `string` The owner of the repo; the `<owner>` in `https://github.com/<owner>/<repo>`. |

| `repo` | `string` The name of the repo; the `<repo>` in `https://github.com/<owner>/<repo>`. |

| `isPrivate` | `boolean` Whether this repo is private. |

| `defaultBranch` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch`)`` The default branch for this repo. |

| `branches\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sources#GitHubBranch`)`` The list of active branches for this repo. |



\## GitHubBranch



A GitHub branch.



| JSON representation |

|---|

| ``` { "displayName": string } ``` |



| Fields ||

|---|---|

| `displayName` | `string` The name of the GitHub branch. |



| ## Methods ||

|---|---|

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sources/get` | Gets a single source. |

| ### `https://developers.google.com/jules/api/reference/rest/v1alpha/sources/list` | Lists sources. |

