\# Method: sessions.list



\- \[HTTP request](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list#body.HTTP\_TEMPLATE)

\- \[Query parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list#body.QUERY\_PARAMETERS)

\- \[Request body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list#body.request\_body)

\- \[Response body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list#body.response\_body)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/list#body.ListSessionsResponse.SCHEMA\_REPRESENTATION)



Lists all sessions.



\### HTTP request



`GET https://jules.googleapis.com/v1alpha/sessions`



The URL uses \[gRPC Transcoding](https://google.aip.dev/127) syntax.



\### Query parameters



| Parameters ||

|---|---|

| `pageSize` | `integer` Optional. The number of sessions to return. Must be between 1 and 100, inclusive. If unset, defaults to 30. If set to greater than 100, it will be coerced to 100. |

| `pageToken` | `string` Optional. A page token, received from a previous `sessions.list` call. |



\### Request body



The request body must be empty.



\### Response body



Response message for sessions.list.



If successful, the response body contains data with the following structure:



| JSON representation |

|---|

| ``` { "sessions": \[ { object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#Session`) } ], "nextPageToken": string } ``` |



| Fields ||

|---|---|

| `sessions\[]` | ``object (`https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#Session`)`` The sessions from the specified request. |

| `nextPageToken` | `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. |

