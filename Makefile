update:
	poetry update

requirements.txt:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: requirements.txt