from typing import List, Optional
from app.models.poll import Poll
from app.models.option import Option

class PollService:
    def __init__(self):
        self.polls: dict[int, Poll] = {}
        self.options: dict[int, List[Option]] = {}

    def create_poll(self, poll: Poll) -> Poll:
        if poll.poll_id in self.polls:
            raise ValueError("Poll ID already exists.")
        self.polls[poll.poll_id] = poll
        self.options[poll.poll_id] = [
            Option(option_id=i+1, poll_id=poll.poll_id, name=option)
            for i, option in enumerate(poll.options)
        ]
        return poll

    def get_poll(self, poll_id: int) -> Optional[Poll]:
        return self.polls.get(poll_id)

    def list_polls(self) -> List[Poll]:
        return list(self.polls.values())

    def close_poll(self, poll_id: int):
        if poll_id not in self.polls:
            raise ValueError("Poll not found.")
        self.polls[poll_id].is_active = False
