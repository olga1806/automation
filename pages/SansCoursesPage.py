from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SansCoursesPage:
    def __init__(self, driver):
        self.driver = driver

    # Define locators
    SEARCH_FIELD = (By.XPATH, "//input[@placeholder='Enter a course name or other keyword']")
    CLEAR_SEARCH = (By.XPATH, "//input[@placeholder='Enter a course name or other keyword']/following-sibling::a[@alt='Clear filter']")
    FILTER_CLOUD_SECURITY = (By.XPATH, "//div[@class='filters-container closed']//div[@class='checkbox']/label[contains(text(), 'Cloud Security')]")
    FILTER_NEW_TO_CYBER = (By.XPATH, "//div[@class='filters-container closed']//div[@class='checkbox']/label[contains(text(), 'New to Cyber (200-399)')]")


    # Define methods to interact with the page elements
    def type_search_query(self, search_query):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(search_query)

    def press_enter(self):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(Keys.RETURN)

    def verify_search_results(self, expected_search_query):
        # Construct the XPath for search results based on the expected_search_query
        search_results_xpath = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f"//div[@class='main']//div[@class='title' and contains(text(), '{expected_search_query}')]")))

        # Retrieve the search results
        search_results = self.driver.find_elements(By.XPATH, search_results_xpath)

        # Verify that the text of each search result matches the expected query
        for result in search_results:
            result_text = result.text
            assert expected_search_query in result_text, f"Expected '{expected_search_query}' in result, but got '{result_text}'"
    def clear_search_parameter(self):
        clear_search_button = self.driver.find_element(*self.CLEAR_SEARCH)
        clear_search_button.click()

    def enter_search_keyword(self, keyword):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(keyword)

    def hit_enter(self):
        search_field = self.driver.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(Keys.RETURN)
    def select_cloud_security_filter(self):
        cloud_security_filter = self.driver.find_element(*self.FILTER_CLOUD_SECURITY)
        cloud_security_filter.click()

    def select_new_to_cyber_filter(self):
        new_to_cyber_filter = self.driver.find_element(*self.FILTER_NEW_TO_CYBER)
        new_to_cyber_filter.click()

    def verify_filter_results(self, expected_filters):
        # Construct the XPath for filter results based on the expected filters
        filter_results_xpath = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f"//div[@class='main']//div[@class='title' and contains(text(), '{expected_filters}')]")))

        # Retrieve the filter results
        filter_results = self.driver.find_elements(By.XPATH, filter_results_xpath)

        # Verify that the text of each filter result matches the expected filter criteria
        for result in filter_results:
            result_text = result.text
            assert any(expected_filter in result_text for expected_filter in expected_filters), f"Expected filter criteria not found in result: {expected_filters}"

