import re
import os
import requests
## made by kddco
## https://github.com/kddco
path= "C:\\Users\\wayne\\Downloads\\HackMD_User_1643382432883\\"
files_dir = os.listdir(path)

os.chdir(path)

for file in files_dir:
    f = open(file, 'r', encoding="utf-8")

    while True:
        str1 = f.readline()
        if(len(str1)!=0):

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
                print(resp.request.path_url)
        else:
            break
print("共執行",len(files_dir),"個檔案")
