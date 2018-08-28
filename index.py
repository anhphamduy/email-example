
from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import base64
from email.mime.text import MIMEText


SCOPES = 'https://mail.google.com/'


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    # load in token.json and can get from the Google APIs

    # get crednetials
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # create message base64 with MIMEText format
    created_message = create_message(
        "Anh", "phamduyanh249@live.com", "sdfsdf", "sdfsdf")

    # send message
    message = (service.users().messages().send(userId="me", body=created_message)
               .execute())


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


if __name__ == '__main__':
    main()
