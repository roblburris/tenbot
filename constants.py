from datetime import datetime, timedelta

timezone = 'US/Pacific'

event = {
  'summary': '',
  'location': 'Bellevue, Washington',
  'description': '',
  'start': {
    'dateTime': '',
    'timeZone': timezone,
  },
  'end': {
    'dateTime': '',
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
    ]  
    },
}

freebusy = {
    "calendarExpansionMax": 42, # Maximal number of calendars for which FreeBusy information is to be provided. Optional. Maximum value is 50.
    "groupExpansionMax": 42, 
    "timeMax": "A String", 
    "items": [ # List of calendars and/or groups to query.
      {
        "id": "primary", # The identifier of a calendar or a group.
      },
    ],
    "timeMin": "A String", # The start of the interval for the query formatted as per RFC3339.
    "timeZone": timezone, # Time zone used in the response. Optional. The default is UTC.
}
