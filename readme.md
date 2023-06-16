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

### main.py 실행

### enjoy your free time!
