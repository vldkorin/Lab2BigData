from src.core.job.mapper import Mapper
from src.student_jobs.common.constants.vowels import VOWELS
from src.student_jobs.common.utils.get_words import get_words


class LetterRatioMapper(Mapper):
    def map(self, record, emit):
        for word in get_words(record):
            vowel_count = sum(character in VOWELS for character in word)
            consonant_count = len(word) - vowel_count
            emit(len(word), (vowel_count, consonant_count))
