# Convention Administration Project


#####Project that allows creation, alteration, visualization and deletion of profiles and convention rooms.



This project used some technologies built for python. 

* **SQLAlchemy**

* **Flask**

* **Pytest**




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
 
 ## Create Conventions
 
 **URL** 
 
 * **Method:** `POST` : http://127.0.0.1:5000/conventions
 
 #### URL Params

  * **Required:**
  
    
   `name=[string]`
   
   
   `capacity=[integer]`
   
   
   `id=[string] - automatically generated id`
 ##### Example Json:
 ```
    {

        "name":"Great Room",

        "capacity": 100

    }
```
 * **Success Response:**

  * **Code:** 201 <br />
  
    **Content:** 
    
    
        {
        
        "capacity": 100,
        "id": "57c4630a-cde4-4204-8532-9c91ee773048",
        "name": "Great Room"
        
        }
 
 Exemplo `GET` at Postman:
 
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