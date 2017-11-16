Scenario Outline: withdraw fixed amount
   Given I have <Balance> in my account
   When I choose to Withdraw the fixed amount of <Withdraw>
   then i should receive <Received> cash
       And the balance of my account should be <Remaining>
Examples: A
  | Balance         | Withdraw |Received   |Remaining  |
   | $500            | $50      |$50        | $450      |
   | $500            | $100      |$100        | $400      |
   | $500            | $200      |$200        | $300      |
Examples: b
  | Balance         | Withdraw |Received   |Remaining  |
   | $500            | $50      |$50        | $450      |
   | $500            | $100      |$100        | $400      |
   | $500            | $200      |$200        | $300      |
