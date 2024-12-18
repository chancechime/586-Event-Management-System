from quick_imports import *
import json

class EventDetails:
    def __init__(self, event_id, name="", date="", location="", description="", tickets=None):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.location = location
        self.description = description
        self.tickets = tickets or []  # Default to an empty list if no tickets are provided
 
    def populate_event(self, json_data):
        """
        Populates the event details with the provided data from a JSON object.
        """
        try:
            self.name = json_data.get('name', self.name)
            self.date = json_data.get('date', self.date)
            self.location = json_data.get('location', self.location)
            self.description = json_data.get('description', self.description)
            self.tickets = json_data.get('tickets', self.tickets)
        except Exception as e:
            print(f"Error populating event details: {e}")
            raise  # Re-raise the exception for proper handling