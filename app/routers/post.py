from fastapi import Response, status, HTTPException, Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session

from . import oauth2
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/", response_model=List[schemas.Post])
def get_posts(db:Session=Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #               (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    
    # new_post = models.Post(title=post.title, content=post.content, published=post.published) or 
    print(current_user.email)
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}", response_model=schemas.Post)
def get_post_by_id(id: int, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    #cursor.execute("""SELECT * FROM posts WHERE id=%s""", (str(id)))
    #post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if post:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Post with id: {id} not found")
    #response.status_code = status.HTTP_404_NOT_FOUND
    #return {"message": f"Post with id: {id} not found"}

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    #cursor.execute("""DELETE FROM posts WHERE id=%s returning *""", (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostBase, db: Session = Depends(get_db), current_user: int= Depends(oauth2.get_current_user)):
    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id=%s RETURNING * """, 
    #               (post.title, post.content, post.published, str(id)))
    #update_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} not found"
        )
    
    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()