from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time


class Meet:
    def __init__(self, meet_url, email, password, browser_path, chrome_driver_path):

        self.meet_url = meet_url
        self.email = email
        self.password = password
        self.browser_path = browser_path
        self.chrome_driver_path = chrome_driver_path

        # create a browser instance
        opts = ChromeOptions()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument('--start-maximized')
        opts.add_experimental_option('prefs', {

            'profile.default_content_setting_values.media_stream_mic': 1,
            'profile.default_content_setting_values.media_stream_camera': 1,
            'profile.default_content_setting_values.geolocation': 0,
            'profile.default_content_setting_values.notifications': 1
        })
        opts.binary_location = self.browser_path  # set custom browser path

        self.driver = webdriver.Chrome(options=opts, executable_path=self.chrome_driver_path)

    def log_into_gmail(self):

        # log in using your account
        self.driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/'
                        '&ec=GAZAAQ')

        # input mail address
        email_input = self.driver.find_element_by_name('identifier')
        email_input.send_keys(self.email)
        next_button_1 = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        next_button_1.click()
        self.driver.implicitly_wait(5)
        time.sleep(1.0)

        # input password
        password_input = self.driver.find_element_by_name('password')
        password_input.send_keys(self.password)
        next_button_2 = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        next_button_2.click()
        self.driver.implicitly_wait(5)
        time.sleep(1.0)

        print('Logged in your gmail account\n\nYou\'ll be redirected to your meeting')

        time.sleep(4.0)

    def login_into_meeting(self):

        # wait a while
        time.sleep(2)

        # enter to meeting
        self.driver.get(self.meet_url)

        # turn off camera and audio
        camera = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/'
                                                   'div/div/div[1]/div[1]/div/div[4]/div[1]/div/div')
        camera.click()

        audio = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/'
                                                  'div/div/div[1]/div[1]/div/div[4]/div[2]/div')
        audio.click()

        print('\nCamera and audio turned off')
