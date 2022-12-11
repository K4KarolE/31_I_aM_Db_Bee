#!/bin python3.11

import webbrowser

def search(titleRead, yearRead):
    link = 'https://www.mafab.hu/search/&search='+ ' '.join([titleRead, yearRead])
    webbrowser.open(link)
