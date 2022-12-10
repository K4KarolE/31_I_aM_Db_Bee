
import webbrowser
# from functions import scraping

def search(titleRead, yearRead):
    # titleRead, yearRead, directors, stars, lengthHour, lengthMinute = scraping.web_driver()
    link = 'https://www.mafab.hu/search/&search='+ ' '.join([titleRead, yearRead])
    webbrowser.open(link)
