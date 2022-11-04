import datetime
import pytest
from library.excel_lib import ReadExcel
from POM.red_rail import RedRail
from library.config import Config
import time


class TestRedRail:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Config.rr_data_sheet)

    @pytest.mark.parametrize('from_stn,to_stn,irctc_usr,name,age,email,ph_no,upi', data)
    def test_click_rr(self, from_stn, to_stn, irctc_usr, name, age, email, ph_no, upi, init_driver):
        driver = init_driver
        try:
            rr = RedRail(init_driver)
            rr.red_rail()
            rr.from_station(from_stn)
            driver.implicitly_wait(10)
            rr.f_stn()
            rr.to_station(to_stn)
            driver.implicitly_wait(10)
            rr.t_stn()
            driver.implicitly_wait(10)
            rr.src_btn()
            driver.implicitly_wait(10)
            rr.trn_cls()
            rr.click_go_btn()
            driver.implicitly_wait(10)
            rr.click_irctc_usr()
            time.sleep(1)
            rr.enter_irctc_usr(irctc_usr)
            time.sleep(2)
            rr.click_check_btn()
            time.sleep(5)
            rr.click_add_psgr()
            driver.implicitly_wait(15)
            rr.enter_name(name)
            time.sleep(1)
            rr.enter_age(age)
            time.sleep(1)
            rr.click_gender()
            time.sleep(1)
            rr.click_pref()
            time.sleep(1)
            # rr.click_meal_pref()
            time.sleep(1)
            rr.click_add_passenger()
            time.sleep(1)
            rr.chs_pref()
            time.sleep(1)
            rr.chs_pref_1()
            time.sleep(1)
            rr.chs_pref_2()
            time.sleep(1)
            rr.save_pref()
            time.sleep(1)
            rr.enter_email(email)
            time.sleep(1)
            rr.enter_ph_no(ph_no)
            time.sleep(1)
            rr.click_prcd()
            driver.implicitly_wait(60)
            rr.click_UPI()
            time.sleep(1)
            driver.implicitly_wait(10)
            rr.enter_UPI(upi)
            time.sleep(1)
            driver.implicitly_wait(10)
            rr.click_verify()
            time.sleep(5)
            driver.implicitly_wait(10)
            rr.click_paynow()

        except AssertionError as error_msg:
            td = datetime.datetime.now()
            name = f'screenshot_{td.hour}{td.minute}{td.second}.png'
            driver.save_screenshot(Config.screenshot_path + name)
            raise error_msg