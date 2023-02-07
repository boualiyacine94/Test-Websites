from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
from Website import constants


class land_to_website(webdriver.Chrome):
    def __init__(self,driver_path =r"C:\seleniumdrivers\chromedriver_win32 (1)"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(land_to_website,self).__init__()
        self.implicitly_wait(60)
        self.maximize_window()

    def land_to_moalim(self):
        try:
            self.get(constants.BASE_URL_MOALIM)
            print('Landed to moalim successfully')
        except:
            print('Website moalim note found')

    def land_to_inkidia(self):
        try:
            self.get(constants.BASE_URL_INKIDIA_DZ)
            print('landed to inkidia successfully')
        except:
            print('Website inkidia note found')

    def land_to_deltalog(self):
        try:
            self.get(constants.BASE_URL_DELTALOG_DZ)
            print('landed to deltalog successfully')
        except:
            print('Website deltalog note found')
    def land_to_GLPI(self):
        try:
            self.get(constants.BASE_URL_GLPI)
            print('landed to GLPI successfully')
        except:
            print('Website deltalog note found')

    def land_to_preprod(self):

        self.get(constants.BASE_URL_preprod)






