from selenium import webdriver

def initialize():
	browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
	response = browser.get('https://www.nfl.com/stats/player-stats/')
	print('on stats page')
	zxcv


initialize()