from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    urls = {
        "Galway County":"https://www.booking.com/region/ie/county-galway.en-gb.html", #1022
        "Galway City": "https://www.booking.com/city/ie/galway.en-gb.html", #429
        "Connemara": "https://www.booking.com/region/ie/connemara.en-gb.html" #431
    }
    driver = webdriver.Chrome()
    driver.get(urls["Galway County"])
    elements = driver.find_elements(By.XPATH, "//a")    
    for element in elements:
        print(element.text)
        print(element.get_attribute("text"))
    driver.quit()

if __name__ == "__main__":
    main()