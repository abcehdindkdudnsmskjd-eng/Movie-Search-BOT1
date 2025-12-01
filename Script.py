class script(object):
    START_TXT = """<b><u>🍿Welcome to The UNIVERSE of CINEMA🍿</u></b>

<b>ʜᴇʏ {}, {}</b>

<b>🤖 ɪ ᴀᴍ <a href=https://t.me/moviesearch0294bot{}>{}</a>, ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.</b>
"""


    GSTART_TXT = """<b>🍿Welcome to The UNIVERSE of CINEMA🍿</b>

<b>ʜᴇʏ {},</b>

<b>🤖 ɪ ᴀᴍ <a href=https://t.me/moviesearch0294bot{}>{}</a>, ᴛʜᴇ ᴍᴏꜱᴛ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ꜰᴇᴀᴛᴜʀᴇꜱ.</b>"""

    
    HELP_TXT = """<b>


👑 𝐕𝐈𝐏 𝐋𝐨𝐮𝐧𝐠𝐞 — 𝐄𝐱𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐀𝐜𝐜𝐞𝐬𝐬

✨ Need a Movie / Series?  
Your request must follow the Royal Format ↓

💼 𝐒𝐞𝐫𝐢𝐞𝐬  
➤ Title + S01

💼 𝐇𝐢𝐧𝐝𝐢 𝐃𝐮𝐛  
➤ Title + Hindi

💼 𝐌𝐨𝐯𝐢𝐞𝐬  
➤ Title + Year (e.g., Joker 2019)

🌟 𝐏𝐫𝐨 𝐓𝐢𝐩  
Use Google for exact title before typing.  
Precision = Priority Service ⚡

</b>"""

    ABOUT_TXT = """<b>

🎬 𝙋𝙧𝙤𝙟𝙚𝙘𝙩 𝘿𝙖𝙩𝙖𝙘𝙖𝙧𝙙 — 𝙁𝙞𝙡𝙚 𝙄𝘿: 𝘼𝘽𝙊𝙐𝙏/𝟎𝟎𝟏

👤 𝐁𝐨𝐭 𝐍𝐚𝐦𝐞 : <a href="https://t.me/moviesearch0249bot{}">{}</a>  
🛠️ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 : <a href="{}">Owner</a>  

─────────────────────

📦 𝐒𝐲𝐬𝐭𝐞𝐦 𝐁𝐚𝐬𝐞 : Pyrogram  
🐍 𝐂𝐨𝐝𝐞 𝐋𝐚𝐧𝐠 : Python 3  
🗄️ 𝐃𝐚𝐭𝐚 𝐂𝐨𝐫𝐞 : MongoDB  
🌐 𝐍𝐨𝐝𝐞 : Heroku Cloud  

─────────────────────

📡 𝐂𝐮𝐫𝐫𝐞𝐧𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : v1.4  • Stable

</b>"""

    RESTART_TXT = """
<b>{} Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code> v1.4 [ Sᴛᴀʙʟᴇ ]</code>
</b>"""

    CHANNELS = """
<b>

📡 𝘽𝙧𝙤𝙖𝙙𝙘𝙖𝙨𝙩 𝙉𝙚𝙩𝙬𝙤𝙧𝙠 — 𝘾𝙝𝙖𝙣𝙣𝙚𝙡𝙨 & 𝙂𝙧𝙤𝙪𝙥𝙨

🎬 Daily drops of new Movies & Series  
⚡ Ultra-fast bots synced to the network  
🎁 Completely free — no limits, no fuss  
🌙 24/7 service uptime for nonstop access  

</b>
"""

    MULTI_STATUS_TXT = """<b>

🎛️ 𝙎𝙮𝙨𝙩𝙚𝙢 𝘿𝙖𝙨𝙝𝙗𝙤𝙖𝙧𝙙 — 𝙍𝙚𝙖𝙡-𝙩𝙞𝙢𝙚 𝙎𝙩𝙖𝙩𝙪𝙨

📂 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝟏  
• Users           : <code>{}</code>  
• Groups          : <code>{}</code>  
• Premium Users   : <code>{}</code>  
• Total Files     : <code>{}</code>  
• Storage Used    : <code>{}</code>  
• Storage Free    : <code>{}</code>  

────────────────────────────

🗄️ 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 𝟐  
• Files Indexed   : <code>{}</code>  
• Size            : <code>{}</code>  
• Free Space      : <code>{}</code>  

────────────────────────────

🤖 𝐁𝐨𝐭 𝐒𝐲𝐬𝐭𝐞𝐦  
• Uptime          : {}  
• RAM Usage       : <code>{}%</code>  
• CPU Load        : <code>{}%</code>  

────────────────────────────

🧾 𝐒𝐲𝐧𝐜𝐞𝐝 𝐅𝐢𝐥𝐞𝐬 (𝐁𝐨𝐭𝐡 𝐃𝐁𝐬) : <code>{}</code>

</b>"""

    STATUS_TXT = """<b>

🎛️ 𝙎𝙮𝙨𝙩𝙚𝙢 𝙈𝙤𝙣𝙞𝙩𝙤𝙧 — 𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚

📂 Users          : <code>{}</code>  
📂 Groups         : <code>{}</code>  
💎 Premium Users  : <code>{}</code>  
🗄️ Total Files    : <code>{}</code>  
📦 Used Storage   : <code>{}</code>  
🧰 Free Storage   : <code>{}</code>  

────────────────────────────

🤖 𝐁𝐨𝐭 𝐌𝐞𝐭𝐫𝐢𝐜𝐬  
⏱ Uptime         : {}  
📊 RAM Usage      : <code>{}%</code>  
⚙️ CPU Load       : <code>{}%</code>  

</b>"""

    LOG_TEXT_G = """#NewGroup
    
Gʀᴏᴜᴘ = {}
Iᴅ = <code>{}</code>
Tᴏᴛᴀʟ Mᴇᴍʙᴇʀs = <code>{}</code>
Aᴅᴅᴇᴅ Bʏ - {}
"""

    LOG_TEXT_P = """#NewUser
    
Iᴅ - <code>{}</code>
Nᴀᴍᴇ - {}
"""
    NT_ADMIN_ALRT_TXT = """<b>⚠️ 𝐀𝐜𝐜𝐞𝐬𝐬 𝐃𝐞𝐧𝐢𝐞𝐝  
You are not an admin in this group.</b>"""


    NT_ALRT_TXT = """<b>⚠️ Access Denied  
This action is not assigned to you.</b>"""

    
    ALRT_TXT = """<b>⚠️ Hello {},  
This request does not belong to you.  
Please submit your own request.</b>"""


    OLD_ALRT_TXT = """<b>🔄 Hey {},  
This message is outdated.  
Please submit your request again.</b>"""


    PRE_STREAM = """<b>🔒 Premium Feature Locked  
This option is available only for premium users.

✨ Unlock advanced tools & exclusive content  
💳 Upgrade to Premium to continue.</b>"""


    PRE_STREAM_ALERT = """<b>⚠️ Premium Content  
Unlock this feature by upgrading to Premium.</b>"""


    CUDNT_FND = SPELLING_ERROR_TXT = """<b>⚠️ Spelling Error Detected</b>  
<b>Please select the correct title from the list below 👇</b>

<blockquote>👇 Choose the correct movie title from the suggestions below</blockquote>"""


    DEL_MSG = """⚠️ This file/video will be deleted in <b><u><code>{}</code></u></b>

<blockquote expandable><b><i>Please forward this file elsewhere and begin your download there.</i></b></blockquote>"""






    I_CUDNT = """<b>⚠️ No results found for: <u>{}</u></b>

<b>Please verify the spelling on Google and try again.</b>

<b>🎬 Movie Format:</b>  
• Example: Jawan  
• Example: Jawan 2023  

<b>📺 Series Format:</b>  
• Example: Loki S01  
• Example: Loki S01E04  
• Example: Lucifer S03E24  

<b>🚫 Avoid using symbols like: ' : ( ! , . / )</b>"""

    
    I_CUD_NT = """<b>⚠️ I couldn’t find any movie related to: <u>{}</u></b>

<b>Possible reasons:</b>
1) The movie has not been released on OTT/DVD yet  
2) Try searching with the release year (Example: Jawan 2023)  
3) The movie is not available in the database — you may report it to the admins  
"""

    MVE_NT_FND = NOT_FOUND_TXT = """<b>⚠️ This movie is not available in the database.</b>

<blockquote>The requested title could not be located. Please verify the spelling or try a different title.</blockquote>"""

    
    TOP_ALRT_MSG = """🔎 Searching for your query in the database..."""


    MELCOW_ENG = """<b>👋 Hello {},

Welcome to <u>{}</u> 🎬

🔎 Search any movie or series simply by typing its name.  
The system will fetch the best match instantly.

If you experience any issue while downloading or accessing files,  
you can contact support using the button below.</b>"""

    
    DISCLAIMER_TXT = """
<b>This is an open-source project.

All files indexed by this bot are publicly available on the internet or uploaded by third parties on Telegram.  
This bot only provides an easier way to search and locate those files.

We respect all copyright laws and comply with DMCA and EUCD.  
If any content violates legal rights, please contact us for immediate removal.

Users must not download, stream, share, or reproduce copyrighted content without proper authorization from the rightful owner.  
The bot does not host or store any files — it only indexes links already available on Telegram.</b>
"""


    DREAMXBOTZ_DONATION = DONATE_TXT = """<b>👋 Hello {},</b>

<blockquote><b>💖 Support the Developer</b></blockquote>

<b>To keep this service online, add new features, and maintain high-quality movie/series uploads, your support truly helps.  
Donations assist with server costs and continuous development.</b>

<b>You may contribute any amount you wish.</b>

<blockquote><b>🎉 Choose your donation method below:</b></blockquote>

➤ 📷 QR Code → <a href='{}'>Scan Here</a>  
➤ 💸 UPI ID → <code>{}</code>

<b>📌 Please send a screenshot after completing the donation.</b>"""


    SINFO = """
<b>📺 Series Request Format</b>

To get accurate results:
• Search the correct series name on Google  
• Copy the exact title  
• Paste it here without adding extra symbols

<b>Example:</b>  
• Loki S01E01

<b>⚠️ Avoid using characters like: ' : ( ! , . / )</b>
"""


    NORSLTS = """<b>#NoResults</b>

<b>ID:</b> <code>{}</code>  
<b>Name:</b> {}  

<b>Message:</b> <i>{}</i>"""

    
    CAPTION = """<b>{file_name}</b>

🎬 Enjoy your movie/series."""

    
    MOVIE_UPDATE_NOTIFY_TXT = """
<b><a href="{poster_url}">📥</a> <a href="{imdb_url}">New {tag} Added</a></b>

<blockquote>
🎬 <b>Title:</b> <code>{filename}</code>
🎭 <b>Genres:</b> {genres}
📺 <b>OTT:</b> {ott}
🎞️ <b>Quality:</b> {quality}
🔊 <b>Audio:</b> {language}
⭐ <b>Rating:</b> {rating}
{episodes}
</blockquote>

🔍 <b>Search:</b> {search_link}
"""


    IMDB_TEMPLATE_TXT = """
<b><a href="{url}">{title}</a> (<a href="{url}/releaseinfo">{year}</a>)</b>

⭐ <b>Rating:</b> <a href="{url}/ratings">{rating}</a>
🎭 <b>Genres:</b> {genres}
🔊 <b>Audio:</b> {languages}
"""


    LOGO = r"""
███████╗ █████╗ ██████╗ ████████╗██╗  ██╗ █████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██║ ██╔╝
███████╗███████║██████╔╝   ██║   ███████║███████║█████╔╝ 
╚════██║██╔══██║██╔══██╗   ██║   ██╔══██║██╔══██║██╔═██╗ 
███████║██║  ██║██║  ██║   ██║   ██║  ██║██║  ██║██║  ██╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

🚀 BOT STARTED SUCCESSFULLY...
"""



    #PLANS

    PAGE_TXT = """
Why so curious? 🤔
"""

    PURCHASE_TXT = """
Please select your payment method.
"""

    

    PREMIUM_TEXT = """
<blockquote><b>🎖️ Available Premium Plans</b></blockquote>

◉ 7 Days  —  ₹10
◉ 15 Days —  ₹20
◉ 30 Days —  ₹40
◉ 45 Days —  ₹55
◉ 60 Days —  ₹75

<b>📌 After completing the payment, please send a screenshot for verification.</b>
<b>⏳ Allow some time for your premium access to be activated.</b>
"""

    PREMIUM_STAR_TEXT = """
<blockquote><b>Payment Method: Telegram Stars ⭐</b></blockquote>

You can purchase premium access using Telegram Stars.

If you face any issue during the payment process, please take a screenshot
and send it to @sarthakpawar0294.

Select your desired amount and choose a subscription plan below. 👇
"""



    PREMIUM_UPI_TEXT = """
<blockquote><b>Payment Method: UPI 💳</b></blockquote>

You can purchase premium access using UPI or net banking.

<b>UPI ID:</b> <code>{}</code>

Please send a payment screenshot after completing the transaction.
Once submitted, allow some time for your premium access to be activated.
"""


    PREMIUM_END_TEXT = """
<b>Hey {},</b>

<b>Your premium access has ended.</b>  
<b>Thank you for using our service.</b>  
<b>Tap /plan to view available subscription options.</b>
"""


    
    BPREMIUM_TXT = """
<blockquote><b>🎁 Premium Features</b></blockquote>

○ No verification required  
○ No external link opening  
○ Direct file access  
○ Ad-free experience  
○ High-speed download links  
○ Multi-player streaming links  
○ Unlimited movies & series  
○ Full admin support  
○ Requests completed within 1 hour (if available)

• You can get premium by referring friends or purchasing a plan.

•─────•─────────•─────•
◉ Check your active plan: /myplan
"""


    PREPLANS_TXT = PREMIUM_TXT = """
<b>👋 Hey {},</b>

<blockquote><b>🎖️ Available Premium Plans</b></blockquote>

◉ 7 Days  —  ₹10  
◉ 15 Days —  ₹20  
◉ 30 Days —  ₹40  
◉ 45 Days —  ₹55  
◉ 60 Days —  ₹75  

•─────•─────────•─────•

🏷️ <b>Payment Methods</b>

💸 UPI ID → <code>{}</code>  
📷 QR Code → <a href="{}">Scan Here</a>  

<b>🧾 Pay according to your plan and enjoy premium access.</b>

<b>📌 Please send a payment screenshot after completing your transaction.</b>  
<b>⏳ Allow some time for your premium access to be activated.</b>

💎 <b>Check your plan → /myplan</b>
"""


    FREE_TXT = """
<b>👋 Hey {},</b>

<b>🎉 <u>Free Trial</u> — Available for 5 minutes</b>

○ No link verification  
○ Multi-player streaming links  
○ Ad-free experience  

<b>👨‍💻 Contact @sarthakpawar0294 to activate your free trial.</b>

➛ Use /plan to view all premium plans  
➛ Check your active plan with /myplan
"""

    
    UPI_TXT = """
<b>👋 Hey {},</b>

Please pay the required amount according to your selected plan  
and enjoy premium membership.

💵 <b>UPI ID:</b> <code>{}</code>

<b>📌 Please send a payment screenshot after completing the transaction.</b>
"""

    QR_TXT = """
<b>👋 Hey {},</b>

Please pay the required amount according to your selected plan  
and enjoy premium membership.

📸 <b>QR Code:</b> <a href="{}">Click here to scan</a>

<b>📌 Please send a payment screenshot after completing the transaction.</b>
"""


    SOURCE_TXT = """
<b>Source Code:</b> 👇

This is an open-source project.  
You may use or modify it freely, but selling the source code is strictly prohibited.

🔗 <a href="https://github.com/abcehdindkdudnsmskjd-eng/Movie-Search-BOT1">MovieSearchBOT</a>
"""


    SETTING_TXT = """    
<u>ꜱᴇᴛᴛɪɴɢꜱ</u> :
- ꜱᴇᴛᴛɪɴɢꜱ ɪꜱ ᴛʜᴇ ᴍᴏꜱᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ꜰᴇᴀᴛᴜʀᴇ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ.
- ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ᴛʜɪꜱ ʙᴏᴛ ꜰᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ.

<u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</u> :
• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""
    
    VERIFICATION_TEXT = """
