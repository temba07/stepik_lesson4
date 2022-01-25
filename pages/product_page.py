from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import ProductPageLocators


class PageObject(BasePage):
    def go_to_basket(self):
        self.browser.find_element_by_css_selector("[class = 'btn btn-lg btn-primary btn-add-to-basket']").click()
        self.solve_quiz_and_get_code()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

