import asyncio
from discord.ext import commands
from discord import app_commands
import discord
import random

class JudgmentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def reset_nickname(self, member, original_nickname):
        await asyncio.sleep(3600)
        await member.edit(nick=original_nickname)

    @app_commands.command(name="judgment", description="指定されたユーザーにランダムな判決を下しちゃうんだって♥")
    async def judgment(self, interaction: discord.Interaction, user: discord.User):
        member = interaction.guild.get_member(user.id)
        if member.guild_permissions.administrator:
            await interaction.response.send_message(f"{user.mention} はサーバー管理者だから、判決なんて効かないんだって♥")
            return
        guilty_nicknames = [
            "不良品のざこちゃん♥", "罪のプロフェッショナル♥", "法律ブレイカー♥",
            "黒歴史製造機♥", "罪袋くん♥", "ギルティ・ブラザー♥",
            "犯罪界の新星♥", "罪の重さ測定士♥", "ルール破りのチャンピオン♥", "法の外側の探検家♥"
        ]
        death_penalty_nicknames = [
            "終末のカウントダウン♥", "最後のダンスのパートナー♥", "黄泉のガイドブック♥",
            "死神のお茶会ゲスト♥", "エピローグの主人公♥", "終焉の伝説♥",
            "フィナーレのフィーチャー♥", "最終呼出しの旅人♥", "グランドエグジットのスター♥", "永遠のお休みの先生♥"
        ]

        member = interaction.guild.get_member(user.id)
        original_nickname = member.nick

        judgment = random.choice(["有罪", "無罪", "死刑"])

        if judgment == "有罪":
            new_nickname = random.choice(guilty_nicknames)
            await member.edit(nick=new_nickname)
            await interaction.response.send_message(f"{user.mention} は有罪ってばよ！ざまぁみろ♥ 法の裁きってやつをガッツリ味わっちゃえ♥")
            self.bot.loop.create_task(self.reset_nickname(member, original_nickname))
        elif judgment == "死刑":
            new_nickname = random.choice(death_penalty_nicknames)
            await member.edit(nick=new_nickname)
            await interaction.response.send_message(f"{user.mention} に下った判決は… 死刑だってさ♥ オホ♥オホ♥ざっこ♥ 最後の晩餐、何がいい？ざこざこおにいさん♥")
            self.bot.loop.create_task(self.reset_nickname(member, original_nickname))
        else:
            await interaction.response.send_message(f"{user.mention}、ラッキーだね〜、無罪だって♥ 自由を満喫しちゃえ、お兄さん♥")

async def setup(bot):
    await bot.add_cog(JudgmentCog(bot))