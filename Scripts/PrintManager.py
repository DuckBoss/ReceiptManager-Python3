import PrintUtils as PU

def PrintBillCommands():
	PU.PrintDashes(40)
	print("\t-Bill Commands-\n")
	print("\tAdd Item To Bill - [A/a]")
	print("\tRemove Item From Bill - [R/r]")
	print("\tCalculate Bill Total - [T/t]")
	print("\tPrint Full Bill List - [P/p]")
	print("\tSave Full Bill To File - [S/s]")
	print("\tExit To Menu - [B/b]")
	PU.PrintDashes(40)

def PrintMainMenuCommands():
	PU.PrintDashes(40)
	print("\t-Main Commands-\n")
	print("\tStart New Bill - [N/n]")
	print("\tQuit - [Q/q]")
	PU.PrintDashes(40)