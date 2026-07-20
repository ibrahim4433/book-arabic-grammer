### `./system-workspace/tools/automation/modules/jules_youtube_dispatcher.py`
- **Status:** Usable
- **Purpose:** Resolves YouTube playlists or single URLs and dispatches automated tasks (via `JulesClient`) to a Jules AI session. It builds a detailed markdown prompt instructing the agent to download the media locally, transcribe it precisely in Arabic with Tashkeel, save it as a raw `.txt` file, and perform cleanup.
- **Inputs:** `video_url` (YouTube video URL), `video_title` (String), `seq_num` (Integer)
- **Outputs:** Creates a Jules session/PR that will generate a raw text file in `system-workspace/text-data/video-raw/`.
- **Usage:** `python -c "from modules.jules_youtube_dispatcher import JulesYouTubeDispatcher; d = JulesYouTubeDispatcher('.'); d.dispatch_session('https://www.youtube.com/watch?v=...', 'Title', 1)"`
- **Workflow Integration:** This allows outsourcing the heavy transcription work directly to a separate Jules AI agent session. It generates the base raw text material required before the core system can slice it and initiate the '1-Plan-Per-Page' generation engine.
