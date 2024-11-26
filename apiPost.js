//requisição facilitada para HTTP
const axios = require('axios')

//URL da APi
const url = "https://jsonplaceholder.typicode.com/posts";

//Dados que queremos enviar para API (Um novo post, por exemplo)
const novoPost = {
    title: "Charizard gripado",
    body: "Este é um exemplo de como fazer POST com axios",
    userId: 1
}

//Fazendo uma requisição POST para criar um novo recurso nas API
axios.post(url, novoPost)
    .then(response => {
        //Se a requisição foi bem sucedida, a resposta será aqui
        console.log("Recurso criado com sucesso: ")
        console.log(response.data)
    })
    .catch(error => {
        //Se ocorrer um erro, será capturado aqui
        console.error(`Erro ao tentar criar o recurso: ${error}`)
    })

