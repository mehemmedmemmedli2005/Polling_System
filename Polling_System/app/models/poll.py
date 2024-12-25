from pydantic import BaseModel
from typing import List

class Poll(BaseModel):
    poll_id: int
    question: str
    options: List[str]  # List of option names
    is_active: bool = True
