# Flask-Intro-Ex
Exercises to practice the use of flask
## **Greet**

In the ***greet*** folder, Make a simple Flask app that responds to these routes with simple text messages:

***/welcome***   Returns “welcome”

***/welcome/home***   Returns “welcome home”

***/welcome/back***   Return “welcome back”
## **Calc**

Build a simple calculator with Flask, which uses URL query parameters to get the numbers to calculate with.

Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, ***a*** and ***b***, which will be passed in as URL GET-style query parameters.

***/add***   Adds ***a*** and ***b*** and returns result as the body.

***/sub***   Same, subtracting ***b*** from ***a***.

***/mult***   Same, multiplying ***a*** and ***b***.

***/div***   Same, dividing ***a*** by ***b***.

For example, a URL like ***http://localhost:5000/add?a=10&b=20*** should return a string response of exactly **30**.

Write the routes for this but **don’t hardcode the math operation in your route function** directly. Instead, we’ve provided helper functions for this in the file ***operations.py***:
## **Further Study**

You probably have a lot of code duplication in your ***calc*** routes, given that you’re doing such similar things in each.

Make a single route/view function that can deal with 4 different kinds of URLs:

- ***/math/add***
- ***/math/sub***
- ***/math/mult***
- ***/math/div***

You can write this in one function with one route by using a route parameter for the actual operation (“add”, “sub”, etc).
