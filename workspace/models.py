from abc import ABC, abstractmethod
from typing import List, Tuple

from summarizer.sbert import SBertSummarizer
from transformers import pipeline


class TextForSummarizationNotProvided(Exception):
    pass


class SummaryModel(ABC):
    """raises error if provided file does not exist or provided file and full_text are empty"""
    def __init__(self, filepath: str = None, full_text: str = None):
        if not full_text:
            self.full_text = self.__open_file(filepath)
        else:
            self.full_text = full_text
        if not self.full_text:
            raise TextForSummarizationNotProvided

    @staticmethod
    def __open_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            return infile.read()

    def get_summarization(self) -> Tuple[str, float]:
        summarization = self._summarize()
        return summarization, round(len(summarization)/len(self.full_text) * 100, 2)

    @abstractmethod
    def _summarize(self) -> str:
        pass

    def _split_text_into_sequences_smaller_then_chars(self, max_length=1024) -> List[str]:
        sequences = self.__split_text_into_seq()

        chunks = []
        chunk = ''
        for seq in sequences:
            if len(chunk) > max_length:
                chunks.append(chunk)
                chunk = ''
            chunk = chunk + ' ' + seq

        return chunks

    def __split_text_into_seq(self) -> List[str]:
        split_text = '.'
        sequences = self.full_text.split(split_text)
        return [seq + split_text for seq in sequences if seq]


class HuggingfaceSummaryModel(SummaryModel, ABC):
    @property
    @abstractmethod
    def _model(self):
        pass

    def _summarize(self) -> str:
        summarizer = pipeline('summarization', model=self._model)
        chunks = self._split_text_into_sequences_smaller_then_chars()
        result = list()
        for chunk in chunks:
            summ = summarizer(chunk)
            result.append(summ[0]['summary_text'])
        summarize_text = ' '.join(result)
        return summarize_text


class BartSummaryModel(HuggingfaceSummaryModel):
    _model = 'philschmid/bart-large-cnn-samsum'


class FacebookSummaryModel(HuggingfaceSummaryModel):
    _model = 'facebook/bart-large-cnn'


class SbertBasedSummaryModel(SummaryModel):
    def _summarize(self) -> str:
        model = SBertSummarizer('paraphrase-MiniLM-L6-v2', random_state=1)
        summarize_text = model(self.full_text)
        return summarize_text
