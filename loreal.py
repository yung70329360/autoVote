from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import numpy as np
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from joblib import Parallel, delayed


class GetInputs():
    def __init__(self):
        pass
    

    def getName(self, names, driver):
        content = np.random.choice(names).split(' ')
        # driver.get('https://name.longwin.com.tw/name2passport.php')
        # nameInp = xpathWait(driver, '//*[@id="div_form"]/form/input[1]')
        # nameInp.send_keys(randomName)
        # searchButton = xpathWait(driver, '//*[@id="div_form"]/form/input[2]')
        # searchButton.click()
        # driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # content = xpathWait(driver, '//*[@id="result"]/ul[1]/li[1]').text.split(' ')
        firstName = content[0]
        secondName = content[1] + ' ' +content[2]

        return firstName, secondName
    
    def getMail(self):
        letters = 'a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z'.split('、')
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        letterNum = np.random.choice(list(range(6, 10)))
        numberNum = np.random.choice(list(range(6, 10)))
        order = np.random.choice([0, 1])

        email = ''
        if order == 0:
            for i in range(letterNum):
                letter = np.random.choice(letters)
                email += letter
            for i in range(numberNum):
                number = np.random.choice(numbers)
                email += number
        else:
            for i in range(numberNum):
                number = np.random.choice(numbers)
                email += number           
            for i in range(letterNum):
                letter = np.random.choice(letters)
                email += letter

        ends = ['@google.com', '@yahoo.com', '@outlook.com', '@porton.me']
        end = np.random.choice(ends)
        return email + end

    def getPassword(self):
        letters = 'a、b、c、d、e、f、g、h、i、j、k、l、m、n、o、p、q、r、s、t、u、v、w、x、y、z'.split('、')
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        letterNum = np.random.choice(list(range(4, 6)))
        numberNum = np.random.choice(list(range(4, 6)))
        order = np.random.choice([0, 1])
        password = ''
        if order == 0:
            for i in range(letterNum):
                letter = np.random.choice(letters)
                password += letter
            for i in range(numberNum):
                number = np.random.choice(numbers)
                password += number
        else:
            for i in range(numberNum):
                number = np.random.choice(numbers)
                password += number           
            for i in range(letterNum):
                letter = np.random.choice(letters)
                password += letter
        return password


def xpathWait(driver, xpath):
        result = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return result

def get_inputs(names, driver):
    get = GetInputs()
    name= get.getName(names, driver)
    email = get.getMail()
    password = get.getPassword()
    return name, email, password

def inspect(driver):
    try:
        secondPage(driver)
        
    except:
        error = xpathWait(driver, '//*[@id="centerPanel"]/div/div[2]/div/div[2]/div/div[1]')
        email_inp = xpathWait(driver, '//*[@id="63:2;a"]')
        get = GetInputs()
        email = get.getMail()
        password = get.getPassword()

        email_inp = xpathWait(driver, '//*[@id="76:2;a"]')
        email_inp.clear()
        email_inp.send_keys(email)
        
        password_inp = xpathWait(driver, '//*[@id="91:2;a"]')
        password_inp.clear()
        password_inp.send_keys(password)
        
        passwordCheck_inp = xpathWait(driver,'//*[@id="104:2;a"]' )
        passwordCheck_inp.clear()
        passwordCheck_inp.send_keys(password)
        nextStep = xpathWait(driver, '//*[@id="centerPanel"]/div/div[2]/div/div[2]/div/div[7]/button')
        nextStep.click()
        # time.sleep(5)
        inspect(driver)

def firstPage(name, email, password, driver):

    # time.sleep(3)

    firstName_inp = xpathWait(driver, '//*[@id="50:2;a"]')
    firstName_inp.send_keys(name[0])
    # time.sleep(3)
    secondName_inp = xpathWait(driver, '//*[@id="63:2;a"]')
    secondName_inp.send_keys(name[1])
    # time.sleep(3)
    email_inp = xpathWait(driver, '//*[@id="76:2;a"]')
    email_inp.send_keys(email)
    # time.sleep(3)
    password_inp = xpathWait(driver, '//*[@id="91:2;a"]')
    password_inp.send_keys(password)
    # time.sleep(3)
    passwordCheck_inp = xpathWait(driver,'//*[@id="104:2;a"]' )
    passwordCheck_inp.send_keys(password)
    nextStep = xpathWait(driver, '//*[@id="centerPanel"]/div/div[2]/div/div[2]/div/div[6]/button')
    # time.sleep(3)
    nextStep.click()
    

