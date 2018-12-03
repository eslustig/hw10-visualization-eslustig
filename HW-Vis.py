# Import statements
import unittest
import sqlite3
import twitter_info # still need this in the same directory, filled out
import matplotlib.pyplot as plt

## [PART 1]
# Finish writing the function getDayDict which takes a database cursor and returns a 
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue", 
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# cur - the database cursor
def getDayDict(cur):
    pass

## [Part 2]
# Finish writing the function drawBarChart which takes the dictionary and draws a bar 
# chart with the days of the week on the x axis and the number of tweets on the named day on 
# the y axis.  The chart must have an x label, y label, and title.  Save the chart to 
# "bar.png" and submit it on canvas.  
#
# dayDict - a dictionary with the days of the week and the number of tweets per day
def drawBarChart(dayDict):
    pass

## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection 
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.  
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the 
# expected value.  Also call drawBarChart in test_getDayDict. 
class TestHW10(unittest.TestCase):

# run the main method
if __name__ == "__main__":
    unittest.main(verbosity=2)
