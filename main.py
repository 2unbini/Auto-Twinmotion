import mouse
import pyautogui
import pydirectinput
import psutil
import re
import time


# main function
def main():
    start_no = int(input('파일 시작 번호를 입력하세요: '))
    end_no = int(input('파일 끝 번호를 입력하세요: '))
    open_path = input('오픈할 파일의 절대 경로를 입력하세요: ')
    save_path = input('저장할 파일의 절대 경로를 입력하세요: ')

    print('5초 뒤 실행 시작합니다.')
    time.sleep(5)
    result = auto_export_by_cursor(start_no, end_no, open_path, save_path)

    if result is False:
        print('비정상적으로 종료되었습니다.')
    else:
        print('정상적으로 종료되었습니다.')


# position.txt 파일에 저장된 커서 위치 정수 배열로 쪼개는 함수
def file_split() -> [[int]]:
    positions = []

    with open('position.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]

    for line in lines:
        # Extract integer values for x and y using regular expressions
        match = re.match(r'Point\(x=(\d+),\s*y=(\d+)\)', line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            positions.append([x, y])

    return positions


# 커서 위치에 따라 정해진 동작 수행 하는 함수
def auto_export_by_cursor(start_no: int, end_no: int, open_path, save_path) -> bool:
    movement_count = 4

    while start_no <= end_no:
        cursor_pos = file_split()

        # position.txt 에서 받아온 커서 위치가 동작의 개수와 맞지 않으면 종료
        if len(cursor_pos) < movement_count:
            return False

        for i, pos in enumerate(cursor_pos):
            if i == 0:
                # 1. click file tab in twin motion
                pydirectinput.click(x=pos[0], y=pos[1])
            elif i == 1:
                # 2. click open in file tab
                pydirectinput.click(x=pos[0], y=pos[1])
                time.sleep(1)
                # 3. search file to open and press enter
                pyautogui.write(open_path + str(start_no), interval=0.25)
                # pyautogui.press('enter')
                # check if alert appeared or not
                # if alert appeared:
                #     return False
            elif i == 2:
                # 4. click export panel
                pydirectinput.click(x=pos[0], y=pos[1])
            elif i == 3:
                # 5. click export button (if needed, scroll to bottom)
                # mouse.wheel()
                pydirectinput.click(x=pos[0], y=pos[1])
                time.sleep(1)
                # 6. search file to export and press enter
                pyautogui.write(save_path + str(start_no) + '\\' + str(start_no), interval=0.25)
                pyautogui.press('enter')
                # check if alert appeared or not
                # if alert appeared:
                #     return False
            # elif i == 4:
            #     # 7. run export
            #     pyautogui.click(x=pos[0], y=pos[1])

            # sleep 1 sec for each gui control
            time.sleep(2)

        # wait until export ends
        time.sleep(5)

        # continue to next file no
        start_no += 1

    return True


# Run Function
main()
