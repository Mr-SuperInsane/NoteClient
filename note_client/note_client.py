from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from janome.tokenizer import Tokenizer
from time import sleep
from random import randint


class Note:

    def __init__(self, email:str, password:str, user_id:str):
        '''
        Enter the email address and password for your note account
        '''
        self.email = email
        self.password = password
        self.user_id = user_id

    def __str__(self):
        return f"Email : {self.email} / User ID : {self.user_id} / Password : {self.password}"

    def create_article(self, title:str, file_name:str, input_tag_list:list, post_setting:bool=False, headless:bool=True):
        '''
        Create new article
        -----
        > title : article title
        > file_name : article content file
        > tag_list : tag of article
        > post_setting : save draft or post (default : save draft)
        > headless : show or not show page (default : not show)
        '''

        if title and input_tag_list and isinstance(input_tag_list, list):
            options = Options()
            if headless:
                options.headless = True

            driver = webdriver.Firefox(options=options)
            driver.get('https://note.com/login?redirectPath=%2Fnotes%2Fnew')

            wait = WebDriverWait(driver, 10)

            sleep(1)
            email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
            email.send_keys(self.email)
            sleep(0.5)
            password = wait.until(EC.presence_of_element_located((By.ID, 'password')))
            password.send_keys(self.password)
            sleep(0.5)
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".o-login__button button")))
            button.click()
            sleep(0.5)

            sleep(2)
            textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
            textarea.click()
            textarea.send_keys(title)
            textarea.send_keys(Keys.ENTER)


            with open(file=file_name, mode='r', encoding='utf-8')as f:
                text = f.read()

            edit_text = text.split('\n')

            for i, text in enumerate(edit_text):
                '''
                記事処理の方法を改善
                '''
                pattern = re.compile(r'\d+\. ')

                if '## ' in text:
                    if '### ' in text:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys("###")
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.SPACE)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace('### ',''))
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER) 

                    else:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys("##")
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.SPACE)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace('## ',''))
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER) 

                elif text.startswith('- '):
                    if edit_text[i-1].startswith('- '):
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace('- ',''))
                    else:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys("-")
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.SPACE)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace('- ',''))
                    try:
                        if edit_text[i+1].startswith('- '):
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                        else:
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                    except:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)

                elif pattern.search(text):
                    number = text[0]
                    if pattern.search(edit_text[i-1]):
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace(f'{number}. ',''))
                    else:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(f'{number}.')
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.SPACE)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(text.replace(f'{number}. ',''))
                    try:
                        if pattern.search(edit_text[i+1]):
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                        else:
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                    except:
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)
                
                elif text.count('-') >= 3:
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys('---')
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(Keys.ENTER)

                elif text == '':
                    try:
                        if edit_text[i+1].startswith('## ') or edit_text[i+1].startswith('- ') or pattern.search(edit_text[i+1]) or text == '':
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                        else:
                            continue
                    except:
                        continue
                        
                else:
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(text)
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(Keys.ENTER)

                    try:
                        if edit_text[i+1].startswith('## ') or edit_text[i+1].startswith('- ') or pattern.search(edit_text[i+1]):
                            sleep(0.5)
                            active_element = driver.execute_script("return document.activeElement;")
                            active_element.send_keys(Keys.ENTER)
                    except:
                        continue

            sleep(0.5)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            driver.execute_script('window.scrollTo(0, 0)')
            sleep(1)

            t = Tokenizer()
            keywords = [token.surface for token in t.tokenize(title) if token.part_of_speech.startswith('名詞,一般') or token.part_of_speech.startswith('名詞,固有名詞') or token.part_of_speech.startswith('名詞,サ変接続')]
            search_word = max(keywords, key=len) if keywords else None
            # 手動でキーワードを入力

            sleep(0.5)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/main/div[1]/button")))
            button.click()
            sleep(0.5)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/main/div[1]/div/div[2]/button")))
            button.click()
            sleep(1)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/button")))
            button.click()
            sleep(0.5)
            keyword = driver.execute_script("return document.activeElement;")
            keyword.send_keys(search_word)
            # 検索ボタン
            sleep(2)
            button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/button")
            button.click()
            # 画像の取得
            sleep(3)
            parent_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]")))
            img_elements = parent_element.find_elements(By.TAG_NAME, 'img')
            # 画像の選択
            # index = randint(0,len(img_elements)-1) ランダム指定
            index = 0 #　上位指定
            img_elements[index].click()
            # 全画像URL取得
            # img_url_list = []
            # for img_element in img_elements:
            #     src_url = img_element.get_attribute('src')
            #     img_url_list.append(str(src_url))
            ## 画像の挿入
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div[2]/div/div[5]/button[2]")))
            button.click()
            sleep(2)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/button[2]")))
            button.click()
            sleep(10)

            # 投稿ボタン
            if post_setting:
                button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/header/div/div[2]/div/button[2]")))
                button.click()

                # 記事URL
                sleep(2)
                url = driver.current_url
                cut_url = url.split('/')
                post_id = cut_url[4]
                post_url = f'https://note.com/{self.user_id}/n/{post_id}'

                # おすすめのタグを取得
                # tag_list = []
                # for i in range(len(driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/main/section[1]/div[2]/div/div[2]/div//button"))):
                #     button = wait.until(EC.presence_of_element_located((By.XPATH, f"/html/body/div[1]/div[3]/div[1]/div[2]/main/section[1]/div[2]/div/div[2]/div/button[{i+1}]")))
                #     tag_list.append(str(button.text))

                # タグ指定(リスト)
                sleep(1)
                input_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[2]/main/section[1]/div[2]/div/div[1]/input')))
                input_element.click()
                sleep(0.5)
                input = driver.execute_script("return document.activeElement;")
                for tag in input_tag_list:
                    sleep(0.5)
                    input.send_keys(tag)
                    sleep(0.5)
                    input = driver.execute_script("return document.activeElement;")
                    input.send_keys(Keys.SPACE)

                button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div/button")))
                button.click()

                driver.quit()

                return post_url

            # 下書き保存ボタン
            else:
                button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/header/div/div[2]/div/button[1]")))
                button.click()

                driver.quit()

                return 'success'
            
        else:
            return 'error'
