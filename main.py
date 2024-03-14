import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client(intents=discord.Intents.default())
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()

@tree.command(name="sample_command", description="This is samole command")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("Hi!", ephemeral=True)

@client.event # 通話の開始を通知
async def on_voice_state_update(mem:discord.Member, bf:discord.VoiceState, af:discord.VoiceState):
    if bf.channel == None and len(af.channel.members) == 1:
        print(f'[LOG] {mem.display_name} が {af.channel.name} に参加しました。')
        await client.get_channel(int(os.environ['NOTICE_CHANNEL_ID'])).send(f'{af.channel.name}に誰か来たようです！')

from yt_dlp import YoutubeDL
from gfile import GFile

@tree.command(name="youtube_dowonload", description="Download YouTube video.")
async def download_youtube_command(interaction: discord.Interaction, url:str):
    await interaction.response.send_message('処理中...')
    # youtubeダウンロード
    opt = {
            'outtmpl': './download/%(title)s.%(ext)s',
            'format': 'best',
        }
    path = ""
    with YoutubeDL(opt) as ydl:
        inf = ydl.extract_info(url, download=True)
        path = ydl.prepare_filename(inf)
    # gigafileへアップロード
    gfile_url = GFile(path, progress=False).upload().get_download_page()
    # 一時ファイルの削除
    os.remove(path)

    await interaction.followup.send(content=f'ダウンロード完了！\nダウンロードは[こちら]({gfile_url})')

client.run(os.environ['APP_BOT_TOKEN'])