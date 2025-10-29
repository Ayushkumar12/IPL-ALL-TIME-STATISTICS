# IPL All Time Statistics

## Overview
This project provides a menu-driven Python application for exploring historical Indian Premier League (IPL) batting statistics. It loads data from `ipl.csv`, exposes quick access to descriptive statistics, and offers built-in visualizations and analytics to highlight standout player performances.

## Dataset
- **Source file**: `ipl.csv`
- **Columns**: `player`, `matches`, `inns`, `runs`, `highest score`, `average`, `strike rate`, `n100`, `n50`, `4s`, `6s`
- **Indexing**: Players are used as the DataFrame index to simplify lookups by name.

## Requirements
- **Python**: 3.8 or newer
- **Packages**:
  - `pandas`
  - `matplotlib`

Install dependencies with:
```bash
pip install pandas matplotlib
```

## Getting Started
1. Ensure `ipl.csv` and `main.py` remain in the same directory.
2. Open a terminal in the project root.
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to navigate the menus.

## Main Menu Options
1. **Fetch Data**: Prints the full DataFrame for all tracked players.
2. **Dataframe Statistics**: Opens a submenu with shape, dimension, data types, and other DataFrame metadata.
3. **Display Records**: Offers head/tail views, custom record counts, single-player lookups, and full listings.
4. **Search Specific Row/Column**: Lets you query by player name or by column heading.
5. **Data Visualization**: Provides interactive charts rendered with Matplotlib.
6. **Data Analytics**: Highlights players leading specific statistical categories.
7. **Exit**: Returns to the previous menu or closes the application.

## Visualization Menu
- **Line Plot**: Matches played by each player.
- **Histogram**: Run distribution across players.
- **Horizontal Bar Plot**: Strike rate comparison.
- **Vertical Bar Plot**: Side-by-side count of fours and sixes.

Charts open in separate Matplotlib windows; close each window to return to the menu.

## Analytics Menu
- Maximum and minimum matches played
- Maximum and minimum innings
- Maximum centuries (`n100`)
- Maximum half-centuries (`n50`)

Each selection prints both the statistic value and the players who achieved it.

## Tips
- Player names must match the casing used in `ipl.csv` when performing lookups.
- If Matplotlib windows do not appear, verify that your Python environment supports GUI backends (e.g., install `tkinter` on some systems).
- Update `ipl.csv` with new player rows to extend the analysis; keep the same column structure.
