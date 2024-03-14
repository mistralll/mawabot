import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ['APP_BOT_TOKEN']
notice_channel_id = int(os.environ['NOTICE_CHANNEL_ID'])
