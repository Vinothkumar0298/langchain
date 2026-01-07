import re
import time
from typing import Any

from langchain_core.tools import tool
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

from com.learnings.agent.tools import browser_handler


def _wait_for_element_to_displayed(driver, xpath: str):
    for _ in range(10):
        if len(driver.find_elements(By.XPATH, xpath)) < 0:
            time.sleep(5)
        else:
            break


def valid_xpath_format(xpath: str):
    XPATH_SANITY_REGEX = re.compile(
        r"""
        ^(
            /{1,2}                                    # / or //
            ([a-zA-Z_][\w\-\.:]*)|\*                  # node name or *
        )
        (
            (                                        # repeated steps
                /([a-zA-Z_][\w\-\.:]*|\*)
                (\[
                    [^\[\]]+                         # simple predicate
                \])*
            )
        )*
        $
        """,
        re.VERBOSE
    )

    return bool(XPATH_SANITY_REGEX.match(xpath))


@tool
def launch_browser(url: str):
    """Lunch web browser"""
    driver = browser_handler.browser_handler.get_driver()
    driver.get(url)

    return "Browser launch successfully"


@tool
def click_element(xpath: str) -> str:
    """Click the element"""
    if valid_xpath_format(xpath):
        return f"invalid xpath format :: {xpath}"
    driver = browser_handler.browser_handler.get_driver()
    _wait_for_element_to_displayed(driver, xpath)
    try:
        driver.find_element(By.XPATH, xpath).click()
    except:
        return "Element is not clickable"
    return "Element clicked successfully"


@tool
def close_browser():
    """close browser"""
    driver = browser_handler.browser_handler.get_driver()
    try:
        driver.close()
    except:
        return "Browser is not closed"
    browser_handler.browser_handler.close_driver()
    return "Browser closed successfully"


@tool
def enter_text_value(xpath: str, txt_input: str):
    """enter the value into text field"""
    if valid_xpath_format(xpath):
        return f"invalid xpath format :: {xpath}"
    driver = browser_handler.browser_handler.get_driver()
    _wait_for_element_to_displayed(driver, xpath)
    try:
        driver.find_element(By.XPATH, xpath).send_keys(txt_input)
    except:
        return "Value is not entered"
    return "Value entered successfully"


@tool
def wait_for_element_to_displayed(xpath: str):
    """wait for element to displayed"""
    if valid_xpath_format(xpath):
        return f"invalid xpath format :: {xpath}"
    driver = browser_handler.browser_handler.get_driver()
    _wait_for_element_to_displayed(driver, xpath)
    return "waited for the element to displayed"


@tool
def get_text(xpath: str):
    """get text from element"""
    if valid_xpath_format(xpath):
        return f"invalid xpath format :: {xpath}"
    driver = browser_handler.browser_handler.get_driver()
    _wait_for_element_to_displayed(driver, xpath)
    return driver.find_element(By.XPATH, xpath).text


@tool
def get_page_source():
    """get page source"""
    driver = browser_handler.browser_handler.get_driver()
    return driver.page_source