<b>👋 Hey {},</b>

<b>You are not verified today.</b>  
Please complete the verification to get unlimited access until the next reset.

<b>#Verification: 1/3 ✓</b>

If you want direct file access without verification,  
you may upgrade to premium.
"""

    

    VERIFY_COMPLETE_TEXT = """
<b>👋 Hey {},</b>

<b>Your first verification is complete. ✓</b>

You now have unlimited access until the next verification cycle.
"""


    SECOND_VERIFICATION_TEXT = """
<b>👋 Hey {},</b>

<b>You are not verified.</b>  
Tap the verify button to unlock unlimited access until the next verification cycle.

<b>#Verification: 2/3 ✓</b>

If you prefer direct file access without verification,  
you can upgrade to premium.
"""

    SECOND_VERIFY_COMPLETE_TEXT = """
<b>👋 Hey {},</b>

<b>Your second verification is complete. ✓</b>

You now have unlimited access until the next verification cycle.
"""

    THIRDT_VERIFICATION_TEXT = """
<b>👋 Hey {},</b>

<b>You are not verified.</b>  
Tap the verify button to unlock unlimited access for the full next day.

<b>#Verification: 3/3 ✓</b>

If you prefer direct file access without verification,  
you can upgrade to premium.
"""

    THIRDT_VERIFY_COMPLETE_TEXT = """
