from fastapi import FastAPI, Response, status, APIRouter
from .. import schema, database, auth, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
  prefix= "/",
  tags= ["Votes"])
  
@router.post("/", status_code= status.HTTP_201_CREATED)
def vote(vote : schema.Vote, db: Session = Depends(database.get_db), current_user : int = Depends(oauth2.get_current_user)):
  vote = db.query(models.Votes).filter(models.Votes.post_id== vote.id, models.Votes.user_id ==current_user.id).first()
  if (vote.dir ==1):
    if vote:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
  else:
    if not vote:
      raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    vote.delete(synchronize_session=False)
    return {"deletion": "done"}


  


