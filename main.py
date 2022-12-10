from functions import messages
from functions import scraping
from functions import excel_sheet
from functions import hun_title

messages.message('bee_noise', 2, 'banner')

scraping.get_link()

titleRead, yearRead, directors, stars, lengthHour, lengthMinute = scraping.web_driver()

excel_sheet.write_sheet(titleRead, yearRead, directors, stars, lengthHour, lengthMinute)

hun_title.search(titleRead, yearRead)

messages.message('bee_noise', 1.5, 'outro')