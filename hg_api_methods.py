import os
import requests

hg = os.environ['hg']
login = os.environ['login']
password = os.environ['pass']


def clients_list():
    get_clients = requests.get(hg+'clients', auth=(login, password))
    dzejson = get_clients.json()
    nicks_list = []
    for i in dzejson:
        nicks_list.append(i['client_nickname'])
    nick_counter = len(nicks_list)
    return "For now we have {} active users on Hellgate: {}".format(nick_counter,  ', '.join(nicks_list))


def channels_occupancy():
    get_channels = requests.get(os.environ['hg']+'channels', auth=(os.environ['login'], os.environ['pass']))
    dzejson = get_channels.json()
    channels_total = {}
    for i in dzejson:
        if i["channel_name"] == "World of Warcraft" and int(i["total_clients"]) > 0:
            channels_total[(i["channel_name"]).upper()] = i["total_clients"]
        elif int(i["total_clients"]) > 0:
            channels_total[i["channel_name"].lower()] = i["total_clients"]
    return channels_total


print(clients_list())
print(channels_occupancy())
