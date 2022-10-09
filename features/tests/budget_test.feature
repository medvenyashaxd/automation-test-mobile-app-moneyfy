# Created by medvenyashaXD at 06-Oct-22
Feature: Test budget
  # Enter feature description here
  Background: Setting a budget
    Given Setting a budget 1000

  Scenario: Budget change
    When Budget expense
    When Budget income
    Then Result: The budget has changed
