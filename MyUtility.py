from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import xlrd

br = webdriver.Firefox(executable_path="C:\\Users\\shubhana\\Downloads\\engine\\geckodriver.exe")
br.get("https://www.snapdeal.com/")
action=ActionChains(br)

loc= ("C:\\Users\\shubhana\\PycharmProjects\\cred.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
_username = int(sheet.cell_value(0, 1))
_password = str(sheet.cell_value(1, 1))

class Util():


    def _doLogin(self):
        # login
        print('entering username')
        br.find_element_by_xpath('//*[@id="username"]').send_keys(_username)  # Enter username for signup
        time.sleep(3)
        br.find_element_by_xpath('//*[@id="login-continue"]').click()  # Click on continue
        # br.find_element_by_xpath('//*[@id="w_password"]').send_keys('Snapdeal@1234')      #Enter Password
        time.sleep(3)
        # br.find_element_by_xpath('//input[@id="w_password"').send_keys('Snapdeal@1234')  #Enter pwd
        br.find_element_by_xpath('//input[@name="password"]').send_keys(_password)  # enter pwd
        br.find_element_by_css_selector('#login-done').click()


    def _doSinUp(self):
        pass

    def _doLogOut(self):
        time.sleep(5)
        br.find_element_by_xpath('//a[@href="https://www.snapdeal.com"]').click()

        time.sleep(3)
        menu =br.find_element_by_class_name('accountUserName')
        hidden_submenu = br.find_element_by_xpath('//a[@href="https://www.snapdeal.com/logout"]')
        action.move_to_element(menu).click(hidden_submenu).perform()

        pass

    def _search_and_add(_keys, _model):
        local_model= f'//p[@title="{_model}"]'
        print(local_model)
        br.find_element_by_id('inputValEnter').send_keys(_keys)
        br.find_element_by_class_name('searchformButton').click()
        br.find_element_by_xpath(local_model).click()
        #Switching window
        time.sleep(5)
        br.switch_to.window(br.window_handles[1])

        #Adding item to bucket
        time.sleep(5)
        br.find_element_by_id('add-cart-button-id').click()

        #proceed to checkout
        time.sleep(3)
        br.find_element_by_class_name('marR5').click()