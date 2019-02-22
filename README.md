# discordbots
discord bots

To work in this repo, make sure you have a `venv` folder up and running in the root directory. If not, run:
```
virtualenv -p `which python3` venv
```

This will install a local python3 instance using the python3 you have installed.If

After that, always activate the virtual environment by entering the command (in the root directory):
```
source venv/bin/activate
```

You will see a `(venv)` prepended to your terminal input, denoting it is activated.activate

After that, everytime you install a module using `pip`, it will install it in the local venv instance. 

IMPORTANT: If you are using the local venv Python instance, you use it using `python ...` **NOT** `python3 ...` because now the Python version inside the venv instance is bound to the alias `python` which is the version it was installed as (in our case 3.6.5). Same thing goes for `pip`, you use it as `pip` inside the activated venv and not `pip3` (how you would normally if using your system wide install).

To install the required packages inside your `requirements.txt`, simply run (once):
```
pip install -r requirements.txt
```

And that's it!

Whenever you need to come back and work on your project, to activate venv and start Togepi, simply write in terminal:
```
source start.sh
```

To easily work on your Python project locally and not having to replace the tokens all the time, you could use a module that takes care of that for you. This is what the `.env` file does. Make sure never to push that onto GitHub (make sure it's in your `.gitignore` along with the `venv` folder cause you don't want to push that).

