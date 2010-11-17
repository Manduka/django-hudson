INSTALLED_APPS = ('django.contrib.sessions', # just to enshure that dotted apps test works
                  'django_hudson',
                  'dummyapp',)
DATABASE_ENGINE = 'sqlite3'
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
