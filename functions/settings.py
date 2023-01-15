import json

def open_settings():
    with open('settings.json') as f:
        settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open('settings.json', 'w') as f:
        json.dump(settings_data, f, indent=2)
    return



settings_data = open_settings()

settings_data['test'] = "1414"

save_settings(settings_data)


'''
Information from the user

checkbox: 4
searchbox: 2
field: 1
rolldown: 1

checkbox     "imdb_link_in_clipboard": true,     mandatory
searchbox    "path_movies_sheet": "",
searchbox    "path_movie_new_record": "",        mandatory
checkbox     "title_search": true,
field        "title_search_link": "",            if "title_search": true - mandatory // roll down menu? greyed out otherwise? - able to add new link?
checkbox     "poster_open_in_new_tab": true,
rolldown     "poster_size": "",                  small by default / medium / larger // greyed out otherwise?
checkbox     "run_by_start": false

button - save current settings - message: will load automatically with next start

'''
