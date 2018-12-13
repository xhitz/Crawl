try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import sys
    from time import sleep
    from tqdm import tqdm
    import random
except ImportError as e:
    import sys
    import bs4
    sys.exit(1)

def selection(agent):
    # function to choose a random line inside a file, making sure not to choose the same one twice.
    line = next(agent)
    seen = set()
    for num, aline in enumerate(agent):
        if random.randrange(num+2):continue
        line = aline
        if line not in seen:
            print('[!] selecting {} [!]'.format(line))
            seen.add(str(line))
            return line
        if line in seen:
            print("[!] already used {} [!]".format(line))
            continue

def progress_bar(duration):
    for i in tqdm(range(int(duration))):
        sleep(1)
while True:
    try:
        driver = Options()
        driver.add_argument('headless')
        web = webdriver.Remote(command_executor='http://localhost:0000', desired_capabilities=DesiredCapabilities.CHROME)
 #       WebDriver driver=
        while True:
            import os
            os.system('clear')
            ran = random.randint(500,5000)
            f_name = open('./agents.txt', 'r')
            feed = selection(f_name)
            driver.add_argument(feed)
            web.get("http://xgames.espn.com/xgames/real/23592788/martinez-23592917")
            assert "Real BMX 2018" in web.title
            print("{}".format(web.title))
            element = web.find_element_by_xpath('')
            print('{}'.format(element))
            element.click()
            #element = web.find_element_by_xpath('Insert xpath here')----------------To Add More Elements
            #element.click()
            #second =web.select_element_by_name("Insert Text Here")
            #second.click()
            web.quit()
            progress_bar(ran)
            continue
    except AssertionError:
        ran = random.randint(500,1000)
        progress_bar(ran)
        continue
