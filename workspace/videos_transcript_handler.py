from pathlib import Path


STORAGE_DIRECTORY_NAME = 'videos_transcript'


def clear_videos_transcript():
    for path in Path(STORAGE_DIRECTORY_NAME).glob('*'):
        path.unlink()
