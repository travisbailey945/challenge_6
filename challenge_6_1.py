#! /usr/bin/env python3
''' challenge 6.1

	Travis Bailey
	Sun 6/11/2017

	"Write a program that asks the user to enter an item's wolesale cost
	and its markup percentage. IT should then display the item's retail 
	price."
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
logging.disable(logging.CRITICAL)

def calculateRetail():
	logging.debug('Start of calculateRetail(%s)')

	print("What is the WHOLESALE_PRICE?")
	WHOLESALE_PRICE = float(input('--> '))
	if (WHOLESALE_PRICE < 0):
		raise Exception('Prices must be non-negative to be valid.\n')


	# Ask for and revieve the Percentage 
	print("What is the MARKUP_PERCENTAGE? Enter percents in the format")
	print('##.## == 00.00 %')


	MARKUP_PERCENTAGE = float(input('--> '))/100
	logging.debug('MARKUP_PERCENTAGE is ' + str(MARKUP_PERCENTAGE))

	if (MARKUP_PERCENTAGE < 0):
		raise Exception('Percentages must be non-negative to be valid.\n')

	RETAIL_PRICE = MARKUP_PERCENTAGE * WHOLESALE_PRICE
	logging.debug('RETAIL_PRICE is ' + str(RETAIL_PRICE))

	print('This item retails at: $' + '{:,.2f}'.format(RETAIL_PRICE) + '\n')

try:
	print('***************')
	print('Howdy! This program takes input and calculates a retail price.')
	print('Use CTRL-C to exit.')
	loop = True
	while(loop):
		logging.debug('Beginning of while(%s)')
		calculateRetail()
		logging.debug('End of while(%s)')
		print('Contine? (y/n)')
		usr = str(input())
		if (usr.lower() == 'n'):
			print('\n*****\nYou\'ve elected to leave the program. Quitting.\n*****\n')
			loop = False
	logging.debug('End of program(%s)')
except KeyboardInterrupt:
	print('\n*****\nYou\'ve elected to leave the program. Quitting.\n*****\n')
	exit

except Exception as err:
	print('An excpetion has occured:' + str(err))

