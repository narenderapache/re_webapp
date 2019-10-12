**WebApp Exercise**
# **This code is only for the exercise purpose**
 
## Libraries used
- Flask - application module to serve application with end points
- Flask-SQLAlchemy - ORM module to handle DB responses -> Not used in the current implementation
- requests - to handle external requests -> Not used in the current implementation

## Technical nuances
 - **Flask:** It is one of the light weight easy to setup library to create rest api applications in a whip of time. It is reliable, quick to deploy and easy to setup.
 - **SQLite:** Needed a totally light weight easy to load and save backend. SQLite was or first choice. It is a file based system. As our requirement just involved only little amount of data we chose this.

### containerise the application using docker
- `docker build -t my-webapp .` -> build the app locally
- `docker run -d --name my-webapp -p 80:80  my-webapp:latest` -> to test the web app locally
- `curl localhost:80` or `localhost:80` on browser

### running integration tests
- integration tests are useful when we define the pipeline/stages for ci/cd -> Not part of this code






