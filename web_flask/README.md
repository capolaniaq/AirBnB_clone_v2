# 0x04. AirBnB clone - Web framework

By Guillaume, CTO at Holberton School

Author Carlos Andres Polania (capolaniaq@correo.udistrital.edu.co)

## Learning Objectives

-   What is a Web Framework
-   How to build a web framework with Flask
-   How to define routes in Flask
-   What is a route
-   How to handle variables in a route
-   What is a template
-   How to create a HTML response in Flask by using a template
-   How to create a dynamic template (loops, conditions…)
-   How to display in HTML data from a MySQL database

## Tasks
### 0. Hello Flask!
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
-   You must use the option  `strict_slashes=False`  in your route definition


### 1. HBNB

Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
-   You must use the option  `strict_slashes=False`  in your route definition


### 2. C is fun!
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ” followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
-   You must use the option  `strict_slashes=False`  in your route definition
### 3. Python is cool!
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
-   You must use the option  `strict_slashes=False`  in your route definition
### 4. Is it a number?
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
-   You must use the option  `strict_slashes=False`  in your route definition
### 5. Number template
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
    -   `/number_template/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`” inside the tag  `BODY`
-   You must use the option  `strict_slashes=False`  in your route definition

### 6. Odd or even?
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   Routes:
    -   `/`: display “Hello HBNB!”
    -   `/hbnb`: display “HBNB”
    -   `/c/<text>`: display “C ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
    -   `/python/(<text>)`: display “Python ”, followed by the value of the  `text`  variable (replace underscore  `_`  symbols with a space  )
        -   The default value of  `text`  is “is cool”
    -   `/number/<n>`: display “`n`  is a number”  **only**  if  `n`  is an integer
    -   `/number_template/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`” inside the tag  `BODY`
    -   `/number_odd_or_even/<n>`: display a HTML page  **only**  if  `n`  is an integer:
        -   `H1`  tag: “Number:  `n`  is  `even|odd`” inside the tag  `BODY`
-   You must use the option  `strict_slashes=False`  in your route definition

### 7. Improve engines
Before using Flask to display our HBNB data, you will need to update some part of our engine

### 8. List of states
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   After each request you must remove the current SQLAlchemy Session:
    -   Declare a method to handle  `@app.teardown_appcontext`
    -   Call in this method  `storage.close()`

### 9. Cities by states
Write a script that starts a Flask web application:

-   Your web application must be listening on  `0.0.0.0`, port  `5000`
-   You must use  `storage`  for fetching data from the storage engine (`FileStorage`  or  `DBStorage`) =>  `from models import storage`  and  `storage.all(...)`
-   To load all cities of a  `State`:
    -   If your storage engine is  `DBStorage`, you must use  `cities`  relationship
    -   Otherwise, use the public getter method  `cities`
    
### 10. States and State