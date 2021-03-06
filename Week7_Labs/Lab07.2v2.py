# Shauna Byrne
# Code adapted from Lab instructions from Lab07.2 given by Andrew Beatty - GMIT - Computing & Data Analytics 2019
# Reference - https://developers.google.com/gmail/api/quickstart/python

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from xlwt import *
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    response = service.users().messages().list(userId='me').execute()
    #print (response)

    messages = []
    if 'messages' in response:
        messages.extend(response['messages'])
    
    while 'nextPageToken' in response:
        page_token = response['nextPageToken']
        response = service.users().messages().list(userId='me', pageToken=page_token).execute()
        messages.extend(response['messages'])

    for message in messages:
        #print(message['id'])
        CompleteMessage = service.users().messages().get(userId='me', id=message[0]['id']).execute()
        print(CompleteMessage['snippet'])

        headers = CompleteMessage['payload']['headers']
        subject = list(filter(lambda  h: h['name']=='Subject', headers))[0]['value']
        receiver = list(filter(lambda  h: h['name']=='To', headers))[0]['value']
        sender = list(filter(lambda  h: h['name']=='From', headers))[0]['value']
        print(subject)
        print(receiver)
        print(sender)

        w = Workbook()
        ws = w.add_sheet('emails')
        row = 0
        ws.write(row, 0, subject)
        ws.write(row, 1, receiver)
        ws.write(row, 2, sender)
        row += 1
        w.save('emails.xls')


    #with open('emails.json', 'w') as e:
        #json.dump(CompleteMessage, e, indent=4)

if __name__ == '__main__':
    main()