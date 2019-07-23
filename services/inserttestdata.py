from conf import baseurl
import requests
import json


headers = {'Content-Type': 'application/json'}


def insertclassroom():
    classroomlist = [("北教201", "北教学楼二层阳面西数第一个教室", "*@*"),
                     ("北一阶", "教学楼一层阶梯教室", "一!1,2#二@*#三@1,2,6,7#四,五!5,6,7")]
    for cr in classroomlist:
        url = baseurl + "/classroom/"
        payload = {"classroom_name": cr[0],
                   "classroom_position": cr[1],
                   "classroom_available": cr[2]}
        requests.post(url=url,
                      headers=headers,
                      data=json.dumps(payload))


def insertteacher():
    teacherlist = [("张三", "12312342121", "一@1,2,3,4#二@5,6,7"),
                   ("王五", "2321312321", "*@1,2,3,4")]
    for tea in teacherlist:
        url = baseurl + "/teacher/"
        payload = {"teacher_name": tea[0],
                   "teacher_mobile": tea[1],
                   "teacher_request": tea[2]}
        requests.post(url=url,
                      headers=headers,
                      data=json.dumps(payload))


def insertclass():
    classlist = [("2019网络技术班", "1", "1"),
                 ("2019平面设计一班", "2", "2")]
    for cla in classlist:
        url = baseurl + "/class/"
        payload = {"class_name": cla[0],
                   "teacher_id": cla[1],
                   "classroom_id": cla[2]}
        requests.post(url=url,
                      headers=headers,
                      data=json.dumps(payload))


insertclassroom()
insertteacher()
insertclass()
