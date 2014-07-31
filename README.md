breadplan
=========

`Breadplan` generates baking plans based on the recipes in Chad Robertson's [Tartine Bread](http://www.tartinebread.com).

I wrote this script primarily for my own personal use, but if any of my fellow bakers want to use or modify it, be my guest!

~ Hawk

Installation/Contents
---------------------

The script is `breadplan.py`. There are a couple dependencies (`docopt` and `tabulate`), which you can install using `pip install -r requirements.txt`. `Breadplan Science.ipynb` contains the IPython notebook I used to do a little stats to get average density values for assorted flours.


Usage
-----

#### Commands

+ `breadplan.py basic` generates a recipe for Basic Country Bread
+ `breadplan.py baguette` generates a recipe for baguettes
+ `breadplan.py rye` generates a recipe for rye bread
+ `breadplan.py wholewheat` generates a recipe for whole-wheat bread

Note that only Basic Country Bread is currently implemented; I'm working on the other recipes, though.

#### Options

+ `--hydration=PERCENT` or `-y=PERCENT` allows you to specify your own hydration percentage
+ `--loaves=LOAVES` or `-l=LOAVES` allows you to generate a recipe for a specified number of loaves (default is 2)
+ `--sugar` or `-s` adds brown sugar for the crust (Chad Robertson doesn't use this, but I prefer it)
