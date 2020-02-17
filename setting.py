import os

MONGODB_NAME = os.getenv('MONGODB_NAME', "bn-easy-sme-test")
MONGODB_URI = os.getenv('MONGODB_URI', "mongodb://localhost:27017")
MONGODB_GRID_FS_BOT_IMG = os.getenv('MONGODB_GRID_FS_BOT_IMG', 'http://localhost:3000/v1/bot/gridfs?id=')