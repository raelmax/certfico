KQWAIT := $(shell command -v kqwait 2> /dev/null)

run:
	FLASK_APP=certifico FLASK_DEBUG=True flask run

setup:
	pip install -r requirements.txt

test:
	MONGODB_URI=mongodb://localhost:27017/certifico_testing_db python -m unittest

test_watch:
ifdef KQWAIT
	while true; do kqwait tests; make test; done
else
	@echo "You need kqwait installed to run this command. :/"
endif
