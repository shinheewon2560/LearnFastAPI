#데이터를 열고 닫는 것을 자동으로 해 주기위헤 데코레이터를 설정하기 위해
#조금더 자세히 설명하면 with문이 하는 행동을 정의하는 것
#with문을 사용하기 위해 의존성 주입을 하기 위해 하는 것
# import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Database 접속 주소
#root directory에 저장하라는 의미
SQLALCHMY_DATABASE_URL = "sqlite:///./FastAPI.db"

#creat_engine은 커넥션 풀을 만드는 명령어 (접속 객체를 일정갯수 미리 만들어서 자동 제어하는 장치)
#그냥 DB가 저장되는 방식에 대한 기초적인 설정이라고 이해하고 넘어가자
engine = create_engine(
    SQLALCHMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

#auto commit = True 이면 수정하자마자 바로 DB에 반영이 된다
#즉, commit으로 저장하는 행위, rollback행위 모두 작동하지 않는다는 의미이다.
#sqlalchemy의 문법이니 나중에 따로 공부하자
#database생성 문법 seeseionmaker()
Sessionlocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#DB설명 끝 후 반환
Base = declarative_base()

#열고 닫는 과정에서 해야하는 동작을 여기서 명시
#with문을 사용할때 의존성 주입을 위한 전처리
"""
@contextlib.contextmanager
def get_db():
    db = Sessionlocal()
    try:
        #제어권을 호춣한 쪽으로 잠깐 넘기는 것을 의미
        yield db
    finally:
        db.close()
"""
#fastapi의 Depend()를 사용해서 의존성 주입을 위한 전처리
def get_db():
    db = Sessionlocal()
    try:
        #제어권을 호춣한 쪽으로 잠깐 넘기는 것을 의미
        #새션을 받아서(db)반환 후 작업이 끝나면 새션을 반환
        yield db
    finally:
        db.close()