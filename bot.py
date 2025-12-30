import discord
from discord.ext import commands

import os

STYLES = [
    "Isagi", "Chigiri", "Hiori",
    "Bachira", "Otoya", "Gagamaru",
    "Nagi", "Reo", "Rin", "Yukimiya",
    "Shidou", "Aiku", "Roi",
    "Kaiser", "Charles",
    "Sae", "Don Lorenzo",
    "Loki", "Lavinho"
]
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


class StyleSelect(discord.ui.Select):
    def __init__(self):
        options = [discord.SelectOption(label=style) for style in STYLES]
        super().__init__(
            placeholder="Choisis ton style BLR",
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        style = self.values[0]

        channel = discord.utils.get(
            interaction.guild.text_channels,
            name="recap-style-blr"
        )

        if channel is None:
            await interaction.response.send_message(
                "❌ Salon #recap-style-blr introuvable",
                ephemeral=True
            )
            return

        await channel.send(
            f"📌 **STYLE BLR**\n"
            f"Joueur : {interaction.user.mention}\n"
            f"Style : **{style}**"
        )

        await interaction.response.send_message(
            f"✅ Style choisi : **{style}**",
            ephemeral=True
        )

class StyleView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(StyleSelect())

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def styles(ctx):
    embed = discord.Embed(
        title="🎮 CHOIX DU STYLE – BLR",
        description="\n".join(STYLES),
        color=0x2F3136
    )
    await ctx.send(embed=embed, view=StyleView())

bot.run(os.getenv("DISCORD_TOKEN"))
