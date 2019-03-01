import unittest
import  HTMLTestRunner
import os
from testsuites .test_forum1 import Forum1
from testsuites.test_forum2 import Forum2
from testsuites.test_forum3 import Forum3
from testsuites.test_forum4 import Forum4
#设置报告文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path+"/..","report")
if not os.path.exists(report_path):os.mkdir(report_path)
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Forum1))
suite.addTest(unittest.makeSuite(Forum2))
suite.addTest(unittest.makeSuite(Forum3))
suite.addTest(unittest.makeSuite(Forum4))




if __name__=='__main__':
    #打开一个文件，将结果写入文件中
    html_report=report_path+r"\result.html"
    fp=open(html_report,"wb")
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)