import discord

client = discord.Client()
bot_token = "TOKEN ID"

# ロールID
Minecraft_role = 914446401189081148
AmongUs_role = 914446340291969054
Valorant_role = 914446491102355457
Apex_role = 914446515701973022
DyingLight2_role = 938897626848452628
PUBG_role = 938897539120377856
# ロールIDリスト
role_IDs = [
    Minecraft_role,
    AmongUs_role,
    Valorant_role,
    Apex_role,
    DyingLight2_role,
    PUBG_role,
    ]
# 絵文字
Minecraft_emoji = "⚒️"
AmongUs_emoji = "🚀"
Valorant_emoji = "⚔️"
Apex_emoji = "🔫"
DyingLight2_emoji = '🧟'
PUBG_emoji = '🕵️'
# 絵文字リスト
emoji_IDs = [
    Minecraft_emoji,
    AmongUs_emoji,
    Valorant_emoji,
    Apex_emoji,
    DyingLight2_emoji,
    PUBG_emoji,
]
# 各ロールのメンバー表リスト
Minecraft_member = []
AmongUs_member = []
Valorant_member = []
Apex_member = []
DyingLight2_member = []
PUBG_member = []
# 各ロールのメンバー表テキスト
Minecraft_txt = 'Minecraft_member.txt'
AmongUs_txt = 'AmongUs_member.txt'
Valorant_txt = 'Valorant_member.txt'
Apex_txt = 'Apex_member.txt'
DyingLight2_txt = 'DyingLight2_member.txt'
PUBG_txt = 'PUBG_member.txt'
# メンバー表テキストを読み込む関数
def member_txt_load(role_txt, list_name):
    with open(role_txt, encoding='UTF-8') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            list_name.append(line)
            line = f.readline()
        print(list_name)

# BOT打ち込みチャンネル
Bot_channel_id = 882629635190439956
# 概要チャンネル(結果)
Oviw_channel_id = 882629482530344981
# ロールメンバー表チャンネル
role_member_channel_id = 922150568951152650
# 概要チャンネルのテキストID
Oviw_text_id = "まだ取得されてません"
# ロールメンバー表チャンネルのテキストID
role_member_text_id = "まだ取得されてません"

# 起動時処理
@client.event
async def on_ready():
    print('ログインしました')
# 概要チャンネルの最後のテキストIDを自動的に取得する
    global Oviw_text_id
    channel = client.get_channel(Oviw_channel_id)
    last_msg = await channel.fetch_message(channel.last_message_id)
    Oviw_text_id = last_msg.id
    print(Oviw_text_id,'概要チャンネルのテキストIDです')
# メンバー表のテキストを読み込む
    member_txt_load(Minecraft_txt, Minecraft_member)
    member_txt_load(AmongUs_txt, AmongUs_member)
    member_txt_load(Valorant_txt, Valorant_member)
    member_txt_load(Apex_txt, Apex_member)
    member_txt_load(DyingLight2_txt, DyingLight2_member)
    member_txt_load(PUBG_txt, PUBG_member)
# メンバー表チャンネルの最後のテキストIDを取得する(なければ投稿する)
    global role_member_text_id
    channel = client.get_channel(role_member_channel_id)
    last_msg = await channel.fetch_message(channel.last_message_id)
    role_member_text_id = last_msg.id
    print(role_member_text_id,'ロールメンバー表チャンネルのテキストIDです')

    test_list = Minecraft_member + AmongUs_member + Valorant_member + Apex_member
    role_member_list = "\n".join(test_list)
    print(role_member_list)

@client.event
async def on_message(message):
    global Oviw_text_id
# BOT打ち込みチャンネルから概要チャンネルへの転送とリアクション付与
    if message.content.startswith("/rols"):
    # 送信されたチャンネルとBOTの打ち込みチャンネルが正しいか
        if message.channel.id == Bot_channel_id:
    # 送信された文章のコマンド部分の削除と概要チャンネルへの送信
            channel = client.get_channel(Oviw_channel_id)
            msg_content = message.content.lstrip("/rols ")
            await channel.send(msg_content)
    # 概要チャンネルへ送信された文章にリアクションをつける
    if message.channel.id == Oviw_channel_id:
        for Emoji in emoji_IDs:
            await message.add_reaction(Emoji)
            Oviw_text_id = message.id

# BOT打ち込みチャンネルからメンバー表チャンネルのへの転送
    if message.content.startswith("/rolm"):
        if message.channel.id == Bot_channel_id:
            channel = client.get_channel(role_member_channel_id)
            msg_content = message.content.lstrip("/rolm ")
            await channel.send(msg_content)

# 概要チャンネルのメッセージを編集する
    if message.content.startswith("/rolE"):
        channel = client.get_channel(Oviw_channel_id)
        rolE_content = message.content.lstrip("/rolE ")
        msg = await channel.fetch_message(Oviw_text_id)
        await msg.edit(content=rolE_content)

# 概要のテキストにリアクションを手動で追加する
    if message.content.startswith("/rolade"):
        channel = client.get_channel(Oviw_channel_id)
        msg = await channel.fetch_message(Oviw_text_id)
        for Emoji in emoji_IDs:
            await msg.add_reaction(Emoji)

