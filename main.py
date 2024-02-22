import discord
import os
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.all())

load_dotenv()
token = os.environ['APP_BOT_TOKEN']
notice_channel_id = int(os.environ['NOTICE_CHANNEL_ID'])

@client.event # 通話の開始を通知
async def on_voice_state_update(mem:discord.Member, bf:discord.VoiceState, af:discord.VoiceState):
    if bf.channel == None and len(af.channel.members) == 1:
        print(f'[LOG] {mem.display_name} が {af.channel.name} に参加しました。')
        await client.get_channel(notice_channel_id).send(f'{af.channel.name}に誰か来たようです！')

client.run(token)