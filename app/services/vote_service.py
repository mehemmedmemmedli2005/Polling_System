from typing import List
from app.models.option import Option

class VoteService:
    def __init__(self, poll_service):
        self.poll_service = poll_service

    def vote(self, poll_id: int, option_id: int) -> Option:
        poll_options = self.poll_service.options.get(poll_id)
        if not poll_options:
            raise ValueError("Poll not found.")
        if not self.poll_service.polls[poll_id].is_active:
            raise ValueError("Poll is closed.")
        for option in poll_options:
            if option.option_id == option_id:
                option.votes += 1
                return option
        raise ValueError("Option not found.")

    def get_results(self, poll_id: int) -> List[Option]:
        poll_options = self.poll_service.options.get(poll_id)
        if not poll_options:
            raise ValueError("Poll not found.")
        return poll_options
