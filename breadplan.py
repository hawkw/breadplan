#!/usr/env python3.4
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
    print ("Ingredient\t\tQuantity\tPercentage")
    print ("----------\t\t--------\t----------")
    print_ingredient(
                        "Water (80F)",
                        water_grams_to_cup(375*loaves),
                        hydration,
                        "cups"
                    )
    print_ingredient(
                        "Leaven",
                        leaven_grams_to_cup(100*loaves),
                        20,
                        "cups"
                    )
    print_ingredient(
                        "White Flour",
                        flour_grams_to_cup(450*loaves,BREAD_FLOUR),
                        90,
                        "cups"
                    )
    print_ingredient(
                        "Whole Wheat Flour",
                        flour_grams_to_cup(50*loaves,WHOLE_WHEAT),
                        10,
                        "cups"
                    )
    print_ingredient(
                        "Salt",
                        salt_grams_to_tbsp(10*loaves),
                        2,
                        "Tbsp"
                    )
    if sugar:
            print_ingredient(
                        "Sugar",
                        (.5*loaves),
                        "Tbsp"
                    )

def print_ingredient(name, quantity, percentage,measurement):
    print ("{n}\t\t{q} {m}\t{p}%".format(
            n = name,
            q = quantity,
            p = percentage,
            m = measurement
            )
        )

if __name__ == "__main__":
    opts = docopt(doc, help=True, version="0.1")
    if opts["basic"]:
        basic_country(float(opts["--loaves"]), float(opts["--hydration"]), opts["--sugar"])
    else:
        print ("Sorry, breads other than the Basic Country Bread are not currently supported")