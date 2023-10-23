Feature: SANS Navigation

  Scenario: Navigate to the Full Course List - Scenario 1
    Given I am on the SANS homepage
    When I navigate the header menu to "Train and Certify" > "Courses" > "Full Course List"
    Then I should be on the "Cybersecurity Courses & Certifications" page

  Scenario:  Search Field Functionality - Scenario 2
    Given I am on the "Cybersecurity Courses & Certifications" page
    When I type “SEC504” into the “Enter a course name or other keyword” field
    And I press "Enter"
    Then results should be relevant
    When I clear the search parameter by clicking "X"
    And I type "cyber security"
    And I hit "Enter"
    Then results should be relevant to search

    # Test Plan for SANS Website Search Feature

# 1. Test Empty Search
# - Enter an empty search query and verify the system's response.

# 2. Test Search with Special Characters
# - Enter search queries containing special characters (e.g., &, $, !) and verify the results.

# 3. Test Search with Various Keyword Lengths
# - Enter short, medium, and long search queries to test how the system handles different input lengths.

# 4. Test Search with Multiple Keywords
# - Enter multiple keywords and verify that the search returns results relevant to all keywords.

# 5. Test Case Sensitivity
# - Test the search feature with keywords in different cases (e.g., "security," "Security," "SECURITY") to check for case sensitivity.

# 6. Test Search with Stop Words
# - Test with search queries containing common stop words ("a", "an", "the", "but", etc) and ensure they are handled correctly.

# 7. Test Search Auto-Suggestions
# - Check if the search auto-suggestions are relevant and functioning as expected.

# 8. Test Searching While Filters Applied
# - Apply filters to the search results and verify that search with filters returns relevant results.

# 9. Test Advanced Search Options - Out of Scope
# - If advanced search options are available, test that they work correctly.

# 10. Test Pagination of Search Results
# - If search results span multiple pages, verify that pagination works, and results are accurate on each page.


  Scenario: Filters Functionality - Scenario 3
    Given I am on the "Cybersecurity Courses & Certifications" page
    When I select "Cloud Security" and "New to Cyber" in the "Filters:" menu
    Then results should be relevant to filters

# Test Plan: SANS Website Filter Functionality

# Objective:
# The objective of this test plan is to thoroughly test the filtering functionality on the SANS website to ensure it works as expected.

# Test Scope:
# Testing the filtering functionality using Focus Areas, Skill Levels, Status and Training Formats check boxes.
# Verifying that filtered results in the right pane match the selected filter criteria.
# Evaluating the system's performance under different filter combinations.

# Test Scenarios:

# 1. Individual Filter Testing:
#    For each available filter, select it individually.
#    Verify that the displayed results match the selected filter.

# 2. Combination Filters:
#    Test various combinations of filters (e.g., Focus Area, Skill Level, Status, etc.).
#    Verify that results accurately reflect the combined filter criteria.

# 3. Performance and Scalability:
#    Evaluate system performance when handling multiple filter selections.
#    Measure response times and system stability under varying loads.

# 4. Negative Testing:
#    Test edge cases and invalid combinations to ensure the system handles them gracefully.
#    Verify that the system provides meaningful error messages for invalid filter combinations.

# Test Data:
# Prepare a list of valid filter combinations.
# Create data sets for performance testing with different filter combinations.

# Assertions:
# Verify that filtered results match the selected filter criteria.
# Ensure that the number of results displayed is consistent with the filters applied.
# Check that no unexpected errors or issues occur during filtering.

# Test Plan Comments:
# Due to the extensive number of possible filter combinations, it's essential to create a structured test data set that covers a representative sample of scenarios.
# Focus on testing common use cases and critical paths, such as selecting one filter, multiple filters, and filter combinations that should not work together.
# Perform scalability and performance testing to assess system response under varying loads.