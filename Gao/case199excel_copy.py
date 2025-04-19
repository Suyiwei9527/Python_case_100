import pandas as pd

# 读取Excel文件
excel_file = pd.ExcelFile('Gao/F5_iRules.xlsx')

# 获取所有工作表名
sheet_names = excel_file.sheet_names

# 打开tcl_file以追加模式写入
with open('tcl_file', 'a') as f:
    for sheet_name in sheet_names:
        # 读取每个工作表的内容
        df = excel_file.parse(sheet_name)
        
        # 将工作表内容写入tcl_file
        name = "D:\Python_case_100\Gao\ePolicy\\"
        f.write(f'{ name+ sheet_name}\n')
        f.write(df.to_string(index=False))
        f.write('\n\n')