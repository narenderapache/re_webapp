from flask import Flask, g
import sqlite3
import os

DATABASE = "./database/name.db"

# Create app
app = Flask(__name__)

# check if the database exist, if not create the table and insert a few lines of data
if not os.path.exists(DATABASE):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name);")
    conn.commit()
    # Have used the {name} variable which need to be fetched from the db
    cur.execute("INSERT INTO users VALUES('Narender');")
    conn.commit()
    conn.close()


# helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# helper to close
@app.teardown_appcontext
def close_connection(ex):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    cur = get_db().cursor()
    # res = cur.execute("select * from users")
    res = cur.execute("select name from users")
    for record in res:
        # Get the {name} from the database entry as per the requirement
        return "Hello " + str(record[0])


if __name__ == "__main__":
    """
	Use python sqlite3 to create a local database, insert some basic data and then
	display the data using the flask templating.

	http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
    """
    app.run(host='0.0.0.0', port=80)
