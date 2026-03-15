.Phony: all setup clean run

all: setup
	@echo "Not done yet"

venv: 
	python -m venv ./$@

setup: venv
	source ./$</bin/activate && python -m pip install -r requirements.txt && deactivate

clean: venv
	rm -rf ./venv

run: setup
	echo '{"foo": "bar"}' | python src/main.py

