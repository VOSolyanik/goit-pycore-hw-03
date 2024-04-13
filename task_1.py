
from datetime import datetime

def get_days_from_today(date: str) -> int:
	"""Function to get days from date to today"""
	try:
		date = datetime.strptime(date, '%Y-%m-%d')
	except ValueError:
		print('Invalid date format. Correct format is YYYY-MM-DD.')
		return 0
	
	today = datetime.today()
	delta = today - date
	return delta.days

print(get_days_from_today('2024-01-01'))
print(get_days_from_today('2025-01-01'))