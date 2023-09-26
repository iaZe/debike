import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Permitir apenas conexões autenticadas
        if self.scope['user'].is_anonymous:
            await self.close()
        else:
            await self.accept()

    async def disconnect(self, close_code):
        # Lógica de desconexão (se necessário)
        pass

    async def receive(self, text_data):
        # Recebe e processa mensagens do cliente
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Salvar a mensagem no banco de dados ou fazer o que for necessário

        # Envia a mensagem de volta ao cliente
        await self.send(text_data=json.dumps({
            'message': message
        }))
