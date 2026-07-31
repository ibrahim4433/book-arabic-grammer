\# Jules API



\## Introduction





The Jules API lets you programmatically access Jules's capabilities to automate and enhance your software development lifecycle.

You can use the API to create custom workflows, automate tasks like bug fixing and code reviews, and embed Jules's intelligence directly into the tools you use every day, such as Slack, Linear, and GitHub.



> \[!NOTE]

>

> \*\*Note:\*\* The Jules API is in an alpha release, which means it is experimental.

> Be aware that we may change specifications, API keys, and definitions as we work toward stabilization.

> In the future, we plan to maintain at least one stable and one experimental version.



\## Authentication



To get started with the Jules API, you'll need an API key.



\### Generate Your API Key



In the Jules web app, go to the \*\*\[Settings](https://jules.google.com/settings#api)\*\* page to create a new API key. You can have at most 3 API keys at a time.

!\[Jules API Key creation interface](https://developers.google.com/static/jules/assets/jules-api-key-settings.png)



\### Use Your API Key



To authenticate your requests, pass the API key in the `X-Goog-Api-Key` header of your API calls.



> \[!WARNING]

> \*\*Important:\*\* Keep your API keys secure. Don't share them or embed them in public code. For your protection, any API keys found to be publicly exposed will be \[automatically disabled](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable-exposed-keys) to prevent abuse.



\## API concepts



The Jules API is built around a few core resources. Understanding these will help you use the API effectively.



\*\*Source\*\*

:   An input source for the agent (e.g., a GitHub repository). Before using a source using the API, you must first \[install the Jules GitHub app](https://jules.google/docs) through the Jules web app.



\*\*Session\*\*

:   A continuous unit of work within a specific context, similar to a chat session. A session is initiated with a prompt and a source.



\*\*Activity\*\*

:   A single unit of work within a Session. A Session contains multiple activities from both the user and the agent, such as generating a plan, sending a message, or updating progress.



\## Quickstart: Your first API call



We'll walk through creating your first session with the Jules API using curl.



\### Step 1: List your available sources



First, you need to find the name of the source you want to work with (e.g., your GitHub repo). This command will return a list of all sources you have connected to Jules.



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sources' \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY'



The response will look something like this:



&#x20;   {

&#x20;     "sources": \[

&#x20;       {

&#x20;         "name": "sources/github/bobalover/boba",

&#x20;         "id": "github/bobalover/boba",

&#x20;         "githubRepo": {

&#x20;           "owner": "bobalover",

&#x20;           "repo": "boba"

&#x20;         }

&#x20;       }

&#x20;     ],

&#x20;     "nextPageToken": "github/bobalover/boba-web"

&#x20;   }



\### Step 2: Create a new session



Now, create a new session. You'll need the source name from the previous step. This request tells Jules to create a boba app in the specified repository.



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sessions' \\

&#x20;       -X POST \\

&#x20;       -H "Content-Type: application/json" \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY' \\

&#x20;       -d '{

&#x20;         "prompt": "Create a boba app!",

&#x20;         "sourceContext": {

&#x20;           "source": "sources/github/bobalover/boba",

&#x20;           "githubRepoContext": {

&#x20;             "startingBranch": "main"

&#x20;           }

&#x20;         },

&#x20;         "automationMode": "AUTO\_CREATE\_PR",

&#x20;         "title": "Boba App"

&#x20;       }'



The `automationMode` field is optional. By default, no PR will be automatically created.



The immediate response will look something like this:



&#x20;   {

&#x20;           "name": "sessions/31415926535897932384",

&#x20;           "id": "31415926535897932384",

&#x20;           "title": "Boba App",

&#x20;           "sourceContext": {

&#x20;             "source": "sources/github/bobalover/boba",

&#x20;             "githubRepoContext": {

&#x20;               "startingBranch": "main"

&#x20;             }

&#x20;           },

&#x20;           "prompt": "Create a boba app!"

&#x20;         }



You can poll the latest session information using GetSession or ListSessions. For example, if a PR was automatically created, you can see the PR in the session output.



&#x20;   {

&#x20;     "name": "sessions/31415926535897932384",

&#x20;     "id": "31415926535897932384",

&#x20;     "title": "Boba App",

&#x20;     "sourceContext": {

&#x20;       "source": "sources/github/bobalover/boba",

&#x20;       "githubRepoContext": {

&#x20;         "startingBranch": "main"

&#x20;       }

&#x20;     },

&#x20;     "prompt": "Create a boba app!",

&#x20;     "outputs": \[

&#x20;       {

&#x20;         "pullRequest": {

&#x20;           "url": "https://github.com/bobalover/boba/pull/35",

&#x20;           "title": "Create a boba app",

&#x20;           "description": "This change adds the initial implementation of a boba app."

&#x20;         }

&#x20;       }

&#x20;     ]

&#x20;   }

&#x20;       

By default, sessions created through the API will have their plans automatically approved. If you want to create a session that requires explicit plan approval, set the `requirePlanApproval` field to `true`.



\### Step 3: Listing sessions



You can list your sessions as follows.



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sessions?pageSize=5' \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY'



\### Step 4: Approve plan



If your session requires explicit plan approval, you can approve the latest plan as follows:



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sessions/SESSION\_ID:approvePlan' \\

&#x20;       -X POST \\

&#x20;       -H "Content-Type: application/json" \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY'



\### Step 5: Activities and interacting with the agent



To list activities in a session:



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sessions/SESSION\_ID/activities?pageSize=30' \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY'



To send a message to the agent:



&#x20;   curl 'https://jules.googleapis.com/v1alpha/sessions/SESSION\_ID:sendMessage' \\

&#x20;       -X POST \\

&#x20;       -H "Content-Type: application/json" \\

&#x20;       -H 'X-Goog-Api-Key: YOUR\_API\_KEY' \\

&#x20;       -d '{

&#x20;         "prompt": "Can you make the app corgi themed?"

&#x20;       }'



The response will be empty because the agent will send its response in the next activity. To see the agent's response, list the activities again.



Here is an example of a ListActivities response.



&#x20;   {

&#x20;     "activities": \[

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/02200cce44f746308651037e4a18caed",

&#x20;         "createTime": "2025-10-03T05:43:42.801654Z",

&#x20;         "originator": "agent",

&#x20;         "planGenerated": {

&#x20;           "plan": {

&#x20;             "id": "5103d604240042cd9f59a4cb2355643a",

&#x20;             "steps": \[

&#x20;               {

&#x20;                 "id": "705a61fc8ec24a98abc9296a3956fb6b",

&#x20;                 "title": "Setup the environment. I will install the dependencies to run the app."

&#x20;               },

&#x20;               {

&#x20;                 "id": "bb5276efad354794a4527e9ad7c0cd42",

&#x20;                 "title": "Modify `src/App.js`. I will replace the existing React boilerplate with a simple Boba-themed component. This will include a title and a list of boba options.",

&#x20;                 "index": 1

&#x20;               },

&#x20;               {

&#x20;                 "id": "377c9a1c91764dc794a618a06772e3d8",

&#x20;                 "title": "Modify `src/App.css`. I will update the CSS to provide a fresh, modern look for the Boba app.",

&#x20;                 "index": 2

&#x20;               },

&#x20;               {

&#x20;                 "id": "335802b585b449aeabb855c722cd9c40",

&#x20;                 "title": "Frontend Verification. I will use the `frontend\_verification\_instructions` tool to get instructions on how to write a Playwright script to verify the frontend application and generate a screenshot of the changes.",

&#x20;                 "index": 3

&#x20;               },

&#x20;               {

&#x20;                 "id": "3e4cc97c7b2448668d1ac75b8c7b7d69",

&#x20;                 "title": "Submit the changes. Once the app is looking good and verified, I will submit my work.",

&#x20;                 "index": 4

&#x20;               }

&#x20;             ]

&#x20;           }

&#x20;         },

&#x20;         "id": "02200cce44f746308651037e4a18caed"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/2918fac8bc54450a9cbda423b7688413",

&#x20;         "createTime": "2025-10-03T05:43:44.954030Z",

&#x20;         "originator": "user",

&#x20;         "planApproved": {

&#x20;           "planId": "5103d604240042cd9f59a4cb2355643a"

&#x20;         },

&#x20;         "id": "2918fac8bc54450a9cbda423b7688413"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/5b3acd1b3ca2439f9cbaefaccf7f709a",

&#x20;         "createTime": "2025-10-03T05:44:16.700231Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "Ran bash command",

&#x20;           "description": "Command: \\nnpm install\\nOutput: added 1326 packages, and audited 1327 packages in 25s\\n\\n268 packages are looking for fundingExit Code: 0"

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "bashOutput": {

&#x20;               "command": "\\nnpm install",

&#x20;               "output": "added 1326 packages, and audited 1327 packages in 25s\\n\\n268 packages are looking for funding"

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "5b3acd1b3ca2439f9cbaefaccf7f709a"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/1ad545d812614a5b84c23a33f6120063",

&#x20;         "createTime": "2025-10-03T05:44:19.502115Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "I have installed the dependencies using `npm install`."

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "changeSet": {

&#x20;               "source": "sources/github/bobalover/boba",

&#x20;               "gitPatch": {

&#x20;                 "baseCommitId": "36ead0a4caefc451b9652ed926a15af9570f4f35"

&#x20;               }

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "1ad545d812614a5b84c23a33f6120063"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/3a2b46329f894ebea1faf6b8fb956428",

&#x20;         "createTime": "2025-10-03T05:44:29.265425Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "I have replaced the boilerplate in `src/App.js` with a Boba-themed component."

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "changeSet": {

&#x20;               "source": "sources/github/bobalover/boba",

&#x20;               "gitPatch": {

&#x20;                 "unidiffPatch": "",

&#x20;                 "baseCommitId": "36ead0a4caefc451b9652ed926a15af9570f4f35"

&#x20;               }

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "3a2b46329f894ebea1faf6b8fb956428"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/4e8dd66f15e247e3ae5e48eeff89ef47",

&#x20;         "createTime": "2025-10-03T05:44:37.721013Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "I have updated the CSS in `src/App.css` to give the app a fresh, modern look."

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "changeSet": {

&#x20;               "source": "sources/github/bobalover/boba",

&#x20;               "gitPatch": {

&#x20;                 "unidiffPatch": ""

&#x20;               }

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "4e8dd66f15e247e3ae5e48eeff89ef47"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/100901155a4141d3b37e8e8d2950f3b7",

&#x20;         "createTime": "2025-10-03T05:44:51.048996Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "Ran bash command",

&#x20;           "description": "Command: \\nOutput: Command failed due to an internal error.\\nExit Code: 1"

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "bashOutput": {

&#x20;               "output": "Command failed due to an internal error.",

&#x20;               "exitCode": 1

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "100901155a4141d3b37e8e8d2950f3b7"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/a76b35353eda42d09b1c37aedaa56047",

&#x20;         "createTime": "2025-10-03T05:47:49.628363Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "Frontend verification",

&#x20;           "description": "Agent provided UI verification."

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "media": {

&#x20;               "data": "",

&#x20;               "mimeType": "image/png"

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "a76b35353eda42d09b1c37aedaa56047"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/db089c7052024cbeb9e37b8c584bc964",

&#x20;         "createTime": "2025-10-03T05:47:53.669642Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "I have successfully verified the frontend changes by building the app, runnin...",

&#x20;           "description": "I have successfully verified the frontend changes by building the app, running a Playwright script, and inspecting the resulting screenshot."

&#x20;         },

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "changeSet": {

&#x20;               "source": "sources/github/bobalover/boba",

&#x20;               "gitPatch": {

&#x20;                 "unidiffPatch": "",

&#x20;                 "baseCommitId": "36ead0a4caefc451b9652ed926a15af9570f4f35"

&#x20;               }

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "db089c7052024cbeb9e37b8c584bc964"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/890e16e30dbb4bf99a92613bdccec212",

&#x20;         "createTime": "2025-10-03T05:48:14.434427Z",

&#x20;         "originator": "agent",

&#x20;         "progressUpdated": {

&#x20;           "title": "Code reviewed",

&#x20;           "description": "The user wants to create a \\"boba app\\". This is a very open-ended request, but the agent's implementation suggests the goal is to create a simple, static web page about boba."

&#x20;         },

&#x20;         "id": "890e16e30dbb4bf99a92613bdccec212"

&#x20;       },

&#x20;       {

&#x20;         "name": "sessions/14550388554331055113/activities/022837dbc0e940eabcc1bc53608e15fc",

&#x20;         "createTime": "2025-10-03T05:48:35.523200Z",

&#x20;         "originator": "agent",

&#x20;         "sessionCompleted": {},

&#x20;         "artifacts": \[

&#x20;           {

&#x20;             "changeSet": {

&#x20;               "source": "sources/github/bobalover/boba",

&#x20;               "gitPatch": {

&#x20;                 "unidiffPatch": "",

&#x20;                 "baseCommitId": "36ead0a4caefc451b9652ed926a15af9570f4f35",

&#x20;                 "suggestedCommitMessage": "feat: Create simple Boba App\\n\\nThis commit transforms the default Create React App boilerplate into a simple, visually appealing Boba-themed application."

&#x20;               }

&#x20;             }

&#x20;           }

&#x20;         ],

&#x20;         "id": "022837dbc0e940eabcc1bc53608e15fc"

&#x20;       }

&#x20;     ]

&#x20;   }



\## Full API reference



View the full \[API reference](https://developers.google.com/jules/api/reference/rest) documentation for the Jules API.



\*\*\* \*\* \* \*\* \*\*\*

