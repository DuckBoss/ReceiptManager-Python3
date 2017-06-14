class Product:
	def __init__(self, itemName, itemPrice, itemQuantity):
		self.ItemName = str(itemName)
		self.ItemPrice = float(itemPrice)
		self.ItemQuantity = int(itemQuantity)

	def GetPrice(self):
		return self.ItemPrice

	def GetName(self):
		return self.ItemName

	def GetQuantity(self):
		return self.ItemQuantity

	def GetTotalPrice(self):
		return (self.ItemPrice * self.ItemQuantity)