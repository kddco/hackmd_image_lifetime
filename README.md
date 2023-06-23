# hackmd_image_lifetime
## 最新公告
- Hackmd官方已將所有圖片一併上傳到Hackmd專屬空間，不再依賴第三方圖床
 自動拜訪md筆記中的圖片，避免圖片過期而死去
 本程式只在Windows系統下可正常運作
## 原版
### 使用步驟
1. 下載筆記
![image](https://user-images.githubusercontent.com/52121443/151647079-6a230f70-73f1-4d28-a69e-4ce6495093f1.png)
2. 更改main.py裡面的path參數，設定為hackmd筆記所在目錄
### 執行結果
描述共執行了幾個檔案
![image](https://user-images.githubusercontent.com/52121443/151647118-051a55c0-b913-4aa0-aa7f-aa452be31444.png)
## 進階版
- 當你需要多次訪問圖片，你得用這個，更有效率
- main2.py會將圖片網址記錄下來
- main3.py會直接訪問圖片網址，免再翻找md
1. 下載筆記
![image](https://user-images.githubusercontent.com/52121443/151647079-6a230f70-73f1-4d28-a69e-4ce6495093f1.png)
2. 更改main2.py裡面的path參數，設定為hackmd筆記所在目錄
3. 執行main2.py 一次就好
4. 執行main3.py
