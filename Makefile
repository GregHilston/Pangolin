PYTHON=python3
PID=pangolin.pid

run:
	$(PYTHON) pangolin.py
start:
	$(PYTHON) pangolin.py > /dev/null 2>&1 & echo $$! > $(PID)
kill:
	kill $$(cat $(PID))
