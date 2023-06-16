## Twin Motion 렌더링 자동화

Epic Games의 Twin Motion 이미지 렌더링을 자동화하는 python 코드입니다.

렌더링 큐가 따로 구현되어있지 않아 2-3시간씩 걸리는 렌더링을 직접 기다려야 하는 불편함을 해소하고자 만들었습니다.

23.06.16 기준 position과 sleep time에 대해 직접 추가해야합니다.

### python 설치
[점프 투 파이썬 도큐먼트](https://wikidocs.net/8)에 따라 설치합니다.

### pycharm 설치
[파이참 community 버전](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)을 설치합니다.

### pip install
파이참으로 해당 레포지토리를 열고 main.py, position.py의 상단에 `import` 되어 있는 모듈에 대해 설치를 진행합니다.

```python
import pyautogui
import pydirectinput
import re
import time
import os
```

다음과 같은 부분에서 `pyautogui`, `pydirectinput` 등에 대해 빨간 밑줄을 누르면 설치할 수 있도록 안내가 되어 있습니다.

### position.py 실행
- 이전 파일 저장여부 선택하는 팝업(yes/no 선택)
- export panel 버튼
- start export 버튼

프로그램을 실행한 후 세 요소에 대해 마우스 커서의 좌표를 저장하면 됩니다.

저장을 원하는 위치에 마우스 커서를 놓고, `alt`키를 누르면 해당 좌표가 저장됩니다.

모든 좌표를 저장했다면 `esc`키를 눌러 프로그램을 종료합니다.

### main.py 실행
프로그램을 실행하기에 앞서 자동으로 불러올 파일의 이름을 1부터 n까지 지정합니다.

프로그램을 실행한 후, 시작 파일 번호에 1을, 종료 파일 번호에 n을 입력하고 부가적으로 입력해야 하는 정보들을 입력합니다.

23.06.16 기준으로 정해진 단계에 따라 아주 기본적인 기능에 한해 하드코딩 되어 있습니다.

다음과 같은 순서로 진행됩니다.

1. 새 파일 열기(ctrl + o)
2. 파일 경로 찾고 열기
3. 이전 파일 저장 여부 선택하기
4. 2의 파일 경로 이름으로 새 폴더 생성하기
5. export 패널 열기
6. start export 버튼 누르기
7. 4의 폴더 경로 찾고 export 시작하기
8. 특정 시간 동안 main.py 정지하기

### enjoy your free time!
