# Created by medvenyashaXD at 06-Oct-22
Feature: Test budget
  # Enter feature description here

  Scenario: Setting a budget and changing it
    Given Setting a budget
    When Budget expense
    When Budget income
    Then Result: The budget has changed
