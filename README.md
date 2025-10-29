# IPL All Time Statistics - Complete Documentation with Output Screens

## Overview
This project provides a menu-driven Python application for exploring historical Indian Premier League (IPL) batting statistics. It loads data from `ipl.csv`, exposes quick access to descriptive statistics, and offers built-in visualizations and analytics to highlight standout player performances.

---

## Dataset
- **Source file**: `ipl.csv`
- **Columns**: `player`, `matches`, `inns`, `runs`, `highest score`, `average`, `strike rate`, `n100`, `n50`, `4s`, `6s`
- **Indexing**: Players are used as the DataFrame index to simplify lookups by name.

---

## Requirements
- **Python**: 3.7 or newer
- **Packages**:
  - `pandas`
  - `matplotlib`

Install dependencies with:
```bash
pip install pandas matplotlib
```

---

## Getting Started
1. Ensure `ipl.csv` and `main.py` are in the same directory.
2. Open a terminal in the project root.
3. Run the application:
   ```bash
   python main.py
   ```
4. Follow the on-screen prompts to navigate the menus.

---

# Output Screens & Examples

## 1. Main Menu

When you run the program, you'll see:

```
Main Menu
1. Fetch Data
2. Dataframe Statistics
3. Display Records
4. Search specific row/column
5. Data Visualization
6. Data Analytics
7. Exit
Enter your choice: 
```

**Description**: The main menu is the entry point of the application. Users can navigate to different modules by entering the corresponding number.

---

## 2. Fetch Data (Option 1)

**Input**:
```
Enter your choice: 1
```

**Output**:
```
DISPLAYING ALL TIME IPL STATISTICS DATA
========================================
                matches  inns  runs  highest score  average  strike rate  n100  n50   4s   6s
player                                                                                         
V Kohli             192   182  5878            113    37.97       130.41     5   38  480  201
RG Sharma           195   187  5230            109    31.31       130.61     1   36  422  213
SK Raina            193   186  5368            100    33.34       137.00     1   37  506  194
DA Warner           142   140  5254            126    41.59       142.39     4   42  522  195
AB de Villiers      154   151  4849            133    40.40       151.68     3   33  343  235
MS Dhoni            204   183  4632             84    40.99       136.75     0   23  299  209
RV Uthappa          189   184  4607             87    27.51       130.47     0   27  387  207
S Dhawan            176   171  5197            106    34.84       126.64     2   41  569  148

Do you want to continue? (y/n):
```

**Description**: Displays the complete IPL statistics dataset with all players and their batting statistics.

---

## 3. Dataframe Statistics (Option 2)

**Submenu**:
```
Dataframe Statistics Menu
1. Display all column names
2. Display the indexes
3. Display the shape
4. Display the dimension
5. Display the data types of all columns
6. Display the size
7. Exit
Enter choice:
```

### 3.1 Display Column Names

**Input**: `1`

**Output**:
```
Index(['matches', 'inns', 'runs', 'highest score', 'average', 'strike rate', 
       'n100', 'n50', '4s', '6s'], dtype='object')
```

### 3.2 Display Indexes (Player Names)

**Input**: `2`

**Output**:
```
Index(['V Kohli', 'RG Sharma', 'SK Raina', 'DA Warner', 'AB de Villiers',
       'MS Dhoni', 'RV Uthappa', 'S Dhawan'], dtype='object', name='player')
```

### 3.3 Display Shape

**Input**: `3`

**Output**:
```
(8, 10)
```

**Meaning**: 8 rows (players) and 10 columns (statistics)

### 3.4 Display Dimension

**Input**: `4`

**Output**:
```
2
```

**Meaning**: The DataFrame is 2-dimensional (rows and columns)

### 3.5 Display Data Types

**Input**: `5`

**Output**:
```
matches          int64
inns             int64
runs             int64
highest score    int64
average         float64
strike rate     float64
n100             int64
n50              int64
4s               int64
6s               int64
dtype: object
```

### 3.6 Display Size

**Input**: `6`

**Output**:
```
80
```

**Meaning**: Total number of elements (8 players × 10 statistics = 80)

---

## 4. Display Records (Option 3)

**Submenu**:
```
Display Records Menu
1. Top 5 Records
2. Bottom 5 Records
3. Specific number of records from the top
4. Specific number of records from the bottom
5. Details of a specific Player
6. Display details of all Players
7. Exit
Enter choice:
```

### 4.1 Top 5 Records

**Input**: `1`

**Output**:
```
                matches  inns  runs  highest score  average  strike rate  n100  n50   4s   6s
player                                                                                         
V Kohli             192   182  5878            113    37.97       130.41     5   38  480  201
RG Sharma           195   187  5230            109    31.31       130.61     1   36  422  213
SK Raina            193   186  5368            100    33.34       137.00     1   37  506  194
DA Warner           142   140  5254            126    41.59       142.39     4   42  522  195
AB de Villiers      154   151  4849            133    40.40       151.68     3   33  343  235
```

### 4.2 Bottom 5 Records

**Input**: `2`

