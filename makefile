test:
	python3 tests.py

generate:
    if [[ `git st -s` > /dev/null ]]; then
        python3 generate.py
        git add site
    fi
