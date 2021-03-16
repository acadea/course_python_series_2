import string
import pprint
from chart import chart

class WordCounter:
    def __init__(self, text: str):
        self._text = text

    def _preprocess(self):
        # removing ' from punctuation list
        punctuations = string.punctuation.replace("'", "")

        # clean up punctuations
        # making a table to map all punctuation to none
        # https: // www.programiz.com / python - programming / methods / string / maketrans
        translation_table = str.maketrans("", "", punctuations)

        self._text = self._text.translate(translation_table)

        # clean up contractions
        to_replace = {
            "'s": "",
            "'ll": "",
            "'m": " am",
            "'d": "",
            "n't": " not",
            "'re": " are",
            #  replacing line break
            "\n": " ",
            # replace dash to space
            "-": " ",
            # replacing remaining single quote
            "'": " ",
        }

        for abbv, replacement in to_replace.items():
            # Note: using string replace is slow, we should use regex instead
            self._text = self._text.replace(abbv, replacement)

        # to lower case
        self._text = self._text.lower()

    def analyse(self) -> dict:
        """
        This function returns a dictionary that consist of word count
        :rtype: dict
        """
        self._preprocess()

        # split into iterable
        split = self._text.split(" ")

        # get unique by using set
        unique_words = set(split)

        # remove empty string in set
        unique_words.discard("")

        # loop thru unique and count
        # generate a dict of word against count
        analysed = {word: split.count(word) for word in unique_words}

        # sort by word count
        sorted_words = sorted(analysed.items(), key=lambda item: item[1], reverse=True)

        return {key: count for key, count in sorted_words}


if __name__ == '__main__':
    with open("alice.txt", 'r') as file:
        text = file.read()
        counter = WordCounter(text)
        analysis = counter.analyse()
        chart.plot_word_count(analysis)

