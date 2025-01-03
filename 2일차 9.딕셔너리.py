# 딕셔너리(사전) : [국어사전] 단어 : 뜻 -> 키 : 값
# 변수 = {키:값, 키1:값1, 키2:값2, ....}
dic1 = {1:'a',2:'b',3:'c'}
print("키를 숫자로 이용한 경우 : ", dic1)

dic2 = {'a':1,'b':2,'c':3}
print("키를 문자로 이용한 경우 : ", dic2)

# 서로 다른 값을 그룹으로 처리할 때 사용 -> java에서 map과 비슷
student = {'학번':1322, '이름':'홍길동', '학과':'컴퓨터학과'}
print(student)
# 추가는 새로운 키 값으로 저장하면
print("키로 값을 출력 : ", student['학번'])
student['학번'] = 9999
print("키로 값을 변경 : ", student['학번'])
print(student)

# 존재하지 않는 키로 저장 시 추가
student['연락처'] = '010-1234-5678'
print(student)

# 주요 함수
# 딕셔너리.clear() : 딕셔너리의 모든 항목을 제거한다.
# 딕셔너리.copy() : 딕셔너리의 모든 항목을 복사한다.
# 딕셔너리.get(키, default=none) : 해당 키의 값을 읽어온다. default는 없을 때 기본 값
# 딕셔너리.items() : 딕셔너리의 키와 값을 쌍으로 해서 읽어온다.
# {'a':1,'b':2,'c':3} -> ('a',1),('b',2),('c',3)
# 딕셔너리.keys() : 딕셔너리의 모든 키를 읽어온다.
# 딕셔너리.pop(키) : 딕셔너리에서 해당 키의 키와 값을 삭제한다.
# 딕셔너리.popitem() : 딕셔너리의 마지막 키와 값을 삭제한다.
# 딕셔너리.setdefault(키, default=값) : 딕셔너리에 키가 존재하지 않으면
#                                     default의 값으로 키를 읽어온다.
# 딕셔너리.update(딕셔너리2) : 새로운 딕셔너리를 기존 딕셔너리에 추가한다.
#                           동일한 키가 존재하면 값을 변경한다.
# 딕셔너리.values() : 딕셔너리의 모든 값을 읽어온다.
# 딕셔너리.fromkeys([키,..], 값 ) : 지정한 키들의 값을 모두 변경한다.
#        keys = ['국어','영어','수학']
#        성적표.formkeys(keys,0) -> 국어, 영어, 수학의 값을 0으로 변경
# del 딕셔너리[키] : 해당 키를 삭제한다.
# dict (키=값,키=값, ....) : 새로운 딕셔너리를 생성한다.
#       성적표 = dict(a=1,b=2,c=3)