<b>👋 Hey {},</b>

<b>Your third verification is complete. ✓</b>

You now have unlimited access for the entire next day.
"""

    VERIFIED_LOG_TEXT = """
User verified successfully ✓

👤 Name: {}  [<code>{}</code>]

📆 Date: <code>{}</code>

#Verification_{}_Completed
"""



    ADMIN_CMD = """ʜᴇʏ 👋,

📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴀʟʟ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ⇊

• /start - <code>ᴛᴏ ᴜꜱᴇ ᴍʏ ꜰᴇᴀᴛᴜʀᴇꜱ.</code>
• /stats - <code>ɢᴇᴛ ᴛʜᴇ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ ᴀɴᴅ ᴄʜᴀᴛꜱ.</code>
• /del_msg - <code>ʀᴇᴍᴏᴠᴇ ғɪʟᴇ ɴᴀᴍᴇ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ɴᴏтɪғɪᴄᴀᴛɪᴏɴ...</code>
• /movie_update - <code>ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code> 
• /pm_search - <code>ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ / ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...</code>
• /verify - <code>ᴛᴜʀɴ ᴏɴ / ᴏꜰꜰ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ (ᴏɴʟʏ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ)</code>
• /logs - <code>ɢᴇᴛ ᴛʜᴇ ʀᴇᴄᴇɴᴛ ᴇʀʀᴏʀꜱ.</code>
• /delete - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.</code>
• /users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /chats - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ.</code>
• /leave  - <code>ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ᴀ ᴄʜᴀᴛ.</code>
• /disable  -  <code>ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ.</code>
• /ban  - <code>ʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /unban  - <code>ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ.</code>
• /broadcast - <code>ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ.</code>
• /grp_broadcast - <code>ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘs.</code>
• /deletefiles - <code>ᴅᴇʟᴇᴛᴇ CᴀᴍRɪᴘ ᴀɴᴅ PʀᴇDVD ғɪʟᴇs ғʀᴏᴍ ᴛʜᴇ ʙᴏᴛ's ᴅᴀᴛᴀʙᴀsᴇ.</code>
• /send - <code>ꜱᴇɴᴅ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴜꜱᴇʀ.</code>
• /add_premium - <code>ᴀᴅᴅ ᴀɴʏ ᴜꜱᴇʀ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ.</code>
• /remove_premium - <code>ʀᴇᴍᴏᴠᴇ ᴀɴʏ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴘʀᴇᴍɪᴜᴍ.</code>
• /premium_users - <code>ɢᴇᴛ ʟɪꜱᴛ ᴏꜰ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀꜱ.</code>
• /get_premium - <code>ɢᴇᴛ ɪɴꜰᴏ ᴏꜰ ᴀɴʏ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ.</code>
• /restart - <code>ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ.</code>"""

    GROUP_CMD = """ʜᴇʏ 👋,
