from src.core.job.mapper import Mapper
from src.student_jobs.common.utils.get_words import get_words


class LongWordCountMapper(Mapper):
    def map(self, record, emit):
        for word in get_words(record):
            if len(word) > 5:
                emit(word, 1)
