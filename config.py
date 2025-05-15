from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

main_menu_text = """<b>🍔 Welcome to Crackdonalds</b>
Home of financial fast food and zero-nutritional-value alpha. Powered by <b>$CRACK</b>, built for the true Solana degen. Choose from the menu below and order your daily dose of irony:"""

general_info_text = """<b>📰 General Info</b>

<b>Welcome to Crackdonalds — Solana’s favorite financial fast-food joint.</b>\n
We don’t do utility. We do community, chaos, and cholesterol-level pumpage. <b>$CRACK</b> isn’t just a token — it’s a lifestyle. Inspired by McDonald’s but built for the memechain, we’re flipping burgers into bags, and dips into Bugattis.

So come for the memes, stay for the liquidity (or the lack of it)."""
roadmap_text = """<b>📅 Roadmap</b>

<b>🍟 The $CRACK Franchise Plan</b>
We’ve got more phases than a greasy kitchen shift. Here’s how we plan to take over the memeconomy:

<b>Phase 1 – Kitchen Prep</b>
🔹 Token launch on Solana
🔹 Hit 1000 Twitter followers
🔹 Launch this glorious bot
🔹 Cook up a website + memes

<b>Phase 2 – Open for Business</b>
🔹 Get listed on Jupiter, Raydium
🔹 Collab with other degen tokens
🔹 Launch the Whale Chat (shhh...)
🔹 Mint our first NFT drop – <i>McFrens</i>

<b>Phase 3 – Franchising</b>
🔹 CrackDAO: for community governance (and more memes)
🔹 Open the community treasury
🔹 Beta test <i>CrackChain</i> – the meme layer of Solana
🔹 Get on Tier 2 CEXs

<b>Phase 4 – Global Takeover</b>
🔹 Meme merch you didn’t ask for
🔹 <i>Crackburger Simulator</i> – yes, it’s real
🔹 Fast-food-themed metaverse
🔹 Cease & Desist from McDonald's = ultimate win"""

whale_text = """<b>🐳 Whale Chat Access</b>

<b>🔒 Access Denied? You’re not fry-cooked enough.</b>
The Whale Chat is reserved for absolute units holding <b>50M+ $CRACK</b>. That’s right — no scrubs in this deep fryer.

Inside, you’ll find:
💬 Alpha leaks
🧠 Strategy memes
💩 Possibly financial advice (not really)

<b>Connect your wallet</b> (feature coming soon) and prove your $CRACK stack to enter the grill zone."""

links_text="""<b>💬 Community Links</b>

<b>Pull up to the drive-thru window of web3 degeneracy:</b>

🐦 <b>Twitter:</b> <a href="https://twitter.com/crackdonalds">@crackdonalds</a>
📣 <b>Telegram Lounge:</b> <a href="https://t.me/cracklounge">t.me/cracklounge</a>
🌐 <b>Website:</b> <a href="https://crackdonalds.xyz">crackdonalds.xyz</a>

Follow, join, and maybe even shill. We don’t judge (unless it’s low effort)."""

charts_text="""<b>🧻 Chart</b>

<b>Track $CRACK like a true degen.</b>
Whether you're here for the pump, the dump, or just to watch the grease bubble:

🔗 <b>Birdeye:</b> <i><a href="https://twitter.com/crackdonalds">CRACK on Birdeye</a></i>
🔗 <b>Dexscreener:</b> <i><a href="https://twitter.com/crackdonalds">CRACK on Dexscreener</a></i>

Refresh every 5 seconds like it’ll change something. Spoiler: it won’t. But it’s fun.
"""

airdrop_text = """<b>🎁 Claim Airdrop</b>

<b>🚨 FREE MONEY ALERT?</b>
Just kidding. This airdrop isn’t live yet. But hey — it makes the bot look serious, doesn’t it?

We’ll be dropping <b>$CRACK bombs</b> soon.
✅ Follow Twitter
✅ Join the Lounge
✅ Wait for whitelist info

<b>Reminder:</b> If anyone DMs you, it’s a scam. If we DM you, it’s still a scam.
"""

nft_text = """<b>🕹️ McFrens NFT</b>

<b>🚧 Under Construction – Wipe your greasy hands.</b>
The <i>McFrens</i> are 777 NFT fry cooks, janitors, and rogue managers ready to flip your bags and maybe your burgers.

🔸 Mint price: TBD
🔸 Utility: LOL
🔸 Vibe: Immaculate

Stay tuned for sneak peeks, mint date, and how to hire your first McFriend.
"""

main_menu_markup = InlineKeyboardBuilder()
button1 = types.InlineKeyboardButton(text = "📰General Info", callback_data = "general")
button2 = types.InlineKeyboardButton(text = "📅Roadmap", callback_data = "roadmap")
button3 = types.InlineKeyboardButton(text = "🐳 Whale Chat Access", callback_data = "whale")
button4 = types.InlineKeyboardButton(text = "💬 Community Links", callback_data = "links")
button5 = types.InlineKeyboardButton(text = "🧻 Chart", callback_data = "chart")
button6 = types.InlineKeyboardButton(text = "🎁 Claim Airdrop", callback_data = "airdrop")
button7 = types.InlineKeyboardButton(text = "🕹️ McFrens NFT", callback_data = "nft")
main_menu_markup.row(button1, button2) 
main_menu_markup.row(button3, button4)
main_menu_markup.row(button5, button7)
main_menu_markup.row(button6)

back_markup = InlineKeyboardBuilder()
back_btn = types.InlineKeyboardButton(text="Back", callback_data="back")
back_markup.row(back_btn)