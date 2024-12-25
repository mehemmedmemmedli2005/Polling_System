from fastapi import APIRouter, HTTPException
from app.services.vote_service import VoteService
from app.services.poll_service import PollService

router = APIRouter()
poll_service = PollService()
vote_service = VoteService(poll_service)

@router.post("/{poll_id}/vote/{option_id}")
def cast_vote(poll_id: int, option_id: int):
    try:
        option = vote_service.vote(poll_id, option_id)
        return {"message": "Vote cast successfully", "option": option}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{poll_id}/results")
def get_results(poll_id: int):
    try:
        results = vote_service.get_results(poll_id)
        return {"poll_id": poll_id, "results": results}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
