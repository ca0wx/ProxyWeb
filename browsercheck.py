import os

def brows():
    browser_paths = {
        "chrome": [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
        ],
        "brave": [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
        ],
        "edge": [
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        ],
        "opera": [
            os.path.expandvars(r"%LOCALAPPDATA%\Programs\Opera\launcher.exe"),
            r"C:\Program Files\Opera\launcher.exe"
        ],
        "firefox": [
            r"C:\Program Files\Mozilla Firefox\firefox.exe",
            r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe"
        ],
        "chromium": [
            os.path.expandvars(r"%LOCALAPPDATA%\Chromium\Application\chrome.exe"),
            r"C:\Program Files\Chromium\Application\chrome.exe"
        ],
        "safari": [
            r"C:\Program Files\Safari\Safari.exe",
            r"C:\Program Files (x86)\Safari\Safari.exe"
        ]
    }

    checked_browsers = {}
    found_executable_paths = {}

    for tarayici, yollar in browser_paths.items():
        found_paths_for_this_browser = []
        
        for yol in yollar:
            if os.path.exists(yol):
                found_paths_for_this_browser.append(yol)

        if found_paths_for_this_browser:
            checked_browsers[tarayici] = 1
            found_executable_paths[tarayici] = found_paths_for_this_browser

    return checked_browsers, found_executable_paths