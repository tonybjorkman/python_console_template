# Python Console Template #

## Features ##

* SQLAlchemy ORM with Postgres
* Alembic Database migration
* Application config file
* Logging
* Pytest Unit testing
* Shell scripts for common tasks

## Directories ##
File | &nbsp; | Description
--- | --- | ---
alembic/  | &nbsp; |        _Alembic migrations and support script_
logs/      | &nbsp; |       _Application logs_
src/       | &nbsp; |       _Source code for app_
&nbsp; |  app/   |    _main application_
 &nbsp; | db/     |     _database and models_
&nbsp; |  util/    |       _provides various utility functions_
 &nbsp; | main.py       |      _main file to run_
 &nbsp; | utility.py     |     _for performing maintenance tasks/ad-hoc test_
tests/  |   &nbsp;  |       _unit tests for application_
alembic.ini | &nbsp;  |      _alembic specific settings_
config.ini |  &nbsp;  |     _application config in use_
config.ini.example | &nbsp; | _example of application config_
pytest.ini    | &nbsp; |     _settings for pytest_
requirements.txt | &nbsp; |   _requirements for application_
run_pytest.sh  | &nbsp; |    _simply run pytest_
setup_venv.sh  | &nbsp; |    _sets up the virtual environment_
upgrade_database.sh | &nbsp; | _updates the database schema to definitions in models.py_ 




