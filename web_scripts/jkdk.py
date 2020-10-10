from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def logout(driver: webdriver.Edge):
    mainMenu_url = 'http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/MainMenu.asp'
    if mainMenu_url not in driver.current_url:
        print('no need to logout')
        return
    driver.get(mainMenu_url)
    exitBtn = driver.find_element_by_xpath(
        '/html/body/center/table[2]/tbody/tr/td[2]/a/b')
    exitBtn.click()


def login(driver: webdriver):
    # 填入账号密码
    driver.get("http://jszx-jxpt.cuit.edu.cn/Jxgl/Xs/netKs/sj.asp?UTp=Xs&jkdk=Y")
    # username = driver.find_element_by_xpath('/html/body/div[4]/div/form/dl/dd[2]/ul/li[2]/div/ul[1]/li[2]/input')
    if 'http://login.cuit.edu.cn/Login/xLogin/Login.asp' not in driver.current_url:
        return

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'TxtUserNameCssClass'))
        )
        print('[*] loading finished')
    except Exception as e:
        print('[X] Login page waiting timeout')
        print(e)
    # driver.implicitly_wait(3)

    username = driver.find_element_by_class_name('TxtUserNameCssClass')
    # Write your username here
    username.send_keys("2019XXXXXX")
    password = driver.find_element_by_class_name('TxtPasswordCssClass')
    # Write your password here
    password.send_keys("XXXXXX")
    enterBtn = driver.find_element_by_class_name('IbtnEnterCssClass')
    enterBtn.click()


def fill_table(driver):
    q3 = driver.find_element_by_xpath(
        '/html/body/form/div[2]/table/tbody/tr[4]/td[2]/div/select[3]')
    q4 = driver.find_element_by_xpath(
        '/html/body/form/div[2]/table/tbody/tr[4]/td[2]/div/select[4]')
    q5 = driver.find_element_by_xpath(
        '/html/body/form/div[2]/table/tbody/tr[4]/td[2]/div/select[5]')
    q6 = driver.find_element_by_xpath(
        '/html/body/form/div[2]/table/tbody/tr[4]/td[2]/div/select[6]')

    Select(q3).select_by_value('1')
    Select(q4).select_by_value('1')
    Select(q5).select_by_value('1')
    Select(q6).select_by_value('1')

    print('[*] filled the table')


if __name__ == '__main__':
    driver = webdriver.Edge(executable_path=r'./msedgedriver.exe')

    # logout(driver)
    login(driver)
    print('[*] successfully logged in')

    # test if this can correctly open the latest one
    latest = driver.find_element_by_xpath(
        '/html/body/div[2]/table/tbody[2]/tr[2]/td[2]/a')
    latest.click()

    assert 'editSj.asp' in driver.current_url

    fill_table(driver)

    # confirm submitting
    submit = driver.find_element_by_xpath('/html/body/form/div[1]/table/tbody/tr/td[1]/input')
    submit.click()


    sleep(10)
