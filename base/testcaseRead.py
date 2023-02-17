import pandas


def  testcaseread():
         df = pandas.read_excel(r'C:\Users\奋斗的小菜鸟\Desktop\testcase.xlsx',engine= 'openpyxl')
         testcasemap = tuple(zip(df['是否执行'],df['代码方法']))
         # print(testcasemap)
         do_testcase = list(k[1] for k in testcasemap if k[0] =='是')
         # print(do_testcase)
         for k in do_testcase:
             print(k)
             k='TestCases.'+k+'.'+k
             print(k)
             eval(k)()



if __name__ == '__main__':
    testcaseread()

