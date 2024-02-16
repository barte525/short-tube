from ddt import data, ddt
from unittest import TestCase

from models import BartSummaryModel, FacebookSummaryModel, SbertBasedSummaryModel


@ddt
class TestSummaryModels(TestCase):
    def setUp(self):
        self.text = 'Some text to summarize. I think it should have like 3 sentences at least. So that is third one.'
        self.text_length = len(self.text)

    @data(BartSummaryModel, FacebookSummaryModel, SbertBasedSummaryModel)
    def test_summary_models(self, model):
        summary_len = len(model(full_text=self.text).get_summarization())
        self.assertNotEqual(summary_len, 0)
        self.assertGreater(self.text_length, summary_len)
