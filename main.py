import pyautogui
import pydirectinput
import re
import time
import os


# main function
def main():
    start_no = int(input('프로젝트 시작 번호를 입력하세요: '))
    end_no = int(input('프로젝트 끝 번호를 입력하세요: '))
    file_count = int(input('렌더링될 이미지 파일 개수를 입력하세요: '))
    estimated_min = int(input('예상되는 렌더링 시간(분)을 입력하세요: '))

    folder_name = input('폴더 이름을 입력하세요: ')

    path = "C:\\Users\\arcle\\OneDrive\\PROJECT\\PROJECT 2023\\MoDeF\\"
    save_path = path + folder_name

    if folder_name == "":
        print('비정상적으로 종료되었습니다.')
        return

    if save_path[len(save_path) - 1] != '\\':
        save_path += '\\'

    print('5초 뒤 실행 시작합니다.')
    time.sleep(5)
    result = auto_export_by_cursor(start_no, end_no, estimated_min, file_count, save_path)

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
def auto_export_by_cursor(start_no: int, end_no: int, estimated_min: int, file_cnt: int, save_path) -> bool:
    current_no = start_no

    while current_no <= end_no:
        cursor_pos = file_split()

        print('No. %d 진행중...' % current_no)

        # 1. open file in twin motion
        print('1. open file in twin motion')

        with pyautogui.hold('ctrl'):
            pyautogui.press('o')
        time.sleep(1)

        # 2-1. search file to open
        print('2-1. search file to open')

        file_name = save_path + str(current_no)
        pyautogui.write(file_name, interval=0.05)
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)

        # 2-2. open file
        print('2-4. open file')
        pyautogui.press('enter')
        time.sleep(3)

        # 2-3. save no button if dialog appeared
        print('2-5. save no button if dialog appeared')
        pydirectinput.click(x=cursor_pos[0][0], y=cursor_pos[0][1])

        # save no 버튼 누른 후 로딩 시간
        load_sec = 5
        time.sleep(load_sec)

        # 3. make folder named after the one that copied on the clipboard
        print('3. make folder named after the one that copied on the clipboard')
        directory = save_path + str(current_no)
        # print(directory)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            time.sleep(1)
        except OSError:
            print('Error: Creating directory. ' + directory)

        # 4. click export panel
        print('4. click export panel')
        pydirectinput.click(x=cursor_pos[1][0], y=cursor_pos[1][1])
        time.sleep(3)

        # 5. click export button
        print('5. click export button')
        pydirectinput.click(x=cursor_pos[2][0], y=cursor_pos[2][1])
        time.sleep(3)

        # 6. search file to export and press enter
        print('6. search file to export and press enter')

        pyautogui.write(directory, interval=0.05)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)

        # 7. wait until the dialog disappears
        print('7. wait until the dialog disappears')

        # 렌더링 시간 설정
        plus_sec = 60 * 10
        estimated_sec = 60 * estimated_min * file_cnt + plus_sec
        time.sleep(estimated_sec)

        # 8. repeat to 1
        print('No.%d 완료.' % current_no)
        current_no += 1

    return True


# Run Function
main()
