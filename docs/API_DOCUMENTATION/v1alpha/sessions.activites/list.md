\# Method: sessions.activities.list



\- \[HTTP request](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.HTTP\_TEMPLATE)

\- \[Path parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.PATH\_PARAMETERS)

\- \[Query parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.QUERY\_PARAMETERS)

\- \[Request body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.request\_body)

\- \[Response body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.response\_body)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities/list#body.ListActivitiesResponse.SCHEMA\_REPRESENTATION)



Lists activities for a session.



\### HTTP request



`GET https://jules.googleapis.com/v1alpha/{parent=sessions/\*}/activities`



The URL uses \[gRPC Transcoding](https://google.aip.dev/127) syntax.



\### Path parameters



| Parameters ||

|---|---|

| `parent` | `string` Required. The parent session, which owns this collection of activities. Format: sessions/{session} It takes the form `sessions/{session}`. |



\### Query parameters



| Parameters ||

|---|---|

| `pageSize` | `integer` Optional. The number of activities to return. Must be between 1 and 100, inclusive. If unset, defaults to 50. If set to greater than 100, it will be coerced to 100. |

| `pageToken` | `string` Optional. A page token, received from a previous `activities.list` call. |



\### Request body



The request body must be empty.



\### Response body



Response message for the activities.list RPC.



If successful, the response body contains data with the following structure:



| JSON representation |

|---|

| ``` { "activities": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Activity`) } ], "nextPageToken": string } ``` |



| Fields ||

|---|---|

| `activities\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions.activities#Activity`)`` The activities from the specified session. |

| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

