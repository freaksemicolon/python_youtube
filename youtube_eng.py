try :
    import tkinter as tk
    from tkinter import *
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.chrome.options import Options
    import subprocess
    from pytube import YouTube
    import pyautogui 
    import pyperclip
    import os
except ImportError:
    import pip
    pip.main(['install', 'selenium'])
    pip.main(['install', 'webdriver'])
    pip.main(['install', 'pyautogui'])
    pip.main(["install","pytube"])
    pip.main(["install","YouTube"])
    pip.main(['install', 'subprocess'])    
    from selenium import webdriver
    import subprocess
    import pyautogui 
    from pytube import YouTube
import time

root = tk.Tk()
lbl = Label(root, text=f"\nYouTube Premium (Windows only)\n*Start by clicking the button below*\n(It may take a long time due to the download check at startup.)\n================== =======\nFeature\n1. Remove ads\n2. Save offline\n<Save offline only after logging in\nSave when offline save is clicked>\n")
lbl.configure(font=("Courier", 30, "italic"))
lbl.pack()
lbl['bg'] = 'gray'
button = tk.Button(root, text = "start", command = root.destroy, width=15, height=2)
button.configure(font=("Courier", 30, "italic"))
button.pack()
button['bg'] = 'black'
button['fg'] = 'gray'
root.attributes("-fullscreen", True)
root.wm_attributes("-topmost", 1)
root.configure(bg='gray')
root.mainloop()

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

def down_check():
    global url
    if (url == driver.current_url):
        return 0
    else:
        url = driver.current_url
        down(url)
    return 0

def down(url):
    url = url
    doot = tk.Tk()

    def high_down():
        global url
        doot.destroy()
        YouTube(url).streams.get_highest_resolution().download()
    
        root = tk.Tk()
        lbl = Label(root, text=f"Download Complete")
        lbl.configure(font=("Courier", 30, "italic"))
        lbl.pack()
        root.wm_attributes("-topmost", 1)
        root.mainloop()

    def low_down():
        global url
        doot.destroy()
        YouTube(url).streams.first().download()

        root = tk.Tk()
        lbl = Label(root, text=f"Download Complete")
        lbl.configure(font=("Courier", 30, "italic"))
        lbl.pack()
        root.wm_attributes("-topmost", 1)
        root.mainloop()

    def mp3_down():
        global url
        doot.destroy()
        YouTube(url).streams.first().download()
        filePath = YouTube(url).streams.filter(only_audio=True).first().download()
        mp3FilePath = filePath.replace('mp4', 'mp3')
        os.rename(filePath, mp3FilePath)

        root = tk.Tk()
        lbl = Label(root, text=f"Download Complete")
        lbl.configure(font=("Courier", 30, "italic"))
        lbl.pack()
        root.wm_attributes("-topmost", 1)
        root.mainloop()

    doot.title("Download")
    lbl = Label(doot, text=f"\n\n  If you close YouTube while downloading, the download may be interrupted. \nIf you click the button below, it will be saved in this file location accordingly\nWhen the download is complete, it will say \"Complete\"\nYou cannot download the same video continuously\n If there is a file with the same name, an error may appear\nIf you download another video before the download completion appears\nAn error may appear\n")
    lbl.pack()
    button1 = tk.Button(doot, text = "low quality", command = low_down)
    button1.pack()
    lbl = Label(doot, text=f"\n")
    lbl.pack()
    button2 = tk.Button(doot, text = "high quality", command = high_down)
    button2.pack()
    lbl = Label(doot, text=f"\n")
    lbl.pack()
    button3 = tk.Button(doot, text = "low quality + mp3", command = mp3_down)
    button3.pack()
    lbl = Label(doot, text=f"\n")
    lbl.pack()
    doot.wm_attributes("-topmost", 1)
    doot.mainloop()

text_file_path = findfile("cipher.py", "C:/")
new_text_content = ''
with open(text_file_path,'r') as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        if i == 29:
            new_string = '        var_regex = re.compile(r"^\$*\w+\W")'
        else:
            new_string = l.rstrip('\n')
        
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open(text_file_path,'w') as f:
    f.write(new_text_content)

filepath = findfile("chrome.exe", "C:/")
print(filepath)
subprocess.Popen(r''+filepath+' --remote-debugging-port=9222 --user-data-dir="C:\\chromeCookie"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=option)
#driver = webdriver.Chrome()
url = ""
driver.get("https://youtube.com")
while(True):
    try:
        driver.find_element(By.CLASS_NAME, 'ytp-ad-timed-pie-countdown')
        driver.find_element(By.CLASS_NAME, 'ytp-ad-skip-button-icon').click()
    except NoSuchElementException:
        try:
            driver.find_element(By.CLASS_NAME, 'ytp-ad-image')
            pyautogui.hotkey('ctrl', 'shift', 'j')
            pyperclip.copy("setInterval(() => {\n	if (document.querySelectorAll('.ad-showing').length > 0) {\n		const video = document.querySelector('video');\n		if (video) {\n			video.currentTime = video.duration;\n		}\n	}\n}, 500);")
            #pyperclip.copy("if (document.querySelectorAll('.ad-showing').length > 0) {\n	const video = document.querySelector('video');\n	if (video) {\n		video.currentTime = video.duration;\n	}\n}")
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('F12')
            pyperclip.copy("hello world")
        except NoSuchElementException:
            try:
                a = driver.find_element(By.CLASS_NAME, 'style-scope ytd-offline-promo-content')
                pyautogui.hotkey('F5')
                down_check()
            except NoSuchElementException:
                pass