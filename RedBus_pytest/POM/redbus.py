import re
import time
from Library.excel_lib import ReadExcel
from Library.config import Config

class RedBus:
    read_xl = ReadExcel()
    rb_locators = read_xl.read_locator(Config.redbus_locators_sheet)

    def __init__(self,driver):
        self.driver = driver

    def bus_tickets(self):
        locators = self.rb_locators['red_bus_']
        self.driver.find_element(*locators).click()

    def from_destination(self):
        locators = self.rb_locators['from_dst']
        self.driver.find_element(*locators).click()

    def enter_from_destination(self, fd_place):
        locators = self.rb_locators['enter_from_dst']
        self.driver.find_element(*locators).send_keys(fd_place)
        assert re.findall('[a-zA-Z]', fd_place)
        self.driver.implicitly_wait(10)

    def select_from_destination(self):
        locators = self.rb_locators['select_from_dst']
        self.driver.find_element(*locators).click()

    def to_destination(self):
        locators = self.rb_locators['to_dst']
        self.driver.find_element(*locators).click()

    def enter_to_destination(self, to_place):
        locators = self.rb_locators['enter_to_dst']
        self.driver.find_element(*locators).send_keys(to_place)
        assert re.findall('[a-zA-Z]', to_place)
        self.driver.implicitly_wait(10)

    def select_to_destination(self):
        locators = self.rb_locators['select_to_dst']
        self.driver.find_element(*locators).click()

    def onward_date(self):
        locators = self.rb_locators['onward_date_']
        self.driver.find_element(*locators).click()

    def enter_onward_date(self):
        locators = self.rb_locators['enter_onward_date_']
        self.driver.find_element(*locators).click()

    def search_buses_btn(self):
        locators = self.rb_locators['search_buses_']
        self.driver.find_element(*locators).click()

    def modify_btn(self):
        locators = self.rb_locators['modify_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(5)

    def modify_from_destination(self,md_fd_place):
        locators = self.rb_locators['modify_from_dst']
        self.driver.find_element(*locators).click()
        locators = self.rb_locators['modify_from_dst']
        self.driver.find_element(*locators).send_keys(md_fd_place)
        assert re.findall('\w', md_fd_place)

    def modify_to_destination(self,md_to_place):
        locators = self.rb_locators['modify_to_dst']
        self.driver.find_element(*locators).click()
        locators = self.rb_locators['modify_to_dst']
        self.driver.find_element(*locators).send_keys(md_to_place)
        assert re.findall('\w', md_to_place)

    def modify_search_btn(self):
        locators = self.rb_locators['modify_search_btn_']
        self.driver.find_element(*locators).click()
        self.driver.implicitly_wait(15)

    # def ok_got_it_btn(self):
    #     self.driver.find_element('xpath', '//span[text()="Ok, got it"]').click()

    # def primo_buses(self):
    #     self.driver.find_element('xpath', '//li[@class="clearfix"]/span[contains(text(),"Primo Bus")]').click()
    #
    # def departure_time(self):
    #     self.driver.find_element('xpath', '(//label[@title="After 6 pm"])[1]').click()
    #
    # def bus_types(self):
    #     self.driver.find_element('xpath', '//label[text()="SLEEPER"]').click()
    #
    # def arrival_time(self):
    #     self.driver.find_element('xpath', '(//label[@title="After 6 pm"])[2]').click()

    def view_seats_btn(self):
        self.driver.implicitly_wait(15)
        locators = self.rb_locators['click_on_view_seats']
        self.driver.find_element(*locators).click()
        self.driver.implicitly_wait(10)

    # def hide_seats(self):
    #     self.driver.find_element('xpath', '//div[@class="button hide-seats fr"]').click()

    def boarding_point(self):
        locators = self.rb_locators['boarding_point_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def dropping_point(self):
        locators = self.rb_locators['dropping_point_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def fare_details(self):
        locators = self.rb_locators['fare_details_']
        self.driver.find_element(*locators).click()

    def change_btn(self):
        locators = self.rb_locators['change_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def change_boarding_point(self):
        locators = self.rb_locators['change_boarding_point_']
        self.driver.find_element(*locators).click()
        time.sleep(2)
    def continue_btn(self):
        locators = self.rb_locators['continue_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def proceed_to_book(self):
        locators = self.rb_locators['proceed_to_book_']
        self.driver.find_element(*locators).click()

    def enter_name(self,name):
        locators = self.rb_locators['name_']
        self.driver.find_element(*locators).send_keys(name)
        assert re.findall('\w', name)
        # assert re.findall('\D', name)
        time.sleep(2)

    def select_male_radio_btn(self):
        locators = self.rb_locators['male_radio_btn_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def enter_age(self,age):
        locators = self.rb_locators['age_']
        self.driver.find_element(*locators).click()
        self.driver.find_element(*locators).send_keys(age)
        # assert re.findall('^\d{2}$', age)
        time.sleep(3)

    def enter_email(self,email):
        locators = self.rb_locators['email_id']
        self.driver.find_element(*locators).send_keys(email)
        assert re.findall('\W', email)
        time.sleep(2)

    def enter_phone_no(self,phone):
        # if isinstance(phone,float):
        #     phone = str(int(phone))
        # assert len(phone) == 10
        locators = self.rb_locators['phone_no']
        self.driver.find_element(*locators).send_keys(phone)
        # assert re.findall('^\d{10}$', phone)
        time.sleep(2)

    def insurance_checkbox(self):
        locators = self.rb_locators['insurance_checkbox_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def donate_covid_checkbox(self):
        locators = self.rb_locators['donate_covid_checkbox_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def proceed_to_pay(self):
        locators = self.rb_locators['proceed_to_pay_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def select_payment_method(self):
        locators = self.rb_locators['payment_method_']
        self.driver.find_element(*locators).click()
        time.sleep(2)

    def enter_upi_id(self,upi_id):
        locators = self.rb_locators['upi_id_']
        self.driver.find_element(*locators).send_keys(upi_id)
        assert re.findall('\W', upi_id)
        time.sleep(5)

    def verify_btn(self):
        locators = self.rb_locators['verify_btn_']
        self.driver.find_element(*locators).click()
        # time.sleep(7)

    def pay_now_btn(self):
        time.sleep(3)
        locators = self.rb_locators['pay_now_btn_']
        self.driver.find_element(*locators).click()
