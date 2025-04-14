#작업이 반복될 수 있으니 반복되는 작업을 함수화
#따라서 어노테이션을 활용하진 않음
#어노테이션은 API를 직접적으로 사용하는 곳에서 여기서 정의한 함수를 가져가 호출할 것
from model import Question
from sqlalchemy.orm import Session

def get_question_list(db : Session):
    #.desc는 함수이니 괄호를 꼭붙여줘야한다
    question_list = db.query(Question).order_by(Question.id.desc()).all()
    return question_list