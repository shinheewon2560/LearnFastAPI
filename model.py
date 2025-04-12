#데이터의 형태를 설정하기 위한 페이지
#sqlalchemy를 이용해서 Database의 데이터 구조를 여기서 설정해줌
#class형태로 Database 형태를 구성해줌
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


#Question에 사용되는 데이터들을 정의
#String과 Text의 차이는 글자 수의 차이가 얼만큼 있는가에 차이임
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key = True)
    subject = Column(String, nullable = False)
    content = Column(Text, nullable = False)
    create_date = Column(DateTime, nullable = False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key = True)
    content = Column(Text, nullable = False)
    create_date = Column(DateTime, nullable = False)
    #Question의 tablename이 question이기 때문에 question이 되는거고 그 중에 id항목을 원하는 거니까 question.id가 된다.
    question_id = Column(Integer, ForeignKey("question.id"))
    #이건 Answer에서 Qustion을 참조하기 위한 처리. 첫 파라미터는 참조하기 위한 데이터, 뒷 파라미터는 역참조가 가능하게 하는 것이다.
    question = relationship("Question", backref = "answer")

