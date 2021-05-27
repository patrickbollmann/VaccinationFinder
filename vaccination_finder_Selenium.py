from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import telegram_send
from datetime import datetime

keyString = "Keine Plätze frei" #string to search for (if this is found there is no appointment)
found = 0
while True:
	try:
		print("Checking for vaccination appointments")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		
		url = "https://www.hausaerzte-rahden.de/corona-erstimpfung/"    #link of the website containing the appointments
		chrome_options = Options()
		chrome_options.add_argument("--headless")
	 
		driver = webdriver.Chrome(executable_path='chromedriver.exe')   #define your chrome driver here
        
        #parse website
		driver.get(url)
		time.sleep(1)
		text = driver.page_source
		driver.quit()

		soup=BeautifulSoup(text, 'lxml')
		appointments = soup.find_all("div", {"class": "am-event-wrapper"})
		
		print(current_time)

		for appointment in appointments:
			if keyString in str(appointment):
				print("no appointments found")
			else:
				print("fount vaccination")
				gefunden = 1
				telegram_send.send(messages=["your success message"])   #send success msg
				telegram_send.send(messages=[url])  #send link to booking website
		
		time.sleep(60)
		if(found == 1):
			found = 0
			time.sleep(240)
	except Exception as e:
		print(e)