# Python Console Template #

## Features ##

* SQLAlchemy ORM with Postgres
* Alembic Database migration
* Application config file
* Logging
* Pytest Unit testing
* Shell scripts for common tasks

## Directories ##

alembic/            _Alembic migrations and support script_
logs/               _Application logs_
src/                _Source code for app_
   app/                _main application_
   db/                 _database and models_
   util/               _provides various utility functions_
   main.py             _main file to run_
   utility.py          _for performing maintenance tasks/ad-hoc test_
tests/              _unit tests for application_
alembic.ini         _alembic specific settings_
config.ini          _application config in use_
config.ini.example  _example of application config_
pytest.ini          _settings for pytest_
requirements.txt    _requirements for application_
run_pytest.sh       _simply run pytest_
setup_venv.sh       _sets up the virtual environment_
upgrade_database.sh _updates the database schema to definitions in models.py_ 




