from .models import SessionState
from .knowledge import QUESTIONS_DB
from .responses import get_response

class QuizEngine:
    def __init__(self):
        self.sessions = {}

    def process_input(self, user_input: str, session_id: str) -> dict:
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionState()
        session = self.sessions[session_id]
        # Process input and update session state
        # Return response

    def get_statistics(self) -> dict:
        # Calculate and return statistics
        return {}
