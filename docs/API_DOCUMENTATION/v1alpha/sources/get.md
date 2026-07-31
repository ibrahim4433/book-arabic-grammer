\# Method: sources.get



\- \[HTTP request](https://developers.google.com/jules/api/reference/rest/v1alpha/sources/get#body.HTTP\_TEMPLATE)

\- \[Path parameters](https://developers.google.com/jules/api/reference/rest/v1alpha/sources/get#body.PATH\_PARAMETERS)

\- \[Request body](https://developers.google.com/jules/api/reference/rest/v1alpha/sources/get#body.request\_body)

\- \[Response body](https://developers.google.com/jules/api/reference/rest/v1alpha/sources/get#body.response\_body)



Gets a single source.



\### HTTP request



`GET https://jules.googleapis.com/v1alpha/{name=sources/\*\*}`



The URL uses \[gRPC Transcoding](https://google.aip.dev/127) syntax.



\### Path parameters



| Parameters ||

|---|---|

| `name` | `string` Required. The resource name of the source to retrieve. Format: sources/{source} It takes the form `sources/{+source}`. |



\### Request body



The request body must be empty.



\### Response body



If successful, the response body contains an instance of `https://developers.google.com/jules/api/reference/rest/v1alpha/sources#Source`.

