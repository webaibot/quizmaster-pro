from dataclasses import dataclass
from typing import List

@dataclass
class SessionState:
    score: int = 0
    hints_used: int = 0
    questions_answered: List[str] = None
