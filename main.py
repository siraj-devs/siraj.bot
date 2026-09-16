import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from ui import WelcomeView
from utils import Log

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def on_ready(self):
        Log.info("Bot", f"Logged in as {self.user}")

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

    async def on_member_join(self, member: discord.Member):
        try:
            await member.send(
                embed=(
                    discord.Embed(
                        title="🌟 أهلاً بك في نادي سراج!",
                        description=f"حياك الله يا **{member.name}** في مجتمعنا.\n\nستجد هنا صحبة صالحة 🤝 تعينك على التقرب إلى الله، وبيئة مليئة بالعلم والعمل.",
                        color=discord.Color.gold(),
                    )
                    .add_field(
                        name="💡 خطوتك الأولى",
                        value="خذ وقتك للتعرف على الأعضاء في القنوات العامة، وشاركنا اهتماماتك.",
                        inline=False,
                    )
                    .set_footer(text="نتمنى لك وقتاً نافعاً ومباركاً معنا!")
                ),
                view=WelcomeView(),
            )
            Log.info("WELCOME", f"Successfully welcomed {member.name} ({member.id})")

        except discord.Forbidden:
            Log.error("WELCOME", f"Could not DM {member.name} ({member.id})")


async def main():
    bot = MyBot()
    await bot.start(TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        Log.info("Bot", "Bot stopped manually")
