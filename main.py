import os
import sys
import time

from selenium import webdriver

platformWin10 = "Windows 10"
platformMac = "CATALINA"
platformLinux = "LINUX"

platform = platformLinux

desired_cap_chrome = {
 "build" : "Lambdatest Build 2",
 "name" : "Lambdatest Test",
 "platform" : platform,
 "browserName" : "Chrome",
 "version" : "latest",
 "visual" : False,
 "video" : True,
 "network": True,
 'goog:chromeOptions': {'args': ['--window-size=400x300']},
}

desired_cap_firefox = {
 "build" : "Lambdatest Build 2",
 "name" : "Lambdatest Test",
 "platform" : platform,
 "browserName" : "Firefox",
 "version" : "latest",
 "visual" : False,
 "video" : True,
 "network": True
}

desired_cap_edge = {
 "build" : "Lambdatest Build 2",
 "name" : "Lambdatest Test",
 "platform" : platform,
 "browserName" : "MicrosoftEdge",
 "version" : "latest",
 "visual" : False,
 "video" : True,
 "network": True
}

print(sys.argv)

hub = "https://" + os.getenv('LT_USERNAME') + ":" + os.getenv('LT_ACCESS_KEY') + "@hub.lambdatest.com/wd/hub"

def OneTest(caps, sleepTime):
    begin = time.time()
    driver = webdriver.Remote(command_executor=hub, desired_capabilities=caps)
    end = time.time()
    print(f"Startup time for {caps['browserName']} {end - begin} , {begin} , {end}")
    # driver.maximize_window()
    driver.get("https://lambdatest.com")
    time.sleep(sleepTime)
    driver.quit()


OneTest(desired_cap_chrome, 25)
time.sleep(10)
OneTest(desired_cap_firefox, 10)
# time.sleep(10)
# OneTest(desired_cap_edge, 10)
