.PHONY: download-data
download-data:
	mkdir -p data
	./download-data.sh > data/list.csv

.PHONY: setup-venv
setup-venv:
	pyenv local 3.12
	python -m venv venv
	pip install -r requirements.txt

.PHONY: generate-graphs
generate-graphs: setup-venv
	python timeline-activity-plotly.py
	python timeline-plotly.py

