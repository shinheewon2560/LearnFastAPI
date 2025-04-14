from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

#API를 여기서 최종 결합하기 위해 python 파일 호출
from domain.question import question_router

#app에 FastAPI를 할당.
#이제부터 API작성 가능
app = FastAPI()

#주소 설정
origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]
#frontend설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
@app.get("")
def hello():
    return {"message": "안녕하세요 파이보"}
"""
#API작성된 것을 그대로 가져온 것
#app에 API를 가져다 붙임. routerAPI를 붙이기로함. 그 API는 question_router이라는 파일에 router이라는 API를 붙임
app.include_router(question_router.router)