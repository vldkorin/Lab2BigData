from src.student_jobs.common.constants.letters import APOSTROPHES, LETTERS


def get_words(record):
    record = str(record).lower()
    for apostrophe in APOSTROPHES:
        record = record.replace(apostrophe, "")

    cleaned_record = "".join(
        character if character in LETTERS else " "
        for character in record
    )
    return cleaned_record.split()
