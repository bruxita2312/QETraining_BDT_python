@given(u': I have $(amount:d) in my account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given : I have $(amount) in my account')

@given(u'I have a wallet')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have a wallet')

@when(u': I need to save my money')
def step_impl(context):
    raise NotImplementedError(u'STEP: When : I need to save my money')

# 15-11-2017
@given(u'I login application')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I login application')

@when(u'I click on my User icon')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on my User icon')

@then(u'I see My Profile')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see My Profile')

@given(u'I select change password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I select change password')

@when(u'I save my new password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I save my new password')

@then(u'I should see confirmation message')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should see confirmation message')

@given(u'I select change picture')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I select change picture')

@when(u'I select a new image from my pc')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select a new image from my pc')

@then(u'I see new picture loaded')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see new picture loaded')

# Data table
@given(u'these Users')
def step_impl(context):
    for row in context.table:
        assert(True,row['name']==('Michael Jackson'))

@given(u'these Users')
def step_impl(context):
    for row in context.table:
        assert(True,('Michael Jackson' in row['name'])

@given(u'these Users')
def step_impl(context):
    for row in context.table:
        any.add.user['name'], row['date of birthday']

