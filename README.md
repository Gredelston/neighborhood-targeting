# Setup

This setup assumes that you already have a working installation of Python.

You will need to install the libraries `shapefile` and `shapely`. Both are available via pip:

```
> python -m pip install shapefile
> python -m pip install shapely
```

# Usage

Run the script from the command line, passing in two arguments: latitude and longitude. (No comma, please!)
If neither argument is passed, it defaults to Fuji Cafénear the Pearl Street Mall.
If the point is found to lie within any neighborhoods, then it will print metadata about the neighborhood (name, city, state, county, Region ID).

```
> python main.py 40.018423 -105.279782
Neighborhood found: Whittier, City of Boulder, CO — Boulder County (Region ID 416094)
```

# Features to build out
Right now the script is configured to only search within the state of Colorado. It would be nice to search other states, too.
Neighborhood shapefiles can be found on Zillow: https://www.zillow.com/howto/api/neighborhood-boundaries.htm
