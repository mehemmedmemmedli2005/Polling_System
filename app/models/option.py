from pydantic import BaseModel

class Option(BaseModel):
    option_id: int
    poll_id: int
    name: str
    votes: int = 0
