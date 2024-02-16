#isort
import time
from os.path import exists
from pathlib import Path

import whisper
import yt_dlp as youtube_dl


class TextExtractor:
    """raises youtube_dl.utils.DownloadError if provided incorrect url"""

    SOUND_FILE_EXT = '.mp3'
    STORAGE_DIRECTORY_NAME = 'videos_transcript'

    def __init__(self, yt_url: str):
        self.yt_url = yt_url
        self.video_info = youtube_dl.YoutubeDL().extract_info(url=self.yt_url, download=False)
        self.video_title = self.video_info['title']

    @property
    def video_sound_name(self) -> str:
        return f'{self.video_title}{self.SOUND_FILE_EXT}'

    @property
    def transcript_filepath(self) -> str:
        return f'{self.STORAGE_DIRECTORY_NAME}/{self.video_title}'

    def extract_text_to_file(self) -> str:
        if exists(self.transcript_filepath):
            print('Transcript of this video is already in the system')
            return self.transcript_filepath
        self.__save_video_sound_to_file()
        transcript = self.__fetch_transcript()
        self.__delete_video_sound_file()
        self.__save_transcript_to_file(transcript)
        return self.transcript_filepath

    def __save_video_sound_to_file(self) -> None:
        download_configuration = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': self.video_sound_name,
        }

        with youtube_dl.YoutubeDL(download_configuration) as ydl:
            ydl.download([self.video_info['webpage_url']])

    def __fetch_transcript(self) -> str:
        start = time.time()
        model = whisper.load_model('base')
        result = model.transcribe(self.video_sound_name)

        print('Whisper time: ', time.time() - start)

        return result['text']

    def __delete_video_sound_file(self) -> None:
        p = Path(self.video_sound_name)
        p.unlink()

    def __save_transcript_to_file(self, transcript: str):
        with open(self.transcript_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(transcript)
