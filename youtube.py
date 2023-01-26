from pytube import YouTube

youtube_link = ''
youtube_video = YouTube(youtube_link)

print(youtube_video.title)

for stream in youtube_video.streams.filter(only_audio=True):
    print(stream)

streams = youtube_video.streams.filter(only_audio=True)
print(streams)

stream = streams.first()
print(stream)

audio_file=''
# download audio
stream.download(filename=audio_file)

