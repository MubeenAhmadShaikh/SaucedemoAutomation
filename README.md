
# Saucedemo Automation

The saucedemo.com website is a popular demo e-commerce platform developed by saucelabs where users can browse and purchase various products. To ensure the functionality and reliability of this website, it is essential to perform automated testing. This project aims to automate testing for saucedemo.com using Python, Selenium, Pytest, and the Page Objects Model. The project will include a range of features such as Data-Driven Tests, Cross-Browser Tests, Negative Tests, Logging Functionality and Report Generation using Allure Reports.

## Run Locally

Clone the project

```bash
git clone https://github.com/MubeenAhmadShaikh/SaucedemoAutomation
```

Go to the project directory

```bash
cd SaucedemoAutomation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Navigate to tests directory
```bash
cd tests
```

Run all the tests

```bash
pytest -s -v
```


## Details for running the tests in Command line

#### navigate to the tests directory
```bash
cd tests
```
#### Run the tests using following command
```bash
pytest test_filename.py -s -v -m "marker_name" --browser_name=firefox --html=path_to_save_report/report.html
```

| Parameter | Option     | Description                |
| :-------- |:-----------| :------------------------- |
| `pytest` | `required` | Pytest command to run the tests from terminal |
| `test_filename.py` | `optional` | To run the tests from specific file if not provided all the files with 'test_' or '_test' will be considered |
| `-s` | `optional` | for displaying console logs|
| `-v` | `optional` | for displaying additional details |
| `-m "marker_name"` | `optional` | To run the customised markers \| **Accepted values**: [positive, negative]|
| `--browser_name="browser_name"` | `optional` | To select the browser at run time  \| **Accepted values** : [ch, ff, chrome, firefox, Chrome, Firefox]|
| `--html="Path/file_name.html"` | `optional` | To generate the html report at given path  |



## Features

- Cross-browser Testing
- Page Object Models
- HTML Reporting
- Data logging
- Data driven tests 
- End-to-end tests 
- Negative Testing 


## Developed using

- Python
- Selenium
- PyTest
- Allure Reports
- PyCharm

## 🛠 Skills

`Python` `JavaScript` `HTML&CSS` `Selenium` `Automation Testing` `API Testing` `Cloud Testing` `AWS` `Postman API Testing` `RESTapi` `Jenkins` `JIRA` `Database` `SQL` `MySql` `FastAPI` `Agile` `Scrum` `Project Management` 

