# __author__ = 'Udit Gupta'

import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from settings import logger


class SeleniumAdaptor:
    CLEAR_TEXTBOX = 1
    INSERT_TEXTBOX = 2
    SELECT_VALUE_SELECT_BOX = 3
    CLICK = 4
    ELEMENT_DISPLAY = 5
    event_type = {
        1: 'CLEAR_TEXTBOX',
        2: 'INSERT_TEXTBOX',
        3: 'SELECT_VALUE_SELECT_BOX',
        4: 'CLICK',
        5: 'ELEMENT_DISPLAY',

    }

    def __init__(self, download_directory=None, **kwargs):
        self.options = Options()
        # running chrome as headless
        if kwargs.get('headless_browser'):
            self.options.add_argument("headless")
        if kwargs.get('start_maximized'):
            self.options.add_argument("start-maximized")
        if kwargs.get('incognito'):
            self.options.add_argument("incognito")
        if download_directory:
            preferences = {"download.default_directory": download_directory,
                           "directory_upgrade": True,
                           "download.prompt_for_download": False,
                           "safebrowsing.enabled": True,
                           'profile.default_content_setting_values.automatic_downloads': 1}
            self.options.add_experimental_option("prefs", preferences)
        self.driver = Chrome(executable_path='assets/chromedriver', chrome_options=self.options)

    def close_all(self):
        self.driver.quit()

    def close(self):
        self.driver.close()

    def trigger_event(self, event, element, value=None, tear_down=False, **kwargs):
        find_element = self.driver.find_element_by_id
        if kwargs.get('via_class'):
            find_element = self.driver.find_element_by_class_name

        logger.info(
            f"Selenium-Hitting (Event-{self.event_type.get(event)}) for (Element-{element}) with (Value-{value})")
        try:
            if event == self.CLEAR_TEXTBOX:
                find_element(element).clear()
            elif event == self.INSERT_TEXTBOX:
                find_element(element).send_keys(value)
            elif event == self.SELECT_VALUE_SELECT_BOX:
                Select(find_element(element)).select_by_value(value)
            elif event == self.CLICK:
                find_element(element).click()
            elif event == self.ELEMENT_DISPLAY:
                find_element(element).is_displayed()
        except StaleElementReferenceException:
            logger.info("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if event == self.CLEAR_TEXTBOX:
                find_element(element).clear()
            elif event == self.INSERT_TEXTBOX:
                find_element(element).send_keys(value)
            elif event == self.SELECT_VALUE_SELECT_BOX:
                Select(find_element(element)).select_by_value(value)
            elif event == self.CLICK:
                find_element(element).click()
            elif event == self.ELEMENT_DISPLAY:
                find_element(element).is_displayed()
        except Exception as e:
            logger.info(
                f"Selenium-Hitting (Error-{str(e)}) Event-{self.event_type.get(event)})"
                f" for (Element-{element}) with (Value-{value})")
        if tear_down:
            self.close_all()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert()
        alert_text = alert.text
        return alert_text

    def wait_for_select_event_completion(self, element_id, is_selected=False):

        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_located_selection_state_to_be(
                (By.ID, element_id), is_selected=is_selected)
        )

    def wait_for_event_completion(self, expected_conditions_type, by_lookup, element, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions_type(
                (by_lookup, element))
        )

    @staticmethod
    def wait(time_to_wait):
        time.sleep(time_to_wait)

    @property
    def browser_cookies(self):
        return self.driver.get_cookies()
