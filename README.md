# pdf2image
해당 기능은 poppler를 설치하고 PATH에 추가해야 사용이 가능함. 

Windows에서 poppler를 설치하고 PATH에 추가하는 방법:

1. poppler 다운로드:
  https://github.com/oschwartz10612/poppler-windows/releases 에서 최신 버전의 poppler를 다운로드합니다.
  "Release-xx.xx.x-0.zip" 파일을 다운로드하세요 (xx.xx.x는 버전 번호).


2. 압축 해제:
  다운로드한 zip 파일의 압축을 풉니다.
  예: C:\Program Files\poppler에 압축을 해제합니다.


3. 시스템 PATH에 추가:
  시작 메뉴에서 "시스템 환경 변수 편집"을 검색하여 실행합니다.
  "환경 변수(N)..." 버튼을 클릭합니다.
  "시스템 변수(S)" 섹션에서 "Path" 변수를 찾아 선택하고 "편집(E)..." 버튼을 클릭합니다.
  "새로 만들기(N)" 버튼을 클릭하고, poppler의 bin 폴더 경로를 추가합니다.
  예: C:\Program Files\poppler\Library\bin
  "확인" 버튼을 눌러 모든 창을 닫습니다.


4. 시스템 재시작:
  변경사항을 적용하기 위해 컴퓨터를 재시작합니다.


5. 설치 확인:
  새 명령 프롬프트를 열고 다음 명령어를 입력합니다:
  Copypdftoppm -v
  버전 정보가 표시되면 설치가 성공적으로 완료된 것입니다.
