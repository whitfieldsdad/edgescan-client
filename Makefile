default: update lock requirements.txt

update:
	poetry update

lock:
	poetry lock

requirements.txt:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

.PHONY: requirements.txt