# Steps to recreate what i did
1. In the console:
    * `take my_project`
    * `python3 -m venv venv`
    * `activate`
    * `pip3 install Flask`

This should allow you to run the Flask server in your virtual environment<br>

2. Navigate to ./venv/bin/activate and do the following:
    * near the bottom add `export FLASK_APP=(YOUR_APP_NAME).py`, ignore that the location is likely `../../app.py`, it just works
    * near the bottom add `export FLASK_DEBUG=1`
    * inside the `deactivate()` function, add `unset FLASK_APP`

When you run the venv `activate` you should be able to `echo $FLASK_APP` and see your app file <br>
When you run `deactivate` and run `echo $FLASK_APP` you should see no output <br>

3. create in the root an `app.py` file with the following code:
 ```   
    from flask import Flask
    app = Flask(__name__)
    #note that __name__ is two underscores on each side

    @app.route('/')

    def hello_world():
        return 'Hello, World!'
```

4. `flask run` inside your venv should now work, going to `http://127.0.0.1:5000/` you should see your Hello World message


5. We'll be using a PostgreSQL db, to do so we'll need a driver and an ORM, so we'll use psycopg2 and SQLAlchemy respectively<br>
    * In your Virtual Env (venv is active):
    * `pip3 install flask-sqlalchemy psycopg2`
    * `pip3 freeze --local > requirements.txt` this line saves dependencies to a .txt file for your future self

6. We'll need database access, so add these lines to your activate script (venv/bin/activate)
    *   ```
        export POSTGRES_URL="127.0.0.1:5432"
        export POSTGRES_USER="user"
        export POSTGRES_PW="dbpw"
        export POSTGRES_DB="test"
        ```
    * If you're not sure of these values, open up psql and type `\conninfo`


    save for later:
    ```
    def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

    # the values of those depend on your setup
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PW = get_env_variable("POSTGRES_PW")
    POSTGRES_DB = get_env_variable("POSTGRES_DB")
    ```