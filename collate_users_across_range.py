import os
import logs_to_dicts as ld
import User
from social_connection import SocialConnection


def get_conversations_site19():
    site19_logs_path = ''
    site19_conversations = os.listdir(site19_logs_path)
    site19_conversations.sort()
    site19_conversations.remove('.DS_Store')
    for i in range (0, len(site19_conversations)):
        site19_conversations[i] = site19_logs_path + site19_conversations[i]
    return site19_conversations


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


def calculate_weights_between_users(deep_users_list):
    for user_a in deep_users_list:
        for user_b in deep_users_list:
            if user_a.social_connections.get(user_b.username) is None and \
                            user_b.social_connections.get(user_a.username) is None:
                mentions_of_b = user_a.keywords.get(user_b.username, 0)
                mentions_of_a = user_b.keywords.get(user_a.username, 0)
                social_connection = SocialConnection(user_a=user_a,
                                                     user_b=user_b,
                                                     mentions_of_a=mentions_of_a,
                                                     mentions_of_b=mentions_of_b)
                user_a.social_connections[user_b.username] = social_connection
                user_b.social_connections[user_a.username] = social_connection


def get_username_mentions(user, user_mentioned):
    return user.username_mentions[user_mentioned]


convo_list = get_conversations_site19()
instances = get_deep_users_list_from_all_conversations(convo_list)
size = len(instances)
get_social_network(instances)
