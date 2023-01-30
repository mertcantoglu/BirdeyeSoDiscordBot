from selenium import webdriver
from bs4 import BeautifulSoup
import time
from database import Database
from logger import Logger
from Trade import Trade
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1069711987354910831/tA_M5IwrWcw4DzrQrBK8TmbTRk77i1peKtu8j2XSh5JHGe-NEClC_XXXx12w-izX2nbi')
DB = Database("O5O.db")
logger = Logger()
COLORS = {"buy" : "00c38c" ,"sell" : "f94d5c"}

url = "https://birdeye.so/trades/9LdHzY1CZFP9SYgGSzQe1j6BXqtfU5akFYPqnvrYik56"


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 


def send_message(obj: Trade):
    lines = obj.value.split("(")
    try:
        embed = DiscordEmbed(title=f'$O5O {obj.type.upper()} @everyone', description=f'{obj.numberOfEmoji * "💰"}\n{lines[0]}\n{lines[1]}\n{obj.time}', color=COLORS[f"{obj.type}"])
        webhook.add_embed(embed)
        response = webhook.execute(remove_embeds=True)
    except:
        logger.printe("DiscordBotProblem" ,obj)

    

while True:
    try:
        driver.get(url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.find("div", { "class" : "ant-table-body" })
        for row in table.findAll("tr")[::-1]:
            cells = row.findAll("td")
            if cells[1].text == "buy":
                transOBJ = Trade(cells[0].text,cells[1].text,cells[4].text.replace(")",""))
                if DB.saveHash(transOBJ.value):
                    print(transOBJ)
                    send_message(transOBJ)
                    logger.printe("A new trade has been made, alert is being sent.")
        time.sleep(60) 
    except:
        logger.printe("Error something.")
          
            
        