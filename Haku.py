#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

import Secreto
import discord
import asyncio

client = discord.Client()
token = Secreto.Token()

magenta = 0xFF00FF

@client.event
async def on_ready():
    print('--------------- Haku ---------------')
    print('   ID: {}'.format(client.user.id))
    print(' Nome: {}'.format(client.user.name))
    print('------------------------------------')

    while True:
        await client.change_presence(game=discord.Game(name="🌟 Olá, Meu nome é Haku!", type=1))
        await asyncio.sleep(25)
        await client.change_presence(game=discord.Game(name="🌟 By: Troy", type=1))
        await asyncio.sleep(25)

@client.event
async def on_member_join(member):

    entrada = client.get_channel("480431497690742815")

    mensagem = discord.Embed(
        title='👋 Bem-vindo(a)!',
        color=magenta,
        description="Olá {}, espero que você se divirta no meu servidor!".format(member.mention)
    )
    mensagem.set_thumbnail(url=member.avatar_url)
    mensagem.set_footer(text="Servidor: Solitários")
    await client.send_message(entrada, "{}".format(member.mention))
    await client.send_message(entrada, embed=mensagem)

@client.event
async def on_member_remove(member):

    saida = client.get_channel("480431560659697666")

    mensagem = discord.Embed(
        title='😭 Até nunca mais!',
        color=magenta,
        description="{} saiu do servidor...".format(member.mention)
    )
    mensagem.set_thumbnail(url=member.avatar_url)
    mensagem.set_footer(text="Servidor: Solitários")
    await client.send_message(saida, "{}".format(member.mention))
    await client.send_message(saida, embed=mensagem)

client.run(token)
