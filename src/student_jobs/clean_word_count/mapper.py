from src.core.job.mapper import Mapper
from src.student_jobs.common.utils.get_words import get_words


class CleanWordCountMapper(Mapper):
    def map(self, record, emit):
        for word in get_words(record):
            emit(word, 1)
