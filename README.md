# Code explorer

A quickly-put-together tool to do a preliminary exploration 
of directories full of code.
Displays the code content of each directory as a tree map.
Standing on the shoulders of giants 
like [cloc](https://github.com/AlDanial/cloc),
[pandas](https://pandas.pydata.org/)
and [plotly's treemaps](https://plotly.com/python/treemaps/).

## Dependencies
- cloc
- poetry to manage the python installation (pandas and plotly)

## Installation 
After clone
```bash
cd code-explorer
poetry install
```
And then 
```bash
./explore-driver.sh /path/to/the/repo/to/analyse
```
Plotly should open a browser tab showing a treemap that you can explore.
An html file ending in `...cloc.db.html` should be created 
in the current directory.

## Considerations
- poetry might be overkill
- it would be nice to click on a file on the treemap and open it,
  but alas this requires effort
