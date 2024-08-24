# import webdriver
import time
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# import exeptions if element is not found
from selenium.common.exceptions import NoSuchElementException


###Add Tags here
taglist =["MSFT", "PYPL", "TSLA"]

IncomeStatementSummary = pd.DataFrame()
BalanceSheetSummary = pd.DataFrame()
IncomeStatementQuarterlySummary =pd.DataFrame()
BalanceSheetQuarterlySummary = pd.DataFrame()
StatisticsSummary = pd.DataFrame()

is_link ='https://finance.yahoo.com/lookup'
driver = webdriver.Edge()
driver.get(is_link)
time.sleep(5)



# ...

# Initialize the ChromeDriver service
service = Service(ChromeDriverManager().install())

# Initialize the Chrome browser
driver = webdriver.Chrome(service=service)

# ...

def SearchElements(tag):
    time.sleep(5)  # add a delay of 5 seconds to allow the page to load
    try:
        accept_button = driver.find_element(By.XPATH, '//button[contains(text(), "Accept")]')
        accept_button.click()
    except NoSuchElementException:
        pass
    SearchBar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "yfin-usr-qry")))
    SearchBar.send_keys(tag)
    SearchBar.send_keys(Keys.ENTER)
    time.sleep(5)

    if tag == taglist[0]:
        MayBeLaterBtn = driver.find_element(By.XPATH, '//button[@class="Mx(a) Fz(16px) Fw(600) Mt(20px) D(n)--mobp"]')
        action = ActionChains(driver)
        action.click(on_element = MayBeLaterBtn)
        action.perform()
        time.sleep(5)


#####Get Statistics
def getStatistics(tag):
    global StatisticsSummary
    Statistics = pd.DataFrame(pd.np.empty((0, 61)))
    StatisticsBtn = driver.find_element(By.XPATH,  '//ul[@class="List(n) Whs(nw) fin-tab-items W(100%) Lh(1.7) H(44px) Bdbs(s) BdB(4px) Cf Mb(15px) Bdbc($seperatorColor) "]/li[4]/a[1]')
    action = ActionChains(driver)
    action.click(on_element = StatisticsBtn)
    action.perform()
    time.sleep(5)

    dataStatistics = driver.find_elements(By.XPATH, '//td[contains(@class, "Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px)  Miw(140px)") or contains(@class, "Fw(500) Ta(end) Pstart(10px) Miw(60px)") or contains(@class, "Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px) ")]')
    DataStatisticsList =[]

    #Collect all Names and Values from Statistics Site
    for value in dataStatistics:
        DataStatisticsList.append(value.text)
    
    #Create Columns Names and Append tag to it
    ColumnNames = DataStatisticsList[::2]
    ColumnNames.insert(0, "tag")

    #Create a List that contains all Statistics Values
    Data = DataStatisticsList[1::2]
    Data.insert(0,tag)

    #Add Columns and Data
    Statistics.columns = ColumnNames 
    Statistics.loc[len(Statistics)] = Data
    StatisticsSummary = pd.concat([StatisticsSummary,Statistics], ignore_index=True, sort=False)

#####Get Statistics
def getStatistics(tag):
        global StatisticsSummary
        Statistics = pd.DataFrame(pd.np.empty((0, 61)))
        StatisticsBtn = driver.find_element(By.XPATH,  '//ul[@class="List(n) Whs(nw) fin-tab-items W(100%) Lh(1.7) H(44px) Bdbs(s) BdB(4px) Cf Mb(15px) Bdbc($seperatorColor) "]/li[4]/a[1]')
        action = ActionChains(driver)
        action.click(on_element = StatisticsBtn)
        action.perform()
        time.sleep(5)

        dataStatistics = driver.find_elements(By.XPATH, '//td[contains(@class, "Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px)  Miw(140px)") or contains(@class, "Fw(500) Ta(end) Pstart(10px) Miw(60px)") or contains(@class, "Pos(st) Start(0) Bgc($lv2BgColor) fi-row:h_Bgc($hoverBgColor) Pend(10px) ")]')
        DataStatisticsList =[]

        #Collect all Names and Values from Statistics Site
        for value in dataStatistics:
         DataStatisticsList.append(value.text)
        
        #Create Columns Names and Append tag to it
        ColumnNames = DataStatisticsList[::2]
        ColumnNames.insert(0, "tag")

        #Create a List that contains all Statistics Values
        Data = DataStatisticsList[1::2]
        Data.insert(0,tag)

        #Add Columns and Data
        Statistics.columns = ColumnNames 
        Statistics.loc[len(Statistics)] = Data
       # StatisticsSummary = StatisticsSummary.append(Statistics, ignore_index=True)
        StatisticsSummary = pd.concat([StatisticsSummary,Statistics], ignore_index=True, sort=False)

