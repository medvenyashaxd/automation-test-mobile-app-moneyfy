# Created by medvenyashaXD at 04-Oct-22
Feature: Test setting
  # Enter feature description here

  Scenario: Language, night mode, currency, week, month setting
    Given Tap on three dots at the top right of the screen and tap setting or swipe to bring up the menu
    When The light theme should change to dark
    When The language should change to russian
    When Set currency byn
    When Set first day of week value
    When Set start month
    Then Result: changed settings language, night mode, currency, week and month
