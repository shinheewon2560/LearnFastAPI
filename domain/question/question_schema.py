import datetime

from pydantic import BaseModel

#schema를 만들기 위해 파라미터로 BaseModel을 전달
class Question(BaseModel):
    id : int
    #|뒤에 있는 거는 필수항목인지 설정해 주는 것(지금은 필수 항목이 아니라는 것)
    subject : str #| None = None
    content : str
    #datetime은 라이브러리이니 datetime에서 데이터 구조를 참조해야한다.
    create_date : datetime.datetime

    #여기는 orm 데이터 구조로 반환함을 설정
    #이 전처리를 해줘야 데이터가 깔끔하네 맵핑됨
    class Config:
        orm_mode = True
