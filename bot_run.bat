@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=1951143794:AAHt-9H8XALq3iwz4wRI4gfk7865rWdao0Y

python bot_telegram.py

pause
