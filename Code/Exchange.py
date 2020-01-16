
#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
version: V0.1.1
'''

import os, sys

from collections import defaultdict
from Task import Task
class Exchange:
    def __init__(self):
        self.subscribers = defaultdict(set)

    def attachFunc(self, func, msg = None):
        if func:
            task = Task()
            task.respone = func
            self.attach(task, msg)


    def attach(self, task, msg = None):
        if msg == None:
            msg = "_Ordinary_Msg_" 
        task.addResponeMessage(msg)
        if msg in self.subscribers:
            subSet = self.subscribers[msg]
            subSet.add(task)
        else:
            subSet = set()
            subSet.add(task)
            self.subscribers.setdefault(msg, subSet)

    def detachByTask(self, task):
        for subSet in self.subscribers:
            if task in subSet:
                subSet.remove(task)

    def detachByMsgAndTask(self, msg, task):
        if msg in self.subscribers:
            if task in self.subscribers[msg]:
                self.subscribers[msg].remove(task)
    
    def detachByMsg(self, msg):
        if msg in self.subscribers:
            for task in self.subscribers[msg]:
                self.subscribers[msg].remove(task)
            self.subscribers.remove[msg]

    def send(self, msg, args):
        if msg in self.subscribers:
            for subscriber in self.subscribers[msg]:
                subscriber.send(msg, args)
        if "_Ordinary_Msg_" in self.subscribers:
            for subscriber in self.subscribers["_Ordinary_Msg_"]:
                subscriber.send("_Ordinary_Msg_", args)

    def sendAll(self, args):
        for msg in self.subscribers:
            for subscriber in self.subscribers[msg]:
                subscriber.respone(args)

