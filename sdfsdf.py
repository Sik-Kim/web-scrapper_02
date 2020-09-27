import requests  #html의 정보를 가져오는 라이브러리!(파이썬 자체 기능도 있지만 requests가 훨씬 강력해서 사용)
from bs4 import BeautifulSoup  #html에서 정보를 추출하는 라이브러리
#soup이라는 애가 데이터를 추출함
LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    #requests 라이브러리 사용해서 indeed 사이트 http를 last page.
    #print(result)를 하면 <response [200]>이 찍히는데 응답 성공이라는 의미임.

    

    soup = BeautifulSoup(result.text, "html.parser")
    #beautifulsoup 라이브러리 이용해서 requests로 가져온 http의 text 정보를 쭉 가져옴(프린트하면 방대한 text가 출력되곘지)


    
    pagination = soup.find("div", {"class": "pagination"})
    #자 이제 위에서 모든 text를 가져왔고 그 중 pages 정보를 가져오려고 함
    #soup.find_all('a'). # site page부분 요소검사로 class명 찾아봄. a들 상위로 class가 pagination인 div가 있었음.
    # <a class="pagination" href=https://www.indeed.com/jobs?q=python&limit=50></a>

    links = pagination.find_all('a')
    #div(class:pagination) 하부 anchor를 가져옴.

    pages = []

    for link in links[:-1]:
        # pages.append(link.find("span").string)
        pages.append(int(
            link.string))  #anchor 바로 밑의 string을 가져와도 span에서 가져온거랑 같은 결과
    #각각의 anchor 하부의 span(페이지넘버)들을 pages라는 리스트에 넣어줌

    max_page = pages[-1]
    #이제 page별(20개)로 계속 request 하는 방법을 알아야 함
    #max_page를 range에 넣어서 request를 불러올꺼야
    return max_page

    


