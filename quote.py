#quote.py

import csv
import random

###########################################
# Quote format saved in csv as Name,Quote #
###########################################

def get_quote(person):
	with open('quote.csv', newline='') as quotecsv:
		quotereader = csv.reader(quotecsv, delimiter=',')
		quotes = [i[1] for i in quotereader if i[0] == person]
		quote = random.choice(quotes)
		quote_formatted = '"{}" - **{}** '.format(quote, person)
		quotecsv.close()
		return(quote_formatted)

def get_random_name():
	with open('quote.csv', newline='') as quotecsv:
		quotereader = csv.reader(quotecsv, delimiter=',')
		names = [i[0] for i in quotereader]
		random_name = random.choice(names)
		quotecsv.close()
		return(random_name)
