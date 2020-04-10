from bs4 import BeautifulSoup
import requests , sys

def formatter(data):# formats the data
	chars = list(data)
	result = ""
	newLine = True
	dollars = 0
	for char in chars:
		if char=='%':
			result += "%\n"
			newLine = True  # prints new lines
		elif char=='$':
			result += ";$" # seperates money values
			dollars += 1
		else:
			if newLine==True:
				result += char+">"
				newLine = False    # adds > after index position
			elif dollars==3 and char==' ':
				result += " ;"# adds semi-colon before value
				dollars = 0
			else:
				result += char
	return result
def collector():
	url = "https://coinmarketcap.com/" 
	try:
		resp = requests.get(url)
		soup = BeautifulSoup(resp.text,"html.parser")
		fields = soup.findAll("tr")
		return fields
	except ConnectionError:
		print("Connection to target site failed: Please check your internet connection")
	except Exception as e:
		print(f"An exception of type {e} occured !")
		sys.exit()
	return False
def organizer():
	count = 3
	aggregator = ""
	fields = collector()
	if fields==False:
		print("Please try again after fixing network issues.")
		sys.exit()
	for field in fields:
		if count==0:
			aggregator += field.text
		else:
			count -= 1
	# available fields on webpage name, market cap , price, volume(24h) , circulating supply , change(24h) , price graph
	with open("cryptoWeb.txt","w") as fl:
		fl.write(formatter(aggregator))
if __name__=='__main__':
	organizer()