class TDDExample():

    def __init__(self):
        pass

    def reverse_string(self, input_str: str) -> str:
        return input_str[::-1]

    def find_longest_word(self, sentence: str) -> str:
        words = sentence.split()
        return max(words, key=len)

    def reverse_list(self, input_list: list) -> list:
        return input_list[::-1]

    def count_digits(
        self,
        input_list: list,
        number_to_be_counted: int
    ) -> int:
        return input_list.count(number_to_be_counted)