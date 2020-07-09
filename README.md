# five-gents-trivial-purfuit
Johns Hopkins Summer 2020 Foundations Of Software Engineering Group Project

## Development Setup
When developing, we should all be in a virtualenv to ensure pip always has the correct dependencies.

### Requirements
- python3.7
- pip 20.1.1

### Setup
```shell script
git clone https://github.com/mattladany/five-gents-trivial-purfuit.git
cd five-gents-trivial-purfuit
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Exit virtualenv
```shell script
deactivate
```

### Reactivate virtualenv
```shell script
source venv/bin/activate
```

## Q/A Database
To Run the unit test class, from the project's root directory:

```shell script
python -m Trivial_Purfuit.test.qa_database.test_question_manager
```