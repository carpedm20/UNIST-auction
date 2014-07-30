init:
	find ./ -name "migrations" -exec rm -rf {} \;
	rm db.sqlite3
	python ./manage.py syncdb
	python ./testcase.py

workon:
	workon comment
