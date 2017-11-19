# nba

Ridiculously simple script to tell you if your NBA team won. I have league pass to watch my Warriors, but I'm a sore loser and sometimes don't feel like watching losses. However, I don't want to know the score if we DO win, thus leaving the method of destruction a mystery. So, this script will simply tell you "GSW beat POR", regardless of how many 3's from Sunnyvale that Curry hit. This way, I know if we won, but nothing else (sort of like Jon Snow, but if he knew who sits on throne in the end).

### Usage
1. Navigate to `.../nba/`
2. `python did_we_win.py <team> <days_ago>`

### Command line arguments
* **team**: 3 letter team signifier (GSW, DET, etc). Default 'GSW'.
* **days_ago**: calendar days ago the game occurred (EST). Default 1.