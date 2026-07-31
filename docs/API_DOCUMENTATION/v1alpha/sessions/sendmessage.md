\# Method: sessions.sendMessage



\- \[HTTP request](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage#body.HTTP\_TEMPLATE)

\- \[Path parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage#body.PATH\_PARAMETERS)

\- \[Request body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage#body.request\_body)

&#x20; - \[JSON representation](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage#body.request\_body.SCHEMA\_REPRESENTATION)

\- \[Response body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/sendMessage#body.response\_body)



Sends a message from the user to a session.



\### HTTP request



`POST https://jules.googleapis.com/v1alpha/{session=sessions/\*}:sendMessage`



The URL uses \[gRPC Transcoding](https://google.aip.dev/127) syntax.



\### Path parameters



| Parameters ||

|---|---|

| `session` | `string` Required. The resource name of the session to post the message to. Format: sessions/{session} It takes the form `sessions/{session}`. |



\### Request body



The request body contains data with the following structure:



| JSON representation |

|---|

| ``` { "prompt": string } ``` |



| Fields ||

|---|---|

| `prompt` | `string` Required. The user prompt to send to the session. |



\### Response body



If successful, the response body is empty.

