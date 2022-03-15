
const puppeteer = require('puppeteer');// inclui a biblioteca puppeteer
 
const express = require('express'); // inclui a biblioteca express
const app = express(); //inicia o express
const port = 3000;// porta do serviço


//busca os parametros do post com json
var bodyParser = require('body-parser')
app.use(bodyParser.json());

//mostra o tempo da aplicação no console
app.use(function (req, res, next) {
  console.log('Time:', Date.now());
  next();
});


//retorna um Hello Word! pra quem acessar base
app.get('/', (req, res) => {
  var resulte = {'Server':'Hello Word!'};
  var atte = {content: resulte};
    ste =  JSON.stringify(atte);
  res.end(ste);
})


//metodo post para consultar usuarios, recebe como parametro um json, com o user e senha do adm, e usuario que está buscando
app.post('/callback_user_smarters', function(req, res) {
  
  console.time('tempo');

  var content = req.body; // tranfere os parametros que recebeu para uma variavel interna
  if(content.user.length == 10){//verifica se o usuario está nos parametros

    (async () => {
  
      const browser = await puppeteer.launch({//inicia o navegador
        headless: false, // diz se vai habilitar ou não a visualização da janela
      });
      
    const page = await browser.newPage();//inicia a pagina navegador
    
    await page.setViewport({//defini o tamanho da pagina quando exibida
      width: 1080,
      height:1080
    });
    
    await page.goto('https://smarters.app/login'); //acessa a pagina de login
    
    
    // Insere o login e a senha nos campos do form na pagina 
    await page.type('[name="login"]', content.admin);
    await page.type('[name="password"]', content.password);
    // Submete o login e senha para validação, clicando no botão
    await page.click('[type="submit"]');

    //Espera a proxima pagina apos o login ser carregada, para ter certaza do login
    await page.waitForNavigation();
    
    // ACESSAR essa pagina com a grid de usuarios
    await page.goto('https://smarters.app/admin/gerenciar-linhas-testes');
    //Insere o nome de usuario no campo de busca
    await page.type('[type="search"]',content.user);
    //espear um tempo pro js da table atualizar
    await page.waitForTimeout(2000);
  
  //cria um array com a 1ª linha da tabela
  const WinArray = await page.evaluate(
    () => [...document.querySelectorAll(
      'table > tbody > tr')]
        .map(elem => elem.innerText)
  );
  
  //array com o titulo das informações que vão ser retornadas
  const textsArray = [
    "#",
    "user",
    "senha",
    "acesso",
    "Criacao",
    "Vencimento",
    "status",
  ];
  
  //estancia um objeto vazio
  var result = {};
  //Tranforma o array de retorno em string, separando cadas dado por '\t'  e colocando em campo do novo array
  var strin  = WinArray.toString().split('\t');
  
  if(strin != null){//verifica se houver array de retorno ou se está vazio
      textsArray.forEach((textsArray, i) =>
      result[textsArray] = strin[i]);//se tiver dados
      //vai adcionar campos ao objeto RESULT usando o titulo do array TEXTSARRAY e o dado do array STRIN
  }

    await browser.close();// feixa o navegador
  
    var att = {content: result};// cria um objeto com o array de resultado
      st =  JSON.stringify(att); //tranforma esse objeto em string
      
      res.end(st);// retorna string

      console.timeEnd('tempo');
  
    })();
  }else{
   
    // se o nome de usuario não atender os parametros
    //retorna um ERRO
    var resulte = {'#':'Erro : 300'};
    var atte = {content: resulte};
      ste =  JSON.stringify(atte);
    res.end(ste);
  
  }

});

























app.post('/callback_user_add_smarters', function (req, res, next) {
  
  console.time('tempo');
  
  var content = req.body;

  if(content.user.length == 10){

  (async () => {

    const browser = await puppeteer.launch({
      headless: false,
    });
    
  const page = await browser.newPage();
  
  await page.setViewport({
    width: 1080,
    height:1080
  });
  
  await page.goto('https://smarters.app/login');
  
  //await page.waitForNavigation();
  
  // Troque os valores de process.env.UNSPLASH_EMAIL e process.env.UNSPLASH_PASS pelo seu login e senha :)
 await page.type('[name="login"]', content.admin);
 await page.type('[name="password"]', content.password);
  
  await page.click('[type="submit"]');
  
  await page.waitForNavigation();
    
  // ACESSAR essa pagina com a grid de usuarios
  await page.goto('https://smarters.app/admin/gerenciar-linhas-testes');
  //Insere o nome de usuario no campo de busca
  await page.type('[type="search"]',content.user);
  //espear um tempo pro js da table atualizar
  await page.waitForTimeout(2000);

//cria um array com a 1ª linha da tabela
const WinArray = await page.evaluate(
  () => [...document.querySelectorAll(
    'table > tbody > tr')]
      .map(elem => elem.innerText)
);

  if (WinArray[0] == "Nenhum registro encontrado"){

    page.on('dialog', async dialog =>{

    console.log(dialog.message());

    if(dialog.message() == 'Teste criado com sucesso!'){
      await dialog.accept();
    }else{
      await dialog.accept();

      var resulte = {'#':'Erro : 500'};

      var atte = {content: resulte};

        st2 =  JSON.stringify(atte);

      res.end(st2); 
    }
  
  })

    
  await page.goto(' https://smarters.app/admin/linha-ativa-teste');
  
  await page.type('[name="user"]', content.user);

  if(content.p1 == 1){
      await page.click('#customControlValidation95');
  }
  
  await page.type('[name="wpp"]', content.wpp);
  
  await page.click('[type="submit"]');
  

  // ACESSAR essa pagina
  await page.goto('https://smarters.app/admin/gerenciar-linhas-testes');
  //await page.waitForNavigation();
  await page.type('[type="search"]', content.user);

await page.waitForTimeout(2000);


const WinArray = await page.evaluate(
  () => [...document.querySelectorAll(
    'table > tbody > tr')]
      .map(elem => elem.innerText)
);

const textsArray = [
  "#",
  "user",
  "senha",
  "acesso",
  "Criacao",
  "Vencimento",
  "status",
];


var result = {};

//console.log(WinArray);

    var strin  = WinArray.toString().split('\t');

    //console.log(strin);
if(strin != null){
    textsArray.forEach((textsArray, i) =>
    result[textsArray] = strin[i]);
}
//console.log(result);


  var att = {content: result};
    st =  JSON.stringify(att);
    
    
    res.end(st);

}else{

  var resulte = {'#':'Erro : 500'};

  var atte = {content: resulte};

    st2 =  JSON.stringify(atte);

  res.end(st2);
}

await browser.close();
console.timeEnd('tempo');

})();

}else{

  var resulte = {'#':'Erro : 300'};  
  var atte = {content: resulte};
    ste =  JSON.stringify(atte);
  res.end(ste);

}
});





















app.listen(port, () => {
  //console.log(`Server running at http://localhost:${port}/`);
});

