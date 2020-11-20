'''
Adapter Demo  (via implement)
适配器案例
'''

from __future__ import annotations
from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, file_name):
        pass

class AdvanceMediaPlayer(ABC):
    @abstractmethod
    def playVLC(self, file_name):
        pass
    @abstractmethod
    def playMP4(self, file_name):
        pass

class VLCMediaPlayer(AdvanceMediaPlayer):
    def playVLC(self, file_name):
        print('I can play some VLC file:', file_name)
    def playMP4(self, file_name):
        pass

class MP4MediaPlayer(AdvanceMediaPlayer):
    def playVLC(self, file_name):
        pass
    def playMP4(self, file_name):
        print('I can play some MP4 file:', file_name)


class MediaAdapter (MediaPlayer):
    def __init__(self, audio_type):
        self.mediaPlayer = MP4MediaPlayer()  if audio_type == 'mp4' else VLCMediaPlayer()
    def play(self, file_name):
        audio_type = file_name[file_name.find('.')+1:]
        if audio_type == 'mp4':
            self.mediaPlayer.playMP4(file_name)
        elif audio_type == 'vlc':
            self.mediaPlayer.playVLC(file_name)


class AudioPlayer(MediaPlayer):

    def play(self, file_name):
        audio_type = file_name[file_name.find('.')+1:]
        if audio_type == 'mp3':
            print('I can play some audio file:', file_name)
        elif audio_type == 'mp4' or audio_type == 'vlc':
            adapter = MediaAdapter(audio_type)
            adapter.play(file_name)
        else :
            print('Not Supported:', file_name)

if __name__ == '__main__':
    audioPlayer = AudioPlayer()
    audioPlayer.play("beyond the horizon.mp3")
    audioPlayer.play("alone.mp4")
    audioPlayer.play("far far away.vlc")
    audioPlayer.play("mind me.avi")