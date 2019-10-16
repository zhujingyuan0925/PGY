import json
import unittest
import paramunittest
import requests
import urllib.parse
import read.readExcel as readExcel
from common.configHttp import RunMain
import read.readConfig as readConfig
import common.getCommonInfo as getCommonInfo

ship_xls = readExcel.ReadExcel().get_xls("login.xls","ship")
url = readConfig.ReadConfig().get_http("gzhbaseurl")#获取配置文件中的url地址
ownerid = getCommonInfo.shipOwnerId

@paramunittest.parametrized(*ship_xls)
class testShip(unittest.TestCase):
    def setParameters(self,case_name,path,data,method,isTest):
        self.case_name = str(case_name)
        self.path = str(path)
        self.data = str(data)
        self.method = str(method)
        self.isTest = str(isTest)
    #调用测试方法
    def testShip(self):
        self.getCategorys()
        self.gettags()
        # self.addship()
        # self.shiplist()
        # self.shipdetail()
        # self.shipzedit()


    #获取群分类
    def getCategorys(self):
        if self.case_name == "categorys":
            #data = json.loads(self.data)-----
            #print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path,self.data)
            print("caturl",url+self.path)
            res = json.loads(info)
            print("cat",res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #获取群标签
    def gettags(self):
        if self.case_name == "tags":
            # data = json.loads(self.data)-----
            #print(url, self.path, self.data)
            info = RunMain().run_main(self.method, url + self.path, self.data)
            res = json.loads(info)
            print("tag",res)
            self.assertEqual(res['Code'], "000000")
            self.assertFalse(res['IsError'])

    #群添加
    # def addship(self):
    #     if self.case_name == "addship":
    #         data = json.loads(self.data)
    #         print(url, self.path, self.data)
    #         info = RunMain().run_main(self.method, url + self.path,self.data)
    #         res = json.loads(info)
    #         print(res)
    #         self.assertEqual(res['Code'], "000000")
    #         self.assertFalse(res['IsError'])
    #群列表
    # def shiplist(self):
    #     if self.case_name == "shiplist":
    #         #data = json.loads(self.data)
    #
    #         #print("ownerid",ownerid)
    #         #print(url + self.path+ownerid+"/list",self.data)
    #         info = RunMain().run_main(self.method, url + self.path, self.data)
    #         res = json.loads(info)
    #         self.assertEqual(res['Code'], "000000")
    #         self.assertFalse(res['IsError'])
    #         global shipid
    #         shipid = res['Data'][0]["Id"]
    #         print("群id：",shipid)
    #
    # #群详情
    # def shipdetail(self):
    #     if self.case_name == "shipdetail":
    #         #data = json.loads(self.data)
    #         #print(url, self.path, self.data)
    #         info = RunMain().run_main(self.method, url + self.path+shipid+"/detail", self.data)
    #         res = json.loads(info)
    #         self.assertEqual(res['Code'], "000000")
    #         self.assertFalse(res['IsError'])
    # #群信息修改
    # def shipzedit(self):
    #     if self.case_name == "ediship":
    #         data = json.loads(self.data)
    #         #print(url, self.path, self.data)
    #         info = RunMain().run_main(self.method, url + self.path, data)
    #         res = json.loads(info)
    #         self.assertEqual(res['Code'], "000000")
    #         self.assertFalse(res['IsError'])


if __name__ == '__main__':
    testShip().testShip()