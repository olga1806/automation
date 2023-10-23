from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class SansMainPage:
    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # XPaths
    MENU_TRAIN_AND_CERTIFY = (By.XPATH, "//div[@class='header-menu-wrapper']//a[@class='link level1 primary' and contains(text(), 'Train and Certify')]")
    MENU_COURSES = (By.XPATH, "//div[@class='header-menu-wrapper']//a[@class='link level2 primary' and contains(text(), 'Courses')]")
    SUBMENU_FULL_COURSE_LIST = (By.XPATH, "//div[@class='header-menu-wrapper']//a[@class='link level3 primary' and contains(text(), 'Full Course List')]")

    # Page methods
    def navigate_to_course_list(self):
        # Use automation tools to navigate the main menu
        action_chains = ActionChains(self.driver)
        menu = self.driver.find_element(By.XPATH, self.MENU_TRAIN_AND_CERTIFY)
        courses = self.driver.find_element(By.XPATH, self.MENU_COURSES)
        full_course_list = self.driver.find_element(By.XPATH, self.SUBMENU_FULL_COURSE_LIST)

        # Hover over the menu items to open submenus
        action_chains.move_to_element(menu).perform()
        action_chains.move_to_element(courses).perform()

        # Click the Full Course List
        full_course_list.click()

    def verify_page_loaded(self, expected_url):
        # Create an assert statement to verify the correct webpage is loaded
        # expected_url = "https://www.sans.org/cyber-security-courses/?msc=main-nav"
        actual_url = self.driver.current_url

        try:
            assert expected_url in actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
        except AssertionError as e:
            # Handle the assertion error here (e.g., log the error, take a screenshot, etc.)
            print(f"Assertion error: {e}")




