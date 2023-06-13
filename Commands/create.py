import discord
from discord import app_commands
from discord.ext import commands


class Create(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="create", description="Create anything.")
    async def runes(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Test")
        await interaction.response.send_message(embed=embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Create(client))
