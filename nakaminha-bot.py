# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import random
import datetime

# token
TOKEN = 'NDMzMjc2MDY3NDk1NTQyNzg0.WszNyA.itRFDiJXEd8d2XJVn6Q4wBGmq_Y'

# variaveis
cargo_de_ponto = "Classe Operária"
pontos_batidos = []
greets = ["Eae, {}", "Tranquilo, {}?", "De buenas, {}?", "Salve meu rei.", "No que posso te ajudar, {}?", "Como vai, {}?"]

# cliente
client = discord.Client()


# actions
@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content == "!ponto":
		
		msg = ""

		if str(message.channel) != "relógio-de-ponto":
			msg += "Usar a sala relógio-de-ponto para bater o ponto.\n"
			await message.channel.send(msg)
			return
	
		cargos = [c.name for c in message.author.roles]
		if cargo_de_ponto not in cargos:
			msg += "Você não faz parte da Classe Operária.\n"
			await message.channel.send(msg)
			return

		data = datetime.datetime.now()  # Some datetime object.

		msg += "Data: [{}]\n".format(data.strftime('%d/%m/%Y'))
		
		for ponto in pontos_batidos:
			
			if (message.author.name) == "cTRLLL":
				msg += "cuzão\n"

			if (ponto["id"] == message.author.id and ponto["horario_entrada"]):
				ponto["horario_saida"] = data
				msg += "Horário de entrada: {}]\n".format(ponto["horario_entrada"].strftime('%H:%M'))
				msg += "Horário de saida: {}\n".format(data.strftime('%H:%M'))
				msg += "Ponto batido! Bom descanso!\n"
				pontos_batidos.remove(ponto)
				await message.channel.send(msg)
				return
		
		ponto = {}
		ponto["id"] = message.author.id
		ponto["horario_entrada"] = data
		pontos_batidos.append(ponto)
		
		msg += "Horário de entrada: {}\n".format(data.strftime('%H:%M'))
		msg += "Ponto batido! Bom serviço campeão!\n"
		await message.channel.send(msg)
		return
	
	if 'tamujunto' or 'tmj' or 'tamo junto' or 'tamojunto' in message.content:
		msg = ":tamujunto:"
		await message.channel.send(msg)
		return
		
	if message.content.startswith('!nakaminha'):
		msg = random.choice(greets).format(message.author.mention)
		await message.channel.send(msg)
		return

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
