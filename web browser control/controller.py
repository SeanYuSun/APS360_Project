from selenium import webdriver

# test code
class motionDriver(object):
    def __init__(self,url='https://google.com'):
        EXE_PATH = r'./chromedriver'
        driver = webdriver.Chrome(executable_path=EXE_PATH)
        driver.get('https://google.com')
        self.driver = driver


    def automateMotion(self,motion =2, distance=200):
        if motion == 0:
            # move down
            self.driver.execute_script("window.scrollBy(0, %d);"%(distance))
        elif motion == 1:
            # move up
            self.driver.execute_script("window.scrollBy(0,%d)"%(distance))

    def scrollUp(self, distance = -200):
        self.driver.execute_script("window.scrollBy(0,%d)"%(distance))

    def scrollDown(self, distance = 200):
        self.driver.execute_script("window.scrollBy(0,%d)"%(distance))
