import json
import datetime

import pyrogram
from pyrogram import Client
from database import Event

app = Client("your_account", api_id=12345, api_hash="your_app_hash")


@app.on_raw_update()
def raw(client, update, users, chats):
    update_info = json.loads(str(update))
    if update_info.get('_') == 'telegram:UpdateUserStatus':
        current_user = app.get_users(update.user_id)
        username = f"{current_user.first_name} {current_user.last_name}"
        user_status = update_info.get('status')
        if user_status is None:
            print("Empty user status, bad raw")
            return

        if user_status.get('_') == 'telegram:UserStatusOnline':
            status = True
        elif user_status.get('_') == 'telegram:UserStatusOffline':
            status = False
        else:
            return
        print(f"{username}: {user_status.get('_')}")
        event = Event(user_id=update.user_id, name=username, time=datetime.datetime.now(), status=status)
        event.save()


if __name__ == '__main__':
    try:
        app.start()
    except pyrogram.api.errors.exceptions.flood_420.FloodWait:
        print("Too many login retries")



