import discord

__all__ = ["WelcomeView"]


class WelcomeView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(
            discord.ui.Button(
                label="إنستغرام",
                url="https://instagram.com/siraj_1337",
                style=discord.ButtonStyle.link,
                emoji="📸",
            )
        )
        self.add_item(
            discord.ui.Button(
                label="واتساب",
                url="https://whatsapp.com/channel/0029Vb7aNirDeON7nvguNp3G",
                style=discord.ButtonStyle.link,
                emoji="💬",
            )
        )
        self.add_item(
            discord.ui.Button(
                label="تيليجرام",
                url="https://t.me/siraj_club",
                style=discord.ButtonStyle.link,
                emoji="✈️",
            )
        )
