features
	Scenarios
	Scenarios outline
steps
	*.py
		Actions
		Assertions > > compare library
environment.py >> hooks

config.yml


e.g.
behave -f plain --tags @any --summary --no-capture

AND >> scenario debe contener ambos tags
behave -f plain --tags @any --tags @some --summary --no-capture

OR
behave -f plain --tags @any,@some --summary --no-capture

NOT >> cuando hay un bug q no se fixeara
behave -f plain --tags @any --tags ~@some --summary --no-capture


