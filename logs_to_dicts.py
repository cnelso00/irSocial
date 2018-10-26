import sys
import os
import unittest
import dateutil.parser
import User



# TODO unit tests
# TODO recursive file reader -- Done?
# TODO Semantic Analysis neural net
# TODO social network mapping / close friends mapping
# TODO Stylometric Analysis
# TODO send user text to SMMRY
# TODO parsers for other irc clients

path = '/Users/connornelson/Desktop/Logs/irc.synirc.net.old/Channels/#site19/'

dir_list = os.listdir(path)



#class testDT_FROM_TIMESTAMP(unittest.TestCase):
#    def test(self):
#        self.assertIs(self, dt())


def dt_from_timestamp(timestamp):
    #Date format: YYYY-MM-DDTHH:MM:SS-0500

    message_dt = dateutil.parser.isoparse(timestamp)
    return message_dt
    #dates_and_times = timestamp.split('T')
    #date_list = dates_and_times[0].split('-')
    #time_list = dates_and_times[1].split(':')
    #time_list[2], offset = time_list[2].split('-')[0], time_list[2].split('-')[1]
    #year, month, day, = int(date_list[0]), int(date_list[1]), int(date_list[2])
    #hour, minute, second = int(time_list[0]), int(time_list[1]), int(time_list[2])
    #offset = int(offset)
    #offset = offset / 100
    #offset = tdelta(hours=offset)
    #timezone = dt.tzinfo(offset=-offset)
    #message_dt = dt.datetime(year, month, day, hour=hour, minute=minute, second=second, tzinfo = timezone)
    #return message_dt


def line_to_dict_values(irc_string):
    irc_string_list = irc_string.split(' ', 2)
    time_stamp = irc_string_list[0]
    time_stamp = time_stamp.split('[')[1].split(']')[0]
    username = strip_operator_chars(irc_string_list[1])
    message = strip_trailing_newline(irc_string_list[2])
    return {'username': username, 'timestamp': time_stamp, 'message': message}

def strip_trailing_newline(message):
    message = message[0:-1]
    return message

def strip_operator_chars(username):
    op_chars = ['@','~','%']
    if any(op_char in username for op_char in op_chars):
        username = username[1:]
    return username

def grab_users_userdata(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        usernames = list()
        for line in lines:
            if select_valid_messages(line):
                is_in_list = False
                user_dict = line_to_dict_values(line)
                username = user_dict['username']
                time_stamp = user_dict['timestamp']
                message = user_dict['message']
                #some timestamps don't have time, only date -- filename is the isodate however.
                if 'T' not in time_stamp:
                    convo_date = filename.split('/')[-1]
                    convo_date = convo_date.split('.')[0]
                    time_stamp = convo_date + 'T' + time_stamp
                for i in range(0, len(usernames)):
                    if username == usernames[i].username:
                        usernames[i].add_message(timestamp=time_stamp, message_text=message)
                        is_in_list = True

                if not is_in_list:
                    newUser = User(user=username)
                    newUser.add_message(timestamp=time_stamp, message_text=message)
                    usernames.append(newUser)

        return usernames

def select_valid_messages(message):
    if 'Mode is' in message:
        return False
    if 'Disconnected' in message:
        return False
    if "End Session" in message:
        return False
    if "Begin Session" in message:
        return False
    if len(message) is 0:
        return False
    if "Topic is" in message:
        return False
    if "joined the channel" in message:
        return False
    if "Set by" in message:
        return False
    if "left IRC" in message:
        return False
    check_for_empty_message = message.split(' ', 1)[1]
    if check_for_empty_message == ' \n':
        return False
    if check_for_empty_message == '\n':
        return False
    return True









