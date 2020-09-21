import requests
from bs4 import BeautifulSoup
def kbbi(pesan):
	try:
		url = 'https://www.kamusbesar.com/'+pesan
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
		source=requests.get(url, headers=headers).text
		soup = BeautifulSoup(source, 'html.parser')
		arti = soup.find("span","word_description").text
		arti1 = soup.find("div","title-left").text

		if pesan==arti1:
			try:
				contoh = soup.find("div","word_example").text.replace("~",pesan)
			except:
				contoh = "contoh:"+pesan
			gabung = 'Kamus Besar Bahasa Indonesia : "'+pesan+'"\n\n'+arti+"\n\n"+contoh
		else:
			gabung = 'Kamus Besar Bahasa Indonesia : "'+pesan+'"\n\nTidak ketemu hasilnya.'
	except:
		gabung = 'Kamus Besar Bahasa Indonesia : "'+pesan+'"\n\nTidak ketemu hasilnya.'

	return gabung