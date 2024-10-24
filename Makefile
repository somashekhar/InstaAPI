.PHONY : install test

install:
	pip3 install -r requirements.txt

test:
	pytest --disable-warnings -v -s -x tests/test_users.py