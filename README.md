# MovieCrawler

한국영화데이터베이스(KMDb)에서 영화 정보를 크롤링하는 크롤러입니다.

## Getting Started

1. Cloning project

   ```bash
   git clone https://github.com/DMJaejakdan/MovieCrawler.git
   cd MovieCrawler
   ```

2. Environment Setting

   ```bash
   conda env create -f environment.yml
   conda activate MovieCrawler
   pip install -r requirements.txt
   ```

3. Download ChromeDriver for using Selenium
   - [여기](https://chromedriver.chromium.org/downloads)에서 자신의 운영체제/크롬 버전에 맞게 ChromeDriver를 `exec\chromedriver.exe` 경로에 다운로드

## How to Run

1. KOFIC에서 제공하는 [영화정보 리스트 페이지](https://www.kobis.or.kr/kobis/business/mast/mvie/searchMovieList.do)에서 한국 영화 리스트 파일 다운로드 후 `data/raw/movie_list_YYYY-MM-DD.csv`에 저장
2. [Getting Started](#getting-started)를 참조해 프로젝트 실행 환경 세팅
3. 실행

   실행시 필요한 환경변수는 [여기](#command-line-arguments) 참조

   ```bash
   python main.py
   ```

## Command Line Arguments

- date
  - date type, `YYYY-MM-DD` 형식
  - default: 2023-09-06
  - KOFIC에서 제공하는 한국 영화 리스트 제공 날짜를 의미합니다.