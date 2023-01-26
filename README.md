# I aM D bee
## IMDb scraping app for movies, tv shows, tv mini-series..
- Gets the movie`s IMDb link from clipboard
- Copies the details to the `target excel sheet`:

<img src="docs/guide/target_sheet.png"> 

- Automatically opens the sheet, once the data is saved
- If opt in: 
    - Opens the movie poster in a new browser tab - the poster image is not "right-click copyable" from the movie`s front page by default
    - Searches for the movie in another database in a new browser tab - for the non-english user`s native language movie title
- If the path added:
    - Automatically opens your `movie database excel sheet`
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
- https://www.python.org/

### 2. Selenium
- https://pypi.org/project/selenium/

### 3. Openpyxl
- https://pypi.org/project/openpyxl/

## Others
### 4. Google Chrome
- https://www.google.co.uk/chrome/

### 5. Selenium WebDriver
- https://sites.google.com/chromium.org/driver/

### 6. Excel
- Any excel app installed on your system (`MS Excel`, `LibreOffice Calc`)

### 7. Target Excel Sheet
- Recommended: `docs\ Movies_New_Record.xlsx`


# Guide
## IMDb link in clipboard - Mandatory
- You are requested to copy the link of the movie (or series, TV show, ..)
- It is more for the first time users
<div align="center">
    <img src="docs/guide/link_in_clipboard.png"</img> 
</div>

## Poster in new tab
- The poster image is not "right-click copyable" from the movie`s front page by default (left)
<div align="center">
    <img src="docs/guide/poster.png"</img> 
</div>

## Look for native title
- Takes the title and the release year of the movie
- Adds it to the end of the selected search link
- Opens it in a new browser tab

## Autorun by next start
- Automatically triggers the scraping engine by the next start of the program using the previously saved settings

## Chrome driver path - Mandatory
- You are able to add the location of the driver via UI

## Target sheet path - Mandatory
- Recommended: `docs\ Movies_New_Record.xlsx`
- You are able relocate and add the new location of the sheet via UI
- If you are using your own sheet:
    - It should NOT contain pictures (`openpyxl` module removes the pictures from the sheet)
    - No merged cells for the `Directors`, `Stars` values (more than one cell can be used in the same column)

## Movies DB sheeth path
- You are able to add the location of `movie database excel sheet`
- Not mandatory, no error message, when the field left empty


# Tips and Tricks
## How to add your own "Look for native title" option
- Just add your key-value pair in `settings_db.json / title_search_links` and it will be automatically listed at the next start.
- Make sure your link is suitable for concatenation

<div align="center">
    <img src="docs/guide/title_search_link.png"</img> 
</div>

## How to set up your own skin
- In the `skins` folder create a new folder with the name of your skin
- Place your version of `BG.png` and `icon.ico` into the folder (BG.png: 500x600)
- In the `settings_db.json \ skins` create a new dictionary with the same name of your folder
- In the `settings_db.json \ skins \ your skin` amend the parameters as you wish
- The new skin will be automatically listed at the next start

<div align="center">
    <img src="docs/guide/own_skin.png"</img> 
</div>

## How to test/save your selected skin without running the scraping engine
- Change the skin there and back, every skin update triggers the `save & update function` for the skin

## Alternative start
- Look around in the the `docs\launcher` folder, if you want to launch the program from your desktop* or from Total Commander`s button section
- Do not forget to change the path and python types according to your system
- * = Windows: you can create a shortcut for the `.bat` file

## How to use less information/columns from the target sheet
- No code:
    - Hide the unwanted columns in the `target excel sheet`
    - Save and close it
    - Run the program
    - [Copy visible cells only](https://support.microsoft.com/en-us/office/copy-visible-cells-only-6e3a1f01-2884-4332-b262-8b814412847e)
- Code: amend the `functions / excel_sheet.py` file