from fastapi import FastAPI, Depends
from fastapi import HTTPException
from typing import List, Optional
import uvicorn
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.sql.functions import mode
from sqlalchemy.orm import Session
import schema
from database import engine, sessionLocal, get_db
from pydantic import BaseSettings

origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Settings(BaseSettings):
    database_password : str
    database_username : str
    database_port : str
    database_name : str
    database_hostname : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int
    class Config:
        env_file = ".env"


models.Base.metadata.create_all(bind=engine)
 
app = FastAPI()

app.include_router(vote.router)

@app.get("/sqlalchemy")
def test_posts(db:Session = Depends(get_db), response_model=schemas.PostOut):
    posts = db.query(model.Post).all()
    return {"data": posts}



try:
    conn = psycopg2.connect(host="localhost", port=5432, database= "postgres", user= "postgres", password= "admin")
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    print("Database connection successful")
except Exception as error:
    print("Error connecting to the database", error)

@app.get("/", response_model=List[schemas.Post])
def all_data(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), limit:int = 10,skip = 2, search: Optional[str]=""):
    #cursor.execute("""SELECT * FROM posts""")
    #posts = cursor.fetchall()
    #return {"data": posts}
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return {"data": posts}   


@app.post("/create", response_model=schemas.PostOut)
def create_post(db:session = Depends(get_db), post= schemas.POSTS, current_user: int = Depends(oauth2.get_current_user)): 
    new_post = models.Post(owner_id = current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    return {"data": new_post}
    #cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
    #                 (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
@app.get("/posts/{id}")
def get_post_id(id:str, user_credentials:OAuth2PasswordRequestForm = Depends()):
    cursor.execute("SELECT * FROM posts WHERE ID=%s ", str(id))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"data": post}

@app.delete("/delete/{id}")
def delete_post(id:str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id="%s" RETURNING *""", str(id),)
    #conn.commit()
    #deleted_post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id ==id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    if post.owner_id != oauth2.get_current_user.id:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, details = f"post wuth id : {id} not found")

    return {"message": "Post deleted successfully"}
    
@app.put("/update/{id}")
def update_post(id:str, updated_post: schemas.postcreate, db: session = Depends(get_db), user_credentials:OAuth2PasswordRequestForm = Depends()):
    post = db.query(models.Post).filter(models.Post.id == id)
    post = post.first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    #cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE ID="%s" RETURNING *""",
                   #(post.title, post.content, post.published, str(id),))
    #updated_post = cursor.fetchone()
    #if not updated_post:
        #raise HTTPException(status_code=404, detail="Post not found")
    #conn.commit()
    return {"data": updated_post}

@app.post("/users", response_model=List [dict])
def add_user(new_user: schema.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  
    return {"message": "User added successfully"}


#app.include_router(post.router)
#app.include_router(user.router)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                nk     mmmmmmmmmm


 
 