#####Get IncomeStatement Yearly
def getIncomeStatementYearly(tag):
      
        #Go to Financials
        FinancialsButton = driver.find_element(By.XPATH, '//ul[@class="List(n) Whs(nw) fin-tab-items W(100%) Lh(1.7) H(44px) Bdbs(s) BdB(4px) Cf Mb(15px) Bdbc($seperatorColor) "]/li[7]/a[1]')
        action = ActionChains(driver)
        action.click(on_element = FinancialsButton)
        action.perform()
        time.sleep(3)

        global IncomeStatementSummary

        #Get Income Common Stockholders 
        IncomeCommonStockholders = driver.find_element(By.XPATH, '//button[@aria-label="Net Income Common Stockholders"]')
        action = ActionChains(driver)
        action.click(on_element = IncomeCommonStockholders)
        action.perform()
        time.sleep(0.2)


        ####Here we collect the income statement in full########
        Data = driver.find_elements(By.XPATH, '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)")]')
        Column_Headers = driver.find_elements(By.XPATH, '//div[contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(200px)--mv2 W(185px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(185px)--mv2 W(170px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(170px)--mv2 W(155px) undefined")]')
        Dates = driver.find_elements(By.XPATH,  '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Tt(u) Bgc($lv1BgColor)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)")]')

        IncomeStatementHeaders = []
        IncomeStatementData =[]
        DatesColumn=[]

        for value in Column_Headers:
             IncomeStatementHeaders.append(value.text)

        for value in Data:
             IncomeStatementData.append(value.text)
     
        for value in Dates:
             DatesColumn.append(value.text)
     
        ######Chunck size is len of Dates column
        chunk_size = len(DatesColumn)
        ListOfLists = list()

        for i in range(0, len(IncomeStatementData), chunk_size):
            ListOfLists.append(IncomeStatementData[i:i+chunk_size])
 
        IncomeStatementYearly = pd.DataFrame()
 
        #Add Columns with Chunk size
        for z in range(0, len(IncomeStatementHeaders), 1):
            IncomeStatementYearly[z] = ListOfLists[z]


        IncomeStatementYearly.columns = IncomeStatementHeaders
        IncomeStatementYearly.insert(0, "tag", tag)
        IncomeStatementYearly.insert(1, "Dates", DatesColumn)

        IncomeStatementSummary = pd.concat([IncomeStatementSummary,IncomeStatementYearly], axis=0, ignore_index=True, sort=False)
#####Get IncomeStatement Quarterly
def getIncomeStatementQuarterly(tag):
      
        #Go to Quarterly
        QuarterlyButton = driver.find_element(By.XPATH, '//button[@class="P(0px) M(0px) C($linkColor) Bd(0px) O(n)"]')
        action = ActionChains(driver)
        action.click(on_element = QuarterlyButton)
        action.perform()
        time.sleep(5)

        global IncomeStatementQuarterlySummary

        ####Here we collect the income statement in full########
        Data = driver.find_elements(By.XPATH, '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)")]')
        Column_Headers = driver.find_elements(By.XPATH, '//div[contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(200px)--mv2 W(185px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(185px)--mv2 W(170px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(170px)--mv2 W(155px) undefined")]')
        Dates = driver.find_elements(By.XPATH,  '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Tt(u) Bgc($lv1BgColor)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)")]')

        IncomeStatementHeaders = []
        IncomeStatementData =[]
        DatesColumn=[]

        for value in Column_Headers:
             IncomeStatementHeaders.append(value.text)

        for value in Data:
             IncomeStatementData.append(value.text)
     
        for value in Dates:
             DatesColumn.append(value.text)
     
        ######Chunck size is len of Dates column
        chunk_size = len(DatesColumn)
        ListOfLists = list()

        for i in range(0, len(IncomeStatementData), chunk_size):
            ListOfLists.append(IncomeStatementData[i:i+chunk_size])
 
        IncomeStatementQuarterly = pd.DataFrame()
 
        #Add Columns with Chunk size
        for z in range(0, len(IncomeStatementHeaders), 1):
            IncomeStatementQuarterly[z] = ListOfLists[z]


        IncomeStatementQuarterly.columns = IncomeStatementHeaders
        IncomeStatementQuarterly.insert(0, "tag", tag)
        IncomeStatementQuarterly.insert(1, "Dates", DatesColumn)

        IncomeStatementQuarterlySummary = pd.concat([IncomeStatementQuarterlySummary,IncomeStatementQuarterly], axis=0, ignore_index=True, sort=False)

