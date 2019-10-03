# This module use Gmail API to access user's data
# You may need to create a consent in oder to generate credentials following this document
#
#     https://docs.google.com/document/d/14yxATdW12ysIy9WYT54ZvGDRmv65_5ZOjzrrk3BIzGE
#
# token.pickle file will be generated automatically for the next run

import pickle
import os.path
import re
import time

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import rootpath
import base64
import email

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']
__service = None
__token_file = rootpath.detect() + "/tests/resources/gmail/token.pickle"
__credentials_file = rootpath.detect() + "/tests/resources/gmail/credentials.json"


def service():
    global __service
    if __service is None:
        creds = None
        if os.path.exists(__token_file):
            with open(__token_file, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    __credentials_file, SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        __service = build('gmail', 'v1', credentials=creds, cache_discovery=False)
    return __service


def get_messages(query=''):
    try:
        response = service().users().messages().list(userId='me', q=query).execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service().users().messages().list(userId='me', q=query,
                                                         pageToken=page_token).execute()
            messages.extend(response['messages'])
        return messages
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def delete_message(msg_id):
    try:
        service().users().messages().delete(userId='me', id=msg_id).execute()
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def get_mime_message(query='', delete=True):
    messages = get_messages(query)
    timeout = 60
    while len(messages) == 0 and timeout > 0:
        messages = get_messages(query)
        time.sleep(1)
        timeout = timeout - 1
    if len(messages) == 0:
        raise TimeoutError('Cannot find email: %s in 60 seconds' % query)
    message = service().users().messages().get(userId='me', id=messages[0]['id'], format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_bytes(msg_str)

    # I recommend to delete the email to avoid duplicate issue for next run
    if delete:
        delete_message(messages[0]['id'])
    return mime_msg


def get_confirm_url():
    """
        This is an example for retrieving confirm url when registering a new user
        Assume:
            - Email Title: Welcome to Automation Testing
            - The link we need is in Confirm button
    """
    registered_email = "your_register_email_@gmail.com"
    text = get_mime_message(query=f"to: {registered_email} and Welcome to Automation Testing")
    # Remove some special characters when encoding ASCII
    text = text.replace('=\n', '').replace('\r', '').replace('=3D', '=')
    # Extract href from Confirm button
    confirm_wrapper = re.search("href=\"(.+?)>Confirm", text).group(1)
    return re.search('[\'"]?([^\'" >]+)', confirm_wrapper).group(0)