**Output**:
```
                matches  inns  runs  highest score  average  strike rate  n100  n50   4s   6s
player                                                                                         
DA Warner           142   140  5254            126    41.59       142.39     4   42  522  195
AB de Villiers      154   151  4849            133    40.40       151.68     3   33  343  235
MS Dhoni            204   183  4632             84    40.99       136.75     0   23  299  209
RV Uthappa          189   184  4607             87    27.51       130.47     0   27  387  207
S Dhawan            176   171  5197            106    34.84       126.64     2   41  569  148
```

### 4.3 Specific Number from Top

**Input**: 
```
Enter choice: 3
Enter how many records you want to display from the top: 3
```

**Output**:
```
                matches  inns  runs  highest score  average  strike rate  n100  n50   4s   6s
player                                                                                         
V Kohli             192   182  5878            113    37.97       130.41     5   38  480  201
RG Sharma           195   187  5230            109    31.31       130.61     1   36  422  213
SK Raina            193   186  5368            100    33.34       137.00     1   37  506  194
```

### 4.4 Specific Number from Bottom

**Input**: 
```
Enter choice: 4
Enter how many records you want to display from the bottom: 2
```

**Output**:
```
             matches  inns  runs  highest score  average  strike rate  n100  n50   4s   6s
player                                                                                      
RV Uthappa       189   184  4607             87    27.51       130.47     0   27  387  207
S Dhawan         176   171  5197            106    34.84       126.64     2   41  569  148
```

### 4.5 Details of Specific Player

**Input**: 
```
Enter choice: 5
Enter the player name for which you want to see the details: V Kohli
```

**Output**:
```
matches            192.00
inns               182.00
runs              5878.00
highest score      113.00
average             37.97
strike rate        130.41
n100                 5.00
n50                 38.00
4s                 480.00
6s                 201.00
Name: V Kohli, dtype: float64
```

---

## 5. Search Specific Row/Column (Option 4)

**Submenu**:
```
Search Menu
1. Search for the details of a specific player
2. Search details of a specific as per a specific column heading
3. Exit
Enter choice:
```

### 5.1 Search by Player Name

**Input**: 
```
Enter choice: 1
Enter the name of the player whose details you want to see: MS Dhoni
```

**Output**:
```
matches            204.00
inns               183.00
runs              4632.00
highest score       84.00
average             40.99
strike rate        136.75
n100                 0.00
n50                 23.00
4s                 299.00
6s                 209.00
Name: MS Dhoni, dtype: float64
```

### 5.2 Search by Column Heading

**Input**: 
```
Enter choice: 2
Enter column/heading name whose details you want to see: strike rate
```

**Output**:
```
player
V Kohli           130.41
RG Sharma         130.61
SK Raina          137.00
DA Warner         142.39
AB de Villiers    151.68
MS Dhoni          136.75
RV Uthappa        130.47
S Dhawan          126.64
Name: strike rate, dtype: float64
```

**Another Example - Searching for 6s**:

**Input**: 
```
Enter column/heading name whose details you want to see: 6s
```

**Output**:
```
player
V Kohli           201
RG Sharma         213
SK Raina          194
DA Warner         195
AB de Villiers    235
MS Dhoni          209
RV Uthappa        207
S Dhawan          148
Name: 6s, dtype: int64
```

---

## 6. Data Visualization (Option 5)

**Submenu**:
```
Data Visualization Menu
1. Line Plot --> No. of matches played by each player
2. Histogram --> No. of runs scored by players
3. Horizontal Bar Plot --> Strike rate of each player
4. Vertical bar plot --> No. of 4s and 6s of each player
5. Exit
Enter choice:
```

### 6.1 Line Plot - Matches Played

**Input**: `1`

**Output**: Opens a Matplotlib window displaying:
- **Title**: "No. of matches played by each player"
- **X-axis**: PLAYERS (rotated 90°)
- **Y-axis**: NO. OF MATCHES
- **Graph Type**: Line plot connecting all players
- **Shows**: MS Dhoni with highest matches (204), DA Warner with lowest (142)

### 6.2 Histogram - Runs Distribution

**Input**: `2`

**Output**: Opens a Matplotlib window displaying:
- **Title**: "No. of runs scored by players"
- **X-axis**: RUNS
- **Y-axis**: FREQUENCY
- **Graph Type**: Histogram with 5 bins, red color, black edges
- **Shows**: Distribution of runs across different ranges

### 6.3 Horizontal Bar Plot - Strike Rates

**Input**: `3`

**Output**: Opens a Matplotlib window displaying:
- **Title**: "STRIKE RATE OF EACH PLAYER"
- **X-axis**: STRIKE RATES
- **Y-axis**: PLAYERS
- **Graph Type**: Horizontal bar chart with colorful bars
- **Colors**: Blue, Cyan, Green, Black, Magenta, Red, Blue, Yellow
- **Shows**: AB de Villiers with highest strike rate (151.68)

### 6.4 Vertical Bar Plot - 4s and 6s Comparison

**Input**: `4`

