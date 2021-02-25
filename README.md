# Convention Administration Project


Project that allows creation, alteration, visualization and deletion of profiles and convention rooms.

## Instalation

1º
Clone project on Github

![](app/utils/images/cloneGit.PNG?raw=true)

2º
run on the IDE terminal: pip install --user pipenv 

3º 
run on the IDE terminal: pipenv install

4º
run on the IDE terminal: pipenv run flask run

![](app/utils/images/runApp.PNG?raw=true)


## Run API

Documentation Postman:
https://documenter.getpostman.com/view/10706208/TWDcEZSP

**Method:**
`GET` | `POST` | `DELETE` | `PATCH`
 
``` 
  http://127.0.0.1:5000/profiles
 
  http://127.0.0.1:5000/conventions
 
  http://127.0.0.1:5000/coffee-room
```
 
 Exemplo:
 
 ![](app/utils/images/getConventions.PNG?raw=true)
 
 
 ### requirements
 * python 3.8
 * git 2.0
 * IDE python of your choice 
 
 ## Tests
 1º run on the IDE terminal: 
 
 **pipenv install --dev pytest-cov**
 
 2º run on the IDE terminal: 
 
 **pytest --cov=app/ --cov-report=html**
 
##### Result:



  ![](app/utils/images/tests.PNG?raw=true)