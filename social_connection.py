
class SocialConnection:
    def __init__(self, user_a, user_b, mentions_of_b, mentions_of_a):
        self.users = (user_a, user_b )
        self.mentions = (mentions_of_b, mentions_of_a)

    @staticmethod
    def weighting_function(x, y):
        return x + y

    @property
    def weight(self):
        return self.weighting_function(self.mentions[0], self.mentions[1])

