# 변수 : 저장 공간, 프로그램 작성하기 전에 필요한 값 준비과정
# 명령어 : CPU에 하나의 동작을 지시
# 함수(메소드) : 하나의 기능을 구현,
#              반복적으로 사용할 작업을 미리 만들어놓은 작은 프로그램 단위
# 클래스 : 변수와 함수로 구성된 프로그램 그룹,
#         같은 목적을 위해 만들어 놓은 함수들의 모임
# 패키지 : 클래스의 모임, 여러 클래스를 모아서 하나의 큰 프로그램을 완성
# 프레임워크 : 패키지의 모임, 다양한 목적에 맞게 프로그램을 활용
# def 함수명(인수, ...)
#      return 전달값
# 인수 : 함수를 사용하기 위해 필요한 값
# 전달값 : 함수가 작업을 완료한 후 결과값
# 함수는 호출해서 함수가 실행된 후에 호출한 곳으로 되돌아와야 한다.
# 전달값이 있으면 함수 호출 시 변수로 받으면 되고(변수 생략 가능)
#   hap = sum(3,4,5),   sum(3,4,5)
# 전달값이 없으면 함수 호출만 해서 사용
#   print("연습")

# 모든 함수는 프로그램의 상단에 구성

# 함수 없이 프로그램 작성
# -> 반복작업, 분리해서 관리가 필요, 주 프로그램 연관 없음
# -> 함수로 분리
# 복잡한 프로그램을 함수로 분리해서 해석 및 활용에 편의를 제공할 때
# 함수는 입력, 처리, 출력 별로 따로 구성해서 만든다.
# java, c++ 등은 return 전달하는 결과값은 반드시 한 개만 전달 가능
# But, python은 전달값을 여러개 전달 가능
def coffeeSelect():
    coffee = int(input("원하는 커피를 선택하세요.(1.달달, 2.보통, 3.씁쓸)"))
    return coffee

def coffeeMachine(coffee): # 복사한 내용 중에 변수가 있으면 인수로 받기
    print("1. 뜨거운 물을 준비한다.")
    print("2. 종이컵을 준비한다.")

    if coffee == 1:
        print("3. 달달한 커피를 탄다.")
    elif coffee == 2:
        print("2. 보통 커피를 탄다.")
    elif coffee == 3:
        print("3. 씁쓸한 커피를 탄다.")
    else:
        print("3. 랜덤 커피를 탄다.")

    print("4. 물을 붓는다.")
    print("5. 스푼으로 젓는다.")

# 입력
coffee = coffeeSelect()

# 처리 및 출력
coffeeMachine(coffee) # 사용한 변수를 전달값으로 출력