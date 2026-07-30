import os
import subprocess
import requests
import selects
import browsercheck
from InquirerPy import inquirer

def run():
    secimler = selects.main()
    protocol = secimler[0]
    timeout = secimler[2]
    anonymity = secimler[1]

    proxylist_url = f"https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&protocol={protocol}&proxy_format=ipport&format=text&timeout={timeout}&country=all&ssl=all&anonymity={anonymity}"
    response = requests.get(proxylist_url)
    proxy_listesi = [p.strip() for p in response.text.splitlines() if p.strip()]

    checked_browsers, found_executable_paths = browsercheck.brows()

    if not found_executable_paths:
        print("\033[31m [-] Sistemde desteklenen bir tarayıcı bulunamadı!\033[0m")
        exit()

    for lists in proxy_listesi:
        test_proxy = lists

        if protocol == "http":
            proxies = {
                "http": f"http://{test_proxy}",
                "https": f"http://{test_proxy}"
            }
        elif protocol == "socks4":
            proxies = {
                "http": f"socks4://{test_proxy}",
                "https": f"socks4://{test_proxy}"
            }
        elif protocol == "socks5":
            proxies = {
                "http": f"socks5://{test_proxy}",
                "https": f"socks5://{test_proxy}"
            }

        try:
            check = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=3)

            if check.status_code == 200:
                onay = inquirer.confirm(
                    message=f"[+] {test_proxy} Proxy Canlı! Tarayıcı Açılsın Mı?",
                    default=True
                ).execute()

                if onay:
                    secilen_tarayici = inquirer.select(
                        message="Hangi tarayıcı ile açılsın?",
                        choices=list(found_executable_paths.keys())
                    ).execute()

                    target_exe = found_executable_paths[secilen_tarayici][0]

                    print(f"\033[32m [*] {secilen_tarayici.upper()} proxy ile başlatılıyor...\033[0m")

                    subprocess.Popen([
                        target_exe,
                        f"--proxy-server={protocol}://{test_proxy}",
                        "https://www.google.com"
                    ])

                    break

        except Exception as e:
            print(f"\033[31m [-] {test_proxy} Proxy Ölü! Başka Bir Proxy Deneniyor.\033[0m")

if __name__ == "__main__":
    run()