📚 ʜᴇʀᴇ ᴀʀᴇ ᴍʏ ᴄᴏᴍᴍᴀɴᴅꜱ ʟɪꜱᴛ ꜰᴏʀ ᴄᴜꜱᴛᴏᴍɪᴢᴇᴅ ɢʀᴏᴜᴘꜱ ⇊

• /settings - ᴄʜᴀɴɢᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.
• /set_shortner - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_shortner_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ꜱʜᴏʀᴛɴᴇʀ.
• /set_tutorial - ꜱᴇᴛ ʏᴏᴜʀ 1ꜱᴛ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_2 - ꜱᴇᴛ ʏᴏᴜʀ 2ɴᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_tutorial_3 - ꜱᴇᴛ ʏᴏᴜʀ 3ʀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ .
• /set_time - ꜱᴇᴛ 1ꜱᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_time_2 - ꜱᴇᴛ 2ɴᴅ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ɢᴀᴘ.
• /set_log_channel - ꜱᴇᴛ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ʟᴏɢ ᴄʜᴀɴɴᴇʟ.
• /set_fsub - ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /remove_fsub - ʀᴇᴍᴏᴠᴇ ᴄᴜꜱᴛᴏᴍ ꜰᴏʀᴄᴇ ꜱᴜʙ ᴄʜᴀɴɴᴇʟ.
• /reset_group - ʀᴇꜱᴇᴛ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ.
• /details - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ."""    



    
