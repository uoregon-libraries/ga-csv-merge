# Google Analytics Merge
Script to merge Drupal content export and Google analytics exports

## Requirements
- Install a version of [Python > 3](https://www.python.org/downloads/).
- Open terminal in working dir and `pip install -r requirements.txt`
- Google Analytics spreadsheet has a column called `Page` which contains the relative path URL
- Drupal Export spreadsheet has a column called `Path` which contains the aliased relative path URl
- Drupal Export spreadsheet has a column called `Path - NID` which contains the relative path URL in `/node/<nid>` format
- No columns in either spreadsheet end with `_x` or `_y`

## Usage
- Copy Google Analytics spreadsheet as a csv into working dir, rename to `ga.csv`
  - `ga.csv` must have the `Page` column
  - All other columns are optional and will merge into the final csv
- Copy Drupal export as a csv into working dir, rename to `nodes.csv`
  - `nodes.csv` must have the `Path` and `Path - NID` columns
  - All other columns are optional and will merge into the final csv
- Run `main.py`, Output will be in `out.csv`