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
import os

cwd = os.getcwd()
output_dir = cwd+"/scraping_outputs"

def main():
    st = time.time()
    urls = {
        "Galway County":"https://www.booking.com/region/ie/county-galway.en-gb.html", #1022 #946 #820
        "Galway City": "https://www.booking.com/city/ie/galway.en-gb.html", #429 #376 #344
        "Connemara": "https://www.booking.com/region/ie/connemara.en-gb.html" #431 #422 #400
    }
    driver = webdriver.Chrome()
    driver.get(urls["Connemara"])
    #
    see_all_options = driver.find_element(By.XPATH, "//a[@class='de576f5064 b46cd7aad7 ced67027e5 c7a901b0e7 e4f9ca4b0c ca8e0b9533 a9d40b8d51']")
    print(see_all_options.get_attribute("href"))
    see_all_options.click()
    # next page, search results
    # get number of results on page
    time.sleep(1)
    result_heading = driver.find_element(By.XPATH, "//h1[@aria-live='assertive']")
    r_head_txt = result_heading.text
    # CONTROL
    tot_res_num = int(r_head_txt.split(":")[-1].split(" ")[1])
    #tot_res_num = 100
    print("\n", tot_res_num, "total results")
    # scroll down page to dynamically load content
    keep_scrolling = True
    current_n_res = [0]
    printed = 0
    while keep_scrolling:
        current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
        if len(current_lsts) != printed:
            print("\n",len(current_lsts),"listings found")
            printed = len(current_lsts)
        current_n_res.append(len(current_lsts))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if current_n_res[-1] == current_n_res[-2]:
            try:
                load_more_options_btn = driver.find_element(By.XPATH, "//button[@class='de576f5064 b46cd7aad7 d0a01e3d83 dda427e6b5 bbf83acb81 a0ddd706cc']")
                load_more_options_btn.click()
                time.sleep(1)
                current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
            except Exception as e:
                print(e)
        keep_scrolling = len(current_lsts)<tot_res_num
        if len(current_n_res)>3:
            if current_n_res[-1] == (current_n_res[-2]+current_n_res[-3])/2:
                keep_scrolling = False
    with open(output_dir+"/booking_connemara_urls.txt", "w") as f:
        current_lsts = driver.find_elements(By.XPATH, "//a[@data-testid='title-link']")
        for element in current_lsts:
            f.write(element.get_attribute('href')+"\n")
    driver.quit()
    elapsed = time.time()-st
    print(f"Found {len(current_lsts)} of {tot_res_num} listings")
    print(round(elapsed/60,2), "min")

if __name__ == "__main__":
    main()