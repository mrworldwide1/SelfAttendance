## AutomateAttendance
## September 17, 2023
## By: Lucas Leung


# setup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# ---user configurable options---
driver = webdriver.Chrome() # assumes you're using Chromium-based browser. uncomment/comment whatever browser you use
# driver = webdriver.Firefox()
cellLink = "" # paste in your link to the cell
text = "Here" # the thing that's typed into the doc

# open link to cell
driver.get(cellLink)

# wait till page loads
# time.sleep(1)

# types text then presses enter, via Actions API/Action Chains
actions = ActionChains(driver)
actions.send_keys(text)
actions.send_keys(Keys.RETURN)
actions.perform()

# delay
time.sleep(1)

# quit browser
driver.quit()
