def PrintDashes(count, addNewline=False):
	out = ''
	for x in range(0, count):
		out += '-'
	if(addNewline):
		out += '\n'
	print(out)

def PrintUnderscores(count, addNewline=False):
	out = ''
	for x in range(0, count):
		out += '_'
	if(addNewline):
		out += '\n'
	print(out)

def PrintSymbols(symbol, count, addNewline=False):
	out = ''
	for x in range(0, count):
		out += str(symbol)
	if(addNewline):
		out += '\n'
	print(out)