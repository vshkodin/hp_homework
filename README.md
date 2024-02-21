# hp_homework

## UI Testing Framework

Bug report can be found [HERE](documents/Bug_report_02_20_24.pdf):

## DEMO
![DEMO](documents/2024-02-21.gif)

## Overview  

The UI Python - Selenium Testing Framework crafted to test UI of https://github.com/ocrfin/qa_homework project. This documentation aims to provide comprehensive instructions on the installation, execution, and effective utilization of the framework.  

## Installation

Ensure that you have Python3.11 and latest Chrome browser installed on your machine.
Clone the repository and install the required dependencies using the following commands:

```bash

git clone https://github.com/vshkodin/hp_homework.git
cd hp_homework
python3 -m pip install virtualenv
virtualenv env

# MAC
source env/bin/activate
# WIN
env/Scripts/activate

python3 -m pip install -r requirements.txt

# Need to have allure for cool reports but this is optional 
# MAC
brew install allure
# WIN
scoop install allure

```

### Run locally

```
# service has to run on http://localhost:3000/
curl -I http://localhost:3000/ 2>/dev/null | head -n 1 | cut -d$' ' -f2
# has to return 200, if so we are ok to run 
pytest --local

```


### See Test Report
```commandline
allure serve allure-results 
```


 
## Folder Structure

- `hp_homework/`
- - `documents/`
    - `Bug_report_02_20_24.pdf`: 02/20/24 Bug report
  - `holistiplan/`:
    - `pages/signup.py`: signup page Object (class).
    - `pages/base.py`: base page Object (class).
    - `pages/login_logout.py`: login_logout page Object (class).
    - `pages/home.py`: home page Object (class).
    - `pages/profile.py`: profile page Object (class).
    - `pages/about.py`: placeholder 
  - `tests/`: Includes API test suites.
  - `.gitignore`: Specifies intentionally untracked files to be ignored by Git.
  - `config.json`: config file for tests setup.
  - `conftest.py`: Configuration file for pytest, used for fixtures and plugins.
  - `pytest.ini`: Configuration file for pytest.
  - `README.md`: Documentation file providing information about the UI testing framework.
  - `requirements.txt`: Lists the required Python packages and their versions.

  
## Contribution Guidelines 


Feel free to explore the framework, run tests, and contribute to its development. To contribute: 


1. Fork the repository. 

2. Create a new branch for your feature or bug fix. 

3. Make changes and ensure all tests pass. 

4. Submit a pull request. 

  

If you encounter any issues or have suggestions, please refer to Vladimir Shkodin https://github.com/vshkodin or https://vshkodin.com/ or mailto:v.s.shkodin@gmail.com.