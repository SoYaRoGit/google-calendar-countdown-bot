from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta, date
from config import config



class GoogleCalendarAPI:
    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            config.calendar.service_account_file,
            scopes=config.calendar.scopes
        )
        self._service = build("calendar", "v3", credentials=credentials)


    @property
    def service(self):
        return self._service
    

    def get_all_upcoming_events(self, calendar_id: str, time_min: str = None):
        if time_min is None:
            now = datetime.now(timezone.utc)
            time_min = now.isoformat()
            time_max = (now + timedelta(days=365)).isoformat()

        all_events = []
        page_token = None

        while True:
            events_result = (
                self.service.events()
                .list(
                    calendarId=calendar_id,
                    timeMin=time_min,
                    timeMax=time_max,
                    maxResults=250,
                    singleEvents=True,
                    orderBy="startTime",
                    pageToken=page_token,
                )
                .execute()
            )
            all_events.extend(events_result.get("items", []))
            page_token = events_result.get("nextPageToken")
            if not page_token:
                break

        return all_events


    def get_event_list(self, calendar_id: str) -> str:
        events = self.get_all_upcoming_events(calendar_id)
        if not events:
            return "Нет предстоящих событий."

        lines = []
        today = date.today()
        for i, event in enumerate(events, start=1):
            summary = event.get("summary", "Без названия")
            start = event["start"]
            if "dateTime" in start:
                dt = datetime.fromisoformat(start["dateTime"].replace("Z", "+00:00"))
                event_date = dt.date()
                date_str = dt.strftime("%d.%m.%Y")
            else:
                event_date = date.fromisoformat(start["date"])
                date_str = event_date.strftime("%d.%m.%Y")
            days_left = (event_date - today).days
            lines.append(f'{i}. {summary} | Дата: {date_str} → Осталось: {days_left} дн.')
        return "\n".join(lines)


google_calendar_api = GoogleCalendarAPI()