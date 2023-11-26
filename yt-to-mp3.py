from pytube import YouTube
import os
youtube_url_base = "https://www.youtube.com/watch?v=d403nALfQrE"
yt = YouTube(youtube_url_base,use_oauth = True, allow_oauth_cache=True)
audio = yt.streams.filter(only_audio = True).first()
destination = "./mp3"
out_file = audio.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = "./mp3/joe-biden" + '.mp3'
os.rename(out_file, new_file)
