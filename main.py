import pyautogui
import psutil


# main function
def main():
    
    startNo = int(input('파일 시작 번호를 입력하세요: '))
    endNo = int(input('파일 끝 번호를 입력하세요: '))
    
    print('실행 시작합니다.')
    result = auto_export_by_cursor(startNo, endNo)
    
    if result is False:
        print('비정상적으로 종료되었습니다.')
    else:
        print('정상적으로 종료되었습니다.')
    
    return 0


# auto export function
def auto_export_by_cursor(startFileNo, endFileNo):
    tm_usage = 0
    
    while startFileNo <= endFileNo:
        
        # 1. open twinmotion
        # 2. open file
        # 3. click export panel
        # 4. scroll to the button
        # 5. click export button
        # 6. choose export target file
        # 7. run export
        
        tm_usage = check_tm_usage()
        
        startFileNo += 1
        
    return True
        

# calculate twinmotion cpu usage
def check_tm_usage():
    return 0


# Run Function
main()