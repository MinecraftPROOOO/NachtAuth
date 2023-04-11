import discord
from discord.ext import commands
import json

with open("../config.json") as f:
    config = json.load(f)

# set the token to the token in the config file
token = config["discord"]["bot_token"]
client = commands.Bot()

@client.event
async def on_ready():
    print("Bot is ready")

@client.slash_command(name="setup", description="⚠️ THIS WILL DELETE ALL CHANNELS IN THE SERVER ⚠️")
async def setup(ctx, *, oauth: str):
    for channel in ctx.guild.channels:
        await channel.delete()

    # create all categories 
    Verification = await ctx.guild.create_category("✅ | Verfication")
    Important = await ctx.guild.create_category("📢 | Important")
    Carries = await ctx.guild.create_category("🛡️| Carries")
    General = await ctx.guild.create_category("📚 | General")
    
    # change all category permissions
    await Verification.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
    await Important.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
    await Carries.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False)
    await General.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False, read_messages=False, connect=False, speak=False)

    # create all channels
    Verify = await ctx.guild.create_text_channel("✅│verify", category=Verification)
    Rules = await ctx.guild.create_text_channel("📜│rules", category=Important)
    Announcements = await ctx.guild.create_text_channel("📢│announcements", category=Important)
    Carry = await ctx.guild.create_text_channel("⚔️│carries", category=Carries)
    GeneralText = await ctx.guild.create_text_channel("📚│general", category=General)
    GeneralVoice = await ctx.guild.create_voice_channel("🔊│general", category=General)

    # config certain channels
    await Announcements.set_permissions(ctx.guild.default_role, send_messages=False, add_reactions=False, read_messages=False)

    verificationembed = discord.Embed(
        title = "Verification",
        description = "Verification is required to view this server.",
        color = 0x0000FF
    )
    verificationembed.add_field(name="FAQ", value="**Q:** What is verification?\n**A:** Verification is a process that allows you to view this server. You will be asked to verify by clicking a button below.\n\n**Q:** Why do I need to verify?\n**A:** This server is a private server that requires verification to view. This is to prevent people from joining and spamming the server.\n\n**Q:** How do I verify?\n**A:** Click the button below to verify. You will be asked to authorize the bot to view your information. This is required to verify you. You will then be asked to join a voice channel. Once you join the voice channel, you will be verified.", inline=False)
    verificationembed.add_field(name="Verification", value=f"Click [here]({oauth}) to verify yourself!", inline=False)
    verificationembed.set_footer(text=f"Before you verify, please read the rules in <#{Rules.id}>.")
    await Verify.send(embed=verificationembed)

    # make rules embed
    rulesembed = discord.Embed(
        title = "Rules",
        description = "Please read and follow the rules of the server.",
        color = 0x00FF00
    )
    rulesembed.add_field(name="Rule 1", value="Be respectful and kind to others. No harassment, discrimination, or hate speech will be tolerated.", inline=False)
    rulesembed.add_field(name="Rule 2", value="No NSFW content or discussions are allowed.", inline=False)
    rulesembed.add_field(name="Rule 3", value="Do not spam or excessively self-promote in the server.", inline=False)
    rulesembed.add_field(name="Rule 4", value="Follow Discord's Terms of Service (TOS) and Community Guidelines.", inline=False)
    rulesembed.add_field(name="Rule 5", value="Use appropriate language and keep conversations PG-13.", inline=False)
    rulesembed.add_field(name="Rule 6", value="Do not impersonate staff or other members.", inline=False)
    rulesembed.add_field(name="Rule 7", value="Do not post personal information of others without their consent.", inline=False)
    rulesembed.add_field(name="Rule 8", value="Report any issues or violations to the staff.", inline=False)
    rulesembed.add_field(name="Rule 9", value="Failure to comply with the rules may result in a warning, mute, kick, or ban at the staff's discretion.", inline=False)
    rulesembed.set_footer(text="By verifying yourself, you agree to abide by the rules of the server.")
    await Rules.send(embed=rulesembed)
        # make announcement embed
    announcementsembed = discord.Embed(
        title = "Announcements",
        description = "Important announcements will be posted here.",
        color = 0xFFA500
    )
    announcementsembed.add_field(name="Announcement 1", value="Welcome to the server! Please make sure to read and follow the rules.", inline=False)
    announcementsembed.set_footer(text="Stay updated with announcements in this channel.")
    await Announcements.send(embed=announcementsembed)

    # make carries embed
     # make carries embed
    carriesembed = discord.Embed(
        title = "☠️ Catacombs Carries",
        description="All specifics for dungeon carries.",
        color = 0x0000FF
    )
    carriesembed.add_field(name="Floor 1", value="Price: 50k", inline=False)
    carriesembed.add_field(name="Floor 2", value="Price: 100k", inline=False)
    carriesembed.add_field(name="Floor 3", value="Price: 150k", inline=False)
    carriesembed.add_field(name="Floor 4", value="Price: 200k", inline=False)
    carriesembed.add_field(name="Floor 5", value="Price 300k", inline=False)
    carriesembed.add_field(name="Floor 6", value="Price: 600k", inline=False)
    carriesembed.add_field(name="Floor 7", value="Price: 3m", inline=False)
    carriesembed.add_field(name="Create a ticket", value="at #create-a-ticket to get a carry!", inline=False)
    await Carry.send(embed=carriesembed)

client.run(token)

