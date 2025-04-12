from model import Question, Answer
from datetime import datetime
from database import Sessionlocal

#q = Question(subject = "잘 되고 있나요?", content = "존나어렵네 띠바 ㅋㅋ", create_date = datetime.now())

db = Sessionlocal()
#db.add(q)
q = db.get(Question,1)
#db.delete(q)

#a = Answer(question = q, content = "ㄹㅇㅋㅋ", create_date = datetime.now())
a = db.get(Question, 1)

print(a.answer[0].content)
"""
db.add(a)
db.commit()


print(db.query(Question).all())"""

