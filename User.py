import datetime as dt
import logs_to_dicts as ltd
import Message as Message


class User:
    def __init__(self, user):
        self.username = user
        self.message = Message
        self.message_log = list()
        self.social_connections = dict()
        self.keywords = dict()

    def set_message(self, timestamp, message_text):
        new_message = self.message.copy()
        new_message['timestamp'] = ltd.dt_from_timestamp(timestamp)
        new_message['message'] = message_text
        return new_message

    def add_message(self, message):
        self.message_log.append(message)
        keys = message.keys()
        for word in keys:
            if word not in self.keywords:
                self.keywords[word] = 1
            else:
                self.keywords[word] += message[word]


    def get_user(self):
        return_string  = "Username = " + self.username + "\n"
        len_messages = len(self.message_log)
        return_string = return_string + "Number of messages: " + str(len_messages) + "\n"
        #for item in self.message_log:
        #    return_string = return_string + str(item['timestamp']) + " : " + item['message']

        return return_string




