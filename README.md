# API Flask com MongoDB

Esse projeto foi feito como parte do meu aprendizado de **Flask** e integração com **MongoDB**. A ideia é criar uma **API simples** para estudar como manipular dados no MongoDB com o Flask.

### Funcionalidades

- **POST `/input`**: Envia dados para o banco de dados (usuário e e-mail).
- **GET `/`**: Retorna os dados que foram armazenados no banco.

### Como rodar o projeto

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório**:
   Primeiro, você precisa clonar o repositório para o seu computador. Abra o terminal e digite:
   ```bash
   git clone https://github.com/mauricioluanss/Flask_mongoDb.git
2. **Instale as dependências**: Acesse a pasta do projeto clonado e instale as dependências necessárias.
 
3. **Crie um arquivo .env**: O projeto utiliza o MongoDB, então você precisa adicionar a sua URI de conexão ao MongoDB no arquivo .env. Crie um arquivo .env na raiz do projeto e adicione a variável mongo_uri com a sua URI de conexão. Exemplo:
   ```bash
   mongo_uri='sua-uri-do-mongodb'
   
4. **Rode o código.**
   
5. **Testando a API**: Com o servidor rodando, você pode testar as rotas usando ferramentas como Postman ou curl.
	Para enviar dados (usuário e e-mail) para o banco de dados, use o método POST com um corpo JSON. Para consultar os dados armazenados, use o método GET. Exemplo: Exemplo:
	 ```bash
   curl -X POST http://localhost:5000/input -H "Content-Type: application/json" -d '{"usuario": "johndoe", "email": "johndoe@example.com"}'
  
 	 curl -X GET http://localhost:5000/


### Mais pra frente

Pretendo melhorar e adicionar mais funcionalidades a esse projeto, como:

- Implementação de autenticação (JWT ou OAuth).
- Validação de dados mais robusta.
- Adição de mais rotas para manipulação de dados.
- Talvez uma interface web para facilitar o uso da API.


	



