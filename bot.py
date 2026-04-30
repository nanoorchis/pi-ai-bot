from http import client
import os
from dotenv import load_dotenv
import lark_oapi as lark

print("Loading environment variables from .env file...")
load_dotenv("/home/j/Documents/pi-ai-bot/feishu_bot.env")
APP_ID=os.getenv("FEISHU_APP_ID")
print(f"APP_ID: {APP_ID}")
APP_SECRET=os.getenv("FEISHU_APP_SECRET")
print(f"APP_SECRET: {APP_SECRET}")
VERIFICATION_TOKEN=os.getenv("FEISHU_BOT_VERIFICATION_TOKEN")
print(f"VERIFICATION_TOKEN: {VERIFICATION_TOKEN}")
OLLAMA_API_URL=os.getenv("OLLAMA_API_URL")
print(f"OLLAMA_API_URL: {OLLAMA_API_URL}")
OLLAMA_MODEL=os.getenv("OLLAMA_MODEL")
print(f"OLLAMA_MODEL: {OLLAMA_MODEL}")
print("Environment variables loaded successfully.")

client = lark.Client(app_id=APP_ID, app_secret=APP_SECRET).build()

# come on https://open.feishu.cn/document/server-side-sdk/python--sdk/handle-events