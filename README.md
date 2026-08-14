# Introduction 

TODO: This Project assigmnet is to built basic flask application 

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

Project: Basic Flask Application
What you need to build: A Python fi le that runs a local web server with two working endpoints.

Endpoint                       Expected Response
/                              Welcome to the App
/                              health
App is running
How to verify your work: Visit http://localhost:5000/ and http://localhost:5000/health in your browser. Both should show the correct text.

Project: A Flask-based in-memory password manager with three REST endpoints.

Endpoints implemented:

POST /add — Accepts a JSON body (username, password), validates the fields exist, and stores them in an in-memory Python dictionary. 
Returns 201 on success, 400 if the body is missing required fields.
GET /get/<username> — Looks up a username in the dictionary. Returns the password with 200 if found, or a 404 error if not.
DELETE /delete/<username> — Removes a username's record from the dictionary. Returns 200 with a confirmation message if deleted, or 404 if the username doesn't exist.