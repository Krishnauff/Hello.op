from typing import Dict, List, Union

streamsdb = "mongodb+srv://khushijha5544:karan2020@krishnauff.ndruqrp.mongodb.net/?retryWrites=true&w=majority",


async def get_chat_id(user_id: int) -> int:
    check = await streamsdb.find_one(
      {"user_id": user_id, "chat_id": {"$lt": 0}}
    )
    if not check:
        return 0
    get_chat = check["chat_id"]
    return get_chat


async def is_chat_id(user_id: int, chat_id: int) -> bool:
    is_chat = await get_chat_id(user_id)
    if chat_id == is_chat:
        return True
    return False


async def set_chat_id(user_id: int, chat_id: int) -> bool:
    if await is_chat_id(user_id, chat_id):
        return True
    get_chat = await get_chat_id(user_id)
    await streamsdb.update_one(
        {"user_id": user_id, "chat_id": get_chat},
        {"$set": {"user_id": user_id, "chat_id": chat_id}},
        upsert=True,
    )
    return False