# PRACTICAL-5
# AIM: A program that reads an Excel file and prints the data in a tabular format.

import pandas as pd


def read_excel_data(file_path):
	try:
		output = pd.read_excel(file_path, engine="openpyxl")
		print(output)
	except FileNotFoundError:
		print(f"File '{file_path}' not found.")


excel_file = "delimited.xlsx"
read_excel_data(excel_file)
