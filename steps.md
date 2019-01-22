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

    
    