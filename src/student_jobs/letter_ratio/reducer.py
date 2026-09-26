from src.core.job.reducer import Reducer


class LetterRatioReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = 0
        total_consonants = 0

        for vowel_count, consonant_count in values:
            total_vowels += vowel_count
            total_consonants += consonant_count

        total_letters = total_vowels + total_consonants
        if total_letters == 0:
            return

        vowel_percentage = total_vowels / total_letters * 100
        consonant_percentage = total_consonants / total_letters * 100
        result = (
            f"{vowel_percentage:.2f}% голосних, "
            f"{consonant_percentage:.2f}% приголосних"
        )
        emit(key, result)
