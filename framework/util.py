import xlrd
from framework.logger import Logger
import os
logger = Logger(logger="Util").getlog()

class Util(object):
    @classmethod
    def read_excel(self,excelPath,sheetName="Sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)

        keys=sheet.row_values(0)  #获取第一行作为key值
        rowNum=sheet.nrows   #获取总行数
        cloNum=sheet.ncols   #获取总列数

        if rowNum<=1:
            logger.error("excel表中数据行小于1")
        else:
            r=[]
            for i in range(1,rowNum):
                sheet_data={}
                values=sheet.row_values(i)
                for j in range(0,cloNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
        return r

if __name__=="__main__":
    file_path = os.path.dirname(os.path.realpath(__file__))+"\data.xlsx"
    print(file_path)
    print(Util.read_excel(file_path))
