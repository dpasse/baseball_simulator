test:
	cd tests && pytest -v -s

mypy:
	cd ./src && mypy ./ --ignore-missing-imports

freeze:
	pip freeze > requirements.txt
