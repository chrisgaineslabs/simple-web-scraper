# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from datetime import datetime, timedelta




from selenium import webdriver

def initialize():
	browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
	response = browser.get('https://www.nfl.com/stats/player-stats/')
	print('on stats page')
	zxcv


initialize()