# 理工学堂自动提交代码
# 添加账号密码，自动刷完并满分
from typing import Dict, List
import requests
from time import sleep

baseURl: str = 'http://lgxt.wutp.com.cn/api'

headers: Dict[str, str] = {"Authorization": ''}


def login(loginName: str, password: str) -> str:
    url = baseURl + '/login'
    loginData = {
        "loginName": loginName,
        "password": password
    }
    response = requests.post(url, data=loginData)
    json = response.json()
    return json['data']


def getCourses() -> List[int]:
    url = baseURl+'/myCourses'
    response = requests.post(url, headers=headers)
    json = response.json()
    list = json["data"]
    res: List[int] = []
    for it in list:
        res.append(it["courseId"])
    return res


def getCourseWorks(courseId: int) -> List[int]:
    url = baseURl+'/myCourseWorks'
    response = requests.post(url, headers=headers, data={
        "courseId": courseId
    })
    json = response.json()
    list = json["data"]
    res: List[int] = []
    for it in list:
        res.append(it["workId"])
    return res


def showQuestions(workId: int) -> List[str]:
    url = baseURl+'/showQuestions'
    response = requests.post(url, headers=headers, data={
        "workId": workId
    })
    json = response.json()
    list = json["data"]
    res: List[str] = []
    for it in list:
        res.append(it["answer"])
    return res


def submitAnswer(workId: int, grade: int):
    url = baseURl+'/submitAnswer'
    response = requests.post(url, headers=headers, data={
        "workId": workId,
        "grade": grade
    })
    json = response.json()
    print(json["msg"])


if __name__ == "__main__":
    loginName = ""
    password = ""
    token = login(loginName, password)
    headers["Authorization"] = token
    courseList: List[int] = getCourses()
    for id in courseList:
        workList = getCourseWorks(id)
        for work in workList:
            submitAnswer(work, 100)
            sleep(10)
