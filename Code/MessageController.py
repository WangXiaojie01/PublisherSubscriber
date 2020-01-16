
#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
'''

import os, sys
from collections import defaultdict

from Exchange import Exchange
from Task import Task


exchange = Exchange()
class MessageController:

    @staticmethod
    def registerDefaultSubscriber(task):
        exchange.attach(task)

    @staticmethod
    def registerSubscriber(msg, task):
        exchange.attach(task, msg)

    @staticmethod
    def registerSubscriberFunc(msg, func):
        exchange.attachFunc(func, msg)

    @staticmethod
    def registerDefaultSubscriberFunc(func):
        exchange.attachFunc(func)

    @staticmethod
    def publishToAll(info = None):
        exchange.sendAll(info)

    @staticmethod
    def publishMessage(msg, info = None):
        exchange.send(msg, info)

    @staticmethod
    def releaseSubscriber(msg, task):
        exchange.detachByMsgAndTask(msg, task)
        task.delete()

    @staticmethod
    def releaseTask(task):
        exchange.detachByTask(task)

    @staticmethod
    def cancelMessage(msg):
        self.exchange.detachByMsg(msg)

if __name__ == "__main__":
    task1 = Task()
    MessageController.registerSubscriber("test1", task1)
    class CustomTask(Task):
        def respone(self, args):
            print("My CustomTask %s" % args)
    task2 = CustomTask()
    MessageController.registerSubscriber("test1", task2)
    task3 = CustomTask()
    MessageController.registerSubscriber("test2", task3)
    task4 = Task()
    MessageController.registerDefaultSubscriber(task4)

    def testFunc(args):
        print("Test myFunc %s" % args )

    MessageController.registerSubscriberFunc("test3", testFunc)

    MessageController.publishMessage("test3", {"test1": "1", "ts": "ts"})
    MessageController.publishMessage("test1")
    MessageController.publishToAll()

