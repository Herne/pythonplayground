def example(): 
	try: 
		int('N/A') 
	except ValueError as e: 
		raise RuntimeError('A parsing error occurred') from e

example() 

