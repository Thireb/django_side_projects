# Readme for the project

blog/urls contains the urls for the project, being

- index at '/'
- detail at 'post/{number}'
- new-form at 'form'
- update at 'update'
- delete at 'delete'
- update at 'post/{number}/update'
- feedback at 'feedback'
- feedback Post at 'post/{number}/feedback

If running this project on local machine, then uncomment the STATICFILES_DIRS in the djangogirls/settings.py file.

Make sure you have django installed in your system or virtual enviornment, and run the project in the manage.py directory, using "python manage.py runserver".
Make sure to do the migrations before hand and add some data using django admin panel.
Have fun.
