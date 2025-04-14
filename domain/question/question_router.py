#router api를 작성하기 위해 fast api에서 APIrouter만을 호출
from fastapi import APIRouter,Depends
#데이터 형을 받아오기 위한 전처리
from sqlalchemy.orm import Session

#data 구조 형태를 알기위해 호출
from model import Question
#Database를 가져오기 위해서 호출
from database import get_db
#schema를 알기위해 호출
from domain.question import question_schema, question_CRUD

#URL로 호출할 때 경로를 미리 지정
router = APIRouter(
    prefix = "/api/question",
)

#schema를 이용해 반환값이 Question schema로 구성된 리스트라는 것을 명시
#만일 schema에서 content 항목이 제거 된다면 DB에는 content가 있지만 출력되지는 않는다.
@router.get("/list", response_model = list[question_schema.Question])
#question_CRUD.py를 통해 작엄 함수화 및 호출
def question_list(db : Session = Depends(get_db)):
    _question_list = question_CRUD.get_question_list(db)
    return _question_list


#contextlib을 이용해서 with문의 작동을 제어해 의존성을 주입하는 방법
"""
def question_list():
    #with문에서 반환값은 db를 반환하고 아래 있는 명령이 끝나면 다시 데이터 반환
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    
    return _question_list
"""
#Depend()를 이용해 의존성 주입하는 방법
#위 함수는 함수를 파라미터로 받아서 리턴값을 되돌려줌
#중요한 부분이 파라미터로 함수 자체를 받으니 함수를 호출해 그 값을 받는 get_db()로 주면 안됨
"""
def question_list(db : Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list
"""


