# I aM D bee
## IMDb scraping app for movies, tv shows, tv mini-series..
- Gets the movie`s IMDb link from clipboard
- Copies the details to the target excel sheet: movie title, year of release, director(s), star(s), genre(s), date of the day, length of the movie
- Automatically opens the `target excel sheet`, once the data is saved
- If checked in: opens the movie poster in a new browser tab - the poster image is not "right-click copyable" from the movie`s front page by default
- If checked in: searches for the movie in another database in a new browser tab - for the non-english user`s native language movie title
- If the path added: automatically opens your `movie database excel sheet`

<br>

<div align="center">
    <img src="docs/promo/default.png"</img> 
</div>

<br>

<div align="center">
    <img src="docs/promo/darth.png"</img> 
</div>

# Requirements
## Python and Mondules
### 1. Python 3
https://www.python.org/

### 2. Selenium
https://pypi.org/project/selenium/

### 3. Openpyxl
https://pypi.org/project/openpyxl/

## Others
### 4. Google Chrome
https://www.google.co.uk/chrome/

### 5. Selenium WebDriver
https://sites.google.com/chromium.org/driver/

### 6. Excel
Any excel app installed on your system (`MS Excel`, `LibreOffice Calc`..)

### 7. Target Excel Sheet
- Recommended: `docs\ Movies_New_Record.xlsx`
- You will be able relocate and add the new location of the sheet via UI
- If you are using your own sheet:
- + It should not contain pictures (`openpyxl` module removes the pictures from the sheet)
- + No merged cells for the Directors, Stars values (where we can write more data in one column)

# Guide
## Options
in progress

# Tips and Tricks
## Save settings
in progress

## How to use less information/columns from the target sheet
- No code:
```
https://support.microsoft.com/en-us/office/copy-visible-cells-only-6e3a1f01-2884-4332-b262-8b814412847e
```
- Code: or you can amend the `functions / excel_sheet.py` file

## Alternative start
in progress

## How to add your own "Look for native title" option
Just add your key-value pair in `settings_db.json / title_search_links` and it will be automatically listed at the next start.

<div align="center">
    <img src="docs/guide/title_search_link.png"</img> 
</div>


## How to create your own skin
in progress
