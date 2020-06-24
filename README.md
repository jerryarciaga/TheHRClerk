# TheHRClerk

![TheHRClerk Home Page](/images/thehrclerk_home_page.JPG)

## Overview
Welcome to TheHRClerk! For HR Professionals, managing personnel records can be daunting, tedious and repetitive. This project aims to automate low-level tasks including, but not limited to updating trackers, filling out forms, generating templates and creating certificates.

## Getting Started
### Required Software
* <a href='https://python.org'>Python 3</a> with pip installed
* <a href='https://pypi.org/project/virtualenv/'>Virtualenv</a>

### Setup
#### Setting up the Environment
* Start by cloning this repository: `git clone https://github.com/jerryarciaga/TheHRClerk`
* Move to the location of the repository: `cd TheHRClerk`
* Open up a terminal/powershell, then create a virtual environment for the project using:<br>
`virtualenv -p python3 virtualenv`<br>You can also replace python3 with the path to the Python 3 application
* Activate the virtual environment:<br>
  * For Windows: `.\virtualenv\Scripts\activate\`
  * For MacOS/Linux/Unix: `source virtualenv/source/activate`
* Installed the required dependencies: `pip install -r requirements.txt`
* Create an admin account by running `python manage.py createsuperuser` and following the prompts.
* To migrate data to your database, run `python manage.py migrate`
* Once activated, run the server by executing the `runserver` command from `manage.py`:<br>
  `python manage.py runserver`
* If no errors are encountered, open up a web browser and go to the following available url:
  * localhost:8000

## Contribution
Please feel free to contribute either through pull requests or feedback. I would appreciate any comments and insights to improve my project and my skills.

## Disclaimer
This project is unofficial.
