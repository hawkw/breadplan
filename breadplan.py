#!/usr/bin/env python3.4
doc = """BreadPlan

Usage:
    breadplan.py basic [-sh] [-y=PERCENT] [-l=LOAVES]
    breadplan.py baguette [-sh] [-y=PERCENT] [-l=LOAVES]
    breadplan.py rye [-sh] [-y=PERCENT] [-l=LOAVES]
    breadplan.py wholewheat [-sh] [-y=PERCENT] [-l=LOAVES]

Options:
    -y PERCENT --hydration=PERCENT  Specifies the hydration percentage [default: 75]
    -l LOAVES --loaves LOAVES       Specifies the number of loaves you'd like to bake [default: 2]
    -h --help                       Displays this help message.
    -s --sugar                      Whether or not to add sugar for the crust.
"""

from docopt import docopt
from tabulate import tabulate

WATER           = 240 # Assume water has a density of 1 gram
SALT            = 273
TBSP_PER_CUP    = 16

# See http://nbviewer.ipython.org/github/hawkw/breadplan/blob/master/Breadplan%20Science.ipynb
# for the math behind these density values.
BREAD_FLOUR          = 127.33333333333333
ALL_PURPOSE          = 125.0
WHOLE_WHEAT          = 122.0
RYE                  = 103.66666666666667
FIFTY_FIFTY          = (BREAD_FLOUR + WHOLE_WHEAT)/2

water_grams_to_cup = lambda grams: round(grams / WATER, 1)
flour_grams_to_cup = lambda grams, flour: round(grams/flour, 1)
leaven_grams_to_cup = lambda grams: round(
                                            (
                                                ((grams/2) / FIFTY_FIFTY) + ((grams/2) / WATER)
                                            )/2,
                                            1
                                        )
salt_grams_to_tbsp = lambda grams: round(
                                            (grams / SALT) / TBSP_PER_CUP,
                                            1
                                        )

def basic_country(loaves = 2, hydration = 75, sugar=True):
    table = [
                ["Water (80F)", "{} cups".format(water_grams_to_cup(375*loaves)), "{:.0F}%".format(hydration)],
                [ "Leaven", "{} cups".format(leaven_grams_to_cup(100*loaves)),"20%" ],
                [ "White Flour","{} cups".format(flour_grams_to_cup(450*loaves,BREAD_FLOUR)),"90%" ],
                [ "Whole Wheat Flour","{} cups".format(flour_grams_to_cup(50*loaves,WHOLE_WHEAT)),"10%" ],
                [ "Salt", "{} Tbsp".format(salt_grams_to_tbsp(loaves * 10)),"2%" ]
            ]

    if sugar:
        table.append(["Sugar", "{} Tbsp".format(.5*loaves)])

    print ("Recipe for {l:.0F} loaves of Basic Country Bread:\n".format(l = loaves))
    print (tabulate(table, headers = ["Ingredient", "Quantity", "%"]))

def whole_wheat(loaves = 2, hydration = 80, sugar=True):
    table = [
                ["Water (80F)", "{} cups".format(water_grams_to_cup(400*loaves)), "{:.0F}%".format(hydration)],
                [ "Leaven", "{} cups".format(leaven_grams_to_cup(100*loaves)),"20%" ],
                [ "Whole Wheat Flour","{} cups".format(flour_grams_to_cup(450*loaves,WHOLE_WHEAT)),"70%" ],
                [ "All Purpose Flour","{} cups".format(flour_grams_to_cup(50*loaves,ALL_PURPOSE)),"30%" ],
                [ "Salt", "{} Tbsp".format(salt_grams_to_tbsp(loaves * 10)),"2%" ]
            ]

    if sugar:
        table.append(["Sugar", "{} Tbsp".format(.5*loaves)])

    print ("Recipe for {l:.0F} loaves of Whole Wheat Bread:\n".format(l = loaves))
    print (tabulate(table, headers = ["Ingredient", "Quantity", "%"]))


if __name__ == "__main__":
    opts = docopt(doc, help=True, version="0.1")
    if opts["basic"]:
        basic_country(float(opts["--loaves"]), float(opts["--hydration"]), opts["--sugar"])
    elif opts["wholewheat"]:
       whole_wheat(float(opts["--loaves"]), float(opts["--hydration"]), opts["--sugar"])
    else:
        print ("Sorry, breads other than the Basic Country Bread are not currently supported")