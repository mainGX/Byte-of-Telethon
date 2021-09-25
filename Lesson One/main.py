from telethon import TelegramClient

api_id = 12345
api_hash = "d8d381c18621bccf0685715a345697dc"

with TelegramClient("TelethonLesson", api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message("me", "Первый урок завершен!"))
