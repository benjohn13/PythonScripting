#!/bin/python

# Creating a BMI calculator that takes imperial and metric inputs
def gather_info():
	height = float(raw_input("What is your height? (inches or meters) "))
	weight = float(raw_input("What is your weight? (pounds or kilograms) "))
	unit = raw_input("Are your measurements in imperial or metric units? ").lower().strip()
	return (height, weight, unit)

def calculate_bmi(weight, height, unit='metric'):
	if unit == 'metric':
		bmi = (weight / (height ** 2))
	else:
		bmi = 703 * (weight / (height ** 2))
	print("Excellent! Your BMI is about %s" % bmi)

while True:
	height, weight, unit = gather_info()
	if unit.startswith('i'):
		calculate_bmi (height=height, weight=weight, unit='imperial')
		break
	elif unit.startswith('m'):
		calculate_bmi(weight, height)
		break
	else:
		print("Error: Unknown measurement system. Please use imperial or metric.")