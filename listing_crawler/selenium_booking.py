'''
This script crawls from various booking.com URLS to gather all listing URLs for that area.

It starts at the base URL, then clicks a button at the bottom of the page that redirects to
search results of all listings in that area.
The results on this page populate as a user scrolls. The first 25 load, then once the user
reaches a certain point in the page, loads the next 25, then again lower in the page loads
the next 25 listings.
Once 75 listings are present, a button appears, prompting to load more.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    urls = {
        "Galway County":"https://www.booking.com/region/ie/county-galway.en-gb.html", #1022 #946
        "Galway City": "https://www.booking.com/city/ie/galway.en-gb.html", #429 #376
        "Connemara": "https://www.booking.com/region/ie/connemara.en-gb.html" #431 #422
    }
    driver = webdriver.Chrome()
    driver.get(urls["Galway County"])
    '''
    im_flexible_button = driver.find_element(By.XPATH, "//button[@id='flexible-searchboxdatepicker-tab-trigger']")
    im_flexible_button.click()
    time.sleep(2)
    stay_period_selectors = driver.find_elements(By.XPATH, '//input[@name="flexible-los"]')
    print(stay_period_selectors)
    for selector in stay_period_selectors:
        print(selector.get_attribute("value"))
    stay_period = {
        "weekend":"value=5_1", # WEEKEND value 5_1
        "week":"value=1_5",
        "month":"value=6_28"
    }
    stay_month_ul = "id=':r31:'"
    '''
    see_all_options = driver.find_element(By.XPATH, "//a[@class='de576f5064 b46cd7aad7 ced67027e5 c7a901b0e7 e4f9ca4b0c ca8e0b9533 a9d40b8d51']")
    print(see_all_options.get_attribute("href"))
    see_all_options.click()
    # next page, search results
    time.sleep(1)
    # get number of results on page
    result_heading = driver.find_element(By.XPATH, "//h1[@aria-live='assertive']")
    r_head_txt = result_heading.text
    print(r_head_txt.split(":")[-1])
    print(r_head_txt.split(":")[-1].split(" "))
    tot_res_num = r_head_txt.split(":")[-1].split(" ")[0]
    print("\n", tot_res_num, "total results")
    # scroll down page to dynamically load content
    keep_scrolling = True
    current_n_res = [0]
    while keep_scrolling:
        print(current_n_res)
        current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
        print("\n",len(current_lsts))
        if len(current_lsts) == current_n_res[-1]:
            keep_scrolling = False
        current_n_res.append(len(current_lsts))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    print("\nExited scrolling while loop")
    # should have 75 results before clicking to next page
    # seems like as you scroll, they dynamically load in sets of 25ish?
    ok = True
    while ok:
        try:
            #load_more_options_btn = driver.find_element(By.XPATH, "//button[@class='de576f5064 b46cd7aad7 d0a01e3d83 dda427e6b5 bbf83acb81 a0ddd706cc']")
            #driver.execute_script("arguments[0].scrollIntoView();", load_more_options_btn)
            current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
            load_more_options_btn.click()
            print("\n",len(current_lsts))
        except:
            ok = False
    print("\nButton click loop exited")
    current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
    print(len(current_lsts))
    load_more_options_btn = driver.find_element(By.XPATH, "//button[@class='de576f5064 b46cd7aad7 d0a01e3d83 dda427e6b5 bbf83acb81 a0ddd706cc']")
    while load_more_options_btn:
        current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
        print(len(current_lsts))
        time.sleep(1)
        load_more_options_btn = driver.find_element(By.XPATH, "//button[@class='de576f5064 b46cd7aad7 d0a01e3d83 dda427e6b5 bbf83acb81 a0ddd706cc']")
        load_more_options_btn.click()
    time.sleep(1)
    driver.quit()

if __name__ == "__main__":
    main()