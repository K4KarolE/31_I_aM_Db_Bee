from functions import messages
from functions import scraping
from functions import excel_sheet
from functions import hun_title

messages.message('bee_noise', 2, 'banner')

titleRead, yearRead, directors, stars, genres, lengthHour, lengthMinute = scraping.web_driver()

excel_sheet.write_sheet(titleRead, yearRead, directors, stars, genres, lengthHour, lengthMinute)

hun_title.search(titleRead, yearRead)

messages.message('bee_noise', 1.5, 'outro')