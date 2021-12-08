from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# number_of_articles = driver.find_elements_by_xpath('//*[@id="articlecount"]/a[1]')
# print(number_of_articles[0].text)

# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

fName = driver.find_element_by_name("fName")
fName.send_keys("Cristi")
lName = driver.find_element_by_name("lName")
lName.send_keys("Mihai")
email = driver.find_element_by_name("email")
email.send_keys("test@gmail.com")
button = driver.find_element_by_xpath("/html/body/form/button")
button.click()

# search.send_keys("Python")
# search.send_keys(Keys.ENTER)





