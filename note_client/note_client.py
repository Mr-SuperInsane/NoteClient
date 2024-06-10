from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from janome.tokenizer import Tokenizer
from time import sleep
from random import randint
import builtins
import re

class Note:

    def __init__(self, email:str, password:str, user_id:str):
        '''
        Enter the email address and password for your note account
        '''
        self.email = email
        self.password = password
        self.user_id = user_id

    def __str__(self):
        return f"Email : {self.email} / User ID : {self.user_id}"

    def create_article(self, title:str, input_tag_list:list, image_index='random', post_setting:bool=False, file_name:str=None, headless:bool=True, text:str=None):
        '''
        Create new article
        -----
        > title : article title
        > file_name : article content file ( default : None )
        > tag_list : tag of article
        > image_index : index number of the article image
        > post_setting : save draft or post (default : save draft)
        > headless : show or not show page (default : not show)
        > text : archicle content text (default : None)
        '''

        if title and isinstance(input_tag_list, list) and (image_index=='random' or isinstance(image_index, int) or isinstance(image_index, type(None))) and (file_name is not None or text is not None):
            pass
        else:
            return 'Required data is missing.'

        options = Options()
        if headless:
            # selenium>=4.8.0
            options.add_argument("--headless=new")

        driver = webdriver.Firefox(options=options)
        driver.get('https://note.com/login?redirectPath=%2Fnotes%2Fnew')

        wait = WebDriverWait(driver, 10)

        sleep(5)
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

        if text is None:
            with open(file=file_name, mode='r', encoding='utf-8')as f:
                text = f.read()

        edit_text = text.split('\n')

        url = re.compile(r'https?://')
        pattern = re.compile(r'^\d+\. ')
        minusgt = re.compile(r'^[\->] ')
        blockquote = False
        
        for i, text in enumerate(edit_text):

            if text.startswith('### '):
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

            elif text.startswith('## '):
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

            #elif text.startswith('- '):
            #    if edit_text[i-1].startswith('- '):
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys(text.replace('- ',''))
            #    else:
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys("-")
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys(Keys.SPACE)
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys(text.replace('- ',''))
            #    try:
            #        if edit_text[i+1].startswith('- '):
            #            sleep(0.5)
            #            active_element = driver.execute_script("return document.activeElement;")
            #            active_element.send_keys(Keys.ENTER)
            #        else:
            #            sleep(0.5)
            #            active_element = driver.execute_script("return document.activeElement;")
            #            active_element.send_keys(Keys.ENTER)
            #            sleep(0.5)
            #            active_element = driver.execute_script("return document.activeElement;")
            #            active_element.send_keys(Keys.ENTER)
            #    except:
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys(Keys.ENTER)
            #        sleep(0.5)
            #        active_element = driver.execute_script("return document.activeElement;")
            #        active_element.send_keys(Keys.ENTER)

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

            elif text == "---":
                # note does not support "___" and "***"
                sleep(0.5)
                active_element = driver.execute_script("return document.activeElement;")
                active_element.send_keys(Keys.ENTER)
                sleep(0.5)
                active_element = driver.execute_script("return document.activeElement;")
                active_element.send_keys('---')

            elif text == '':
                if blockquote:
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(' ')
                try:
                    if edit_text[i+1].startswith('## ') or minusgt.search(edit_text[i+1]) or pattern.search(edit_text[i+1]) or text == '':
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)
                    else:
                        continue
                except:
                    continue

            elif url.search(text):
                for i in range(len(text)):
                    sleep(0.1)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(text[i])
                sleep(0.1)
                active_element = driver.execute_script("return document.activeElement;")
                active_element.send_keys(Keys.ENTER)
                
                try:
                    if edit_text[i+1].startswith('## ') or minusgt.search(edit_text[i+1]) or pattern.search(edit_text[i+1]):
                        sleep(0.5)
                        active_element = driver.execute_script("return document.activeElement;")
                        active_element.send_keys(Keys.ENTER)
                except:
                    continue
                
            elif text == "```":
                # block quote
                if blockquote:
                    # exit
                    blockquote = False
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(Keys.ENTER)
                else:
                    # enter
                    blockquote = True
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys('```')
                
            elif minusgt.search(text):
                mark = text[0]
                markspace = f"{mark} "
                if edit_text[i-1].startswith(markspace):
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(text.replace(mark,''))
                else:
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(mark)
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(Keys.SPACE)
                    sleep(0.5)
                    active_element = driver.execute_script("return document.activeElement;")
                    active_element.send_keys(text.replace(mark,''))
                try:
                    if edit_text[i+1].startswith(markspace):
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

            else:
                sleep(0.1)
                active_element = driver.execute_script("return document.activeElement;")
                active_element.send_keys(text)
                sleep(0.1)
                active_element = driver.execute_script("return document.activeElement;")
                active_element.send_keys(Keys.ENTER)

                try:
                    if edit_text[i+1].startswith('## ') or minusgt.search(edit_text[i+1]) or pattern.search(edit_text[i+1]):
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
        search_word = builtins.max(keywords, key=len) if keywords else None

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
        sleep(2)
        button = driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[1]/div/div[2]/button")
        button.click()
        sleep(3)
        parent_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]")))
        img_elements = parent_element.find_elements(By.TAG_NAME, 'img')
        if isinstance(image_index, int) and 0 <= int(image_index)<= int(len(img_elements)-1):
            index = image_index
        else:
            max = len(img_elements)-1
            if max >= 0:
                index = randint(0,max)
            else:
                index = -1
        if index < 0 or isinstance(image_index, type(None)):
            keyword.send_keys(Keys.ESCAPE)
        else:
            img_elements[index].click()
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2]/div/div[2]/div/div[5]/button[2]")))
            button.click()
            sleep(2)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[3]/button[2]")))
            button.click()
            sleep(10)

        if post_setting:
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/header/div/div[2]/div/button[2]")))
            button.click()

            sleep(2)
            url = driver.current_url
            cut_url = url.split('/')
            post_id = cut_url[4]
            post_url = f'https://note.com/{self.user_id}/n/{post_id}'

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
            res = {
                'run':'success',
                'title':title,
                'file_path':file_name,
                'tag_list':input_tag_list,
                'post_setting':'Public',
                'post_url':post_url
            }
        else:
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/header/div/div[2]/div/button[1]")))
            button.click()
            res = {
                'run':'success',
                'title':title,
                'file_path':file_name,
                'tag_list':input_tag_list,
                'post_setting':'Draft',
            }
        driver.quit()
        return res
            
