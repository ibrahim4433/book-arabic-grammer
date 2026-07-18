from pytubefix import YouTube

try:
    yt = YouTube("https://www.youtube.com/watch?v=CCs4ID1pu-I", client="WEB")
    ys = yt.streams.get_audio_only()
    ys.download(filename="test_audio.mp3")
    print("SUCCESS")
except Exception as e:
    print("FAILED", e)
