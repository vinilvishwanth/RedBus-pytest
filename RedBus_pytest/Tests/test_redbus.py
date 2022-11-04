import datetime
import pytest
from Library.excel_lib import ReadExcel
from POM.redbus import RedBus
from Library.config import Config



class TestRedBus:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Config.redbus_testdata_sheet)

    @pytest.mark.parametrize('fd_place,to_place,md_fd_place,md_to_place,name,age,email,phone,upi_id', data)
    def test_select_bus_tickets(self, fd_place, to_place, md_fd_place, md_to_place, name, age, email, phone, upi_id, init_driver):
        driver = init_driver
        try:
            bs = RedBus(init_driver)
            bs.bus_tickets()
            bs.from_destination()
            bs.enter_from_destination(fd_place)
            bs.select_from_destination()
            bs.to_destination()
            bs.enter_to_destination(to_place)
            bs.select_to_destination()
            bs.onward_date()
            bs.enter_onward_date()
            bs.search_buses_btn()
            bs.modify_btn()
            bs.modify_from_destination(md_fd_place)
            bs.modify_to_destination(md_to_place)
            bs.modify_search_btn()
            # bs.ok_got_it_btn()
            # bs.primo_buses()
            # bs.departure_time()
            # bs.bus_types()
            # bs.arrival_time()
            bs.view_seats_btn()
            # bs.hide_seats()
            bs.boarding_point()
            bs.dropping_point()
            bs.fare_details()
            bs.change_btn()
            bs.change_boarding_point()
            bs.continue_btn()
            bs.proceed_to_book()
            bs.enter_name(name)
            bs.select_male_radio_btn()
            bs.enter_age(age)
            bs.enter_email(email)
            bs.enter_phone_no(phone)
            bs.insurance_checkbox()
            bs.donate_covid_checkbox()
            bs.proceed_to_pay()
            bs.select_payment_method()
            bs.enter_upi_id(upi_id)
            bs.verify_btn()
            bs.pay_now_btn()

        except AssertionError as error_msg:      # for all errors we use BaseException
            td = datetime.datetime.now()
            name = f'screenshot_{td.hour}_{td.minute}_{td.second}.png'
            driver.save_screenshot(Config.screenshots_path + name)
            raise error_msg








