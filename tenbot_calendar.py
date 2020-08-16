from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from constants import *
from datetime import datetime, timedelta
import datefinder

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def find_date(start_time):
    matches = list(datefinder.find_dates(start_time))
    if len(matches):
        return matches[0]


def schedule_appointment(service, patient_name, start_time, duration, reason):
    working_event = event.copy()
    start_time = find_date(start_time)
    end_time = start_time + timedelta(hours=duration)

    working_event['summary'] = 'Appointment with ' + str(patient_name)
    working_event['start']['dateTime'] = start_time.strftime("%Y-%m-%dT%H:%M:%S") 
    working_event['end']['dateTime'] = end_time.strftime("%Y-%m-%dT%H:%M:%S")
    working_event['description'] = reason

    return service.events().insert(calendarId='primary', body=working_event).execute()


def find_appointment(service, patient_name, desired_description):
    all_appointments = service.events().list(calendarId='primary').execute()

    not_found = True
    desired_app = None
    for app in all_appointments['items']:
        summary = app['summary']
        if summary[17:] == patient_name and app['description'] == desired_description:
            desired_app = app
            break
    
    return desired_app

def remove_appointment(service, desired_app):
    return service.events().delete(calendarId='primary', eventId=desired_app['id']).execute()

def edit_appointment(service, desired_app):
    ''' TODO: write edit_appointment once rasa is finished''' 


service = authenticate_google()
schedule_appointment(service, 'Jane Appleseed', '24 August 8am', 2, 'COVID Test')
app = find_appointment(service, 'Jane Doe', 'blank 2')
remove_appointment(service, app)
