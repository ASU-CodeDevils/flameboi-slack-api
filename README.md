# Flamboi Slack API

Flameboi is CodeDevils's Slack API bot that posts interactive messages and offers commands to users on CodeDevils' Slack.

## How to Install

### 1) (Optional) Install Virtualenv

This is an optional step, but is reccomended to keep your local Python dependency versions separate from Flamboi's. With many Python projects, bugs can exist in apps when versions of the same dependencies are shared globally across your code repos.

#### Linux

##### Install package

`sudo apt-get install python-virtualenv`

##### Activate easy installation scirpt

`sudo easy_install virtualenv`

##### Install pip Virtualenv

`sudo pip install virtualenv`

##### Ensure Virtualenv is Installed

Ensure Virtualenv is installed by calling `virtualenv`

> If virtualenv appears to not be installed, ensure that it is on your path. You can do this by adding the installation foler to the PATH variable within your profile. An example would be within ~/.bash_profile or ~/.bashrc, adding `PATH=$PATH:~/.local/bin`.
>
> Start an issue or post a question in CodeDevils Slack for further help in adding virtualenv to your path variable.

##### Create a directory

This directory will be used to house the enviroments on your machine. You can name this anything, and place it anywhere, for the purposes of this README it will be **~/virtualenvs/**.

1. `mkdir ~/virtualenvs`

##### Create Your Enviroment

You can name this anything and place it anywhere, but for this README it will be **flameboi-slack-api**.

1. `virtualenv ~/virtualenvs/flameboi-slack-api`

##### Activate Your Enviroment

Do this by calling the `activate` file/script within your newly created vitualenv directory's bin/ directory.

1. `source ~/virtualenvs/flameboi-slack-api/bin/activate`

#### Windows

> WIP

### 2) Install Dependencies

If you are using a virtual enviroment, *ensure that you have activated your enviroment*. You will know if the name of the virtualenv directory is written prior to other text within your shell.

1. `cd /path/to/flameboi`
1. `pip3 install -r requirements.txt`

## Further Reading and Documentation

### Slack Documentation

- [Getting started with Slack apps](https://api.slack.com/slack-apps)
- [Slack Events API documentation](https://api.slack.com/events)
- [Slack Web API documentation](https://api.slack.com/web)

### Documentation for Primary Tools

- [virtualenv](https://virtualenv.pypa.io/en/latest/userguide/) - virtual Python developement environment
- [flask](http://flask.pocoo.org/) - Python web application framework
- [python-slackclient](http://python-slackclient.readthedocs.io/en/latest/) - Python Slack API library

### Documentation for Other Helpful Tools

- [slackeventsapi](https://github.com/ASU-CodeDevils/flameboi-slack-api) - All in one SlackAPI Library used in connectiontester.py
- [ngrok](https://ngrok.com/docs) - Utility to expose a local webserver to the internet
- [postman](https://www.getpostman.com/docs/) - Utility used to design, build, and test APIs
- [Markdown CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) - For Pierson :troll:
- [CodeDevils](https://codedevils.org) - This is us!

# Contributing
Please see CONTRIBUTING.md for information.

# Quality of Code
Please see CONTRIBUTING.md for information.
