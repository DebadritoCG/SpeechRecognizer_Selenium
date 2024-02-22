from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as ServiceEdge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from os import getcwd

chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
try:
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
except:
  driver = webdriver.Edge(service=ServiceEdge(EdgeChromiumDriverManager().install()),options=edge_options)

website = f"{getcwd()}\\voice.html"

driver.get(website)


def Listen():
    driver.get(website)
    driver.find_element(by=By.ID, value='start').click()
    while True:
        text = driver.find_element(by=By.ID, value='output').text
        if text != "":
            driver.find_element(by=By.ID, value='end').click()
            return str(text)

if __name__ == "__main__":
  #Testing
  print('Listening...')
  result = Listen()
  print(f'You Said: {result}')
