import os

import pyautogui
import pydirectinput
import time
import clipboard


# main function
def main():
    start_no = int(input('파일 시작 번호를 입력하세요: '))
    end_no = int(input('파일 끝 번호를 입력하세요: '))
    path = input('폴더의 절대 경로를 입력하세요: ')

    # if path[len(path) - 1] != '/':
    #     path += '/'
    #     print(path)

    print('5초 뒤 실행 시작합니다.')
    time.sleep(5)
    print('실행 시작!')
    result = auto_export_by_cursor(start_no, end_no, path)

    if result is False:
        print('비정상적으로 종료되었습니다.')
    else:
        print('정상적으로 종료되었습니다.')


# 커서 위치에 따라 정해진 동작 수행 하는 함수
def auto_export_by_cursor(start_no: int, end_no: int, save_path) -> bool:
    current_no = start_no

    while current_no <= end_no:
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

        # 2-2. select file name
        print('2-2. select file name')

        pyautogui.keyDown('shift')
        pyautogui.keyDown('fn')
        pyautogui.press('left')
        pyautogui.keyUp('fn')
        pyautogui.keyUp('shift')
        time.sleep(0.5)

        # 2-3. copy file name
        print('2-3. copy file name')

        with pyautogui.hold('ctrl'):
            pyautogui.press('c')
        time.sleep(0.5)

        # 2-4. open file
        print('2-4. open file')

        pyautogui.press('enter')
        time.sleep(5)
        # check if alert appeared or not
        # if alert appeared:
        #     return False

        # 3. make folder named after the one that copied on the clipboard
        print('3. make folder named after the one that copied on the clipboard')

        folder_name = clipboard.paste()
        if not folder_name:
            return False
        directory = folder_name + str(current_no)
        print(directory)
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            time.sleep(1)
        except OSError:
            print('Error: Creating directory. ' + directory)

        # 4. click export panel
        print('4. click export panel')

        export_panel = pyautogui.locateCenterOnScreen('export_panel')
        print(export_panel)
        if export_panel is None:
            return False
        # pyautogui.click(export_panel)
        pydirectinput.click(export_panel)
        time.sleep(5)

        # 5. click export button
        print('5. click export button')

        export_button = pyautogui.locateCenterOnScreen('export_button')
        if export_button is None:
            return False
        # pyautogui.click(export_button)
        pydirectinput.click(export_button)
        time.sleep(5)

        # 6. search file to export and press enter
        print('6. search file to export and press enter')

        pyautogui.write(directory, interval=0.05)
        time.sleep(0.5)
        pyautogui.press('down')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(5)

        # 7. wait until the dialog disappears
        print('7. wait until the dialog disappears')

        while not pyautogui.locateOnScreen('exporting') is None:
            continue
        time.sleep(5)

        # 8. repeat to 1
        print('No.%d 완료.' % current_no)
        current_no += 1

    return True


# Run Function
main()
