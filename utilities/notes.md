**_Python notes_**
Using request.session() to not repeat same code (as auth headers?), personally do not like it
```
se = request.session()
se.auth = auth = ('user', 'password')
```
To send Cookies with an http request in python
```
cookie = { 'cookie_name' : 'value'}
request.get('http://something', cookies = cookie, allow_redirect=False, timeout=1 )
```
**_It will show if there was  a redirection_**
`response.history`

**_To add another cookie to the session_**
```
se.cookies.update({ "key": "value"})
res = se.get('http://something', cookies={"key2", "value2"})
```

**_Attachments_**
```
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r= requests.post(url,files=files)
print(r.status_code)
print(r.text)
```
**_Cucumber in python_**
https://behave.readthedocs.io/en/stable/behave.html#
`pip install behave`

`behave --no-capture` # To run tests with ALL stdout

`behave --tags=smoke`

`pip install allure-behave`

**_This curl should work and is not working_**
```
curl https://github.com/allure-framework/allure2/releases/download/2.19.0/allure-2.19.0.zip -o allure-2.19.0.zip
unzip allure-2.19.0.zip -d allure-2.19.0

behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports
allure-2.19.0/allure-2.19.0/bin/allure serve reports

allure serve reports
behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
allure serve %allure_result_folder%
```
`pip freeze > requirements.txt`

`pip install -r requirements.txt`