def secondPage(driver):
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    gender = xpathWait(driver, f'//*[@id="user_answers_attributes_0_choice_ids"]/option[{np.random.choice([2, 3])}]').click()
    # school = np.random.choice(['ntu', 'ntu', 'nccu', 'nccu', 'ncu', 'nthu', 'ntnu'])
    # schoolName = xpathWait(driver, '//*[@id="user_answers_attributes_1_content-selectized"]')
    # schoolName.send_keys(school)

    # startdate_list = xpathWait(driver, '//*[@id="user_answers_attributes_1_start_at_1i"]').click()
    # random_start = np.random.choice([8, 9, 10, 11])
    # startdate = xpathWait(driver, f'//*[@id="user_answers_attributes_1_start_at_1i"]/option[{random_start}]').click()
    
    
    # end_num = np.random.choice([2, 4])
    # random_end = random_start - end_num
    # enddate_list = xpathWait(driver, '//*[@id="user_answers_attributes_1_end_at_1i"]').click()
    # enddate = xpathWait(driver, f'//*[@id="user_answers_attributes_1_end_at_1i"]/option[{random_end}]').click()
    
    location = xpathWait(driver, '//*[@id="user_answers_attributes_2_choice_ids"]/option[65]').click()
    
    random_age = np.random.choice(list(range(19, 24)))
    age = xpathWait(driver, f'//*[@id="user_answers_attributes_3_choice_ids"]/option[{random_age-16}]').click()
    
    study = xpathWait(driver, f'//*[@id="user_answers_attributes_4_choice_ids"]/option[{np.random.choice(list(range(2, 38)))}]').click()
    
    # driver.find_element(By.XPATH, '//*[@id="user_terms_of_service"]').click()
    # driver.find_element(By.XPATH, '//*[@id="user_privacy_policies"]').click()
    checkbox1 = xpathWait(driver, '//*[@id="new_user"]/div[19]/div/div/label').click()
    checkbox2 = xpathWait(driver, '//*[@id="new_user"]/div[20]/div/div/label').click()

    next = xpathWait(driver, '//*[@id="create-account-submit"]').click()

def thirdPage(driver):
    # driver.get('https://brandstorm.loreal.com/en/juries/vDmsA2-HS7z5FkDQYB6lQQ/participations/47/vote?order=random&amp;scope=all')
    # https://brandstorm.loreal.com/en/juries/vDmsA2-HS7z5FkDQYB6lQQ/participations/205/vote?order=random&amp;scope=all
    # xpathWait(driver, '//*[@id="challenge-37"]/div[1]/div[4]/div/div[2]/div[1]/div[4]/div/form/button').click()
    time.sleep(5)
    xpathWait(driver , '//*[@id="jury-search"]').send_keys('Rebirth')
    # xpathWait(driver , '//*[@id="jury-search"]').send_keys('MTK6')
    time.sleep(5)
    xpathWait(driver, '//*[@id="hits"]/div/div/div[2]/div[3]/div[1]/div/form/button').click()
    time.sleep(5)
    # try:
    #     WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.CSS_SELECTOR, ".link.text-danger"))
    #     like.click()
    #     time.sleep(5)
    # except:
    #     pass


    
    

