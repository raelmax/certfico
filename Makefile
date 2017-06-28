run:
	FLASK_APP=certifico FLASK_DEBUG=True flask run

test:
	MONGODB_URI=mongodb://localhost:27017/certifico_testing_db python -m unittest
