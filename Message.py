import nltk

class Message:
    def __init__(self, message, timestamp):
        self.timestap = timestamp
        self.message = message
        self.keywords = self.find_keywords()

    @staticmethod
    def is_not_common_word(self, word):
        common_words = {
            "the": False,
            "be": False,
            "to": False,
            "of": False,
            "and": False,
            "a": False,
            "in": False,
            "that": False,
            "have": False,
            "I": False,
            "it": False,
            "for": False,
            "not": False,
            "on": False,
            "with": False,
            "he": False,
            "as": False,
            "you": False,
            "do": False,
            "at": False
        }

        return common_words.get(word, True)

    # # going to use nltk freq dist instead and see how that works
    @staticmethod
    def find_keywords(self):
        keywords = dict()
        for word in self.message:
            if self.is_not_common_word(word):
                if word not in keywords:
                    dict[word] = 1
                else:
                    dict[word] += 1
        return keywords
                



