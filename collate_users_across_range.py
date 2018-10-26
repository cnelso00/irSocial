import os
import logs_to_dicts as ld
import User


def get_conversations_site19():
    site19_logs_path = '/Users/connornelson/Desktop/Logs/irc.synirc.net.old/Channels/#site19/'
    site19_conversations = os.listdir(site19_logs_path)
    site19_conversations.sort()
    site19_conversations.remove('.DS_Store')
    for i in range (0, len(site19_conversations)):
        site19_conversations[i] = site19_logs_path + site19_conversations[i]
    return site19_conversations


# this could potentially use a hashmap of username for faster searching?
# map<username, user_data> ?
# too much data to be recursive
# but this is a monstrosity


def get_users_list_from_all_conversations(conversations):
    all_user_instances = list()
    for conversation in conversations:
        user_instances_from_conversation = ld.grab_users_userdata(conversation)
        for user_list in all_user_instances:
            for new_user_instance in user_instances_from_conversation:
                if new_user_instance.username in user_list:
                    for old_user_instance in user_list:
                        if new_user_instance.username is old_user_instance.username:
                            old_user_instance.message_log.append(new_user_instance.message_log)
                            user_instances_from_conversation.remove(new_user_instance)

                else:
                    all_user_instances.append(new_user_instance)
    return all_user_instances



convo_list = get_conversations_site19()
instances = get_users_list_from_all_conversations(convo_list)
size = len(instances)


def list_active_users(instances):
    active_username_list = list()
    for user_instance in instances:
        active_username_list.append(user_instance.get_username())

    return active_username_list

# iterate through user's message log, check for usernames, append to username mentions
# probably faster to do this when initially getting user logs


def list_username_mentions(user, usernames_list):
    for message in user.message_log:
        for username in usernames_list:
            if username in message:
                if username not in user.username_mentions:
                    user.username_mentions[username] = 1
                else:
                    user.username_mentions[username] += user.username_mentions[username]

def calculate_unmodified_social_weights(deep_users_list):
    for user in deep_users_list:
        for username, mention_count in user.username_mentions.items():
            username_and_mentions = dict()
            username_and_mentions['username'] = username
            username_and_mentions['mentions'] = mention_count
            #username_and_mentions['mentioned'] = deep_users_list.find 


def weighting_function(x, y):
    return x + y




