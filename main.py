from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep 

class TescoScrape():

    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.d = webdriver.Chrome(options=options)
        self.d.get("https://apply.tesco-careers.com/v2/spa/#/application/32148034/interviews")

    def login(self):
        #DO NOT PUBLISH EMAIL + PASSWORD TO REPO!!!!!!!!!!!!!!!!!!!!!!!!!
        self.d.find_element(By.ID, "login-email").send_keys("#########")
        self.d.find_element(By.ID, "password").send_keys("########")
        #DO NOT PUBLISH EMAIL + PASSWORD TO REPO!!!!!!!!!!!!!!!!!!!!!!!!!
        self.d.find_element(By.ID, "login-btn").click()

    def interview(self):
        self.d.find_element(By.XPATH, """/html/body/div[1]/div/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/div/div[2]/div/a""").click()
        sleep(5)
        try:
            txt = self.d.find_element(By.XPATH, """/html/body/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div/div/div/h4""").text
            if txt == "No Interviews!":
                print("NO INTERVIEWS!\n"*10)
        except:
            print("INTERVIEW AVAILABLE!\n"*10)
        sleep(3)
            

def main():
    scraping = TescoScrape()
    scraping.setup()
    scraping.login()
    scraping.interview()

if __name__ == "__main__":
    main()
