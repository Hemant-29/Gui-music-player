#    G:\music/Photograph.mp3

import time
import sounddevice as sd
import librosa
import mutagen


class Play:
    def __init__(self):
        self.start_time = 0
        self.pause_time = 0
        self.elapsed_time = 0
        self.lag_time = 0.15
        self.isPlaying = False
        self.audio_file = 'test files/sound2.mp3'
        self.title = ""
        self.artist = ""
        self.album = ""
        self.duration = 0

    def play_audio(self, audio_file, start_time=0):
        if audio_file is not None:
            self.audio_file = audio_file
        self.audio, self.sample_rate = librosa.load(self.audio_file)
        self.get_metadata(self.audio_file)

        self.start_time = time.time()
        self.isPlaying = True
        sd.play(
            self.audio[int(start_time * self.sample_rate):], self.sample_rate)
        self.isPlaying = True

    def pause_audio(self):
        self.pause_time = time.time()
        self.elapsed_time += (self.pause_time-self.start_time)
        self.elapsed_time -= self.lag_time
        print(self.elapsed_time)
        sd.stop()
        self.isPlaying = False

    def goto(self, time):
        self.elapsed_time = time
        self.play_audio(None, time)

    def resume_audio(self):
        self.play_audio(None, self.elapsed_time)

    def get_metadata(self, file):
        metadata = mutagen.File(file)
        self.title = str(metadata.get('TIT2'))
        self.artist = str(metadata.get('TPE1'))
        self.album = str(metadata.get('TALB'))
        self.duration = librosa.get_duration(path=file)

    def getTime(self):
        return self.elapsed_time


a = Play()
a.get_metadata("G:\music/Photograph.mp3")
