import turtle #turtle이라는 모듈을 불러온다.
t = turtle.Turtle()
t.shape("turtle")

size = int(input("집의 크기는 얼마로 할까요?")) #변수 size에 집의 크기의 값을 입력받는다.
t.fd(size) # size만큼 앞으로 직진한다.
t.right(90) #오른쪽으로 90만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.
t.right(90) #오른쪽으로 90만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.
t.right(90) #오른쪽으로 90만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.

t.right(90) #오른쪽으로 90만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.
t.left(120) #왼쪽으로 120만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.
t.left(120)  #왼쪽으로 120만큼 회전
t.fd(size) # size만큼 앞으로 직진한다.
t.left(120)  #왼쪽으로 120만큼 회전
