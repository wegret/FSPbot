from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="chat",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

from nonebot.permission import SUPERUSER
from nonebot.plugin.on import on_command, on_message, on_notice, on_regex
from nonebot.rule import to_me, Rule
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import Message, MessageEvent, PrivateMessageEvent, MessageSegment, GroupMessageEvent
from nonebot.params import Arg, ArgPlainText, CommandArg, Matcher
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.log import logger
from nonebot import on_keyword

import os
import yaml
import requests
import json
from collections import defaultdict

chat_priority = 3

'''
大模型配置文件：config.yaml
'''

current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

# GPT API
API_KEY = config['llm']['API_KEY']
MODEL_NAME = config['llm']['MODEL_NAME']
API_URL = config['llm']['API_URL']


'''
聊天插件
'''

chat_FSP = on_keyword({"强基", "羟基"})
@chat_FSP.handle()
async def chat_FSP_handle(bot: Bot, matcher: Matcher, event: MessageEvent):
    user_id = event.get_user_id()
    
    await bot.send(event=event, message=Message("关键词"))