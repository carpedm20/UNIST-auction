init:
	find ./ -name "migrations" -exec rm -rf {} \;
	rm db.sqlite3
	python ./manage.py syncdb
	python ./testcase.py

workon:
	workon comment

freeze:
	pip freeze > requirements.txt

heroku:
	# heroku config:set DJANGO_SETTINGS_MODULE=auction.settings
	git push heroku master
	heroku ps
	heroku open
	# heroku logs --app pam