**Output**: Opens a Matplotlib window displaying:
- **Title**: "No. of 4s and 6s of each player"
- **X-axis**: PLAYERS (rotated 90°)
- **Y-axis**: NO. OF 4s AND 6s
- **Graph Type**: Grouped vertical bar chart
- **Legend**: Shows "No. of 4s" and "No. of 6s"
- **Shows**: Side-by-side comparison for each player

---

## 7. Data Analytics (Option 6)

**Submenu**:
```
Data Analytics Menu
1. Player with maximum number of matches played
2. Player with minimum number of matches played
3. Player with maximum number of inns
4. Player with minimum number of inns
5. Player with maximum number of centuries
6. Player with maximum number of half-centuries
7. Exit
Enter choice:
```

### 7.1 Maximum Matches Played

**Input**: `1`

**Output**:
```
Player with maximum number of matches played: 204
Player(s): ['MS Dhoni']
```

### 7.2 Minimum Matches Played

**Input**: `2`

**Output**:
```
Player with minimum number of matches played: 142
Player(s): ['DA Warner']
```

### 7.3 Maximum Innings

**Input**: `3`

**Output**:
```
Player with maximum number of inns: 187
Player(s): ['RG Sharma']
```

### 7.4 Minimum Innings

**Input**: `4`

**Output**:
```
Player with minimum number of inns: 140
Player(s): ['DA Warner']
```

### 7.5 Maximum Centuries

**Input**: `5`

**Output**:
```
Player with maximum number of centuries: 5
Player(s): ['V Kohli']
```

**Insight**: Virat Kohli leads with 5 centuries in IPL history

### 7.6 Maximum Half-Centuries

**Input**: `6`

**Output**:
```
Player with maximum number of half-centuries: 42
Player(s): ['DA Warner']
```

**Insight**: David Warner has scored the most fifties (42)

---

## 8. Exit Program

**Input from Main Menu**: `7`

**Output**:
```
Do you want to continue? (y/n): n

Thank you for using IPL Statistics Application!
```

---

## Program Flow Example

Here's a complete session example:

```
Main Menu
1. Fetch Data
2. Dataframe Statistics
3. Display Records
4. Search specific row/column
5. Data Visualization
6. Data Analytics
7. Exit
Enter your choice: 3

Display Records Menu
1. Top 5 Records
2. Bottom 5 Records
3. Specific number of records from the top
4. Specific number of records from the bottom
5. Details of a specific Player
6. Display details of all Players
7. Exit
Enter choice: 5
Enter the player name for which you want to see the details: AB de Villiers
matches            154.00
inns               151.00
runs              4849.00
highest score      133.00
average             40.40
strike rate        151.68
n100                 3.00
n50                 33.00
4s                 343.00
6s                 235.00
Name: AB de Villiers, dtype: float64

Display Records Menu
1. Top 5 Records
2. Bottom 5 Records
3. Specific number of records from the top
4. Specific number of records from the bottom
5. Details of a specific Player
6. Display details of all Players
7. Exit
Enter choice: 7

Do you want to continue? (y/n): y

Main Menu
1. Fetch Data
2. Dataframe Statistics
3. Display Records
4. Search specific row/column
5. Data Visualization
6. Data Analytics
7. Exit
Enter your choice: 6

Data Analytics Menu
1. Player with maximum number of matches played
2. Player with minimum number of matches played
3. Player with maximum number of inns
4. Player with minimum number of inns
5. Player with maximum number of centuries
6. Player with maximum number of half-centuries
7. Exit
Enter choice: 5
Player with maximum number of centuries: 5
Player(s): ['V Kohli']

Data Analytics Menu
1. Player with maximum number of matches played
2. Player with minimum number of matches played
3. Player with maximum number of inns
4. Player with minimum number of inns
5. Player with maximum number of centuries
6. Player with maximum number of half-centuries
7. Exit
Enter choice: 7

Do you want to continue? (y/n): n

Thank you for using IPL Statistics Application!
```

---

## Tips for Using the Application

1. **Player Names**: Must match exact casing from CSV (e.g., "V Kohli" not "v kohli")
2. **Column Names**: Must match exact column heading (e.g., "strike rate" not "Strike Rate")
3. **Navigation**: Use the Exit option (usually 7) to return to previous menus
4. **Visualizations**: Close chart windows to return to menu
5. **Continue**: Choose 'y' to keep exploring, 'n' to exit

---

## Key Statistics Summary

From the sample dataset:

| Statistic | Player | Value |
|-----------|--------|-------|
| Most Matches | MS Dhoni | 204 |
| Most Runs | V Kohli | 5878 |
| Highest Score | AB de Villiers | 133 |
| Best Average | DA Warner | 41.59 |
| Best Strike Rate | AB de Villiers | 151.68 |
| Most Centuries | V Kohli | 5 |
| Most Half-Centuries | DA Warner | 42 |
| Most Fours | S Dhawan | 569 |
| Most Sixes | AB de Villiers | 235 |

---

## Project Information

**Developed By**: Ayush Kumar 
**Date**: 2nd August, 2023
**Language**: Python
**Compiler Version**: Python 3.7.0  
**Libraries Used**: Pandas, Matplotlib