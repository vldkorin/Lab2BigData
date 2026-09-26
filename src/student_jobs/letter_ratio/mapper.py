from src.core.job.mapper import Mapper
from src.student_jobs.common.constants.vowels import VOWELS
from src.student_jobs.common.utils.clean_word import clean_word


class LetterRatioMapper(Mapper):
    def map(self, record, emit):
        for word in str(record).split():
            cleaned_word = clean_word(word)
            if cleaned_word:
                vowel_count = sum(character in VOWELS for character in cleaned_word)
                consonant_count = len(cleaned_word) - vowel_count
                emit(len(cleaned_word), (vowel_count, consonant_count))
