import re
from library.excel_lib import ReadExcel
from library.config import Config
import time

class RedRail:

    read_xl = ReadExcel()
    rd_loc = read_xl.read_locater(Config.rr_loc_sheet)

    def __init__(self, driver):
        self.driver = driver

    def red_rail(self):
        locator = self.rd_loc['red_rail']
        self.driver.find_element(*locator).click()

    def from_station(self, from_stn):
        locator = self.rd_loc['from_place']
        self.driver.find_element(*locator).send_keys(from_stn)
        assert re.findall('\w', from_stn)

    def f_stn(self):
        locator = self.rd_loc['f_place']
        self.driver.find_element(*locator).click()

    def to_station(self, to_stn):
        locator = self.rd_loc['to_place']
        self.driver.find_element(*locator).send_keys(to_stn)
        assert re.findall('\w', to_stn)

    def t_stn(self):
        locator = self.rd_loc['t_place']
        self.driver.find_element(*locator).click()

    def src_btn(self):
        locator = self.rd_loc['search_trains']
        self.driver.find_element(*locator).click()

    def trn_cls(self):
        locator = self.rd_loc['tran_class']
        self.driver.find_element(*locator).click()

    def click_go_btn(self):
        locator = self.rd_loc['go_ahead']
        self.driver.find_element(*locator).click()

    def click_irctc_usr(self):
        locator = self.rd_loc['irctc_username']
        self.driver.find_element(*locator).click()

    def enter_irctc_usr(self, irctc_usr):
        locator = self.rd_loc['enter_irctc_user']
        self.driver.find_element(*locator).send_keys(irctc_usr)
        assert re.findall('\w', irctc_usr)
        assert re.findall('\d', irctc_usr)

    def click_check_btn(self):
        locator = self.rd_loc['check_button']
        self.driver.find_element(*locator).click()
        # time.sleep(4)

    def click_add_psgr(self):
        locator = self.rd_loc['add_passenger']
        self.driver.find_element(*locator).click()

    def enter_name(self, name):
        locator = self.rd_loc['name_']
        self.driver.find_element(*locator).send_keys(name)
        assert re.findall('\w', name)

    def enter_age(self, age):
        locator = self.rd_loc['age_']
        self.driver.find_element(*locator).send_keys(age)
        # assert re.findall('^\d{2}$', age)

    def click_gender(self):
        locator = self.rd_loc['gender_']
        self.driver.find_element(*locator).click()

    def click_pref(self):
        locator = self.rd_loc['pref_']
        self.driver.find_element(*locator).click()

    # def click_meal_pref(self):
    #     locator = self.rd_loc['meal_pref_']
    #     self.driver.find_element(*locator).click()

    def click_add_passenger(self):
        locator = self.rd_loc['add_psngr_']
        self.driver.find_element(*locator).click()

    def chs_pref(self):
        locator = self.rd_loc['choose_pref']
        self.driver.find_element(*locator).click()

    def chs_pref_1(self):
        locator = self.rd_loc['choose_pref1']
        self.driver.find_element(*locator).click()

    def chs_pref_2(self):
        locator = self.rd_loc['choose_pref2']
        self.driver.find_element(*locator).click()

    def save_pref(self):
        locator = self.rd_loc['save_pref']
        self.driver.find_element(*locator).click()

    def enter_email(self,email):
        locator = self.rd_loc['email_']
        self.driver.find_element(*locator).send_keys(email)
        assert re.findall('\W', email)

    def enter_ph_no(self,ph_no):
        locator = self.rd_loc['phone_number_']
        self.driver.find_element(*locator).send_keys(ph_no)
        # assert re.findall('^\d{10}$', ph_no)

    def click_prcd(self):
        locator = self.rd_loc['proceed_']
        self.driver.find_element(*locator).click()

    def click_UPI(self):
        locator = self.rd_loc['upi_']
        self.driver.find_element(*locator).click()

    def enter_UPI(self, upi):
        locator = self.rd_loc['provide_upi']
        self.driver.find_element(*locator).send_keys(upi)
        assert re.findall('\W', upi)

    def click_verify(self):
        locator = self.rd_loc['verify_']
        self.driver.find_element(*locator).click()

    def click_paynow(self):
        locator = self.rd_loc['paynow_']
        self.driver.find_element(*locator).click()
