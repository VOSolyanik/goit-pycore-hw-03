from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> dict:
	"""Function to get upcoming birthdays"""
	
	today = datetime.today().date()
	upcoming_birthdays = []

	# Iterate through all users
	for user in users:
		birthdate = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
		# Calculate this year's birthday
		birthdate_this_year = birthdate.replace(year=today.year)
		# If this year's birthday in past, calculate next year's birthday
		if birthdate_this_year < today:
			birthdate_this_year = birthdate.replace(year=today.year + 1)

		# Calculate days to birthday
		days_to_birthday = (birthdate_this_year - today).days
		# If days to birthday less than or equal to 7, calculate congratulation date
		if days_to_birthday <= 7:
			congratulation_date = birthdate_this_year
			# If congratulation date is weekend, calculate next week's date
			if birthdate_this_year.weekday() >= 5:
				congratulation_date = birthdate_this_year + timedelta(days=7 - birthdate_this_year.weekday())
			# Add user to upcoming birthdays list
			upcoming_birthdays.append({
				'name': user['name'],
				'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
			})

	return upcoming_birthdays

# Date of testing is 2024.04.13
users = [
	{'name': 'John', 'birthday': '1990.01.01'},
	{'name': 'Petter', 'birthday': '1992.04.15'},
	{'name': 'Jim', 'birthday': '1992.04.20'},
]
# Expected output: [{'name': 'Petter', 'congratulation_date': '2024.04.15'}, {'name': 'Jim', 'congratulation_date': '2024.04.22'}]
print(get_upcoming_birthdays(users))