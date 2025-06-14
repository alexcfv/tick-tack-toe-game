from models.db import create_session, db_connect
from models.user import User
from flask import jsonify

engine, connection = db_connect()

async def addUser(user_name: str, password: str) -> bool:
    session = create_session(engine)
    with session:
        check_user_name = session.query(User).filter(User.user_name == user_name).all()
    
        if check_user_name:
            return False
        
        session.add(User(user_name=user_name, password=password))
        session.commit()
        return True

async def getUser(user_name: str) -> User:
    session = create_session(engine)
    with session:
        user_by_name = session.query(User).filter(User.user_name == user_name).first()
        
        if user_by_name:
            return user_by_name
        else:
            return None

async def getUserById(user_id: int) -> bool:
    session = create_session(session)
    with session:
        user_by_id = session.query(User).filter(User.id == user_id).first()
        
        if user_by_id:
            return user_by_id
        else:
            return False
    
async def deleteUserById(user_id: int) -> bool:
    session = create_session(engine)
    with session:
        user_by_id = session.query(User).filter(User.id == user_id).first()
    
        if user_by_id:
            session.delete(user_by_id)
            session.commit()
            return True
        else:
            return False
        
async def updateUserById(user_id: int, data: User) -> bool:
    session = create_session(engine)
    with session:
        user_by_id = session.query(User).filter(User.id == user_id).first()
        
        if user_by_id:
            user_by_id.user_name = data.user_name
            user_by_id.password = data.password
            
            session.commit()
            session.refresh(user_by_id)
            
            return True
        
        else:
            return False