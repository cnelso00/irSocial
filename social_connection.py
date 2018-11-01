
class SocialConnection:
    def __init__(self, user, mentions, mentioned_by):
        self.User = user
        self.mentions = mentions
        self.mentioned_by = mentioned_by

    @staticmethod
    def weighting_function(x, y):
        return x + y

    @property
    def weight(self):
        return self.weighting_function(self.mentions, self.mentioned_by)

