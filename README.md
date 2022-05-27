Previus configure slack api:
https://api.slack.com/start/building/bolt-python#listening

on Terraform:

use it main.tf file

1- terraform plan

2- terraform apply


on Ubuntu:

1- apt-get install -y python3-venv

2- mkdir boltio

3- cd boltio

4- pip install slack_bolt


5- python3 -m venv .venv

6- source .venv/bin/activate

7- export SLACK_APP_TOKEN=[AWS TOKEN]

8- export SLACK_BOT_TOKEN=[AWS TOKEN]

9- python3 app.py