def main():
    names =['CHEN KANG QI',
 'SONG HAN ZHI',
 'CHEN WAN TING',
 'ZHAO XIN YI',
 'CHEN JIAN YU',
 'LI JIA YING',
 'ZHOU JIA YING',
 'GUO ZHI HONG',
 'LAI XIAO TING',
 'HONG HUI LING',
 'CHEN YUN REN',
 'WANG YUN SHAN',
 'CAI ZHI ZHOU',
 'LI ZHEN YUN',
 'LIU JIAO REN',
 'SHE YE RONG',
 'CHEN JUN JIE',
 'GUO YI NAN',
 'HUANG YA PING',
 'SANG WEN HONG',
 'ZHU QIAO SHAN',
 'LIN PEI XUAN',
 'DENG FENG QING',
 'XIE JIA BIN',
 'HONG LI MEI',
 'CAI LIN HUI',
 'CHEN XIAO PING',
 'LI SHU JIE',
 'WANG KAI YUAN',
 'HUANG XUE XIAO',
 'WU WAN JUN',
 'JIANG RU QI',
 'YANG XIN YI',
 'CAI ZHENG GUI',
 'HUANG XIN YI',
 'LIN YI YUE',
 'LI YI JING',
 'LI PEI RONG',
 'ZHOU JIA WEN',
 'GUO WAN YUAN',
 'LIU JING RU',
 'HUANG ZHENG TING',
 'XIE DONG LAN',
 'ZHANG XIN YI',
 'WANG JUN ZUN',
 'JIAN YU SHENG',
 'CAI PING WEI',
 'LIN YA ZHU',
 'CHEN JIA CAN',
 'HE GONG PEI',
 'LI JUN ZUN',
 'WU JUN ZUN',
 'LIN MEI SHUN',
 'HONG XIAO TING',
 'ZHAO SHAO BO',
 'HU XU YA',
 'LIN XIAO LING',
 'HUANG SHI XING',
 'HUANG DAI YING',
 'WANG MING MING',
 'XIE JIN XUAN',
 'WU SHU FANG',
 'HUANG QIAN DA',
 'WU YI GUI',
 'YANG YI XIN',
 'SHE YE YU',
 'WANG YU QIU',
 'LIN SHU PING',
 'ZHENG YA KUN',
 'ZHANG YI TING',
 'HUANG LI WEI',
 'LIU JIAN WEI',
 'WEI YI JUN',
 'CHEN YOU ZI',
 'ZHANG NAI MENG',
 'CHEN JIAN HANG',
 'CAO JUN ZUN',
 'LAI SHU LING',
 'JIN YUE JI',
 'HONG ZHI YUAN',
 'YAN XUE YU',
 'LIU RU LI',
 'WANG CHEN HUI',
 'SONG SI YU',
 'WU ZI YING',
 'CHEN YU HAN',
 'CHEN GU JIA',
 'LIU YA QI',
 'ZHANG JIAN HUI',
 'LIAN WEI MING',
 'LIN WAN YUAN',
 'LU TIAN WEI',
 'ZHONG SHU HUI',
 'LIU GU JIA',
 'CHEN SHI MEI',
 'LIN JIAN YU',
 'LU LIU REN',
 'WU JIA HENG',
 'CHEN SHAN YU',
 'LIN XIN XIANG',
 'LIN GUAN YU',
 'WU QIONG HUI',
 'HUANG DENG LING',
 'CHEN HUI FA',
 'HONG JIA YU',
 'WU DE DEI',
 'ZHANG ZHI JIE',
 'WANG JIA WEI',
 'SHE YE XI',
 'LI AI YI',
 'CHEN JUN ZUN',
 'CHEN YU QI',
 'CHEN KAI GUI',
 'LIN ZHUO ZHONG',
 'WU QING ZHEN',
 'SHI MAO LAN',
 'ZHA CHA WEI',
 'YANG XIAO SHUN',
 'WEN BING MING',
 'LIN SHI ZHE',
 'ZHANG JIA LIN',
 'WEN ZUO RUI',
 'ZHANG GU JIA',
 'WANG ZI EN',
 'LI YU NAN',
 'LI ZHENG XIA',
 'LIU ZHI XING',
 'JIANG REN BANG',
 'LI MENG JUN',
 'WU JING YI',
 'WU YU JING',
 'CHEN WEI JIE',
 'WU YI NI',
 'YANG GU JIA',
 'WU SHU HUI',
 'SUN JIAN ZHI',
 'QIU XUN HE',
 'XIE YI YAO',
 'WU YI TING',
 'LIN WEI AI',
 'HUANG WAN CHANG',
 'ZHANG MEI HUI',
 'SHE YE XIN',
 'ZHANG YI XIANG',
 'SHEN CHEN SONG',
 'ZHANG JIN FENG',
 'ZHUANG YA XUAN',
 'CHEN SU YING',
 'LAN JIAN MING',
 'WANG PEI RU',
 'XIE HANG XING',
 'CAI YA PING',
 'CHEN WEI XIANG',
 'LAI PEI RU',
 'ZHANG DAN ZHONG',
 'CENG ZENG XIN',
 'HONG GUO HUA',
 'MING ZHE WEI',
 'WANG YU TIAN',
 'LIU ZHONG CHONG',
 'LIN WAN YU',
 'CHEN PEI YU',
 'HONG FENG ZHI',
 'KE YA WEN',
 'LIU JIA YING',
 'CHEN ZHI SHUN',
 'ZHANG BI ZHI',
 'ZHENG YA XIANG',
 'KOU ZHE ZI',
 'HE JIA RONG',
 'GONG JUN YI',
 'ZHU JING FAN',
 'ZHANG ZHI JIE',
 'ZHANG XUAN YAN',
 'LI YA JUN',
 'LIU DAI BAO',
 'CHEN HUI BIN',
 'CHEN MEI JUAN',
 'JIANG HAO SHAN',
 'YANG CUI RU',
 'YANG XING XIN',
 'LI XIN KAI',
 'HU MING RU',
 'LIU YAN XIANG',
 'JIANG YAN HAN',
 'ZHANG HAN YING',
 'WANG XIAN YANG',
 'LIN CI YAN',
 'HONG XIAO TING',
 'WANG BO SHI',
 'CHEN WEI ZHU',
 'HUANG YUN TIAN',
 'LIU ZHE YU',
 'LAI JIA LIN',
 'LIAO SHENG HUI',
 'LIU SHU HUI',
 'CHEN YU LUN',
 'SHE YE XIANG',
 'LI RUO RE',
 'SHI YA TING',
 'HUANG LI HU',
 'SHE YE BO',
 'JIN RUI QI',
 'CHEN SHEN XIN',
 'ZHAO YU HAN',
 'ZHOU JUN HAN',
 'CHEN YU RU',
 'CHEN XIN YI',
 'CHEN JIAN HONG',
 'ZHOU JUN ZUN',
 'LI YAN XIANG',
 'ZHANG GU JIA',
 'CHEN SHAN FU',
 'QIU SHU HUA',
 'BI BO YANG',
 'ZHANG YA WEN',
 'LIN MIN XIAN',
 'CHEN SHI XU',
 'ZHOU SHU ZHEN',
 'CHEN HUI YU',
 'CHEN MENG XIU',
 'ZHANG YUN XUAN',
 'CHEN HONG YIN',
 'KE YANG HUA',
 'LI CHENG MIN',
 'WU YU MING',
 'JIANG ZHI YING',
 'WU JIA YUN',
 'LI ZHI JIE',
 'LI CUI CAN',
 'ZHANG YA FANG',
 'CHEN XIN YI',
 'YANG YA TING',
 'ZHANG JING YI',
 'CHEN YI JUN',
 'CHI FANG ZUO',
 'HUANG ZHI TIAN',
 'PING FENG YOU',
 'WEN HONG YI',
 'WU GU JIA',
 'HUANG JIA RONG',
 'ZHANG YU SHAO',
 'LUO LIANG TAI',
 'CHEN YAN LUN',
 'LIN GUAN YUN',
 'YU QIU YAN',
 'LIAO WAN JUN',
 'ZHANG LI WEN',
 'HAN SHU HUI',
 'LIN KAI TING',
 'FENG PEI LING',
 'LIAN WAN TING',
 'RUAN YI RU',
 'LIN RUI WEN',
 'LIN GU JIA',
 'PING FENG HANG',
 'XIE MING FEN',
 'ZHANG BAI HANG',
 'HU KE WAN',
 'HUANG XIN SHI',
 'GAO SHU ZHEN',
 'MENG YU FENG',
 'YANG ZONG YING',
 'WU XIU JUAN',
 'LIN SHU JUN',
 'YUAN ZHI PEI',
 'CHEN JIAN KUN',
 'SONG MING ZHU',
 'HUANG QIAN ZI',
 'LI KUN HUI',
 'MEI WEI LUN',
 'LIN REN WEN',
 'WENG YIN DA',
 'LIN BAO MEI',
 'JIA XIA XIU',
 'XIE LI FANG',
 'SU YA WEN',
 'MA YA TING',
 'LI YANG JING',
 'LAI YA RU',
 'XIAO JUN ZUN',
 'PAN SHAO YU',
 'LIN JUN ZUN',
 'LIN JIAN XUAN',
 'QIU YING DA',
 'HUANG WEN SHU',
 'LAI YI FEN',
 'LAN ZHENG RUI',
 'PENG SU YIN',
 'CHEN YUN NIAN',
 'ZHU SHI MING',
 'CHEN YI GANG',
 'LI JIAN MING',
 'ZHENG WEI (建議用此名字)',
 'XU WEI BO',
 'WANG ZI NIAN',
 'LIN YU QING',
 'XIE YI EN',
 'HUANG WEI JUN',
 'ZHANG YOU YAN',
 'LI DA DAI',
 'LI WEN HUAN',
 'ZHANG YU MING',
 'LIN YU ZHOU',
 'ZHANG GU JIA',
 'CAO GU JIA',
 'SONG SHU FANG',
 'JIANG CHENG HAN',
 'ZHANG ZI LING',
 'ZHANG SHI XIANG',
 'XIE MIN WEN',
 'WANG XI XIN',
 'LIN YU PEI',
 'FANG JIA RONG',
 'GUO WEI TING',
 'LIN JIA LUN',
 'WANG XIAO HANG',
 'MENG XIAO LU',
 'LI DE (建議用此名字)',
 'WU BO LONG',
 'LIU QING JI',
 'WANG SHU HUI',
 'LIN JIA ZHI',
 'LIANG JIAN YU',
 'CAI LING WEN',
 'LIN YU JING',
 'CHEN JIAN LIANG',
 'LIN MEI YU',
 'WU YI GU',
 'HU XU YA',
 'HOU SHU HUA',
 'LIU YI TING',
 'XIE WAN YUAN',
 'CHEN SHU LING',
 'HUANG ZHENG WEI',
 'HUANG JUN ZUN',
 'CHEN ZHI XUAN',
 'CHEN SHENG KAI',
 'CAI ZI HAO',
 'LI YOU CHENG',
 'CAI YI CHEN',
 'LIU JING FANG',
 'HUANG YI LONG',
 'CHEN YA LING',
 'RUAN PENG ZI',
 'CHEN YI XUAN',
 'ZHENG YAN LIANG',
 'GUO YA YI',
 'CHEN WEI TING',
 'JIANG MENG JIANG',
 'LIAO YONG YUN',
 'ZHONG XIAN DING',
 'CHEN SHI KAI',
 'TENG YI TING',
 'QU JIAN TING',
 'CHEN WEI BO',
 'YAO YI TIAN',
 'KE YA TING',
 'LU LIU GUAN',
 'ZHAN SHI HAO',
 'ZHANG LING HUAN',
 'CHEN SHI FA',
 'ZHU YA PING',
 'JIANG TING YU',
 'CHEN YI QIU',
 'CHEN JIA YIN',
 'PING FENG WEN',
 'ZHANG XUAN GU',
 'LIN JUN ZUN',
 'LIN FANG GONG',
 'WU GUI LIN',
 'QIU MEI JUAN',
 'WANG RUO RE',
 'CAI SHANG YU',
 'CHEN GUO NI',
 'CHEN YONG PEI',
 'LI MEI HUI',
 'JIANG REN YUAN',
 'SHE YE HUI',
 'CHEN DENG ZHU',
 'PING FENG FANG',
 'ZHANG GU JIA',
 'GUO YUN YIN',
 'WU WEI TING',
 'CAI JIA SHAN',
 'ZHANG JING YING',
 'HONG SI HAN',
 'YANG YONG FANG',
 'LI LIN WEI',
 'YANG JIA YOU',
 'LI JIA DONG',
 'PENG ZHEN XUAN',
 'LUO YOU GUANG',
 'CHEN YA LING',
 'WANG JIA LING',
 'LIN HANG XING',
 'DING ZHENG ZHE',
 'ZHANG WU YU',
 'HUANG YAN YU',
 'LIN YAN JUN',
 'CHEN SHEN XIN',
 'CHEN WEI HUI',
 'WEN ZHE WEI',
 'HUANG WAN FEI',
 'LI XIU GUI',
 'LI ZONG YING',
 'LIN GU JIA',
 'GUO SHAN SHAO',
 'WU JUN ZUN',
 'CUI GU JIA',
 'CHEN ZHI JIA',
 'ZHANG KAI YUE',
 'LI WEI TING',
 'CHEN JIA RONG',
 'ZHANG YI GONG',
 'CAI SHU FANG',
 'CHEN HUI LING',
 'ZHANG XIU CHEN',
 'LIN YUN BO',
 'WU HUI SHEN',
 'CHEN JING GUANG',
 'HUANG YU REN',
 'CHEN CI TING',
 'DENG JIAN LIN',
 'XIAO YIN QIAN',
 'GUO GU JIA',
 'PING FENG SHU',
 'ZHANG QING RONG',
 'YANG ZHI WEN',
 'FANG LIN ZHI',
 'LU WEI TING',
 'CUI GUO WEI',
 'CAO LIN BIN',
 'CHEN JUN ZUN',
 'CAI YAN WEN',
 'CHEN HUA HE',
 'CHEN LI EN',
 'QIU ZHI JUN',
 'ZHANG YU QUAN',
 'CAI DONG XUAN',
 'WU XING XIN',
 'DU WEI REN',
 'YAN YU HE',
 'WANG YU REN',
 'YANG LI TIAN',
 'LIU XIAO YUN',
 'CHEN YA TING',
 'LIANG GUAN YU',
 'ZHOU LIANG JUN',
 'CHEN PIN SHAN',
 'YOU SHU FANG',
 'XIE GU JIA',
 'WU ZONG XIANG',
 'SONG YIN LAI',
 'ZHANG KAI ZHEN',
 'SHE YE JIAN',
 'WU AI YI',
 'LIN GUAN YU',
 'HUANG MEI QIAN',
 'GUO HAN CAI',
 'ZHANG RONG HENG',
 'HUANG XIANG MING',
 'RUAN SHEN XIN',
 'LAI HUI BO',
 'CAI YUN RU',
 'JIA XIA SI',
 'SU ZHENG ZHE',
 'CAO RU ZHI',
 'LIN JIAN TIAN',
 'CHEN ZHEN YING',
 'LIANG YONG SHEN',
 'CHEN WAN YUAN',
 'LAI DAN SHI',
 'LIN YI YAN',
 'ZHANG JIN FANG',
 'DU SU ZHEN',
 'LAI GENG SHEN',
 'WANG MIAO GONG',
 'WANG YU WEI',
 'WENG MING TING',
 'LIN YI YUE',
 'LIN YA JUN',
 'LU HAN HENG',
 'LI YI WEI',
 'KOU CHEN YU',
 'ZHU YI ZI',
 'CHEN XIAN ZHEN',
 'CHEN SHU HENG',
 'GUO CHENG QIANG',
 'WU JUN YU',
 'WU WEN YIN',
 'CHEN YU SHAN',
 'SUN CHENG EN',
 'HUANG WEI HAN',
 'WANG ZI XIANG',
 'GAO YI WEN',
 'SHEN CHEN YUE',
 'ZHANG BAO YU',
 'HE JUN ZUN',
 'ZHANG ZHI REN',
 'HUANG YUN HUI',
 'XIE JIA JIE',
 'QIU PIN ZHU',
 'LIAN XIN HAI',
 'LIN JIN HENG',
 'CHEN XIAN ZHI',
 'CAI SHU LING',
 'YAO SHU HUA',
 'LIN ZI QIN',
 'CHEN LIN ZHI',
 'WU SHAO LIN',
 'LIN JING YI',
 'HUANG CHANG YOU',
 'LIN HAI RONG',
 'LIN YAN CHENG',
 'ZHANG CHUN XU',
 'LIN YI SHENG',
 'DING ZHENG NAI',
 'CHEN SHEN XIN',
 'HUANG CAI LIANG',
 'LIU JIN DA',
 'LI XIN JUN',
 'ZHANG JIA LING',
 'LI YAN SHU',
 'LU JIA QI',
 'CAI SHI TING',
 'YAN YI JIE',
 'CHEN GU JIA',
 'HONG JUN QIU',
 'FU BO SONG',
 'GUAN JUN ZUN',
 'YANG JIAN ZHONG',
 'WANG GU JIA',
 'WAN JIN YU',
 'LIN PEI WEI',
 'GUO MEI HUI',
 'CAI WEN YUAN',
 'WU YUN RU',
 'HE JIA REN',
 'LI QIAN MEI',
 'WANG ZHENG XIAN',
 'WANG YI LONG',
 'CHEN YAN TING',
 'CENG ZENG CAN',
 'ZHANG YU QIAN',
 'LI YI YI',
 'FANG XIANG ZI',
 'WANG DONG SHUI',
 'NI YU CHUN',
 'PAN WEN CHUN',
 'WU ZONG BING',
 'CHEN YING FU',
 'JING YING PEI',
 'ZHANG YU HUA',
 'CHEN XIU YU',
 'CAI GU JIA',
 'SHEN CHEN YI',
 'SHANG TANG JIAN',
 'ZHANG YU LIN',
 'HUANG SI YING',
 'HUANG JIA WEN',
 'LAI ZHEN QUAN',
 'ZHANG JIA ZI',
 'LIU YA MING',
 'BAI BO XIN',
 'CHEN LI ZHU',
 'LI LIN WEI',
 'ZHENG MIN E',
 'YANG HUI WEN',
 'SHANG TANG ZHEN',
 'BEN BI YUN',
 'LIN YI JUN',
 'ZHOU CHU PING',
 'WU HUAN JUN',
 'CHEN MING GUANG',
 'ZHOU LIANG HAO',
 'HUANG YA XIAO',
 'ZHANG ZHAN MEI',
 'LIN YU BAI',
 'GUO MING RU',
 'WANG JUN ZUN',
 'WU CHONG BA',
 'LIANG JIN BO',
 'CHEN JIA HONG',
 'ZHANG ZHONG JIAO',
 'LIU YAN SHEN',
 'GUO GU JIA',
 'XIE XIN YIN',
 'SHI YU WEI',
 'LIANG JUN XIN',
 'CHEN YI RU',
 'CAI YI LAN',
 'ZHANG ZHI WAN',
 'LIN YA PING',
 'CHEN YI ZHENG',
 'LIN YU JI',
 'ZHENG YOU MIN',
 'ZHANG YUN YANG',
 'ZHU SHI CHANG',
 'XIE HONG HUA',
 'LIN JIN YI',
 'LI XIN FEI',
 'WU YOU FENG',
 'YANG SHAO MING',
 'WU SI GU',
 'LIN HUI YI',
 'CHEN CHANG QI',
 'LUO SHU ZHEN',
 'GUO QUN CHEN',
 'WANG JUN ZUN',
 'LIN PEI ZHE',
 'WANG CHANG SHAN',
 'CHEN LI QING',
 'CHEN YU ZHEN',
 'HUANG GU JIA',
 'HE YI TING',
 'LI YOU YANG',
 'ZHANG LING XING',
 'LI HENG XIANG',
 'YANG QING HE',
 'LIN WEI WEI',
 'FANG JIA LIN',
 'JIANG YA WEI',
 'ZHANG CAI PING',
 'ZHANG SHAO HENG',
 'LIN PEI HUAN',
 'ZHANG JIA RONG',
 'CHEN YAN KANG',
 'CHEN XIAO YIN',
 'JIN YA LIN',
 'CHEN ZHENG QI',
 'CHEN YOU GUI',
 'HU XU JIAN',
 'LIN JIA YING',
 'JIN JIAN ZHANG',
 'WANG YI SHU',
 'CAI JIA SHENG',
 'JIANG YA QI',
 'SUN YUE YAO',
 'HUANG ZONG HAN',
 'SONG ZHAN DING',
 'WU JIN LIANG',
 'LIN SHU PING',
 'WANG YOU HUI',
 'WEI ZE RUI',
 'HU XU YING',
 'GUO TING TING',
 'CENG ZENG CHANG',
 'XIE YI SHAN',
 'CHEN JUN ZUN',
 'LIU GUAN BING',
 'LU BING XIN',
 'LIN JING QUAN',
 'ZHENG GUO WEI',
 'LI ZHONG HONG',
 'WANG SHU JUAN',
 'MOU MIAO HUI',
 'DENG PEI JING',
 'HUANG XIU AI',
 'ZHANG RUI XIU',
 'MA JIAN AN',
 'HU GUAN YIN',
 'GUO ZU TIAN',
 'CHEN JUN FU',
 'LIN XIN CHEN',
 'GUO SHI HUO',
 'LIU YING CHUN',
 'WANG JING FANG',
 'XIE SHU TING',
 'SUN YA ROU',
 'LIAO CHENG SHAO',
 'ZHANG YU GUAN',
 'LIN JING HAN',
 'ZHANG JIA ZHENG',
 'WU YOU ZHOU',
 'HUANG JING YUE',
 'HUANG JUN ZUN',
 'MAO YA WEN',
 'LIU WAN YUAN',
 'HUANG ZHONG WEI',
 'HU YI TING',
 'ZHANG YU QI',
 'HUANG QIONG ZHI',
 'WU REN QI',
 'XIAO YI LING',
 'ZHAO YA TING',
 'CAI YOU YU',
 'YANG CHENG XUAN',
 'CHEN ZHI KANG',
 'LIN FU YING',
 'CHEN GU JIA',
 'ZHANG JIAN YU',
 'PU WAN YUN',
 'HE MU XIN',
 'HUANG YAN HUA',
 'CHEN PEI LUN',
 'LI YI YI',
 'CHEN YA WEN',
 'WANG HUI DI',
 'YU ZU WEN',
 'HU ZHI CHENG',
 'CHEN HAO YUE',
 'CHEN WEI DE',
 'RUI YI TING',
 'HUANG ZHI HAO',
 'ZHOU JIA LING',
 'WANG WEN NAN',
 'ZHANG YI ZHEN',
 'WANG ZHEN WEI',
 'ZONG BEI ZHI',
 'CHEN YU WEN',
 'GUO CAI PING',
 'LIN RU NI',
 'ZHENG SHU YUN',
 'LIU ZI YI',
 'CHEN YA ZHU',
 'HE JIA HONG',
 'LIU ROU ZHEN',
 'CHEN GUO EN',
 'WANG PEI LING',
 'CAO ZI JIE',
 'ZHENG SHI YU',
 'CHEN YA HUI',
 'LI JIANG ZHEN',
 'CHEN SHU JUAN',
 'SHE YE YU',
 'ZHANG GU JIA',
 'HUANG JUN ZUN',
 'XU YI LING',
 'JIA XIA JIAN',
 'CHEN PEI HUA',
 'LI YING XIN',
 'ZHANG YAN LIN',
 'WANG YI QUN',
 'LI SHENG CHENG',
 'HE YU YANG',
 'HUANG YA HUI',
 'BO ZHI WANG',
 'LI SHU FEN',
 'SUN JIAN TING',
 'ZHANG ZHONG YU',
 'YANG PENG FANG',
 'ZHOU ZI YU',
 'BO NAI WEN',
 'YU YA WEN',
 'HE HUI MIN',
 'YAO XIANG DONG',
 'ZHANG JIAO LONG',
 'CHEN WEI JING',
 'CHEN HANG XING',
 'YANG HUI CHUN',
 'XIE YU HONG',
 'YAN YI QING',
 'XU JI KAI',
 'LIN YING MIN',
 'WANG SHU JUAN',
 'CHEN SHUN YUAN',
 'DENG DENG YING',
 'DU JUN ZUN',
 'GUO YI HUI',
 'FANG YI JUN',
 'HU XU YA',
 'YANG GU JIA',
 'SUN XIAO HAN',
 'MAO SHU JUN',
 'LIU MU QIU',
 'ZHANG HUI YU',
 'MAO YU JUAN',
 'HOU XIN MAO',
 'ZHANG ZHI YUE',
 'WANG JIA RONG',
 'BAO PU YA',
 'LIN YI LING',
 'HUANG HUI HUAN',
 'CHENG JUN ZUN',
 'ZHOU CHENG ZHI',
 'LIN YI CHEN',
 'XUE WANG JING',
 'LIU ZHEN JUN',
 'YUAN WU YU',
 'HONG JUN YU',
 'ZHENG WEI LIN',
 'PENG YUE YU',
 'HU XU YUE',
 'LIAN MING HUI',
 'CHEN MENG ZHENG',
 'LI JI ZHU',
 'WEI TING XI',
 'TANG JING FANG',
 'LIN YAN CHEN',
 'LIN XIN HAN',
 'CAI WAN YUAN',
 'WANG ZHI FANG',
 'WANG YUN RU',
 'ZHANG WEI ZHOU',
 'LI JUN ZUN',
 'LI YI XUAN',
 'LAI XIU LING',
 'LIN CHENG MIN',
 'LIU SHU JUAN',
 'JIANG ZHENG EN',
 'LIN YI TING',
 'ZHANG SHU PING',
 'LIU YU XIANG',
 'WANG MENG XIAN',
 'SHE YE JUN',
 'LU YI SHAN',
 'ZHENG YAN QI',
 'SHE YE SHUN',
 'LIN DIAN SONG',
 'WANG YI FAN',
 'WANG MIN MEI',
 'CHEN PEI YU',
 'KE BA BO',
 'ZHANG ZHENG WEI',
 'LIU YI SHENG',
 'CAI SI HAN',
 'CHEN YI XIAN',
 'LIAO HUI RU',
 'ZHA CHA JUN',
 'SHE YE YI',
 'WEN LONG KUN',
 'LAI YI WEN',
 'LI JING BO',
 'LI JUN LIAN',
 'ZHANG JING YI',
 'QIU HUANG YU',
 'YAN YUE QI',
 'ZHAO FENG BIN',
 'WANG MEI HUI',
 'HONG MIN TING',
 'XIAO SHU HUI',
 'QIU WAN TING',
 'CHEN MIN WEN',
 'CHEN YOU DI',
 'HUANG XIANG SHU',
 'HUANG JIE YUN',
 'PI JIA QI',
 'LU XING LIN',
 'WU TIAN ZHAI',
 'ZHANG JING YING',
 'LIN ZHE XIAO',
 'ZHENG SHAN MEI',
 'WANG XIAN WEN',
 'ZHENG YU HUI',
 'HUANG YAN FENG',
 'LI MENG FANG',
 'XU MAN QIAO',
 'XIE HUO ZHU',
 'ZHOU MENG XIU',
 'CAI HAI SONG',
 'LIU HANG XING',
 'LI WEN SHENG',
 'ZHONG MAO LING',
 'LIN HUI WEN',
 'YANG CHEN LI',
 'LIU YI TING',
 'JIANG MING JIE',
 'GUO LIN BO',
 'ZHANG JIA YUAN',
 'CAI JIAN TING',
 'WANG JUN ZUN',
 'QIAN WEN HONG',
 'CHEN KAI LUN',
 'ZHENG HUAN HAN',
 'CHEN JIN YANG',
 'LIN SHI SHAN',
 'CAI ZHI MING',
 'CHEN LI PING',
 'GUO ZHONG HAO',
 'HAN JI PEI',
 'WANG CI PENG',
 'CENG ZENG MING',
 'LI MU FANG',
 'ZHANG JIAN ZHI',
 'WANG BING YAN',
 'CHEN ZHI QIANG',
 'WU DAI HU',
 'JIA XIA QING',
 'CHEN JIAN ZHI',
 'TANG XI PING',
 'CAI MING ZHU',
 'SHI CHANG GU',
 'YANG YU EN',
 'LI ZHI XIANG',
 'HE QING YU',
 'HU XU YA',
 'ZHANG WEI LUN',
 'LI ZONG YI',
 'LAI XIAO TING',
 'HUANG JUN ZUN',
 'SHE YE JING',
 'HU WEN XIAN',
 'WANG SHU HUI',
 'ZHANG RUI FAN',
 'GUO SHU ZHEN',
 'LIN MEI LING',
 'LIN YI JIE',
 'LIU YU FENG',
 'WANG YIN YI',
 'TONG MEI XIAO',
 'HUANG JUN ZUN',
 'CHEN LI YUN',
 'CHEN YA HUI',
 'KANG YING SHI',
 'CHEN CHANG YI',
 'ZHANG HUI DI',
 'SONG QI YONG',
 'LIN JI XIAN',
 'LI YU XIA',
 'LIU XIU YI',
 'FANG ZHI PEI',
 'JIANG HONG DAN',
 'LIU YU WEI',
 'HU XU XIN',
 'HU HE HANG',
 'FU SHI WEI',
 'PAN JUN LAN',
 'ZHAO MU ZHEN',
 'CHEN HUI MIN',
 'LIN YI ZHEN',
 'HUANG SHENG YU',
 'CHEN WEN XING',
 'YOU JIA LIN',
 'YAO HUI LIN',
 'LIU ZHI YING',
 'WU HUI ZHEN',
 'LAI JIAN YU',
 'LI LIN JUN',
 'ZHANG GU JIA',
 'DU YAN CHENG',
 'LIN SHAN XIU',
 'ZHANG ZHI XIANG',
 'WANG HUI YU',
 'GUO DAN YIN',
 'ZHANG JIE ZHONG',
 'LIN HUI XUAN',
 'LI JUN ZUN',
 'HUANG YU WEN',
 'YAO ZHI CHENG',
 'HONG YAN JUN',
 'FU QIONG HUI',
 'XIE KE LIN',
 'ZHANG JING YING',
 'WANG YOU CHENG',
 'LIU YI WEN',
 'CHEN TING HENG',
 'LIN SHU ZHEN',
 'ZHENG WAN YI',
 'WU MEI QI',
 'ZHANG ZI XIANG',
 'LIN SU TING',
 'LIN FANG XUAN',
 'TANG YA PING',
 'LI HUO XIAN',
 'WU YAN YING',
 'LI YU LING',
 'CHEN WEI XIANG',
 'QIU JIA WEN',
 'ZHANG WEN ZHONG',
 'WANG ZI YU',
 'ZHENG TING YI',
 'XIE SI TING',
 'SU GUO WEI',
 'CHEN MENG SHI',
 'LU QING DAN',
 'HU XIN DIAN',
 'NI SHI LI',
 'LIN KUN HENG',
 'ZHENG XIN YI',
 'LU XU HUA',
 'ZHANG WEI YI',
 'CHEN YA LAN',
 'CHEN XIN LIN',
 'LI JIA CHUN',
 'JIAN WU YU',
 'WU SHU HAO',
 'LIN SI HAN',
 'HU MEI HUI',
 'WANG YU MEI',
 'LIU QIU PING',
 'ZHEN SHENG GANG',
 'HUANG GUO LAI',
 'WANG JUN ZUN',
 'HAN YI JIE',
 'ZHANG XING XIN',
 'XIAO YA HUI',
 'LIAO JIAN YU',
 'LI YI YUN',
 'GUO YI TING',
 'WANG MEI YU',
 'YOU A E',
 'LIN MEI HUI',
 'WU YI HANG',
 'CHEN JIAN HONG',
 'LI GUO CEN',
 'GUO ZONG HAN',
 'XIE JIA QI',
 'CHEN SHU FENG',
 'CENG ZENG HONG',
 ]
    chrome_options = Options() 
    # chrome_options.add_argument('--headless') 
