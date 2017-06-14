import sys
from Product import Product
from Bill import Bill
import PrintUtils as PU
import PrintManager as PM

def main():
	while(True):
		PM.PrintMainMenuCommands()
		inp = input("Input - ").upper().strip()
		while not inp:
			inp = input("Input - ").upper().strip()

		if(inp == "N"):
			BillList = Bill()

			while(True):
				PM.PrintBillCommands()
				billInp = input("Input - ").upper().strip()
				while not billInp:
					billInp = input("Input - ").upper().strip()

				if(billInp == "A"):
					print("\t-Add New Item-\n")
					itemName = input("Item Name: ").upper().strip()
					while not itemName:
						itemName = input("Item Name: ").upper().strip()
					itemPrice = input("Item Price: ").strip()
					while not itemPrice:
						itemPrice = input("Item Price: ").strip()
					itemQuantity = input("Item Quantity: ").strip()
					while not itemQuantity:
						itemQuantity = input("Item Quantity: ").strip()
					try:
						newItem = Product(itemName, itemPrice, itemQuantity)
						BillList.AddToBill(newItem)
					except:
						print("There was an error adding this item!\n")
					finally:
						print("Item Added!\n")
						input("Enter a key to continue...")

				if(billInp == "R"):
					print("\t-Remove Item From List-\n")
					itemName = input("Item Name: ").upper().strip()
					while not itemName:
						itemName = input("Item Name: ").upper().strip()
					ListReturn = []
					for x in range(BillList.GetBillLength()):
						if(BillList.GetBillItem(x).GetName() == itemName):
							print("Removed Item - {}".format(BillList.GetBillItem(x).GetName()))
							continue
						ListReturn.append(BillList.GetBillItem(x))
					if(BillList.GetBillLength() == 0):
						print("Item Not Found!")
					BillList = Bill(ListReturn)
					input("Enter a key to continue...")

				if(billInp == "T"):
					print("\nBill Total - {0:.2f}\n".format(BillList.GetBillTotal()))
					input("Enter a key to continue...")
					
				if(billInp == "P"):
					print("-Printing Full list-")
					if(BillList.GetBillLength() == 0):
						print("List Is Empty!\n")
						input("Enter a key to continue...")
					else:
						print("\n")
						for x in range(BillList.GetBillLength()):
							PU.PrintDashes(30)
							print("#{}".format(x))
							print("Product Name - {}".format(BillList.GetBillItem(x).GetName()))
							print("Price - {0:.2f}".format(BillList.GetBillItem(x).GetPrice()))
							print("Quantity - {}".format(BillList.GetBillItem(x).GetQuantity()))
							print("Total Price - {0:.2f}".format(BillList.GetBillItem(x).GetTotalPrice()))
							PU.PrintDashes(30, True)
						input("Enter a key to continue...")
				
				if(billInp == "S"):
					fileNameInp = input("Save File As: ")
					while not fileNameInp:
						fileNameInp = input("Save File As: ")
					fileName = "../Saved Bills/{}.txt".format(fileNameInp)
					
					try:
						with open(fileName, "w") as saveFile:
							for x in range(BillList.GetBillLength()):
								saveFile.write("------------------------------\n")
								saveFile.write("Product Name - {}\n".format(BillList.GetBillItem(x).GetName()))
								saveFile.write("Price - {0:.2f}\n".format(BillList.GetBillItem(x).GetPrice()))
								saveFile.write("Quantity - {}\n".format(BillList.GetBillItem(x).GetQuantity()))
								saveFile.write("Total Price - {0:.2f}\n".format(BillList.GetBillItem(x).GetTotalPrice()))
								saveFile.write("------------------------------\n\n")
							saveFile.write("\nGrand Total - {0:.2f}".format(BillList.GetBillTotal()))

					except:
						print("Cannot currently write to file!\n")
					finally:
						print("Saved Bill List To File - {}\n".format(fileName))
						input("Enter a key to continue...")

				if(billInp == "B"):
					leaveInp = input("Are you sure? Make sure you save your progress. [Yes/No]").upper().strip()
					while not leaveInp:
						leaveInp = input("Are you sure? Make sure you save your progress. [Yes/No]").upper().strip()
					if(leaveInp == "YES"):
						break
					continue

		if(inp == "Q"):
			sys.exit(0)


if __name__ == "__main__":
	main()