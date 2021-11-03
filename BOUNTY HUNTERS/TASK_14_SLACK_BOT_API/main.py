from slack_bot import find_slack_messages

# call function

messages = find_slack_messages()

if (messages[0]):
    print("100 texts from general channel\n\n")
    for message in messages[1]:
        text = message.get("text")
        print(text)
else:
    print("Error creating conversation: {}".format(messages[1]))
