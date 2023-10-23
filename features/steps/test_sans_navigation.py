from behave import step
from POMTests.pages.SansMainPage import SansMainPage
from POMTests.pages.SansCoursesPage import SansCoursesPage

# 1st scenario
@step('I am on the SANS homepage')
def sans_homepage(context):
    context.driver.get('https://www.sans.org')

@step('I navigate the header menu to "Train and Certify" > "Courses" > "Full Course List"')
def navigate_to_full_course_list(context):
    page = SansMainPage(context.driver)
    page.navigate_to_course_list()

@step('I should be on the "{expected_url}" page')
def verify_webpage_loaded(context, expected_url):
    page = SansMainPage(context.driver)
    page.verify_page_loaded(expected_url)

# 2nd scenario
@step('I type “{search_query}” into the “Enter a course name or other keyword” field')
def enter_search_query(context, search_query):
    page = SansCoursesPage(context.driver)
    page.type_search_query(search_query)

@step('I press "Enter"')
def press_enter(context):
    page = SansCoursesPage(context.driver)
    page.press_enter()

@step('results should be relevant')
def verify_search_results(context):
    page = SansCoursesPage(context.driver)
    page.verify_search_results("SEC504")

@step('I clear the search parameter by clicking "X"')
def clear_search_parameter(context):
    page = SansCoursesPage(context.driver)
    page.clear_search_parameter()

@step('I type "cyber security"')
def enter_cyber_security(context):
    page = SansCoursesPage(context.driver)
    page.enter_search_keyword("cyber security")

@step('I hit "Enter"')
def hit_enter(context):
    page = SansCoursesPage(context.driver)
    page.hit_enter()

@step('results should be relevant to search')
def verify_results_relevant(context):
    page = SansCoursesPage(context.driver)
    page.verify_search_results("cyber security")

# 3rd scenario
@step('I am on the "Cybersecurity Courses & Certifications" page')
def cybersecurity_courses_page(context):
    context.driver.get('https://www.sans.org/cyber-security-courses/?per-page=10')

@step('I select "{filter_1}" and "{filter_2}" in the "Filters:" menu')
def select_filters(context, filter_1, filter_2):
    page = SansCoursesPage(context.driver)
    page.select_cloud_security_filter()
    page.select_new_to_cyber_filter()

@step('results should be relevant to filters')
def verify_filter_results(context):
    expected_filters = ["Introduction", "Cloud", "Security"]
    page = SansCoursesPage(context.driver)
    page.verify_filter_results(expected_filters)