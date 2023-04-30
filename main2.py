import re
import os
import requests

# 获取当前脚本的目录路径
script_directory = os.path.dirname(os.path.abspath(__file__))

path= "C:\\Users\\wayne\\Downloads\\HackMD_User_1682844345527\\"
files_dir = os.listdir(path)

os.chdir(path)

output_file = os.path.join(script_directory, "imgurl.txt")

for file in files_dir:
    f = open(file, 'r', encoding="utf-8")

    while True:
        str1 = f.readline()
        if len(str1) != 0:
            try:
                m1 = re.search(r'https://{1}.+\.png{1}', str1).group()
            except:
                m1 = re.search(r'https://{1}.+\.png{1}', str1)

            if not m1:
                print("ERROR:", str1)
                pass
            else:
                print("成功匹配：", m1)
                resp = requests.get(m1)
                print(resp.url)

                with open(output_file, "a+") as f_out:
                    f_out.write(resp.url + "\n")
        else:
            break

print("共執行", len(files_dir), "個檔案")
