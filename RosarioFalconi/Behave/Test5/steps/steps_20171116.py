from compare import expect
@given(u'I have ${balance:d} in my account')
def step_impl(context, balance):
   context.balance = int(balance)

@when(u'I choose to Withdraw the fixed amount of ${withdraw:d}')
def step_impl(context, withdraw):
   context.withdraw = int(withdraw)

@then(u'i should receive ${cash:d} cash')
def step_impl(context, cash):
   print("this is your $",cash)

@then(u'the balance of my account should be ${balance:d}')
def step_impl(context, balance):
   remaining = context.balance-context.withdraw
   expect(remaining).to_equal(int(balance))

####################################################################
@given(u': I have $(amount:d) in my account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given : I have $(amount) in my account')

@given(u'I have a wallet')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a wallet')

@when(u'I need to save my money')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : I need to save my money')
