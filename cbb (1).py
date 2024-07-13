#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import PRICE1, PRICE2, PRICE3, PRICE4, PRICE5, UPI_ID, UPI_IMAGE_URL, SCREENSHOT_URL


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =f"<b>○ ᴏᴡɴᴇʀ : <a href='t.me/InkaLinks'>ɪɴᴋᴀ ᴄʜɪᴘs</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/publicfille'>ᴘᴜʙʟɪᴄ ғɪʟᴇ</a>\n○ ᴘᴀɪᴅ ʙᴏᴛ : <a href='https://t.me/ifeelscam'>ᴍʀ.sʜᴀɪᴋʜ</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/offchats'>ᴄᴏᴅᴇ ᴍᴏɴᴋᴇʏ's </a>\n👨‍💻 ᴅᴇᴠʟᴏᴘᴇʀ  : <a href='https://t.me/ifeelscam'>ʜᴀᴍᴢᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [ [ InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://t.me/+NeqCUg-QDxo2Nzll"),
                  InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ" , url= "https://t.me/publicfille")],
                 [InlineKeyboardButton("ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴀᴅs ɪɴ ᴏɴᴇ ᴄʟɪᴄᴋ ", callback_data = "buy_prem")],
                 [InlineKeyboardButton("ᴡᴀᴛᴄʜ 𝟷𝟾+ sʜᴏʀᴛs ᴠɪᴅᴇᴏs ",url = "http://t.me/UnseenRobot/shorts")],
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ ", callback_data = "home"),
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                    ]
                ]
            )
        )

    elif data == "buy_prem":
        await query.message.edit_text(
            text=f"👋 Hello  {query.from_user.username}\n\n🎖️ Available Plans :\n\n● ₹{PRICE1}Rs For 7 Days Prime Membership\n\n● ₹{PRICE2}Rs For 1 Month Prime Membership\n\n● ₹{PRICE3}Rs For 3 Months Prime Membership\n\n● ₹{PRICE4}Rs For 6 Months Prime Membership\n\n● ₹{PRICE5}Rs For 1 Year Prime Membership\n\n\n🔖 If you want to purchase Prime membership then please Contact Bot Owner & Admin\n\nOwner & Admin accounts are mentioned below",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("ᴏᴡɴᴇʀ", url="t.me/inkax"),
                        InlineKeyboardButton("ᴀᴅᴍɪɴ ",url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("🚫 ᴄʟᴏsᴇ 🚫", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    elif data == "home":
        await query.message.edit_text(
            text=f"<b>I'm advance Token bot with Premium Features of providing videos for @Inkalinks Channel!!.\n\n⤵️ Buy Premium Plans ⤵️\n💸┣➤@lnkachipsbot</b>",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [ InlineKeyboardButton(text="🏡", callback_data="about"),
                    InlineKeyboardButton(text="🛡", callback_data="about"),
                    InlineKeyboardButton(text="💳", callback_data="about"),
                    InlineKeyboardButton(text="💸", callback_data="about"),
                    InlineKeyboardButton(text="🖥", callback_data="about"),
                ],[ InlineKeyboardButton( "ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url = "t.me/InkaLinks" ),
                    InlineKeyboardButton("sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ", url = "https://t.me/+nrNgQ7sT3XQxZTc1")
                ], [ InlineKeyboardButton("ᴡᴀᴛᴄʜ 𝟷𝟾+ sʜᴏʀᴛs ᴠɪᴅᴇᴏs", url = "http://t.me/UnseenRobot/shorts") ],
                [
                    InlineKeyboardButton("🤖 ᴀʙᴏᴜᴛ ᴍᴇ", callback_data = "about"),
                    InlineKeyboardButton("🚫 ᴄʟᴏsᴇ ", callback_data = "close")
                ]
            ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except: 
            pass
    
        
    
