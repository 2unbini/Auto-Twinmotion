import pyautogui
import keyboard

print('커서 위치 저장하는 프로그램입니다.\n')
print('저장하고자 하는 위치에 커서를 놓고 alt 키를 눌러 커서 위치를 파일에 저장합니다.')
print('모든 작업이 끝나면 esc 키를 눌러 커서 위치 저장을 완료하세요.')

input = ('S(start), Q(quit): ')

if input.casefold().__eq__('q'):
    print('프로그램을 종료합니다.')
else:
    print('프로그램을 시작합니다.')
    f = open("position.txt", 'w')
    
    while True:
        if keyboard.is_pressed('esc'):
            print('커서 위치 저장 완료. 파일을 닫습니다.')
            f.close()
            break
        elif keyboard.is_pressed('alt'):
            pos = pyautogui.position()
            f.write(pos)
            print('커서 위치 %s 저장됨.' % pos)
            
    print('커서 위치 저장이 완료됐습니다. position.txt 파일을 확인하세요.')