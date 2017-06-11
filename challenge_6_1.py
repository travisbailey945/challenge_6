#! /usr/bin/env python3
''' challenge 6.1

	Travis Bailey
	Sun 6/11/2017

	"Write a program that asks the user to enter an item's wolesale cost
	and its markup percentage. IT should then display the item's retail 
	price."
'''

def calculateRetail():

	print("What is the WHOLESALE_PRICE?\n")
	WHOLESALE_PRICE = input(-->)
	if (WHOLESALE_PRICE is not float):
		raise Expection('You must enter a number for your price.\n')
	if (WHOLESALE_PRICE < 0):
		raise Expection('Prices must be non-negative to be valid.\n')


	# Ask for and revieve the Percentage 
	print("What is the MARKUP_PERCENTAGE? Enter percents in the format")
	print('##.## == 00.00 %')


	MARKUP_PERCENTAGE = input(-->)

	if (MARKUP_PERCENTAGE is not float):
		raise Expection('You must enter a number for your percentage.\n')
	if (MARKUP_PERCENTAGE < 0):
		raise Expection('Percentages must be non-negative to be valid.\n')

try:
	print('Howdy! This program takes input and calculates a retail price.')
	print('Use CTRL-C to exit.')
	while(true):
		calculateRetail()
except Expection as err:
	print('An excpetion has occured:' + str(err))

