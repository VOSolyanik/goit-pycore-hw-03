import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
	"""Function to get unique random numbers list with some len from range"""
	# Check if min, max and quantity are in valid range
	if min < 1 or max > 1000 or quantity < 0 or quantity > max - min + 1:
		return []
	# Generate numbers list in range
	available_numbers = range(min, max + 1)
	# Get unique random numbers from list
	unique_numbers = random.sample(available_numbers, quantity)
	# Return sorted result
	return sorted(unique_numbers)

print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 6, 7))