def getBalanceSheet(tag):

      global BalanceSheetSummary
      #Go to Balance Sheet
      BalanceSheetBtn = driver.find_element(By.XPATH, '//div[@class="Fw(500) D(ib) Pend(10px) H(18px) BdEnd Bdc($seperatorColor)"]')
      action = ActionChains(driver)
      action.click(on_element = BalanceSheetBtn)
      action.perform()
      time.sleep(5)

      #Go to Balance Sheet
   
      #Open subaccounts of BalanceSheet
      try:
            TotalAssetsBtn = driver.find_element(By.XPATH,  '//button[@aria-label="Total Assets"]')
            action = ActionChains(driver)
            action.click(on_element = TotalAssetsBtn)
            action.perform()
            time.sleep(0.2)

            TotalLiabilitiesBtn = driver.find_element(By.XPATH,  '//button[@aria-label="Total Liabilities Net Minority Interest"]')
            action = ActionChains(driver)
            action.click(on_element = TotalLiabilitiesBtn)
            action.perform()
            time.sleep(0.2)

            TotalEquityBtn = driver.find_element(By.XPATH,  '//button[@aria-label="Total Equity Gross Minority Interest"]')
            action = ActionChains(driver)
            action.click(on_element = TotalEquityBtn)
            action.perform()
            time.sleep(0.2)

      except NoSuchElementException:
            print("Element not found")

      try:      
        Data = driver.find_elements(By.XPATH, '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)")]')
        Dates = driver.find_elements(By.XPATH,'//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Bgc($lv1BgColor)")]' )
        Column_Headers = driver.find_elements(By.XPATH,'//div[contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(200px)--mv2 W(185px) undefined")]' )

        ColumnHeadersList =[]
        DatesList = []
        BalanceSheetList = []

        for value in  Column_Headers:
         ColumnHeadersList.append(value.text)

        for value in Data:
         BalanceSheetList.append(value.text)

        for value in Dates:
         DatesList.append(value.text) 

    
        ListOfLists= list()
        chunk_size = len(DatesList)

        for i in range(0, len(BalanceSheetList), chunk_size):
            ListOfLists.append(BalanceSheetList[i:i+chunk_size])

        BalanceSheetYearly= pd.DataFrame()

        for z in range(0, len(ColumnHeadersList), 1):
         BalanceSheetYearly[z] = ListOfLists[z]
    
        BalanceSheetYearly.columns = ColumnHeadersList

        BalanceSheetYearly.insert(0, "tag", tag)
        BalanceSheetYearly.insert(1, "Dates", DatesList)

        BalanceSheetSummary = pd.concat([BalanceSheetSummary,BalanceSheetYearly], axis=0, ignore_index=True, sort=False)

      except NoSuchElementException:
        print("Element not found")

def getBalanceSheetQuarterly(tag):

      global BalanceSheetQuarterlySummary
      #Go to Quarterly
      QuarterlyButton = driver.find_element(By.XPATH, '//button[@class="P(0px) M(0px) C($linkColor) Bd(0px) O(n)"]')
      action = ActionChains(driver)
      action.click(on_element = QuarterlyButton)
      action.perform()
      time.sleep(2)

      try:
        Data = driver.find_elements(By.XPATH, '//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)")]')
        Dates = driver.find_elements(By.XPATH,'//div[contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)") or contains(@class, "Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Bgc($lv1BgColor)")]' )
        Column_Headers = driver.find_elements(By.XPATH,'//div[contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(215px)--mv2 W(200px) undefined") or contains(@class, "D(ib) Va(m) Ell Mt(-3px) W(200px)--mv2 W(185px) undefined")]' )

        ColumnHeadersList =[]
        DatesList = []
        BalanceSheetList = []

        for value in  Column_Headers:
         ColumnHeadersList.append(value.text)

        for value in Data:
         BalanceSheetList.append(value.text)

        for value in Dates:
         DatesList.append(value.text) 
         
        ListOfLists= list()
        chunk_size = len(DatesList)

        for i in range(0, len(BalanceSheetList), chunk_size):
            ListOfLists.append(BalanceSheetList[i:i+chunk_size])

        BalanceSheetQuarterly= pd.DataFrame()

        for z in range(0, len(ColumnHeadersList), 1):
         BalanceSheetQuarterly[z] = ListOfLists[z]
    
        BalanceSheetQuarterly.columns = ColumnHeadersList

        BalanceSheetQuarterly.insert(0, "tag", tag)
        BalanceSheetQuarterly.insert(1, "Dates", DatesList)

        BalanceSheetQuarterlySummary = pd.concat([BalanceSheetQuarterlySummary,BalanceSheetQuarterly], axis=0, ignore_index=True, sort=False)

      except NoSuchElementException:
        print("Element not found")

for tag in taglist:
    SearchElements(tag)
    getStatistics(tag)
    getIncomeStatementYearly(tag)
    getIncomeStatementQuarterly(tag)
    getBalanceSheet(tag)
    getBalanceSheetQuarterly(tag)


StatisticsSummary.to_excel("C:/Users/User/Desktop/Python/WebScraping/Stats.xlsx",
                 sheet_name='Sheet_name_1')  

IncomeStatementSummary.to_excel("C:/Users/User/Desktop/Python/WebScraping/IncomeStatement.xlsx",
                 sheet_name='Sheet_name_1')  

IncomeStatementQuarterlySummary.to_excel("C:/Users/User/Desktop/Python/WebScraping/IncomeStatementQuarterly.xlsx",
                 sheet_name='Sheet_name_1')  

BalanceSheetSummary.to_excel("C:/Users/User/Desktop/Python/WebScraping/BalanceSheet.xlsx",
                 sheet_name='Sheet_name_1')  

BalanceSheetQuarterlySummary.to_excel("C:/Users/User/Desktop/Python/WebScraping/BalanceSheetQuarterly.xlsx",
                 sheet_name='Sheet_name_1')
