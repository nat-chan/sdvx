import youtube_dl
import sys
url = sys.argv[1]

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([url])
