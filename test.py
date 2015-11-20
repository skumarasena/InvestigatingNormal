from pydub import AudioSegment

song = AudioSegment.from_mp3("always.mp3")

ten_seconds = 10 * 1000

first = song[:ten_seconds]

first.export("tensec.mp3", format="mp3")