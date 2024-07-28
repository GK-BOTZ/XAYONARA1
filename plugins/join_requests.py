from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database.users_chats_db import db
from info import ADMINS, AUTH_CHANNEL


@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def add_join_request(client, message: ChatJoinRequest):
  user = message.from_user.id
  if not await db.find_join_req(user):
    await db.add_join_req(user)

@Client.on_message(filters.command("delete_request") & filters.user(ADMINS))
async def delete_join_requests(client, message):
  try:
     await db.del_join_req()    
     await message.reply("**Deleted All Join Requests From DB 🙂**")
  except:
     print("Can't Delete CJR")
