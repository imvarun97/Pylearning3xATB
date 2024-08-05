### How to run pyTest

- open terminal and enter pyTest to run
- To run specific files we can give absolute path `pytest .\Ex_02_July\test_Lab180.py`
- To run with pattern `meaning files that start with specific keyword -  pytest -k "18"`
- To run a specific marked test case 
  - Add annotation @pytest.regression
  - pytest -m "regression" M:\3xATB\Pylearning3xATB\Ex_02_July
  - Marking helps us to segregate testcases according to tests i.e. smoke, regression, sanity

### How to see the report of PyTest Testcases
- Run below command to crete allure pyTests `pytest M:\3xATB\Pylearning3xATB\Ex_02_July --alluredir=<Any folder name>`
- The allure reports are generated in the above folder
- Make sure that allure commandline is installed `npm install  -g npm allure-commandline`
- Download node.js - to check if node is installed or not `node -v`
- Then install allure commandline - `npm install  -g npm allure-commandline`
- Download java and configure path in env variables
- type `allure` to check if everything is set up - it will give all the options
- now to generate reports run - `allure serve <allure_result_foldername>`
- To view reports you need to have above command running
- The report will be stored under - ` C:\Users\varan\AppData\Local\Temp\18438650248756657668\allure-report`

### To use Requests module
- Requests module helps us to work with http methods
- pip install requests
- 