from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

CHROMEDRIVER_PATH = "/Users/elle/Development/chromedriver"
driver = webdriver.Chrome(CHROMEDRIVER_PATH)

GOOGLE_FORMS_URL = "https://forms.gle/xXEoyb29E27cT6HM7"

for i in range(1, 35):
    salary_report_endpoint = f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}"

    response = requests.get(url=salary_report_endpoint)
    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    majors_info = soup.find_all(class_="data-table__cell csr-col--school-name")
    # print(major_info)
    major_list = [major.getText().split(":")[1] for major in majors_info]
    # print(major)

    careers_pay_info = soup.find_all(class_="data-table__cell csr-col--right")
    # print(early_careers_info)
    early_career_pay_list = [pay.getText().split(":")[1] for pay in careers_pay_info if careers_pay_info.index(pay) % 3 == 0]
    # print(early_career_pay)
    mid_career_pay_list = [pay.getText().split(":")[1] for pay in careers_pay_info if careers_pay_info.index(pay)%3 == 1]
    # print(mid_career_pay)

    for i in range(len(major_list)):
        driver.get(GOOGLE_FORMS_URL)
        time.sleep(5)

        major_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        major_field.send_keys(major_list[i])

        early_career_pay_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        early_career_pay_field.send_keys(early_career_pay_list[i])

        mid_career_pay_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        mid_career_pay_field.send_keys(mid_career_pay_list[i])

        submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        submit_button.click()


