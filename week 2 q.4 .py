def Punctuation(string):
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	for x in string.lower():
		if x in punctuations:
			string = string.replace(x, "")
	print(string)
string = "Hello???@@##$ h$#$ow#$% are%$ ^you$%^&"
Punctuation(string)