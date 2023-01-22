import json

def open_settings():
    f = open(r"d:\_DEV\Python\31_I_aM_D_bee\settings_db.json")
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open('settings_db.json', 'w') as f:
        json.dump(settings_data, f, indent=2)
    return

