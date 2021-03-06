from pymongo import MongoClient
from settings import MONGO_DB
from settings import MONGODB_LINK

mdb = MongoClient(MONGODB_LINK)[MONGO_DB]


def search_or_save_user(mdb, effective_user, message):
    user = mdb.users.find_one({"user_id": effective_user.id})
    if not user:
        user = {
            "user_id": effective_user.id,
            "first_name": effective_user.first_name,
            "last_name": effective_user.last_name,
            "chat_id": message.chat_id
        }
        mdb.users.insert_one(user)
    return user