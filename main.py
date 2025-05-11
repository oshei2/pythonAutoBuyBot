#pythonAutoBuyBot
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

#url for product page and xpath for add to cart button
url = 'https://www.newegg.com/asus-tuf-gaming-tuf-rtx5070ti-o16g-gaming-nvidia-geforce-rtx-5070-ti-16gb-gddr7/p/N82E16814126754'
xpath = '//*[@id="ProductBuy"]/div[1]/div[2]/button'

#starts chrome webdriver and waits for elements to load
webdriver = webdriver.Chrome()
webdriver.implicitly_wait(8)

#opens page finds and clicks add to cart button
webdriver.get(url)
addToCart = webdriver.find_element(By.XPATH, xpath)
addToCart.click()
