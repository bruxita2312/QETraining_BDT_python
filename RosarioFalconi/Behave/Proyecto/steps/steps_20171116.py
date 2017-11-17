from behave import given, when, then
from compare import expect

@given(u'I have connection to "{host}"')
def step_impl(context,host,rootPath):
    expect(context.host).to_equal(host)

@given(u'on service "{rootPath}"')
def step_impl(context,rootPath):
    expect(context.rootPath).to_equal(rootPath)

@when(u'I sent {admin_token}')
def step_impl(context,admin_token):
    expect(context.admin_token).to_equal(admin_token)

@then(u'I receive user token "{usr_token}"')
def step_impl(context,usr_token):
    expect(context.usr_token).to_equal(usr_token)