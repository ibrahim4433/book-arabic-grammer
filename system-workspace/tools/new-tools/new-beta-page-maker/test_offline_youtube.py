from pathlib import Path
import sys
sys.path.append(str(Path.cwd() / "system-workspace/tools/automation/modules"))
from youtube_offline_transcriber import YouTubeOfflineTranscriber

transcriber = YouTubeOfflineTranscriber(Path.cwd())
success, msg = transcriber.process_video("https://www.youtube.com/watch?v=sWCQMMfP8p8", "Test Video", 999)
print(success, msg)
