import os
import time
import csv
import winsound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException

# 驅動路徑
CHROME_DRIVER_PATH = r"chromedriver.exe"

# 帳號檔案路徑 (CSV 格式)
ACCOUNTS_FILE = "accounts.csv"

# 確保截圖存放目錄存在
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# 初始化 ChromeDriver 的 Service
service = Service(CHROME_DRIVER_PATH)

# 單一帳號登入並投票
def login_and_vote(email, password):
    driver = webdriver.Chrome(service=service)
    try:
        # 打開登入頁面
        driver.get("https://youthdream.phdf.org.tw/member/login")
        wait = WebDriverWait(driver, 20)

        # 輸入 Email
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.send_keys(email)

        # 輸入密碼
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        
        while True:
            winsound.MessageBeep()
            time.sleep(0.5)
            manual_captcha = input("請輸入驗證碼：")
            captcha_input = driver.find_element(By.NAME, "captcha")
            captcha_input.clear()
            captcha_input.send_keys(manual_captcha)
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            try:
                wait = WebDriverWait(driver, 5)  # 設置最多等待 10 秒
                wait.until(lambda driver: "member/login" not in driver.current_url)
                if "member/login" not in driver.current_url:
                    print(f"{email} 登入成功！")
                    break
            except TimeoutException:
                print(f"{email} 登入超時，無法確認登入成功！")

        # 跳轉到投票頁面並進行投票
        while True:
            try:
                driver.get(url)
                vote_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "vote-project")))
                vote_button.click()
                print(f"{email} 投票完成！")

                time.sleep(4)

                # 保存截圖
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(SCREENSHOT_DIR, f"{email}_vote_screenshot_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
                print(f"{email} 已保存截圖：{screenshot_path}")
                break

            except UnexpectedAlertPresentException:
                print("檢測到頁面刷新警告，正在重新加載頁面。")
                driver.refresh()
                time.sleep(2)

    except Exception as e:
        print(f"{email} 發生錯誤：{e}")

    finally:
        driver.quit()

# 批量處理帳號
def batch_vote():
    if not os.path.exists(ACCOUNTS_FILE):
        print("未找到帳號檔案，請確認 'accounts.csv' 是否存在！")
        return

    with open(ACCOUNTS_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # 跳過標題行
        for row in reader:
            if len(row) != 2:
                print(f"帳號資料格式錯誤：{row}")
                continue
            email, password = row
            print(f"開始處理帳號：{email}")
            login_and_vote(email, password)

if __name__ == "__main__":
    url = input("請問今天的連結是：")
    batch_vote()