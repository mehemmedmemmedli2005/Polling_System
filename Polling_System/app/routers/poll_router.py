from fastapi import APIRouter, HTTPException
from app.models.poll import Poll
from app.services.poll_service import PollService

router = APIRouter()
poll_service = PollService()

@router.post("/")
def create_poll(poll: Poll):
    try:
        created_poll = poll_service.create_poll(poll)
        return {"message": "Poll created successfully", "poll": created_poll}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def list_polls():
    return poll_service.list_polls()

@router.get("/{poll_id}")
def get_poll(poll_id: int):
    poll = poll_service.get_poll(poll_id)
    if not poll:
        raise HTTPException(status_code=404, detail="Poll not found.")
    return poll

@router.put("/{poll_id}/close")
def close_poll(poll_id: int):
    try:
        poll_service.close_poll(poll_id)
        return {"message": "Poll closed successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
