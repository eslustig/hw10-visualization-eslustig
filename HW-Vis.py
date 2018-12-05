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
conn = sqlite3.connect('tweets.sqlite')
my_cur = conn.cursor()

def getDayDict(cur):
	week_dict = {}
	data = cur.execute('SELECT time_posted FROM Tweets')
	for line in data:
		date = line[0]
		split_date = date.split()
		day = split_date[0]
		if day not in week_dict:
			week_dict[day] = 1
		else:
			week_dict[day] += 1
	return week_dict


## [Part 2]
# Finish writing the function drawBarChart which takes the dictionary and draws a bar 
# chart with the days of the week on the x axis and the number of tweets on the named day on 
# the y axis.  The chart must have an x label, y label, and title.  Save the chart to 
# "bar.png" and submit it on canvas.  
#
# dayDict - a dictionary with the days of the week and the number of tweets per day
def drawBarChart(dayDict):
	x = dayDict.keys()
	y = dayDict.values()
	plt.bar(x,y)
	plt.xlabel("Days of The Week")
	plt.ylabel("Number of Tweets")
	plt.title("Tweets Per Given Day of the Week")
	plt.show()

#drawBarChart(a1)





## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection 
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.  
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the 
# expected value.  Also call drawBarChart in test_getDayDict. 
class TestHW10(unittest.TestCase):
	conn = sqlite3.connect('tweets.sqlite')
	cur = conn.cursor()

	def test_getDayDict(self):
		self.test = getDayDict(self.cur)
		self.assertEqual(3, len(self.test))
		self.assertEqual(77, self.test['Tue'])
		self.assertEqual(69, self.test['Mon'])
		self.assertEqual(90, self.test['Wed'])
		drawBarChart(self.test)





# run the main method
if __name__ == "__main__":
    unittest.main(verbosity=2)
