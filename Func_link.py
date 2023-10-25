# Exemplo da resposta da nossa API
frase = "O Galaxy A14 5G é o melhor celular pra você."

def verificar_palavras_chave(frase):
    palavras_chave = {
        'Galaxy A03': 'https://shop.samsung.com.br/galaxy-a03-core-32gb/p',
        'Galaxy A04e': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a04e-black-64gb-sm-a042mzkhzto/',
        'Galaxy A04s': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a04s-green-64gb-sm-a047mzggzto/',
        'Galaxy A14': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a14-5g-black-128gb-sm-a146mzkgzto/?utm_campaign=br_pd_ppc_googleads%3Asearch_a14_launch_cadastra-cadastra%3Acad15-a1709-especifica_text_na%3Asearch%3Acpc%3Akvl%3Aa14%3Alaunch%3Ana%3Astatic%3Ana_warm%3Alead%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana_152368439648*samsung%20a14*e_&utm_medium=ppc&utm_source=googleads%3Asearch&keeplink=true&cid=br_pd_ppc_googleads%3Asearch_a14_launch_cadastra-cadastra%3Acad15-a1709-especifica_text_na%3Asearch%3Acpc%3Akvl%3Aa14%3Alaunch%3Ana%3Astatic%3Ana_warm%3Alead%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana%3Ana_152368439648*samsung%20a14*e&gad=1&gclid=CjwKCAjw-eKpBhAbEiwAqFL0mgHIs1TRj8hepxu4dp91qIWPfnQSiVyZCGSKmaurMPEAEU8DxNXDGBoCI8IQAvD_BwE',
        'Galaxy A14 5G': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a14-5g-black-128gb-sm-a146mzkgzto/',
        'Galaxy A24': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a24-black-128gb-sm-a245mzkuzto/',
        'Galaxy A34': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a34-5g-lime-128gb-sm-a346mlgazto/',
        'Galaxy A54': 'https://www.samsung.com/br/smartphones/galaxy-a/galaxy-a54-5g-green-256gb-sm-a546elgdzto/',
    }

    for palavra_chave, link in palavras_chave.items():
        if palavra_chave in frase:
            return f"Para mais informações, acesse o link: {link}"

    return "Nenhuma palavra-chave encontrada."

resposta = verificar_palavras_chave(frase)
print(resposta)
