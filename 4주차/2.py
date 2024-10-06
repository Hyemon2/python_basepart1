print('TATA' in 'TATATATATATATATATATATATA') #TATA가 문자열 안에 있으면 true로, 없으면 false로 출력된다.
print('AA' in 'TATATATATATATATATATATATA') #AA가 문자열 안에 없으면 False로, 있으면 True로 출력된다
print('AA' not in 'TATATATATATATATATATATATA') #AA가 문자열 안에 없으면 true로, 있으면 false로 출력된다.
print('AC' + 'TG') #문자열 AC와 TG를 출력한다
print('aaa' + 'ccc' + 'ttt' + 'ggg') #문자열 'aaaccctttggg'을 출력한다.
print('TA' * 12) #‘TA’를 12개 출력한다.
print(6 * 'TA')  #‘TA’를 6개 출력한다.

print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[0]) #인덱스 0번째를 출력한다,
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[1]) #인덱스 1번째를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[-1]) #인덱스 -1번째를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[-5]) #인덱스 -5번째를 출력한다.
#print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[50]) #범위에 벗어났기 때문에 출력이 되지 않는다.

print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[1:4])  #인덱스 1번째부터 3번째까지의 문자열을 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[4:-1]) #인덱스 4번째부터  -2번째까지의 문자열을 출력한다. 
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[-5:-4]) #인덱스 -5번의 문자열을 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[5:5])  #빈 문자열을 출력한다. 시작 인덱스와 끝 인덱스가 같기 때문이다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[-4:-6]) #빈 문자열을 출력한다. 시작 인덱스가 큰 인덱스보다 크기 때문이다. 

print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[:8])  #인덱스 처음부터 7번째까지 문자열을 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[9:])  #인덱스 9번째부터 인덱스 끝까지의 문자열을 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[9:-1]) #인덱스 9번째부터 인덱스 -1번째까지 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[:]) #인덱스 처음부터 끝까지 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[0:9:3]) #인덱스 0부터 인덱스 8까지 3씩 증가하면서 선택된 문자열 출력

print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[16:0:-4]) #인덱스 16번부터 시작까지 4씩 잠소하면서 선택된 문자열 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[16::-4]) #인덱스 16번부터 4씩 감소하면서 선택된 문자열을 출력
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[:25:-1]) #문자열의 뒤에서부터 25번째까지의 문자열을 거꾸로 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'[::-1])  #문자열을 뒤에서부터 거꾸로 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.count('DL')) #문자열에서 'DL'이 등장하는 횟수를 출력한다.

print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.find('DL'))   #문자열에서 'DL'이 처음으로 등장하는 위치를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.find('DL', 5))  #인덱스 5 이후부터 'DL'이 처음 등장하는 위치를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.find('DL', 5, 12)) #인덱스 5 이후부터 11까지 'DL'이 처음 등장하는 위치를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.startswith('DL'))  #문자열이 'DL'로 시작하는지의 여부를 출력한다.
print('MNKMDLVADVAEKTDLSKAKATEVIDAVFA'.startswith('DL', 4)) #인덱스 4부터 시작하는 부분이 문자열 'DL'로 시작하는지에 대한 여부를 출력한다.
