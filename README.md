# Code explorer

A quickly-put-together tool to do a preliminary exploration 
of directories full of code.
Displays the code content of each directory as a tree map.
Standing on the shoulders of giants 
like [cloc](https://github.com/AlDanial/cloc),
[pandas](https://pandas.pydata.org/)
and [plotly's treemaps](https://plotly.com/python/treemaps/).

Exploring the repo of `numpy`:

![A treemap of the numpy repository at the maintenance/1.22.x branch](./numpy-treemap.png)

Picture produced with the command

```bash
$ ./explore-driver-web.sh https://github.com/numpy/numpy maintenance/1.22.x
```

## Dependencies
- cloc
- poetry to manage the python installation (pandas and plotly)

## Installation 
After clone
```bash
cd code-explorer
poetry install
```
## Usage
For local repositories:
```bash
./explore-driver.sh /path/to/the/repo/to/analyse
```
For repositories on the web, one can use 
```bash
./explore-driver-web.sh url-of-repo-to-analyse <branch>
```
Where `<branch>` typically means `master` or `main`.

Plotly should open a browser tab showing a treemap that you can explore.
In the "web" version, the names of files in the treemap will be clickable links
that should point to the file on the web (tested on github).

An html file ending in `...cloc.db.html` should be created 
in the current directory.

## Considerations
- poetry might be overkill
- it would be nice to click on a file on the treemap and open it,
  but alas this requires effort - done for the web version, difficult for the local one.
