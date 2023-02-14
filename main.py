# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from datetime import datetime
import time
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["appium:deviceName"] = "R3CR30LBMKH"
caps["platformName"] = "android"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
# 에어 선택
el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="아이나비 에어")
el1.click()
time.sleep(3)
# 검색창 선택
el2 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvSearchHint")
el2.click()
time.sleep(3)
# 검색어 입력
el3 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/etKeyword")
el3.send_keys("잠실 롯데월드")
time.sleep(3)
# 검색어 결과 첫번째 선택
el4 =driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/rlSingleContents")
el4.click()
time.sleep(2)
# 길찾기 선택
el5 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvButtonText")
el5.click()
time.sleep(3)
# 경로 수정 선택
el6 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/ivExit")
el6.click()
time.sleep(3)
# 출발지 선택
el7 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/name")
el7.click()
time.sleep(3)
# 검색어 입력
el8 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/etKeyword")
el8.send_keys("성지아파트")
time.sleep(3)
# 검색어결과 첫번째 선택
el9 =driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/rlSingleContents")
el9.click()
time.sleep(3)
# 출발지 선택
el10 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvButtonText")
el10.click()
time.sleep(5)
# 탐색버튼 선택
el12 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tvButtonText")
el12.click()
time.sleep(5)
# 가장빠름 선택
el13 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tw_route_info_view")
el13.click()

f = open("C:/Users/pwy2403/Desktop/실험실/에어상용.txt", 'a')
now=datetime.now()
# 메모장 작성시작
dt_string=now.strftime("\nA1@%Y-%m-%d@요일@(1)출근@에어상용")
f.write(dt_string)
# 에어추천 텍스트 작성
el14 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_opt_first_name")
step_output = el14.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 현재시간 작성
dt_string=now.strftime("@%H:%M")
f.write(dt_string)
# 도착예상시간 작성
el15 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_arrival_time")
step_output = el15.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 탐색 거리 작성
el16 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_dist")
step_output = el16.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 탐색거리요금 작성
el16 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_fee")
step_output = el16.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 분기점
dt_string=now.strftime("\nA1@%Y-%m-%d@요일@(1)출근@에어상용")
f.write(dt_string)
# 가장빠름 텍스트 작성
el17 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_opt_other_name")
step_output = el17.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 현재시간 작성
dt_string=now.strftime("@%H:%M")
f.write(dt_string)
# 도착예상시간 작성
el18 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_arrival_time")
step_output = el18.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 탐색 거리 작성
el19 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_dist")
step_output = el19.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
# 탐색거리 요금 작성
el20 = driver.find_element(by=AppiumBy.ID, value="com.thinkware.inaviair:id/tv_route_item_view_fee")
step_output = el20.get_attribute("TEXT")
data = step_output
f.write("@")
f.write(data)
driver.quit()