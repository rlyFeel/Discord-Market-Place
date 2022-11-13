import nextcord
from nextcord.ext import commands
from cfg.cfg import *


class TicketMarket(nextcord.ui.View):
    def __init__(self, ):
        super().__init__(
            timeout=None
        )

    @nextcord.ui.button(
        label='Закрыть тикет', style=nextcord.ButtonStyle.red, emoji='📕'
    )
    async def close_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Тикет скоро закроется...", ephemeral=True)
        await interaction.channel.delete()

    @nextcord.ui.button(
        label='Позвать администрацию', style=nextcord.ButtonStyle.blurple, emoji='💡'
    )
    async def sing_to_help(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        emb = nextcord.Embed(description=f"🔔 {interaction.user.mention} позвал на помощь.",color=nextcord.Color.red())
        await interaction.channel.send(f'<@&{id_staff_role}>', embed=emb)


class Arbitration(nextcord.ui.View):
    def __init__(self, dealer, dealer2):
        self.dealer = dealer
        self.dealer2 = dealer2
        super().__init__()

    @nextcord.ui.button(
        label='Написать продавцу!'
    )
    async def create_ticket_market(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message("a ticket be create", ephemeral=True)
        channel = await interaction.guild.create_text_channel(f'💱 {self.dealer2} и {interaction.user.name}',
                                                              category=nextcord.utils.get(
                                                                  interaction.guild.categories,
                                                                  id=))
        await channel.set_permissions(interaction.user,
                                      send_messages=True,
                                      read_message_history=True,
                                      read_messages=True)
        await channel.set_permissions(interaction.guild.get_member(self.dealer),
                                      send_messages=True,
                                      read_message_history=True,
                                      read_messages=True)
        await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                                      send_messages=False,
                                      read_messages=False)

        await msg.edit(f"Тикет был создан! {channel.mention}")
        emb = nextcord.Embed(title='!',
                             description=f'**Открыл**  - {interaction.user} \n\n'
                                         f'```Тут можете разговаривать,общаться,что-либо обговарить```\n'
                                         f'```В случае затрудней или помощи ввиде "гаранта" - нажмите на кнопку``` \n **"Позвать администрацию"** ',
                             color=nextcord.Color.gold())
        await channel.send(embed=emb, view=TicketMarket())


class market_ticket(nextcord.ui.Modal):
    def __init__(self, bot):
        super().__init__(
            'Открыть свою лавку!',
            timeout=10,
            )

        self.bot = bot

        self.emTitle = nextcord.ui.TextInput(
            label="Сервер",
            min_length=4,
            max_length=15,
            placeholder='Сервер'
        )
        self.add_item(self.emTitle)

        self.emDesc = nextcord.ui.TextInput(
            label="Категория Ресурсы/Аккаунты",
            min_length=4,
            max_length=15,
            placeholder='Категория'
        )
        self.add_item(self.emDesc)

        self.emDesc2 = nextcord.ui.TextInput(
            label="Наименование товара и колличество",
            min_length=4,
            max_length=50,
            placeholder='Название'
        )
        self.add_item(self.emDesc2)

        self.emDesc3 = nextcord.ui.TextInput(
            label="Цена",
            min_length=4,
            max_length=50,
            placeholder='Цена'
        )
        self.add_item(self.emDesc3)

    async def callback(self, interaction: nextcord.Interaction):
        channel = self.bot.get_channel()
        await interaction.response.send_message('Заявка создана!', ephemeral=True)
        emb = nextcord.Embed(title='Новая лавка!',
                             description=f'Лавку открыл - {interaction.user}\n\n'
                                         f'**Сервер - **{self.emTitle.value}\n'
                                         f'**Категория - **{self.emDesc.value}\n'
                                         f'**Наименование - **{self.emDesc2.value}\n'
                                         f'**Цена - **{self.emDesc3.value}\n\n'
                                         f'Id сделки = {interaction.user.id}',
                             color=nextcord.Color.gold())
        emb.set_thumbnail(url=interaction.user.avatar)
        dealer = interaction.user.id
        dealer2 = interaction.user.name
        view=Arbitration(dealer,dealer2)
        await channel.send('@here', embed=emb, view=view)


class CreateMarket(nextcord.ui.View):
    def __init__(self,bot):
        self.bot = bot
        super().__init__()

    @nextcord.ui.button(
        label='Открыть лавку!', emoji='💼'
    )
    async def market(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(market_ticket(self.bot))


class Market(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Cogs is loaded - Market')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def market_place(self, interaction):
        emb = nextcord.Embed(title='Маркет!', description='Хотите начать продажи?', color=nextcord.Color.teal())
        emb.set_image(url='')
        view=CreateMarket(self.bot)
        await interaction.send(embed=emb, view=view)





async def setup(bot):
    bot.add_cog(Market(bot))