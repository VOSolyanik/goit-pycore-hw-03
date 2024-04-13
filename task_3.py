import re

def normalize_phone(phone: str) -> str:
	"""Function for normalizing phone number"""
	# Remove all symbols except digits or + from phone number
	phone = re.sub(r'\D|\+', '', phone)
	# If phone number len is 10, prefix it with +38
	if len(phone) == 10:
		phone = f'+38{phone}'
	# If phone number len is 11 and starts with 8, prefix it with +3
	elif len(phone) == 11 and phone[0] == '8':
		phone = f'+3{phone}'
	# If phone number len is 12, prefix it with +
	elif len(phone) == 12:
		phone = f'+{phone}'

	# if-elseif-else block can be replaced with: phone = f'+38{phone[-10:]}'

	return phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)