import openai

# Substitua 'sua_chave_de_api' pela sua chave de API da OpenAI
openai.api_key = 'sua_chave_de_api'

def conversa_com_chatbot(mensagem):
    resposta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=mensagem,
        max_tokens=2000  # Ajuste o número de tokens de saída desejado
    )
    return resposta.choices[0].text

print("Bem-vindo ao Chatbot! Você pode começar a conversar digitando mensagens. Digite 'sair' para encerrar.")

'''while True:
    usuario_input = input("Você: ")
    
    if usuario_input.lower() == 'sair':
        print("Chatbot: Até logo!")
        break
    
    resposta_chatbot = conversa_com_chatbot(usuario_input)
    print("Chatbot:", resposta_chatbot)'''