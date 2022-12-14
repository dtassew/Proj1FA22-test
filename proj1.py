# -*- coding: utf-8 -*-



# Your name:
# Your student id:
# Your email:
# List who you have worked with on this project:

import io
import sys
import csv
import unittest

def read_csv(file):
    '''
    Reads in the csv, removes the header (first row) and
    stores the data in the following nested dictionary format:
    {'region': {'race/ethnicity': count...}...}

    Parameters
    ----------
    file: string
        the file to read

    Returns
    -------
    data: dict
        a nested dictionary
    '''
    data = {}

def get_percent(data):
    '''
    Calculates the percentage of each demographic using this
    formula: (demographic / total people) * 100

    Parameters
    ----------
    data: dict
        Either SAT or Census data

    Returns
    -------
    pcts: dict
        the dictionary that represents the data in terms of percentage share
        for each demographic for each region in the data set
    '''
    pcts = {}

def get_difference(sat_data, census_data):
    '''
    Takes the absolute value, rounded to 2 deicmal places,
    of the difference between each demographic's percentage
    value in census_data from sat_data

    Parameters
    ----------
    sat_data: dict
        SAT data
    census_data: dict
        Census data

    Returns
    -------
    pct_dif: dict
        the dictionary of the percent differences
    '''
    pct_dif = {}

def csv_out(data, file_name):
    '''
    Writes the data to csv, adding the header as
    the first row

    Parameters
    ----------
    data: dict
        dictionary with percent differences

    file_name: str
        the name of the file to write

    Returns
    -------
        None. (Doesn't return anything)
    '''
    pass

def max_min_mutate(data, col_list):
    # Do not change the code in this function
    '''
    Mutates the data to simplify the implementation of
    `max_min` by moving the race/ethnicity key to the outside
    of the nested dictionary and the region key to the inside
    nested dictionary like so:
    {'race/ethnicity': {'region': pct, 'region': pct, ...}...}

    Parameters
    ----------
    data : dict
        dictionary of data passed in. In this case, it's the
    col_list : list
        list of columns to mutate to.

    Returns
    -------
    demo_vals: dict
    '''
    # Do not change the code in this function
    demo_vals = {}
    for demo in col_list:
        demo_vals.setdefault(demo, {})
        for region in data:
            demo_vals[demo].setdefault(region, data[region][demo])
    return demo_vals

def max_min(data):
    '''
    Finds the max and min regions and vals for each demographic,
    filling a dictionary in the following format:
    {"max": {"demographic": {"region": value}, ...},
     "min": {"demographic": {"region": value}, ...}...}

    Parameters
    ----------
    data: dict
        the result of max_min_mutate

    Returns
    -------
    max_min: dict
        a triple nested dictionary
    '''
    max_min = {}

def nat_percent(data, col_list):
    '''
    EXTRA CREDIT
    Uses either SAT or Census data dictionaries
    to sum demographic values, calculating
    national demographic percentages from regional
    demographic percentages

    Parameters
    ----------
    data: dict
        Either SAT or Census data
    col_list: list
        list of the columns to loop through. helps filter out region totals columns

    Returns
    -------
    data_totals: dict
        dictionary of the national demographic percentages

    '''
    data_total = {}

def nat_difference(sat_data, census_data):
    '''
    EXTRA CREDIT
    Calculates the difference between SAT and Census
    data on a national scale

    Parameters
    ----------
    sat_data: dict
        national SAT data
    census_data: dict
        national Census data

    Returns
    nat_diff: dict
        the dictionary consisting of the demographic
        difference on national level
    '''
    nat_diff = {}

def main():
    # read in the data

    # compute demographic percentages

    # compute the difference between test taker and state demographics

    # output the csv

    # create a list from the keys of inner dict

    # mutate the data using the provided 'min_max_mutate' function

    # calculate the max and mins using `min_max`

    # extra credit here

    pass

main()

# create at minimum four test cases in this class
class HWTest(unittest.TestCase):

    def setUp(self):
        # surpressing output on unit testing
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        # setting up the data we'll need here
        # basically, redoing all the stuff we did in the main function
        self.sat_data = read_csv("sat_data.csv")
        self.census_data = read_csv("census_data.csv")

        self.sat_pct = get_percent(self.sat_data)
        self.census_pct = get_percent(self.census_data)

        self.pct_dif_dict = get_difference(self.sat_pct, self.census_pct)

        self.col_list = list(self.pct_dif_dict["midwest"].keys())

        self.mutated = max_min_mutate(self.pct_dif_dict, self.col_list)

        self.max_min_val = max_min(self.mutated)

        # extra credit
        # providing a list of col vals to cycle through
        self.col_list = self.census_data["midwest"].keys()

        # computing the national percentages
        self.sat_nat_pct = nat_percent(self.sat_data, self.col_list)
        self.census_nat_pct = nat_percent(self.census_data, self.col_list)

        self.dif = nat_difference(self.sat_nat_pct, self.census_nat_pct)

    '''
    Create test functions for the functions you wrote here!
    '''

    # testing the nat_pct extra credit function
    def test_nat_percent(self):
       self.assertEqual(
       nat_percent({"region":{"demo":5,"Region Totals":10}},["demo", "Region Totals"]),
       {"demo":50.0, "Region Totals":10})

    # second test for the nat_pct extra credit function
    def test2_nat_percent(self):
        self.assertEqual(
            self.sat_nat_pct["AMERICAN INDIAN/ALASKA NATIVE"],
            0.73)

    # testing the nat_dif extra credit function
    def test_nat_difference(self):
        self.assertEqual(
            nat_difference({"demo":0.53, "Region Totals": 1},{"demo":0.5, "Region Totals": 1}),
            {"demo":0.03}
            )

    # second test for the nat_diff extra credit function
    def test2_nat_difference(self):
        self.assertEqual(
            self.dif["ASIAN"],
            3.32)

if __name__ == '__main__':
    unittest.main(verbosity=2)