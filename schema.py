from datetime import datetime
from pydantic import BaseModel, conint

class POSTS(BaseModel):
    title: str
    content: str
    published: bool = True

class postcreate(POSTS):
    pass

class PostOut(POSTS):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True 

class User(BaseModel):
    email: str
    password: str
    class Config:
        orm_mode = True

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)

