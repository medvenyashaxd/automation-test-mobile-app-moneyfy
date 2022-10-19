# Created by medvenyashaXD at 04-Oct-22
Feature: Test setting
  # Enter feature description here
  Background: Being on the main page of the application
    Given Tap on three dots at the top right of the screen and tap setting or swipe to bring up the menu

  Scenario: Set language, night mode, currency, week, month
    When The light theme should change to dark
    When The language should change to russian
    When Set currency BYN
    When Set first day of week value
    When Set start month
    Then Result: changed settings language, night mode, currency, week and month
