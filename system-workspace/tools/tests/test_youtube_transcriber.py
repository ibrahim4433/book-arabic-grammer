import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.append(str(project_root / "system-workspace/tools/automation"))

from modules.youtube_transcriber import YouTubeTranscriber


class TestYouTubeTranscriber(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.transcriber = YouTubeTranscriber(
            project_root=self.temp_dir.name, api_key="test_api_key_123"
        )
        # Point raw and temp directory to temporary test dirs
        self.transcriber.raw_dir = Path(self.temp_dir.name) / "raw"
        self.transcriber.raw_dir.mkdir(parents=True, exist_ok=True)
        self.transcriber.temp_dir = Path(self.temp_dir.name) / "temp"
        self.transcriber.temp_dir.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_get_mime_type(self):
        self.assertEqual(self.transcriber.get_mime_type("video.m4a"), "audio/mp4")
        self.assertEqual(self.transcriber.get_mime_type("audio.mp3"), "audio/mpeg")
        self.assertEqual(self.transcriber.get_mime_type("file.webm"), "audio/webm")
        self.assertEqual(self.transcriber.get_mime_type("unknown.xyz"), "application/octet-stream")

    def test_get_next_unused_index(self):
        # Empty directory should start at 1
        self.assertEqual(self.transcriber.get_next_unused_index(), 1)

        # Create dummy file
        (self.transcriber.raw_dir / "1y-raw.txt").write_text("content", encoding="utf-8")
        self.assertEqual(self.transcriber.get_next_unused_index(), 2)

        # Create another dummy file
        (self.transcriber.raw_dir / "5y-raw.txt").write_text("content", encoding="utf-8")
        self.assertEqual(self.transcriber.get_next_unused_index(), 6)

    @patch("yt_dlp.YoutubeDL")
    def test_resolve_urls_single(self, mock_ytdl):
        mock_instance = MagicMock()
        mock_instance.extract_info.return_value = {"_type": "video", "title": "Test Single Video"}
        mock_ytdl.return_value.__enter__.return_value = mock_instance

        urls, is_playlist = self.transcriber.resolve_urls("https://www.youtube.com/watch?v=123")
        self.assertFalse(is_playlist)
        self.assertEqual(len(urls), 1)
        self.assertEqual(urls[0], ("https://www.youtube.com/watch?v=123", "Test Single Video"))

    @patch("yt_dlp.YoutubeDL")
    def test_resolve_urls_playlist(self, mock_ytdl):
        mock_instance = MagicMock()
        mock_instance.extract_info.return_value = {
            "_type": "playlist",
            "entries": [
                {"id": "abc", "title": "Lesson 1"},
                {"url": "https://www.youtube.com/watch?v=def", "title": "Lesson 2"},
            ],
        }
        mock_ytdl.return_value.__enter__.return_value = mock_instance

        urls, is_playlist = self.transcriber.resolve_urls(
            "https://www.youtube.com/playlist?list=xyz"
        )
        self.assertTrue(is_playlist)
        self.assertEqual(len(urls), 2)
        self.assertEqual(urls[0], ("https://www.youtube.com/watch?v=abc", "Lesson 1"))
        self.assertEqual(urls[1], ("https://www.youtube.com/watch?v=def", "Lesson 2"))

    @patch("requests.post")
    @patch("requests.get")
    def test_transcription_pipeline(self, mock_get, mock_post):
        # Mock download_audio_stream
        fake_audio = self.transcriber.temp_dir / "test_audio.m4a"
        fake_audio.write_text("fake binary", encoding="utf-8")
        self.transcriber.download_audio_stream = MagicMock(
            return_value=(str(fake_audio), "Mock Title")
        )

        # Mock Upload File response
        mock_post_resp1 = MagicMock()
        mock_post_resp1.json.return_value = {
            "file": {
                "name": "files/mock-file-123",
                "uri": "https://generativelanguage.googleapis.com/v1beta/files/mock-file-123",
            }
        }

        # Mock Transcribe response
        mock_post_resp2 = MagicMock()
        mock_post_resp2.json.return_value = {
            "candidates": [{"content": {"parts": [{"text": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"}]}}]
        }

        mock_post.side_effect = [mock_post_resp1, mock_post_resp2]

        # Mock Poll response
        mock_get_resp = MagicMock()
        mock_get_resp.json.return_value = {"state": "ACTIVE"}
        mock_get.return_value = mock_get_resp

        # Mock Delete response
        self.transcriber.delete_file = MagicMock()

        # Run process_url
        out_path, title = self.transcriber.process_url(
            "https://www.youtube.com/watch?v=123", sequence_n=1
        )

        self.assertEqual(title, "Mock Title")
        self.assertTrue(Path(out_path).exists())
        self.assertEqual(Path(out_path).read_text(encoding="utf-8"), "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ")
        self.assertEqual(Path(out_path).name, "1y-raw.txt")


if __name__ == "__main__":
    unittest.main()
