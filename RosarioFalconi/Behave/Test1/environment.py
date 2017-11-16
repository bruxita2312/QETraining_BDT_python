def before_feature(context, feature):
  if 'CRUD' in feature.tags:
     print("-----------------feature of CRUD------------------------")

def before_scenario(context, scenario):
   if 'scenario_send' in scenario.tags:
       print("----------------------scenario of scenario_send-------")
   else:
       print("----------------------not scenario of scenario_send-------")

def after_scenario(context, scenario):
   if 'withdraw fixed amount' in scenario.name:
       print("----------------------scenario name is  withdraw fixed amount-------")


def before_all(context):
   print("**************Before all ***********")

def after_all(context):
   print("**************after all ***********")
