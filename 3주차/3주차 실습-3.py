money = int(input("투입한 돈 :")) # 사용자로부터 투입한 돈 값을 입력받아 변수'money'에 저장한다.
price = int(input("물건값:"))#사용자로부터 물건값을 입력받아 변수'price'에 저장한다.

change = money-price #변수 'money'에서 'price'를 뺀 값을 변수 'change'에 저장한다. 
print("거스름돈 :", change) #'print()'를 이용하여 거스름돈을 출력한다.

coin500 = change // 500 #'//'연산자를 이용하여 'change'를 500으로 나눈 몫을 변수'coin500'에 저장한다.
change = change % 500 # 변수 'change'를 500으로 나눈 나머지를 계산하여 다시 변수 'change'에 저장한다.

coin100 = change //100 # '//'연산자를 이용하여 'change'를 100으로 나눈 몫을 변수'coin100'에 저장한다.
change = change % 100 # 변수 'change'를 100으로 나눈 나머지를 계산하여 다시 변수 'change'에 저장한다.

coin50 = change // 50 # '//'연산자를 이용하여 'change'를 100으로 나눈 몫을 변수'coin100'에 저장한다.
change = change % 50 # 변수 'change'를 50으로 나눈 나머지를 계산하여 다시 변수 'change'에 저장한다.

coin10 = change // 10 # '//'연산자를 이용하여 'change'를 10으로 나눈 몫을 변수'coin100'에 저장한다.



print("500원 동전의 개수:",coin500) #'print()'를 이용하여 500원 동전의 개수를 출력한다.
print("100원 동전의 개수:",coin100) #'print()'를 이용하여 100원 동전의 개수를 출력한다.
print("50원 동전의 개수:",coin50) #'print()'를 이용하여 50원 동전의 개수를 출력한다
print("10원 동전의 개수:",coin10) #'print()'를 이용하여 10원 동전의 개수를 출력한다
