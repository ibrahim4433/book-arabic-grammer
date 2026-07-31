\# Method: sessions.get



\- \[HTTP request](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/get#body.HTTP\_TEMPLATE)

\- \[Path parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/get#body.PATH\_PARAMETERS)

\- \[Request body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/get#body.request\_body)

\- \[Response body](https://developers.google.com/jules/api/reference/rest/v1alpha/sessions/get#body.response\_body)



Gets a single session.



\### HTTP request



`GET https://jules.googleapis.com/v1alpha/{name=sessions/\*}`



The URL uses \[gRPC Transcoding](https://google.aip.dev/127) syntax.



\### Path parameters



| Parameters ||

|---|---|

| `name` | `string` Required. The resource name of the session to retrieve. Format: sessions/{session} It takes the form `sessions/{session}`. |



\### Request body



The request body must be empty.



\### Response body



If successful, the response body contains an instance of `https://developers.google.com/jules/api/reference/rest/v1alpha/sessions#Session`.

