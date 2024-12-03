# 安裝與執行

## 1. 環境準備
- 安裝 **Python 3.x**，並確保已加入環境變數。
- 確保電腦已安裝 **Google Chrome 瀏覽器**。

## 2. 安裝相依套件
- 雙擊執行 `install.bat`，自動安裝必要的 **Python 套件**。

## 3. 配置帳號檔案
- 打開 `accounts.csv`，依以下格式填入帳號與密碼：  
email,password  
example1@gmail.com,password1  
example2@gmail.com,password2
-確保檔案儲存為 UTF-8 格式。

## 4. 執行程式
- 雙擊 run.bat 啟動程式。
- 程式將提示輸入當天的投票連結，例如：
請問今天的連結是：https://example.com/vote
- 按照畫面指示操作，手動輸入驗證碼，完成投票。

## 注意事項
- 由於驗證碼需人工輸入，請在提示音響起後立即查看並輸入正確的驗證碼。

- 帳號檔案格式：
確保 accounts.csv 的帳號密碼分隔符為 英文逗號（,），避免格式錯誤。

## 常見問題
1. 程式報錯 chromedriver.exe 無法啟動
請確認 chromedriver.exe 已下載，並與瀏覽器版本相符。
2. 驗證碼輸入錯誤
若輸入錯誤，程式會自動刷新頁面，重新要求驗證碼。
3. 未找到帳號檔案
請確認 accounts.csv 位於程式資料夾內，並正確填寫帳號資訊。

## 聯繫支援
若使用過程中遇到問題，請聯繫開發者提供技術支援。  
感謝ChatGPT全程協助。
