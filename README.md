# I aM D bee
## IMDb scraping app for movies, tv shows, tv mini-series..
- Gets the movie`s IMDb link from clipboard
- Copies the details to the target excel sheet: movie title, year of release, director, stars, genres, date of the day, length of the movie
- Automatically opens the target excel sheet, once the data is saved
$~$

- If checked in: Opens the movie poster in a new browser tab - note: the poster image is not "right-click copyable" from the movie`s IMDb front page by default
- If checked in: Looks for the user`s native language movie title (if checked)
- If checked in: Automatically opens your movie database excel sheet (if the path added)
$~$

<div align="center">
    <img src="https://raw.githubusercontent.com/K4KarolE/31_I_aM_D_bee/main/docs/promo/default.png" width="502px"</img> 
</div>

<br>

<div align="center">
    <img src="https://raw.githubusercontent.com/K4KarolE/31_I_aM_D_bee/main/docs/promo/darth.png" width="502px"</img> 
</div>

# Requirements
## Python and Mondules
### 1. Python 3
- https://www.python.org/

### 2. Selenium
- https://pypi.org/project/selenium/

### 3. Openpyxl
- https://pypi.org/project/openpyxl/

## Others
### 4. Google Chrome
- https://www.google.co.uk/chrome/

### 5. Selenium WebDriver
- you will be able to add the location of the chromedriver.exe via UI once you start the program
- https://sites.google.com/chromium.org/driver/

### 6. Excel sheet
- Movies_New_Record Excel sheet, attached in the docs folder
- you will be able to add the location of the sheet via UI once you start the program
- any excel app installed on your system (MS Excel, LibreOffice Calc..)
- if you are using your own sheet:
- + it should not contain pictures (openpyxl module removes the pictures from the sheet)
- + with no merged cells for the Directors, Stars values (where we can write more data in one column)
