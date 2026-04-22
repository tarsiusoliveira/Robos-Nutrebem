from playwright.sync_api import sync_playwright
import pandas as pd
import time

def limpar_restricoes_escola_199():
    # 1. Carrega o CSV e filtra apenas a escola 199
    print("Carregando base de dados...")
    df = pd.read_csv("dados_robo_teste.csv")
    df_escola = df[df['school_id'] == 199]
    
    total_tarefas = len(df_escola)
    print(f"Total de restrições para limpar na Escola 199: {total_tarefas}")

    with sync_playwright() as p:
        # Abre o navegador visível para você acompanhar (headless=False)
        browser = p.chromium.launch(headless=False)
        
        # Cria um contexto que simula um navegador normal para evitar bloqueios
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        # 2. Fazer Login no Sistema
        print("Iniciando processo de Login...")
        page.goto("https://app.nutrebem.com.br/pt-BR/login") # Ajuste a URL de login se necessário
        
        # ATENÇÃO: Preencha com suas credenciais reais aqui
        page.fill("input[type='text']", "tarsius+admin@easyfood.com.br")
        page.fill("input[type='password']", "92629262Ts")
        page.click("input[type='submit'], button:has-text('Entrar')") # Clica no botão de entrar
        
        time.sleep(3)

        # Aguarda a página inicial carregar após o login
        page.wait_for_load_state('networkidle')
        print("Login realizado com sucesso! Iniciando as correções...")

        # 3. Iterar sobre os produtos da escola 199
        sucessos = 0
        erros = 0
        
        for index, row in df_escola.iterrows():
            produto_id = row['product_id']
            serie_errada = str(row['serie_errada']).strip() # Garante que não tem espaços extras
            
            print(f"[{sucessos + erros + 1}/{total_tarefas}] Produto {produto_id} | Removendo: '{serie_errada}'...")
            
            # Navega direto para a página de edição da restrição
            url_edicao = f"https://app.nutrebem.com.br/pt-BR/canteen_operator/product_restrictions/{produto_id}/edit"
            
            try:
                page.goto(url_edicao)
                page.wait_for_load_state('load') # Garante que a página carregou
                
                # Procura a checkbox que está associada ao texto da série e DESMARCA
                # A estratégia é procurar a 'label' que contém o texto da série e desmarcar
                # seletor_checkbox = f"label:has-text('{serie_errada}')"
                
                # Verifica se a caixinha realmente existe na tela antes de tentar desmarcar
                # page.uncheck(seletor_checkbox)
                    
                # Clica no botão de Salvar (baseado no form que você pescou na aba Network)
                page.click("input[name='commit'][value='Salvar restrições']")
                
                # Aguarda salvar e a página redirecionar
                page.wait_for_load_state('networkidle')
                print(f" -> Sucesso!")
                sucessos += 1
                
                    
            except Exception as e:
                print(f" -> ERRO ao processar produto {produto_id}: {e}")
                erros += 1
                
            # Pausa de 1 segundo entre as requisições para não sobrecarregar o servidor
            time.sleep(1)

        print("\n" + "="*40)
        print("PROCESSO FINALIZADO!")
        print(f"Sucessos: {sucessos} | Erros/Não encontrados: {erros}")
        print("="*40)

        browser.close()

if __name__ == "__main__":
    limpar_restricoes_escola_199()