#     driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()) 
    driver.maximize_window()

    name, email, password = get_inputs(names, driver)

    url = 'https://brandstorm.loreal.com/en/users/sign_in?redirect_to=https%3A%2F%2Fbrandstorm.loreal.com%2Fen%2Fjuries%2FvDmsA2-HS7z5FkDQYB6lQQ'

    driver.get(url)
    cookie = xpathWait(driver, '//*[@id="onetrust-close-btn-container"]/button')
    cookie.click()

    register = xpathWait(driver, '//*[@id="new_user"]/ul/li[1]/a')
    register.click()

    signUp = xpathWait(driver, '//*[@id="centerPanel"]/div/div[2]/div/div[3]/div/div[4]/span[2]/a')
    signUp.click()

    firstPage(name, email, password, driver)

    inspect(driver)

    thirdPage(driver)

def loop(i):
    
    try:
        main()
        print(i)
    except:
        loop(i)


def start(num):
    print('Start')
    time_start = time.time()
    Parallel(n_jobs=-1)(delayed(loop)(i) for i in range(num))
    print('End')
    time_end = time.time()
    print('Total spend', time_end-time_start, 's')
    

if __name__ == '__main__':
    start(2500)
    
        
        # random_number = np.random.choice(list(range(70)))
        # time.sleep(random_number)
