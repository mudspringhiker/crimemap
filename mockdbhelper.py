class MockDBHelper:

	def connect(self, database="crimemap"):
		pass

	def get_all_inputs(self):
		return []


	def add_input(self, data):
		pass

	def clear_all(self):
		pass

	def add_crime(self, category, date, latitude, longitude, description):
		pass

	def get_all_crimes(self):
		return [{'latitude': 30.28863837208974,
	       'longitude': -97.73643493652344,
	       'date': "2000-01-01",
	       'category': "mugging",
	       'description': "mock description"}]
