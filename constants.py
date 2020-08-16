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
