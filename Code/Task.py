
#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.16
author: wangxiaojie
version: V0.1.1
'''

import os, sys

class Task:
    def __init__(self):
        self.message = set()
        self.message.add("_Ordinary_Msg_")
        self.repoeseFunc = None
    
    def addResponeMessage(self, msg):
        if not msg in self.message:
            self.message.add(msg)


    def send(self, msg, args):
        if msg in self.message:
            self.respone(args)

    def respone(self, args):
        if self.repoeseFunc:
            self.repoeseFunc(args)
        else:
            print("recevie args %s" % args)

    def delete(self):
        pass


