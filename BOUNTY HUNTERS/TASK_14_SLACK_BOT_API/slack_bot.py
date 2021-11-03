import slack
import os
from pathlib import Path
from dotenv import load_dotenv

# load environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# create client
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

def find_slack_messages():
    """  """
    conversation_history = []
    channel_general_id = "C01HC495FHN"

    try:
        result = client.conversations_history(channel=channel_general_id)

        conversation_history = result["messages"]

        return (True, conversation_history)

    except slack.errors.SlackApiError as e:
        return ( False, e)
