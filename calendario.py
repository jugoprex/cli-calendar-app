import setup
import datetime

def week_events(service):
    # Call the Calendar API
    for calendar_id in service.calendarList().list().execute().get('items', []):
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        timeMaxBound = datetime.datetime.utcnow() + datetime.timedelta(days=7)
        timeMaxBound = timeMaxBound.isoformat() + 'Z'
        print('Getting the upcoming 10 events in {}'.format(calendar_id.get('summary')))
        events_result = service.events().list(calendarId= calendar_id.get('id'), timeMin=now, timeMax=timeMaxBound,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])