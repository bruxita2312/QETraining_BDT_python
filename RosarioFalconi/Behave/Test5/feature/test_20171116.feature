@CRUD
Feature: Withdraw fixed amount
the "Withdraw cash" menu contains several fixed amounts to speed up transactions for users.

@scenario_send
Scenario Outline: withdraw fixed amount
   Given I have <Balance> in my account
   When I choose to Withdraw the fixed amount of <Withdraw>
   Then i should receive <Received> cash
    And the balance of my account should be <Remaining>

  Examples: A
  | Balance         | Withdraw |Received   |Remaining  |
   | $500            | $50     |$50        | $450      |
   | $500            | $100    |$100       | $400      |
   | $500            | $200    |$200       | $300      |

  Examples: B
  | Balance         | Withdraw |Received   |Remaining  |
   | $500            | $50     |$50        | $450      |
   | $500            | $100    |$100       | $400      |
   | $500            | $200    |$200       | $300      |

@scenario_second
Scenario: Saving my money
    Given:  I have $ in my account
    And:  I have a wallet
    When:  I need to save my money
    Then: I will put my money in my wallet


