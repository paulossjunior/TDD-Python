# Created by paulo at 22/03/16
# Código retirado do site http://code.tutsplus.com/tutorials/behavior-driven-development-in-python--net-26547
# Usando o framework behave ... no lugar do Lettuce
Feature: As a writer for NetTuts
  I wish to demonstrate
  How easy writing Acceptance Tests
  In Python really is

  Background:
    Given I am using the calculator

   Scenario: Calculate 2 plus 2 on our calculator
    Given I input 2 add 2
    Then I should see 4

   Scenario Outline: Calculate x plus y on our calculator
    Given I input <value_one> add <value_two>
    Then I should see <result>
    Examples: Values
    | value_one          | value_two | result|
    | 10                 | 20        | 30    |
    | 11                 | 20        | 31    |
    | 2                  | 2         | 4     |