# コマンドヘルプ ※要調整
    if message.content.startswith("/rolhelp"):
        if message.channel.id == Oviw_channel_id:
            rolhelp = "コマンド一覧です\n/rols → BOT打ち込みチャンネルから概要チャンネルへの転送とリアクション付与\n/ovid → 手動でリアクションの監視対象IDを紐づける\n/rolE → 紐づけられたメッセージを編集する"
            await message.author.send(rolhelp)

# 現在のOviw_text_idを表示する
    if message.content.startswith("/check"):
        if message.channel.id == Bot_channel_id:
            print("現在のOviwIDは" + str(Oviw_text_id) + "です")
            print(Minecraft_member)

@client.event
async def on_raw_reaction_add(payload):
# リアクションが押されたテキストチャンネル、メッセージ、メンバーを取得
    text_channel = client.get_channel(payload.channel_id)
    message = await text_channel.fetch_message(payload.message_id)
    author = await text_channel.guild.fetch_member(payload.user_id)
# ロール付与関数
    def role_give(list_name, roleid, role_name, role_txt):
        list_name.insert(-1, '・' + author.name)
        with open(role_txt, 'w', encoding='UTF-8') as f:
            for d in list_name:
                f.write("%s\n" % d)
        print("{0}に{1}ロールが付与されました".format(author, role_name))
        return author.guild.get_role(roleid)
# リアクションの監視対象
    if payload.message_id == Oviw_text_id:
        # 各ロールの付与
        if payload.emoji.name == emoji_IDs[0]:
            await author.add_roles(role_give(Minecraft_member, role_IDs[0],'Minecraft',Minecraft_txt))
        if payload.emoji.name == emoji_IDs[1]:
            await author.add_roles(role_give(AmongUs_member, role_IDs[1],'AmongUs',AmongUs_txt))
        if payload.emoji.name == emoji_IDs[2]:
            await author.add_roles(role_give(Valorant_member, role_IDs[2],'Valorant',Valorant_txt))
        if payload.emoji.name == emoji_IDs[3]:
            await author.add_roles(role_give(Apex_member, role_IDs[3],'Apex',Apex_txt))
        if payload.emoji.name == emoji_IDs[4]:
            await author.add_roles(role_give(DyingLight2_member, role_IDs[4],'DyingLight2', DyingLight2_txt))
        if payload.emoji.name == emoji_IDs[5]:
            await author.add_roles(role_give(PUBG_member, role_IDs[5],'PUBG', PUBG_txt))
        ALL_member_list = Minecraft_member + AmongUs_member + Valorant_member + Apex_member + DyingLight2_member + PUBG_member
        role_member_list = "\n".join(ALL_member_list)
        channel = client.get_channel(role_member_channel_id)
        msg_id = role_member_text_id
        msg= await channel.fetch_message(msg_id)
        await msg.edit(content=role_member_list)


@client.event
async def on_raw_reaction_remove(payload):
# リアクションが押されたテキストチャンネル、メッセージ、メンバーを取得
    text_channel = client.get_channel(payload.channel_id)
    message = await text_channel.fetch_message(payload.message_id)
    author = await text_channel.guild.fetch_member(payload.user_id)
# ロール剥奪関数
    def role_proscribe(list_name, roleid, role_name, role_txt):
        list_name.remove('・' + author.name)
        with open(role_txt, 'w', encoding='UTF-8') as f:
            for d in list_name:
                f.write("%s\n" % d)
        print("{0}から{1}ロールが剥奪されました".format(author, role_name))
        return author.guild.get_role(roleid)
# リアクションの監視対象
    if payload.message_id == Oviw_text_id:
        # 各ロールの剥奪
        if payload.emoji.name == emoji_IDs[0]:
            await author.remove_roles(role_proscribe(Minecraft_member, role_IDs[0],'Minecraft', Minecraft_txt))
        if payload.emoji.name == emoji_IDs[1]:
            await author.remove_roles(role_proscribe(AmongUs_member, role_IDs[1],'AmongUs', AmongUs_txt))
        if payload.emoji.name == emoji_IDs[2]:
            await author.remove_roles(role_proscribe(Valorant_member, role_IDs[2],'Valorant', Valorant_txt))
        if payload.emoji.name == emoji_IDs[3]:
            await author.remove_roles(role_proscribe(Apex_member, role_IDs[3],'Apex', Apex_txt))
        if payload.emoji.name == emoji_IDs[4]:
            await author.remove_roles(role_proscribe(DyingLight2_member, role_IDs[4],'DyingLight2', DyingLight2_txt))
        if payload.emoji.name == emoji_IDs[5]:
            await author.remove_roles(role_proscribe(PUBG_member, role_IDs[4],'PUBG', PUBG_txt))
        ALL_member_list = Minecraft_member + AmongUs_member + Valorant_member + Apex_member + DyingLight2_member + PUBG_member
        role_member_list = "\n".join(ALL_member_list)
        channel = client.get_channel(role_member_channel_id)
        msg_id = role_member_text_id
        msg= await channel.fetch_message(msg_id)
        await msg.edit(content=role_member_list)

client.run(bot_token)