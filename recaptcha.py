from selenium import webdriver
import requests
import time

def resolve_recaptcha(zoomLink):
    #To locate where the key are in what site
    site_key = "6LfmSyQUAAAAAFLRDxYjF4navVNB9o2sbSXOCsNy"
    page_url = zoomLink
    
    driver = webdriver.Safari()
    driver.get(pageurl)

    form = {"method": "userrecaptcha",
            "googlekey": site_key,
            "key": api_key, 
            "pageurl": pageurl, 
            "json": 1}
    
    response = requests.post('http://2captcha.com/in.php', data=form)
    request_id = response.json()['request']

    #rest API request to 2captha
    url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={request_id}&json=1"
    status = 0
    while not status:
        res = requests.get(url)
        if not res.json()['status']:
            time.sleep(3)
    else:
        requ = res.json()['request']
        js = f'document.getElementById("g-recaptcha-response").innerHTML="{requ}";'
        driver.execute_script(js)
        driver.find_element_by_id("recaptcha-demo-submit").submit()
        status = 1
