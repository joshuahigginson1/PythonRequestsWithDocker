# Python Requests With Docker

**bwarks** A micro-serviced application to generate a random animal, and return their 'noise!' **/bwarks**

This task is a challenge set by Luke Benson of QA Consulting. 

## The Task

Create and test two python web applications with the following properties:

Application 1:
- Runs on port 5000
- Home page with a link which takes you to a 'generate' page.
- The generate page makes a get request to application 2 for a given animal.

- Then then posts that animal to **another** route in application 2, which responds with the animal's noise.

-Both the animal and their noise then need to be displayed on the web page.

Application 2 (API):
- Runs on port 5001.
- It must not display a web page.

- The **animal** route returns the name of an animal, in either text or json form.

- The **noise** route, which takes a given animal, and returns their noise in either text or json form.

Each application should have 100% unit test coverage.
Each application should be containerised.

Stretch Goal 1: Deploy your application over multiple VMs using Docker Swarm.
Stretch Goal 2: Add a database layer to your application.
Stretch Goal 3: Add integration testing to this app.

Hints:
Application 2 is your api, but you can't access it via http://localhost:5000. What do you need to change in order to access it through the docker network?

## Authors

Luke Benson of QA Consulting
Joshua Higginson of QA Consulting


