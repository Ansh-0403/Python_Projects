from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

speed_test_url="https://fast.com/"
x_url="https://twitter.com/i/flow/login"
gmail="anshsteam0403@gmail.com"
password="Cz6ia2rzAJDpq3W"
username="DesiPajji73896"
PROMISED_DOWN=15
PROMISED_UP=10

class Internet_speed():
    def __init__(self,speed_test_url,x_url) :
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach",True)
        self.driver= webdriver.Chrome(options=self.options)
        self.up=0
        self.down=0
    
    def get_vals(self):
        self.driver.get(speed_test_url)
        time.sleep(40)
        go_button = self.driver.find_element(By.XPATH,value='//*[@id="show-more-details-link"]')
        go_button.click()
        time.sleep(20)
        self.down=self.driver.find_element(By.XPATH,value='//*[@id="speed-value"]').text
        self.up=self.driver.find_element(By.XPATH,value='//*[@id="upload-value"]').text
        print(self.down)
        print(self.up)

    def tweet(self):
        self.driver.get(x_url)
        time.sleep(10)
        ent_gmail=self.driver.find_element(By.XPATH,value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        ent_gmail.send_keys(f"{gmail}",Keys.ENTER)
        time.sleep(7)
        try:
            user=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
            user.send_keys(f"{username}",Keys.ENTER)
            time.sleep(7)
            passw=self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            passw.send_keys(f"{password}",Keys.ENTER)
            time.sleep(7)
        except:
            passw=self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            passw.send_keys(f"{password}",Keys.ENTER)
            time.sleep(10)
        finally:
            post=self.driver.find_element(By.XPATH,value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg')
            post.click()
            time.sleep(7)
            message=self.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            message.send_keys(f"I am getting upload speed {self.up} and download speed {self.down}, while i pay for {PROMISED_UP} upload speed and {PROMISED_DOWN} download speed")

temp=Internet_speed(speed_test_url,x_url)
temp.get_vals()
temp.tweet()
