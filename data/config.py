import json

# Подгружаем токен
with open('data/config.ini', 'r') as file:
        tg_data = json.load(file)
# и админов
admins  = []
for adm in tg_data["admins"].split():
    admins.append(adm)

# Bot token
BOT_TOKEN = tg_data["token"] 
# admins
ADMINS = admins 

ADMIN_MODE = False
# TODO: проверить наличие id можно здесь
def change_admin_mode(mode):
    global ADMIN_MODE
    ADMIN_MODE = mode

async def get_admin_mode():
    return ADMIN_MODE