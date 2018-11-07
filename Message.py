import nltk

class Message:
    def __init__(self, message, timestamp):
        self.timestap = timestamp
        self.message = message
        self.keywords = self.find_keywords()

    @staticmethod
    def is_common_word(self, word):
        common_words = {
            "the" : True,
            "be" : True,
            "to" : True,
            "of" : True,
            "and" : True,
            "a" : True,
            "in" : True,
            "that" : True,
            "have" : True,
            "I" : True,
            "it" : True,
            "for" : True,
            "not" : True,
            "on" : True,
            "with" : True,
            "he" : True,
            "as" : True,
            "you" : True,
            "do" : True,
            "at" : True
        }

        return common_words.get(word, False)


    #going to use nltk freq dist instead and see how that works
    @staticmethod
    def find_keywords(self):
        keywords = dict()
        for word in self.message:
            if not self.is_common_word(word):
                



