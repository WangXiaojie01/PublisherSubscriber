
#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.17
author: wangxiaojie
'''

import os, sys
from collections import defaultdict

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)

from MessageController import MessageController
from Task import Task

if __name__ == "__main__":
    #使用范例
    
    #定义响应事件来注册消息
    def response(info):
        print("response my message whit info %s" % info)
    MessageController.registerSubscriberFunc("message1", response)
    MessageController.publishMessage("message1", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message1")
    
    #重写响应任务来注册消息
    class CustomTask(Task):
        def respone(self, info):
            print("This is My CustomTask %s" % info)
    task2 = CustomTask()
    MessageController.registerSubscriber("message2", task2)
    MessageController.publishMessage("message2", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message2")
    
    #注册响应所有消息的任务
    class CustomTask1(Task):
        def respone(self, info):
            print("This is My CustomTask1 %s" % info)
    task3 = CustomTask1()
    MessageController.registerDefaultSubscriber(task3)
    MessageController.publishMessage("message3", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message4")
    
    #注册响应所有消息的事件
    def response2(info):
        print("another response my message whit info %s" % info)

    MessageController.registerDefaultSubscriberFunc(response2)

    MessageController.publishMessage("message5", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message6")
    
    #发送所有事件或任务都响应的消息
    MessageController.publishToAll()
    
    #一个事件响应多个消息
    def response3(info):
        print("the third response my message whit info %s" % info)

    MessageController.registerSubscriberFunc("message7", response3)
    MessageController.registerSubscriberFunc("message8", response3)

    MessageController.publishMessage("message7", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message8", {"test2": "1", "ts3": "ts"})
    
    #一个任务响应多个消息
    class CustomTask2(Task):
        def respone(self, info):
            print("This is My CustomTask2 %s" % info)
    task4 = CustomTask2()
    MessageController.registerSubscriber("message9", task4)
    MessageController.registerSubscriber("message10", task4)
    MessageController.publishMessage("message9", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("message10", {"test2": "1", "ts3": "ts"})
    
    #一个消息发送给多个事件或多个任务
    class CustomTask3(Task):
        def respone(self, info):
            print("This is My CustomTask3 %s" % info)

    class CustomTask4(Task):
        def respone(self, info):
            print("This is My CustomTask4 %s" % info)

    task5 = CustomTask3()
    task6 = CustomTask4()
    MessageController.registerSubscriber("message11", task5)
    MessageController.registerSubscriber("message11", task6)

    def response4(info):
        print("the fourth response my message whit info %s" % info)

    def response5(info):
        print("the fifth response my message whit info %s" % info)

    MessageController.registerSubscriberFunc("message11", response4)
    MessageController.registerSubscriberFunc("message11", response5)

    MessageController.publishMessage("message11", {"test2": "1", "ts3": "ts"})

