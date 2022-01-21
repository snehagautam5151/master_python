class Vehicle:
	vin = ""
	name = ""

	def __int__(self, vin, name):
		self.vin = vin
		self.name = name
  
  
	def get_vin(self, vin):
		return self.vin

	def set_vin(self, vin):
		self.vin = vin
  
	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name