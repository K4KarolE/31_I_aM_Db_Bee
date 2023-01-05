#!/bin python3.11

import webbrowser

lang_dic = {    # user should be able to select / add / edit his own language search parameters (UI - ?)
            'Hungarian': 'https://www.mafab.hu/search/&search=',
            'Czech': 'https://www.csfd.cz/hledat/?q='
            }

def search(titleRead, yearRead):
    link = lang_dic['Hungarian'] + ' '.join([titleRead, yearRead])
    webbrowser.open(link)
