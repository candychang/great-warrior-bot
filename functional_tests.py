from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:3000')

assert 'Django' in browser.title
