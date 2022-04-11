try:
    import fade
    import undetected_chromedriver as uc
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import threading
    from datetime import datetime
except ModuleNotFoundError:
    print('''Make sure you installed all pip commands (pip install xxx) (packages: fade, selenium, undetected-chromedriver) - in CMD''')
    exit()


def time():
    global current_time
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        sleep(0.5)


def main2():
    global driver2
    global wait2
    try:
        try:
            wait2.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button"))).click()
        except:
            driver2.refresh()
            wait2.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button"))).click()

        wait2.until(EC.element_to_be_clickable((By.ID, "searchinput"))).clear()  # clear link input
        wait2.until(EC.element_to_be_clickable((By.ID, "searchinput"))).send_keys(url, "\n")  # input url
        wait2.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"msg\"]/div/div/div[1]/h5/button[3]"))).click()
        print(fade.fire('[* | '+str(current_time)+'] Views sent ! [ttw = 10min] [id=2]'), end="\r")
        sleep(603)
        driver2.refresh()
        main2()
    except:
        try:
            pass
        except:
            print("[x | "+str(current_time)+"] NOT AVAILABLE [homedecoratione.com]")
            driver2.refresh()
            main2()


def main():
    global driver
    global wait

    try:
        # selecting views
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button'))).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/input'))).clear() #clearing input
    except:

        try:
            ck = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[3]/div/div[4]/div/p/small")))
            if ck.text == "soon will be update":
                print("[x | "+str(current_time)+"] Unavailable => Views", end="\r")
                sleep(999)
                captcha_ai()
            else:
                driver.refresh()
                main()
        except:
            pass
        print("[x | "+str(current_time)+"] HUH? ERROR")
        sleep(1)
        driver.refresh()
        sleep(5)
        captcha_ai()
    try:
        print(fade.water('[* | '+str(current_time)+'] Sending URL'), end="\r")
        sleep(0.1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/input'))).send_keys(url)
        sleep(0.1)# input url
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/form/div/div/button'))).click()  # searching
        try:
            #try find send views button
            tv = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[5]/div/div/div[1]/div/form/button"))) #get views num on send button
            print(fade.brazil("[- | "+str(current_time)+"] Total views: " + tv.text), end="\r")
            wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[5]/div/div/div[1]/div/form/button'))).click()  # send views
        except:
            #if no, read timer and wait that amount of time and then reload
            sleep(3)
            lmt = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h4")))
            timer_message = lmt.text
            minutes = int(timer_message.split()[2])
            seconds = int(timer_message.split()[4])

            time_to_wait = (minutes * 60 + seconds)
            print("[* | "+str(current_time)+"] Waiting => ", time_to_wait, 'seconds')
            sleep(time_to_wait)
            main()
        main()
    except:
        try:
            #if no input, refresh and try click on views again
            driver.refresh()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button').click()
            main()
        except:
            #if still can't find element, reload script!
            captcha_ai()


def captcha_ai():
    driver.set_window_position(0, 0)
    print('[*] Make sure that captcha is solved on both windows [id=1]')

    try:
        #solve captcha and try clicking on views
        waits.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button'))).click()
        driver.refresh()
        #driver.find_element(By.XPATH, '')
        print(fade.random("[* | " + str(current_time) + "] Access Enabled [id=zefoy.com]"), end="\r")
        driver.set_window_position(-10000, 0)
        main()
    except:
        print('[*] Make sure that captcha is solved on both windows [id=1]')
        sleep(1)
        captcha_ai()


def captcha_ai2():
    driver2.set_window_position(600, 0)
    print('[*] Make sure that captcha is solved on both windows [id=2]')
    try:
        waits2.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div[1]/div[3]/div/div/button'))).click()
        driver2.refresh()
        print(fade.random("[* | " + str(current_time) + "] Access Enabled [id=homedecoratione.com]!"), end="\r")
        driver2.set_window_position(-10000, 0)
        main2()
    except:
        driver2.set_window_position(0, 0)
        print('[*] Make sure that captcha is solved on both windows [id=2]')
        sleep(1)
        captcha_ai2()


if __name__ == "__main__":
    print(fade.purplepink(r'''
 ██░ ██▓██   ██▓ ▄▄▄▄    ██▀███   ██▓▓█████▄     ██▒   █▓ ██▓▓█████  █     █░  ██████ TM
▓██░ ██▒▒██  ██▒▓█████▄ ▓██ ▒ ██▒▓██▒▒██▀ ██▌   ▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░▒██    ▒ 
▒██▀▀██░ ▒██ ██░▒██▒ ▄██▓██ ░▄█ ▒▒██▒░██   █▌    ▓██  █▒░▒██▒▒███   ▒█░ █ ░█ ░ ▓██▄   
░▓█ ░██  ░ ▐██▓░▒██░█▀  ▒██▀▀█▄  ░██░░▓█▄   ▌     ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█   ▒   ██▒
░▓█▒░██▓ ░ ██▒▓░░▓█  ▀█▓░██▓ ▒██▒░██░░▒████▓       ▒▀█░  ░██░░▒████▒░░██▒██▓ ▒██████▒▒
 ▒ ░░▒░▒  ██▒▒▒ ░▒▓███▀▒░ ▒▓ ░▒▓░░▓   ▒▒▓  ▒       ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░
 ▒ ░▒░ ░▓██ ░▒░ ▒░▒   ░   ░▒ ░ ▒░ ▒ ░ ░ ▒  ▒       ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  ░ ░▒  ░ ░
 ░  ░░ ░▒ ▒ ░░   ░    ░   ░░   ░  ▒ ░ ░ ░  ░           ░░   ▒ ░   ░     ░   ░  ░  ░  ░  
 ░  ░  ░░ ░      ░         ░      ░     ░                        ░   ░     ░  ░    ░   
        ░ ░           ░               ░               ░
[1] You will have to solve 2 captchas
[2] There will be a browser on your left and right
[3] Do not close the 2 browsers --
[4] Full creds to: -* tekky *- | Tekky#9999 | t.me/xtekky | xtekky.ml
[5] Make sure that you joined the server: discord.gg/onlp'''))

    start = input('Press any key to launch: ')
    url = 'https://www.tiktok.com/@crypto.shit/video/7082763044731817221?is_from_webapp=1&sender_device=pc&web_id=7062836892223768069'

    #driver 1 (zefoy.com)
    driver = uc.Chrome()
    driver.get('https://zefoy.com')
    wait = WebDriverWait(driver, 5)
    waits = WebDriverWait(driver, 20)

    #driver 2 ('https://homedecoratione.com)
    driver2 = uc.Chrome()
    driver2.get('https://homedecoratione.com')
    driver2.set_window_position(600, 0)
    wait2 = WebDriverWait(driver2, 5)
    waits2 = WebDriverWait(driver2, 20)

    a = threading.Thread(target=time)
    b = threading.Thread(target=captcha_ai)
    c = threading.Thread(target=captcha_ai2)

    a.start()
    b.start()
    c.start()