from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class browser_handler:
    service = None
    driver = None

    @staticmethod
    def get_driver() -> webdriver:
        if browser_handler.driver is None:
            browser_handler.driver = webdriver.Chrome(service=Service(
                executable_path="C:\\miniproject\\genai\langchain\\1_langchain_crash_course\\RestaurantNameGenerator"
                                "\\drivers\\chromedriver.exe"))

        return browser_handler.driver

    @staticmethod
    def close_driver() -> webdriver:
        #browser_handler.driver.close();

        browser_handler.driver = None
        return browser_handler.driver
