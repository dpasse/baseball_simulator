test:
	cd tests && pytest -v -s

freeze:
	pip freeze > requirements.txt
