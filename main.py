import os
import discord

client = discord.Client()

@client.event
async def on_ready():
  print("Connected successfully as {client.user}".format(client))

#The list below incorporates unconventional financial metric to track the asset - Bitcoin - utilizing on-chain metrics and data. Retrieved from: https://academy.glassnode.com/

metrics_list = ['sopr', 'nupl', 'nvt', 's2f', 'mvrv-z', 'puell']

metrics_dict = {'sopr':'spent output profit ratio - profitability and losses over a particular time-frame; >1 profit; <1 loss ',
'nupl':'net unrealized profit/loss (market cap - realized cap)',
'nvt':'network value to transaction ratio (market cap / daily transfer volume); high-bullish; low-bearish',
's2f':'or stock to flow is the ratio of the current stock of a commodity and the flow of new production; high-sound money; low-not sound',
'mvrv-z':'market-value-to-realized-value score is used to assess whether an asset is overvalued or undervalued relative to its fair value, or the deviation between its market cap and realized cap; helps spot market bottoms and tops',
'puell':'or puell multiple examines the fundamentals of mining profitability. It is the ratio of ( daily coin issuance(usd)/ 365 moving average of daily coin issuance)'
 }

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('?sopr'):
    await message.channel.send('spent output profit ratio - profitability and losses over a particular time-frame; >1 profit; <1 loss')
  if message.content.startswith('?nupl'):
    await message.channel.send('net unrealized profit/loss (market cap - realized cap);>0 profit; <0 loss')
  if message.content.startswith('?nvt'):
    await message.channel.send('network value to transaction ratio (market cap / daily transfer volume); high-bullish; low-bearish')
  if message.content.startswith('?s2f'):
    await message.channel.send('or stock to flow is the ratio of the current stock of a commodity and the flow of new production; high-sound money; low-not sound')
  if message.content.startswith('?mvrv-z'):
    await message.channel.send('market-value-to-realized-value score is used to assess whether an asset is overvalued or undervalued relative to its fair value, or the deviation between its market cap and realized cap; helps spot market bottoms and tops')
  if message.content.startswith('?puell'):
    await message.channel.send('or puell multiple examines the fundamentals of mining profitability. It is the ratio of ( daily coin issuance(usd) / 365 moving average of daily coin issuance)')

client.run(os.environ['TOKEN'])