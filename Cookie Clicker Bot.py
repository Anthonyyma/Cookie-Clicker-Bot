from selenium import webdriver

PATH = "C:\Programming\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

def main():
    driver.implicitly_wait(5)
    
    cookie = driver.find_element_by_id("bigCookie")
    Counter = driver.find_element_by_id("cookies")
    storePrices = [driver.find_element_by_id("productPrice" + str(i)) for i in range(5)]

    while 1:
        for i in range(6):
            cookie.click()
            try:
                if int(Counter.text.split(' ')[0]) > int(storePrices[i].text):
                    driver.find_element_by_id("product" + str(i)).click()
            except:
                pass

main()