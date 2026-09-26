from src.core.job.mapper import Mapper
from src.student_jobs.common.utils.clean_word import clean_word


class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        for word in str(record).split():
            cleaned_word = clean_word(word)
            if cleaned_word:
                emit(cleaned_word, 1)
