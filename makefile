init:
	##############################
	# activating virtual envirment
	# conpulsory for procedding
	###############################
	. venv/bin/activate
run:
	##############################
	# run task 1 {a, b, c}
	###############################
	python src/main.py
	echo "the output is in ./data folder."
install:
	python setup.py bdist_wheel
