from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

def get_images(keyword):
    # 웹 접속 :  네이버 이미지 접속
    print("접속중")

    driver = webdriver.Chrome("E:\dev\python_workspace\chromedriver.exe")
    driver.implicitly_wait(30)

    url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
    driver.get(url)
    
    # 페이지 스크롤 다운
    body = driver.find_element_by_css_selector("body")
    for i in range(10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        
    # 이미지 링크수집
    imgs = driver.find_elements_by_css_selector("img._img")
    # print(imgs)
    
    result = []
    for img in tqdm(imgs):
        if 'http' in img.get_attribute('src'):
            result.append(img.get_attribute('src'))
    
    # print(result)
    # 저장 디렉토리 생성
    import os
    if not os.path.isdir("./{}".format(keyword)):
        os.makedirs("./{}".format(keyword))
        
    # 다운로드
    print("다운로드")
    from urllib.request import urlretrieve
    for index, link in tqdm(enumerate(result)):
        start = link.rfind(".")
        end = link.rfind("&")
        # print(link[start:end])  -> .jpg, .png, .git ...
        filetype = link[start:end]
        
        # 저장위치, 파일명까지
        urlretrieve(link, './{}/{}{}{}'.format(keyword, keyword, index, filetype))
    
    
    

def get_google_images(keyword):
    # 웹 접속 :  네이버 이미지 접속
    print("접속중")

    driver = webdriver.Chrome("E:\dev\python_workspace\chromedriver.exe")
    driver.implicitly_wait(30)

    url = "https://www.google.com/search?sxsrf=ALeKk03ZIZ5MYef70JqkZOQ8Aev_JIgF0g:1605860289770&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiWuIXh15DtAhXFG6YKHY6nBQ4Q_AUoAXoECB8QAw&biw=1443&bih=920&q={}".format(keyword)
    driver.get(url)
    
    # 페이지 스크롤 다운
    body = driver.find_element_by_css_selector("body")
    for i in range(3):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        
    # 이미지 링크수집
    imgs1 = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    print(imgs1)
    imgs2 = [img.get_attribute('src') for img in tqdm(imgs1) if img.get_attribute('src') is not None and 'https:' in img.get_attribute('src')]
    
    result = []
    # for img in tqdm(imgs):
    #     if 'http' in img.get_attribute('src'):
    #         result.append(img.get_attribute('src'))
    #     else:
            
    # print(result)
    
    # 저장 디렉토리 생성
    import os
    if not os.path.isdir("./google{}".format(keyword)):
        os.makedirs("./google{}".format(keyword))
        
    # 다운로드
    print("다운로드")
    from urllib.request import urlretrieve
    # for index, link in tqdm(enumerate(result)):
    for index, img in tqdm(enumerate(imgs2)):
        
        src = img.get_attribute('src')
        
        # 저장위치, 파일명까지
        urlretrieve(src, './google{0}/{0}{1}{2}'.format(keyword, index, '.jpeg'))




if __name__ == "__main__":
    keyword = input("검색 키워드 입력 : ")
    # get_images(keyword)
    get_google_images(keyword)


