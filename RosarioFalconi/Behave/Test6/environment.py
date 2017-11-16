import yaml

global generic_data
generic_data = yaml.load(open('Configuration/config.yml'))

def before_feature(context, feature):
  if 'CRUD' in feature.tags:
     print("-----------------feature of CRUD------------------------")

def before_scenario(context, scenario):
   if 'scenario_send' in scenario.tags:
       print("----------------------scenario of scenario_send-------")
   elif 'scenario_second' in scenario.tags:
       print("----------------------scenario of scenario_second-------")
   else:
       print("----------------------not scenario-------")

def before_all(context):
   print("**************Before all ***********")
   context.host= generic_data['host']
   context.method=generic_data['method']
   context.code = generic_data['code']
   print ('My host ', context.host, ' using method ', context.method)

def after_all(context):
   print("**************after all ***********")
