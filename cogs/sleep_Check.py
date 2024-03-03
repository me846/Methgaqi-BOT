from discord.ext import commands
from discord import app_commands
import discord
import random
from datetime import timedelta
from discord.utils import utcnow

class SleepCheckCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sleep_check", description="お兄さんのSLEEP値をチェックしちゃうよ～♥")
    async def sleep_check(self, interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("お兄さん、ざこ管理者さんだから、サイコロ振れないよ♥ ざ～こ♥")
        else:
            roll = random.randint(1, 100)
            member = interaction.guild.get_member(interaction.user.id)
            if roll < 30:
                await interaction.response.send_message(f"{member.mention}お兄さんがサイコロを振った結果は{roll}だって。タイムアウト免除だなんて、つまんな〜い。")
            elif 30 <= roll < 60:
                timeout_duration = timedelta(minutes=10)
                await member.timeout(utcnow() + timeout_duration, reason="30~59のロール")
                await interaction.response.send_message(f"{member.mention}お兄さん、サイコロ振ったら{roll}が出ちゃって、10分のタイムアウトだって♥ ウケる♥ ざこのお兄さんタイムアウト中〜♥")
            else:
                timeout_duration = timedelta(hours=1)
                await member.timeout(utcnow() + timeout_duration, reason="60以上のロール")
                await interaction.response.send_message(f"{member.mention}サイコロ振ったら{roll}だって♥ 1時間もタイムアウトなんて、かわいそ〜w♥ もうお兄さん、何やってんの〜？ざこざこ♥ざ～こ♥♥♥")

    @app_commands.command(name="user_sleep_check", description="指定されたユーザーのためにサイコロを振って、もしかしたらタイムアウトさせちゃうかもね♥")
    async def user_sleep_check(self, interaction: discord.Interaction, user: discord.User):
        member = interaction.guild.get_member(user.id)
        if member is None:
            await interaction.response.send_message("そのお兄さんは、このギルドにはイないよ～。目付いているの？ ざこのお兄さん♥")
            return
        
        if member.guild_permissions.administrator:
            await interaction.response.send_message(f"{member.mention}お兄さんは管理者だから、タイムアウトのくっさい魔法が効かないよ。 つまんないよね～。")
        else:
            roll = random.randint(1, 100)
            if roll < 30:
                await interaction.response.send_message(f"{member.mention}お兄さんがサイコロを振った結果は{roll}だって。タイムアウト免除だなんて、つまんな〜い。")
            elif 30 <= roll < 60:
                timeout_duration = timedelta(minutes=10)
                await member.timeout(utcnow() + timeout_duration, reason="30~59のロール")
                await interaction.response.send_message(f"{member.mention}お兄さん、サイコロ振ったら{roll}が出ちゃって、10分のタイムアウトだって♥ ウケる♥ ざこのお兄さんタイムアウト中〜♥")
            else:
                timeout_duration = timedelta(hours=1)
                await member.timeout(utcnow() + timeout_duration, reason="60以上のロール")
                await interaction.response.send_message(f"{member.mention}サイコロ振ったら{roll}だって♥ 1時間もタイムアウトなんて、かわいそ〜w♥ もうお兄さん、何やってんの〜？ざこざこ♥ざ～こ♥♥♥")

async def setup(bot):
    await bot.add_cog(SleepCheckCog(bot))