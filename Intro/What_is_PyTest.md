# How to write pytest testcase ? 
* Organize testcase in test package
* pytest only collect and execute when the file names starting with **test_** or **_test**
    * **Ex1 :** test_demo.py
    * **Ex2 :** demo_test.py
* Use pytest **Assert** to validate the testcase     
* Pytest assertions are checks that return either True or False status

### pytest assert syntax
**assert <condition_for_verification>, "message on failure to displayed "**
* **Ex1 :** assert 404==404 #is a successful assertion
  * Assertion is passed 
* **Ex2 :** assert 404==404, "Number validation mismatch" #assertion with message on failure
  * Assertion is passed and no message failure is displayed
* **Ex3 :** assert 404==405 #is a failed assertion
  * Assertion is failed and no message failure is displayed
* **Ex5 :** assert 404==405, "Number validation mismatch" #is a failed assertion
  * Assertion is failed and message failure is displayed



### How to create Package
* Create a new folder <folder_name>
* Create an empty __init__.py file in the <folder_name> folder


### Reference URL :-  
* https://docs.pytest.org/en/latest/how-to/plugins.html

>By<br/>
**Thiness Babu**<br/>
Automation Quality Engineer<br/>
https://github.com/thinessGit/ <br/>
