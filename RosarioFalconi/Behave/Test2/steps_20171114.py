from compare import expect

@given(u'yo tengo  ${balance:d} in my account')
def step_impl(context,balance):
   context.balance=int(balance)

@when(u'I Choose to withdraw the fixed amount of ${withdraw:d}')
def step_impl(context,withdraw):
   context.withdraw=int(withdraw)

@then(u'I should receive ${cash:d} cash')
def step_impl(context,cash):
   print ("This is your $",cash)


@then(u'the balance of my account should be ${balance:d}')
def step_impl(context,balance):
   remaing=context.balance-context.withdraw
   expect (remaing).to_equal(int(balance))
