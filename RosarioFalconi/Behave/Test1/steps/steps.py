@given(u': I have $(amount:d) in my account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given : I have $(amount) in my account')

@given(u'I have a wallet')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a wallet')

@when(u': I need to save my money')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : I need to save my money')


