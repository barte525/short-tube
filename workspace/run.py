import yt_dlp as youtube_dl

from models import (BartSummaryModel, FacebookSummaryModel,
                    SbertBasedSummaryModel)
from text_extractor import TextExtractor
from videos_transcript_handler import clear_videos_transcript

if __name__ == "__main__":
    while True:
        url = input('\nProvide url to yt video: ')
        try:
            filepath = TextExtractor(url).extract_text_to_file()
            print(filepath)
            break
        except youtube_dl.utils.DownloadError:
            print('\nIncorrect url.\n')
    model_id_to_model = {
        '1': BartSummaryModel,
        '2': FacebookSummaryModel,
        '3': SbertBasedSummaryModel
    }
    while True:
        input_key = input('Choose a summarization model:\n1: Bart CNN\n2: Facebook CNN\n3: Sbert\n'
                          '4: Clear downloaded transcripts\n 5: Exit\n')
        if input_key in model_id_to_model:
            summary, compression = model_id_to_model[input_key](filepath).get_summarization()
            print(f'\n Summary:\n {summary}\n\n Summary is {compression}% of original text')
        elif input_key == '4':
            clear_videos_transcript()
        elif input_key == '5':
            break
        else:
            print('\nProvide number from 1 to 5.\n')
