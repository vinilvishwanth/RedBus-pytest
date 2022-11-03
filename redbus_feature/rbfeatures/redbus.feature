Feature: RedBus booking ticket

  Scenario Outline: User should be able to visit RedBus, & Fill all the necessary details to Book a online Bus ticket
    Given I launch chrome browser and open redbus website
    When I select Bus Tickets option
    And Enter "<From_Destination>"
    And Select "<To_Destination>"
    And Select OnwardDate
    Then Click on Search Buses button

#    When I select Modify button
#    When Enter "<modify_frm_dst>" and "<modify_to_dst>"
#    Then Click on modify search button

    When I select ok,got it button

    When I select View Seats button

    Then click on proceed to book

    When Provide "<name>" and "<age>" to add passenger information
    And provide "<email_id>" and "<phone_no>" to add coctact deatils

    Then click on proceed to pay

    When I choose the payment method
    And I should provide valid "<upi_id>" payment details
    Then Click on Verify and proceed button to Book a Bus ticket

    Examples:
      | From_Destination | To_Destination | name   | age | email_id                 | phone_no   | upi_id                |
#      | Hyderabad        | Bangalore      | vinil  | 23  | vinilvishwanth@gmail.com | 9100260674 | vinilvishwanth@okaxis |
#      | 123456           | Bangalore      | vinil  | 23  | vinilvishwanth@gmail.com | 9100260674 | vinilvishwa           |
#      | Hyderabad        | 1234567        | vinil  | 23  | vinilvishwanth@gmail.com | 9100260674 | vinilvishwan          |
#      | Hyderabad        | Bangalore      | 123456 | 23  | vinilvishwanth@gmail.com | 9100260674 | vinilvishwan          |
      | Hyderabad        | Bangalore      | vinil  | 100 | vinilvishwanth@gmail.com | 9100260674 | vinilvishwant         |
#      | Hyderabad        | Bangalore      | vinil  | 23  | vinilvishwanth           | 9100260674 | vinilvishwan          |
#      | Hyderabad        | Bangalore      | vinil  | 23  | vinilvishwanth@gmail.com | 910026     | vinilvishw@yb         |
#      | Hyderabad        | Bangalore      | vinil  | 23  | vinilvishwanth@gmail.com | 9100260674 | vinilupi              |

