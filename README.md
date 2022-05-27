### Slack API:

Previus configure slack api: [https://api.slack.com/start/building/bolt-python#listening](https://api.slack.com/start/building/bolt-python#listening)

### Terraform:
use main.tf file:

    https://github.com/nicosistemas/boltio/blob/6550c2b7e49f2f42c5cd656555fd73ba41676113/main.tf

`terraform plan`
`terraform apply`

### on Ubuntu Server:

1- `apt-get install -y python3-venv`

2- `mkdir boltio`

3- `cd boltio`

4- `pip install slack_bolt`

5- `python3 -m venv .venv`

6- `source .venv/bin/activate`

7- `export SLACK_APP_TOKEN=[AWS TOKEN]`

8- `export SLACK_BOT_TOKEN=[AWS TOKEN]`

9- `python3 app.py`

## about app.py:

Use socket mode for running

https://github.com/slackapi/bolt-python

