from selenium import webdriver

def initialize():
	browser = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
	response = browser.get('https://www.nfl.com/stats/player-stats/')
	print('on stats page')
	rows = browser.find_elements_by_xpath("//*[@id='main-content']/section[3]/div/div/div/div/table/tbody/tr")	
	for row_num in range(1,len(rows) + 1):
		row_xpath = "//*[@id='main-content']/section[3]/div/div/div/div/table/tbody/tr[{}]".format(row_num)
		quarterBack = browser.find_element_by_xpath(row_xpath + '/td[1]').text
		passYds = browser.find_element_by_xpath(row_xpath + '/td[2]').text
		ydsPerAtt = browser.find_element_by_xpath(row_xpath + '/td[3]').text
		numAtts = browser.find_element_by_xpath(row_xpath + '/td[4]').text
		Cmp = browser.find_element_by_xpath(row_xpath + '/td[5]').text
		CmpPercent = browser.find_element_by_xpath(row_xpath + '/td[6]').text
		TD = browser.find_element_by_xpath(row_xpath + '/td[7]').text
		INT = browser.find_element_by_xpath(row_xpath + '/td[8]').text
		print(quarterBack, passYds, ydsPerAtt, numAtts, Cmp, CmpPercent, TD, INT)

initialize()

