import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
@app.message("hola")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
                {
                        "type": "section",
                        "text": {
                                "type": "mrkdwn",
                                "text": "*Boltio listo para hacer _Deploy_* :tada:"
                        }
                },
                {
                        "type": "section",
                        "text": {
                                "type": "mrkdwn",
                                "text": "This button won't do much for now but you can set up a listener for it using the `actions()` method and passing its unique `action_id`. See an example in the `examples` folder within your Bolt app."
                        }
                },
                {
                        "type": "divider"
                },
                {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "action_id": "text-1"
                        },
                        "label": {
                                "type": "plain_text",
                                "text": "Build",
                        }
                },
                {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "action_id": "text-2"
                        },
                        "label": {
                                "type": "plain_text",
                                "text": "Branch",
                        }
                },
                {
                        "type": "actions",
                        "elements": [
                                {
                                        "type": "button",
                                        "text": {
                                                "type": "plain_text",
                                                "text": "Test",
                                        },
                                        "value": "click_me_123",
                                        "action_id": "boton-1"
                                }
                        ]
                }
        ],
    )
@app.action("boton-1")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"acá tiene que traer fatos del los campos build y branch")

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
