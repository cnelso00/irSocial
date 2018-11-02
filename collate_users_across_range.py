import os
import logs_to_dicts as ld
import User
import social_connection as edge


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


def get_deep_users_list_from_all_conversations(conversations):
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


def list_active_users(instances):
    active_username_list = list()
    for user_instance in instances:
        active_username_list.append(user_instance.get_username())

    return active_username_list

# #preparing to turn users into graph


def get_social_network(deep_users_list):
    active_network_edges = dict()
    active_users = list_active_users(deep_users_list)
    for user in deep_users_list:
        for message in user.message_log:
            for username in active_users:
                if username in message:
                    if str(user.username + " " + username) not in active_network_edges:
                        active_network_edges[str(user.username + " " + username)] = user.social_connections.append(edge.SocialConnection(user=username, mentions=1, mentioned_by=0))
                    else:
                        active_network_edges[str(user.username + " " + username)].mentions += 1
    print(active_network_edges)


def list_username_mentions(user, usernames_list):
    for message in user.message_log:
        for username in usernames_list:
            if username in message:
                if username not in user.username_mentions:
                    user.username_mentions[username] = 1
                else:
                    user.username_mentions[username] += user.username_mentions[username]


def calculate_weights_between_users(deep_users_list):
    for user in deep_users_list:
        for username, mention_count in user.username_mentions.items():
            user.social_network.append(edge.SocialConnection(user_instance_from_name(username), mention_count, get_username_mentions(username, user_instance_from_name(user))))


def user_instance_from_name(username, deep_users_list):
        for user in deep_users_list:
            if user.get_username() == username:
                return user
        return None


def get_username_mentions(user, user_mentioned):
    return user.username_mentions[user_mentioned]


convo_list = get_conversations_site19()
instances = get_deep_users_list_from_all_conversations(convo_list)
size = len(instances)
get_social_network(instances)
