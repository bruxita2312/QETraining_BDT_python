@given(u'I have {zipcode:d} in my address')
def step_impl(context, zipcode):
    a_zipcode=76228
    #raise NotImplementedError(u' STEP: Given : I have (zipcode:d) in my address')

@given(u'The {country:w} as residence')
def step_impl(context,country):
    a_country="France"
    #raise NotImplementedError(u' STEP: The (country:D) is their residence')

@given(u'The actual number of habitants is {nro:n}')
def step_impl(context,nro):
    a_nro=250.000
    #raise NotImplementedError(u'STEP: The actual number of habitants is (nro:n)')
