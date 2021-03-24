from django.shortcuts import render, redirect, get_object_or_404
from selenium import webdriver
import time
from themes.models import Local
import json


def themes(request):
    return render(request, 'themes/themes.html')


def data_insert(request):


    #1. 웹드라이버 켜기
    driver = webdriver.Chrome("./chromedriver")
    #2. 네이버 지도 접속하기
    driver.get("https://v4.map.naver.com/")

    # !!)네이버 지도 업데이트로 추
    driver.find_elements_by_css_selector("button.btn_close")[1].click()

    #3. 검색창에 검색어 입력하기 // 검색창: input#search-input
    search_box = driver.find_element_by_css_selector("input#search-input")
    # 검색어 - 서울 반려동물, 서울 반려견 동반
    search_box.send_keys("서울 반려견 동반")
    #4. 검색버튼 누르기 // 검색버튼: button.spm
    search_button = driver.find_element_by_css_selector("button.spm")
    search_button.click()
    #5. 검색 결과 확인하기

    for n in range(1, 31):
        # 지연시간주기
        time.sleep(1)
        l_result = []
        stores = driver.find_elements_by_css_selector("div.lsnx")
        for s in stores:
            my_img = s.find_element_by_css_selector('div > img')
            img_url = my_img.get_attribute('src')
            title = s.find_element_by_css_selector("dl.lsnx_det > dt > a").text
            venue = s.find_element_by_css_selector("dl.lsnx_det > dd.addr").text
            category = s.find_element_by_css_selector("dl.lsnx_det > dd.cate").text

            try:
                tel = s.find_element_by_css_selector("dl.lsnx_det > dd.tel").text
            except:
                tel = "전화번호 없음"

            local_obj = {
                'title': title,
                'venue': venue,
                'category': category,
                'tel': tel,
                'img_url': img_url
            }
            l_result.append(local_obj)

        for l in l_result:
            locals = Local(
                title=l['title'],
                venue=l['venue'],
                category=l['category'],
                tel=l['tel'],
                img_url=l['img_url']
            )
            locals.save()

        # 페이지버튼 div.paginate > *
        page_bar = driver.find_elements_by_css_selector("div.paginate > *")

        try:
            if n%5 != 0:
                page_bar[n%5+1].click()
            else:
                page_bar[6].click()
        except:
            print("수집완료")
            break
    print('성공했어용')
    return redirect('themes:themes')


# 테마 종류 "반려동물 > 반려동물호텔", "반려동물 > 애견훈련"
# 음식점 > 카페,디저트, 음식점 > 카페
def hotel_list(request):
    locals = Local.objects.all()
    hotels = locals.filter(category="반려동물 > 반려동물호텔")
    context = {'hotels': hotels}
    return render(request, 'themes/hotel.html', context)


def training_list(request):
    locals = Local.objects.all()
    training = locals.filter(category="반려동물 > 애견훈련")
    context = {'training': training}
    return render(request, 'themes/training.html', context)


def cafe_list(request):
    locals = Local.objects.all()
    cafes = locals.filter(category="음식점 > 카페,디저트")
    context = {'cafes': cafes}
    return render(request, 'themes/cafe.html', context)


def t_object(request, local_id):
    local = get_object_or_404(Local, pk=local_id)

    mapdict = {'title': local.title,
               'venue': local.venue,
               'category': local.category,
               'tel': local.tel}

    map_json = json.dumps(mapdict)
    return render(request, 'themes/t_object.html', {
        'selected_local': local,
        'map_json': map_json
    })
