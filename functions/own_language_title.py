import webbrowser
from functions import settings

settings_data = settings.open_settings() 

def search(titleRead, yearRead):
    selected_default_link = settings_data['title_search_links'][settings_data['title_search_link_selected']]    # settings_db.json / 'title_search_links' dictionary looking for the 
    link = selected_default_link + ' '.join([titleRead, yearRead])                                              # saved value(link) of the key: Hungarian or Czech..
    webbrowser.open(link)

# search("forrest gump", "0")