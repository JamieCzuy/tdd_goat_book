from selenium import webdriver

# ---- Test Chrome Driver ---- #
browser1 = webdriver.Chrome()
browser1.implicitly_wait(10)
browser1.get('http://www.google.com')

assert 'Google' in browser1.title
browser1.close()

# ---- Test Firefox Driver ---- #
browser2 = webdriver.Firefox()
browser2.implicitly_wait(10)
browser2.get('http://www.google.com')

assert 'Google' in browser2.title
browser2.close()  # <--- Close on Firefox browser does not work
