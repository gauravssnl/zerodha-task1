import csv
import datetime


def read_csv():
	today = str(datetime.date.today())
	year, month, day = today.split("-")
	date = "{}-{}-{}".format(day, month, year)
	print("Today's Date: ", date)
	filename = "EQ{}{}{}.CSV".format(int(day) - 1, month, year[2:])
	print("Filename : ", filename)
	# File context
	with open(filename, "r") as f:
		reader = csv.reader(f)
		row_num = 0
		for row in reader:
			if row_num == 0:
				header = row
				for h in header:
					print(h, end="  |  ")
				print()
				row_num += 1
			else:
				colnum = 0
				"""for col in row:
					print(col, end=" "*len(header[colnum]))
					colnum += 1
				print()"""



if __name__ == '__main__':
		read_csv()	