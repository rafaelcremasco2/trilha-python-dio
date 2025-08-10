## Como Criar um Copiloto com Fluxo de Conversa Personalizado no Microsoft Copilot Studio

### 1. Criar um Copilot em Branco
- Acesse o [Microsoft Copilot Studio](https://copilotstudio.microsoft.com/).
- Clique em **Criar Copilot** e selecione a opção **Em branco**.
- Defina o nome e as configurações iniciais do seu copilot.

### 2. Customizar um Tópico
- No menu lateral, vá em **Tópicos** e clique em **Novo tópico**.
- Dê um nome ao tópico e adicione frases de gatilho (ex: "Quais são os benefícios do Azure?").
- No editor de fluxo, insira perguntas, respostas e ações conforme necessário.

### 3. Personalizar Mensagem de Erro de Tópico
- No fluxo do tópico, adicione um bloco de mensagem para erros.
- Configure o texto para orientar o usuário em caso de dúvidas ou respostas inesperadas (ex: "Desculpe, não entendi. Pode reformular sua pergunta?").

### 4. Ajustar Qualidade das Respostas com GenIA
- Ative o recurso de **Respostas Geradas por IA** no tópico.
- Para aumentar a qualidade, forneça contexto detalhado e exemplos baseados na documentação da Microsoft.
- Para diminuir a qualidade, limite o contexto ou reduza exemplos, tornando as respostas mais genéricas.

> **Exemplo:**  
> Tópico: "Como usar o Microsoft Teams?"  
> - Frase de gatilho: "Como faço para criar uma reunião no Teams?"  
> - Resposta GenIA: "Para criar uma reunião, acesse o calendário do Teams e clique em 'Nova reunião'. Siga as instruções na tela."  
> - Mensagem de erro: "Não consegui encontrar informações sobre isso. Tente perguntar de outra forma."

### Referência
- [Documentação oficial Microsoft Copilot Studio](https://learn.microsoft.com/pt-br/copilot-studio/)
