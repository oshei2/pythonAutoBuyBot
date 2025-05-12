#pythonAutoBuyBot
from selenium.webdriver.common.by import By
import undetected_chromedriver as webdriver
import time

#load profile where you are signed in
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/tmp/botProfile")
chrome_options.add_argument("--profile-directory=Default")

#starts chrome webdriver and waits for elements to load
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(5)

#url for product page and xpath for add to cart button
#url = 'https://www.newegg.com/msi-rtx-5070-ti-16g-vanguard-soc-launch-edition-nvidia-geforce-rtx-5080-16gb-gddr7/p/N82E16814137923'
url = 'https://www.newegg.com/zotac-rtx-5070-ti-solid-core-nvidia-geforce-rtx-5070-ti-16gb-gddr7/p/N82E16814500619'
add_to_cart_xpath = '//*[@id="ProductBuy"]/div/div[2]/button'
no_thanks_xpath = '//*[@id="modal-intermediary"]/div/div/div/div[4]/button[1]'
proceed_xpath = '//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]'
guest_xpath = '//*[@id="signin-signin-wrap"]/div/div[2]/div/div/div/form[2]/div[2]/div/button'
place_xpath = '//*[@id="Summary_Side"]/div[1]/div[1]/button'
cvv_xpath = '//*[@id="app"]/div/section/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/label/div/div[4]/input'

#opens page
driver.get(url)

#finds and clicks buttons to
addToCart = driver.find_element(By.XPATH, add_to_cart_xpath)
addToCart.click()

noThanks = driver.find_element(By.XPATH, no_thanks_xpath)
noThanks.click()

proceed = driver.find_element(By.XPATH, proceed_xpath)
proceed.click()

#enter cvv digits
cvv = driver.find_element(By.XPATH, cvv_xpath)
for digit in "222":
    cvv.send_keys(digit)
    time.sleep(0.2)

#places order
place = driver.find_element(By.XPATH, place_xpath)
place.click()



