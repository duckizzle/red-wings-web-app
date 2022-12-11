import urllib.request, json 


def get_json(url):
    with urllib.request.urlopen(url) as url:
        data = json.load(url)
    return data


def get_event_names(event_json):
    events = []
    for event in event_json["events"]:
        events.append(event["name"])

    return events

def is_team_on(event_list, team):
    success = False
    for event in event_list:
        if team in event:
           # print("WE ON BABY")
            success = True
        else: 
           # print("Nope")
            success = False
    return success
            

data = get_json("http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard")

events = get_event_names(data)


print(is_team_on(events, 'Detroit'))
# print(events) 

# for event in events:
#     print(event)