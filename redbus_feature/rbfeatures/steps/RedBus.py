import re

from behave import *
from selenium import webdriver
import time


@given(u'I launch chrome browser and open redbus website')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r'C:\Users\vinil\PycharmProjects\pythonProject\RED_BUS\drivers\chromedriver.exe')
    context.driver.get(r'https://www.redbus.in/')
    context.driver.maximize_window()

@when(u'I select Bus Tickets option')
def step_impl(context):
    context.driver.find_element('id', 'redBus').click()

@when(u'Enter "{From_Destination}"')
def step_impl(context ,From_Destination):
    context.driver.find_element('xpath', '//input[@placeholder="FROM"]').click()
    try:
        context.driver.find_element('xpath', '//input[@placeholder="FROM"]').send_keys(From_Destination)
        assert re.findall('[a-zA-z]', From_Destination)
    except:
        context.driver.close()
        assert False,'Test Failed'
    time.sleep(2)
    context.driver.find_element('xpath', '//li[text()="Kukatpally, "]').click()
    time.sleep(2)

@when(u'Select "{To_Destination}"')
def step_impl(context, To_Destination):
    context.driver.find_element('xpath', '//input[@placeholder="TO"]').click()
    try:
        context.driver.find_element('xpath', '//input[@placeholder="TO"]').send_keys(To_Destination)
        assert re.findall('[a-zA-z]', To_Destination)
    except:
        context.driver.close()
        assert False, 'Test Failed'
    time.sleep(2)
    context.driver.find_element('xpath', '//li[text()="Majestic, "]').click()

@when(u'Select OnwardDate')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@placeholder="ONWARD DATE"]').click()
    time.sleep(3)
    context.driver.find_element('xpath', '(//span[text()="10"])[2]').click()

@then(u'Click on Search Buses button')
def step_impl(context):
    context.driver.find_element('xpath', '//button[@class="D120_search_btn searchBuses"]').click()
    # context.driver.implicitly_wait(15)
    time.sleep(6)

# @When(u'I select Modify button')
# def step_impl(context):
#     context.driver.find_element('xpath', '//div[text()="Modify"]').click()
#
# @When(u'Enter "{modify_frm_dst}" and "{modify_to_dst}"')
# def step_impl(context,modify_frm_dst,modify_to_dst):
#     context.driver.find_element('xpath', '//input[@value="Kukatpally, Hyderabad"]').click()
#     time.sleep(2)
#     context.driver.find_element('xpath', '//input[@value="Kukatpally, Hyderabad"]').send_keys(modify_frm_dst)
#     context.driver.find_element('xpath', '//input[@value="Majestic, Bangalore"]').click()
#     time.sleep(2)
#     context.driver.find_element('xpath', '//input[@value="Majestic, Bangalore"]').send_keys(modify_to_dst)
#
# @then(u'Click on modify search button')
# def step_impl(context):
#     context.driver.find_element('xpath', '//button[@class=" button ms-btn"]').click()

@when(u'I select ok,got it button')
def step_impl(context):
    context.driver.find_element('xpath', '//span[text()="Ok, got it"]').click()
    context.driver.implicitly_wait(10)

@when(u'I select View Seats button')
def step_impl(context):
    context.driver.find_element('xpath', '(//div[@class="button view-seats fr"])[2]').click()
    # time.sleep(15)
    context.driver.implicitly_wait(30)
    context.driver.find_element('xpath', '//span[@title="LB Nagar"]/../..//div[@class="radio-unchecked"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//span[text()="Indiranagar"]/../..//div[@class="radio-css "]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//h3[@class="fare-toggle-btn fr m-t-0"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//span[@class="fr bpdp-change"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//span[@title="Secunderabad"]/../..//div[@class="radio-unchecked"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//button[@class="button continue inactive text-trans-uc w-h-cont"]').click()
    time.sleep(2)

@then(u'click on proceed to book')
def step_impl(context):
    context.driver.find_element('xpath', '//button[text()="Proceed to book"]').click()
    time.sleep(3)

@when(u'Provide "{name}" and "{age}" to add passenger information')
def step_impl(context,name, age):
    try:
        context.driver.find_element('xpath', '//input[@placeholder="Name"]').send_keys(name)
        assert re.findall('[a-zA-Z]', name)
        # time.sleep(2)
    except:
        context.driver.close()
        assert False, 'Test Failed'
    context.driver.find_element('xpath', '//div[@id="div_22_0"]').click()
    time.sleep(2)
    try:
        assert len(str(age)) <= 2
        context.driver.find_element('xpath', '//input[@placeholder="Age"]').send_keys(age)
        time.sleep(2)
    except:
        context.driver.close()
        assert False, 'Test Failed'
    time.sleep(5)

@when(u'provide "{email_id}" and "{phone_no}" to add coctact deatils')
def step_impl(context, email_id, phone_no):
    try:
        context.driver.find_element('xpath', '//input[@placeholder="Email ID"]').send_keys(email_id)
        assert re.findall('\W', email_id)
        time.sleep(2)
    except:
        context.driver.close()
        assert False, 'Test Failed'
    time.sleep(2)
    try:
        assert len(str(phone_no)) == 10
        context.driver.find_element('xpath', '//label[@class="custinfo_label"]//input[@id="seatno-06"]').send_keys(phone_no)
        time.sleep(2)
    except:
        context.driver.close()
        assert False, 'Test Failed'
    time.sleep(3)
    context.driver.find_element('xpath', '//span[@class="checkmark-radio"]').click()
    time.sleep(2)
    context.driver.find_element('xpath', '//label[@id="addOnFeatureCheckBox"]').click()
    time.sleep(2)

@then(u'click on proceed to pay')
def step_impl(context):
    context.driver.find_element('xpath', '//input[@class="button main-btn gtm-continueBooking"]').click()
    time.sleep(2)

@when(u'I choose the payment method')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element('xpath', '//div[@id="Pay through UPI ID"]').click()


@when(u'I should provide valid "{upi_id}" payment details')
def step_impl(context, upi_id):
    context.driver.find_element('xpath', '//input[@placeholder="Enter UPI ID"]').send_keys(upi_id)
    assert re.findall('\W', upi_id)

@then(u'Click on Verify and proceed button to Book a Bus ticket')
def step_impl(context):
    context.driver.find_element('xpath', '//div[text()="VERIFY"]').click()
    context.driver.find_element('xpath', '//div[text()="Pay Now"]').click()
    context.driver.close()


