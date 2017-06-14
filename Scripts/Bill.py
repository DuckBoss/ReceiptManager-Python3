from Product import Product

class Bill:

	def __init__(self):
		self.Bill = []

	def GetBillTotal(self):
		Sum = 0.00
		for x in range(len(self.Bill)):
			Sum += self.Bill[x].GetTotalPrice()
		return Sum

	def GetBillLength(self):
		return len(self.Bill)


	def AddToBill(self, item):
		self.Bill.append(item)

	def RemoveFromBill(self, item):
		self.Bill.remove(item)


	def GetBill(self):
		return self.Bill

	def GetBillItem(self, index):
		return self.Bill[index]