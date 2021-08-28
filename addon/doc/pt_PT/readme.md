# Lupa do Windows #

* Autor: Cyrille Bougot
* Compatibilidade com o NVDA: 2018.3 e seguintes
* Descarregar a [Versão estável][1]
* Baixar [Versão de desenvolvimento][2]

Este extra melhora a utilização da Lupa do Windows com NVDA.


## Funcionalidades

* Permite anunciar o resultado de alguns comandos de teclado nativos da
  Lupa.
* Permite reduzir os casos em que os comandos de navegação em tabelas entram
  em conflito com os comandos da Lupa...
* Adiciona alguns atalhos de teclado para alternar várias opções da Lupa.


## Configurações

O painel de configurações do extra Lupa do windows permite configurar a forma como o NVDA reage aos comandos nativos da lupa.
Poderá querer que sejam anunciados mais ou menos comandos de acordo com o que vê.
Este painel pode ser aberto através do menu do NVDA, Preferências, Configurações, e depois seleccionando a categoria Lupa, na janela De configurações.
O comando NVDA+Windows+O e depois O também permite abrir directamente este painel de configurações.

O painel contém as seguintes opções:

* Anúncio de movimentos da vista: controla o que é anunciado quando se move
  a vista com os comandos Control+Alt+Setas. As três opções são:
  
    * Desligado: Nada é anunciado.
    * Com voz: uma mensagem anuncia a posição relativa à direcção em que a
      vista ampliada está a ser movida.
    * Com bips: São reproduzidos bips e o seu tom indica a posição relativa
      à direcção em que a vista ampliada está a ser movida.
  
  Esta opção apenas afecta a vista de ecrã inteiro.
  
* Anunciar ligar ou desligar: Se marcado, o estado da Lupa é anunciado
  quando se usa os comandos Windows++ ou Windows+Escape para ligar ou
  desligar a Lupa.
* Anunciar ampliação: Se marcado, o nível de ampliação da lupa é anunciado
  quando se usam os comandos Windows++ ou Windows+-.
* Anunciar inversão de cores: Se marcado, o estado de inversão de cores é
  anunciado quando se usa o comando control+Alt+I.
* Anunciar mudanças de vista: Se marcado, o tipo de vista é anunciado quando
  se utiliza um comando que altera o tipo de vista (Control+Alt+M,
  Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Anunciar o redimensionamento da lente ou da vista ancorada: Se marcado, é
  anunciado quando se utilizam os comandos de redimensionamento
  (Alt+Shift+setas). No modo de vista ancorada, a altura ou a largura é
  anunciada.  Na vista Lente, a nova dimensão não pode ser anunciada por
  agora.  Estes comandos de redimensionamento não parecem estar disponíveis
  em todas as versões do Windows; se a sua versão do Windows não os
  suportar, deve manter esta opção desmarcada.
* Em documentos e listas, passar os comandos controlo+alt+setas para a
  lupa. Existem três opções:
  
    * Nunca: O comando não é passado para a Lupa e a navegação padrão em
      tabelas do NVDA funciona.  Quando utilizado em documentos fora de uma
      tabela, o comando Control+Alt+setas anuncia uma mensagem de erro "Não
      numa tabela". Este é o comportamento padrão do NVDA sem este extra.
    * Apenas quando não está numa tabela: Em tabelas ou listas, os comandos
      Control+Alt+setas executam a navegação de tabela padrão.  Quando usado
      em documentos fora de uma tabela, os comandos Control+Alt+setas
      executam os comandos padrão de movimentação da Lupa.  Se quiser mover
      a vista da Lupa enquanto estiver em tabelas ou listas, terá de
      pressionar NVDA+F2 antes de usar os comandos Control+Alt+setas.  Esta
      opção é o melhor compromisso se quiser usar Control+Alt+setas tanto
      para a lupa como para a navegação em tabelas.
    * Sempre: Os comandos Control+Alt+setas movem a vista da Lupa em
      qualquer caso.  Esta opção pode ser útil se não usar Control+Alt+setas
      para navegar em tabelas, por exemplo, porque mudou os atalhos de
      navegação em tabela do NVDA ou porque usa exclusivamente o extra
      [Navigação fácil em tabelas][5] para navegação em tabelas.


## Comandos adicionados por este extra:

Para além dos comandos nativos da Lupa, este complemento fornece comandos
adicionais que permitem controlar as opções da Lupa sem abrir a sua página
de configuração. Todos os comandos adicionados às opções de controlo da lupa
são acessíveis através dos comandos em camada da Lupa (NVDA+Windows+O):

* NVDA+Windows+O e depois C: Liga ou desliga o seguimento do cursor de
  texto.
* NVDA+Windows+O e depois F: Liga ou desliga o seguimento do foco de teclado
* NVDA+Windows+O depois M: Liga ou desliga o seguimento do rato.
* NVDA+Windows+O e depois T: Liga ou desliga o seguimento a nível global.
* NVDA+Windows+O depois S: Liga ou desliga a suavização.
* NVDA+Windows+O e depois R: Alterna entre modos de seguimento do rato
  (dentro das extremidades do ecrã ou centrado no ecrã); esta característica
  só está disponível no Windows 10 build 17643 ou superior.
* NVDA+Windows+O e depois R: Alterna entre modos de seguimento do rato
  (dentro das extremidades do ecrã ou centrado no ecrã); esta característica
  só está disponível em Windows 10 build 17643 ou superiores.
* NVDA+Windows+O depois V: Move o cursor do rato no centro da vista ampliada
  (comando disponível apenas na vista de ecrã inteiro).
* NVDA+Windows+O depois O: Abre a janela de configurações da Lupa.
* NVDA+Windows+O depois H: Mostra a ajuda dos comandos em camada da lupa.

Não há nenhum comando padrão para os vários comandos, mas pode atribui-los,
normalmente, no diálogo definir comandos, se o desejar. Da mesma forma,
também é possível modificar ou apagar o comando para iniciar os comandos em
camada da Lupa (NVDA+Windows+O). No entanto, não pode modificar a tecla de
atalho dos sub-comandos da camada da Lupa.


## Comandos nativos da Lupa do Windows

O resultado dos seguintes comandos nativos da Lupa pode ser anunciado por
este extra, dependendo das suas configurações:

* Início da Lupa: Windows++ (no teclado alfanumérico ou no numérico)
* Sair da lupa: Windows+Escape
* Aumentar a ampliação: Windows++ (no teclado alfanumérico ou no numérico)
* Diminuir a ampliação: Windows+- (no teclado alfanumérico ou no numérico)
* Alternar a inversão de cores: Controlo+Alt+I
* Seleccionar a vista ancorada: Controlo+Alt+D
* Seleccionar a visualização em ecrã inteiro: Controlo+Alt+F
* Seleccionar a vista Lente: Controlo+Alt+L
* Alterna entre os três tipos de vista: Controlo+Alt+M
* Redimensionar a lente com o teclado: Shift+Alt+seta à
  Esquerda/Direita/Acima/Abaixo.  Nota: embora não pareça estar documentado,
  este comando parece ter sido retirado em versões recentes do Windows, tais
  como Windows 10 2004.
* Mover a vista ampliada: Control+Alt+setas (o anúncio apenas funciona em
  vista de ecrã inteiro)

Eis uma lista de outros comandos nativos da Lupa, apenas para informação:

* Control+Alt+RodaDoRato: Aumenta e diminui a ampliação usando a roda de
  rolagem do rato.
* Control+Windows+M: Abre a janela de configurações da Lupa.
* Control+Alt+R: Redimensiona a lente com o rato.
* Control+Alt+espaço: Mostra rapidamente todo o ambiente de trabalho quando
  se utiliza a vista de ecrã inteiro.

Nenhum dos comandos nativos da Lupa pode ser modificado.


## Notas

* Para computadores equipados com uma placa gráfica Intel, control+alt+seta
  (esquerda/direita/cima/baixo) são comandos para modificar a orientação do
  ecrã. Estes comandos são activados por defeito e entram em conflito com os
  comandos da Lupa, para mover a vista. Terá de os desactivar para poder
  utilizá-los para o aumento pela Lupa. Podem ser desactivados no painel de
  controlo Intel ou no menu Intel presente no tabuleiro do sistema.
* Dependendo da sua versão do Windows, Alt+Shift+setas são comandos da Lupa
  do Windows para redimensionar a vista ampliada (lente ou ancorada). Quando
  a Lupa está activa (mesmo em modo ecrã inteiro), estes comandos são
  capturados pela lupa e não podem ser passados para a aplicação, mesmo que
  se prima NVDA+F2 antes. Para utilizar estes comandos na aplicação actual,
  é necessário abandonar a Lupa (Windows+Escape) e reabri-la depois
  (Windows++). Por exemplo, no MS Word, para diminuir o nível de título:
  
    * Pressione Windows+Escape para sair da lupa.
    * Pressione Alt+Shift+RightArrow para diminuir o nível de título actual.
    * Pressione Windows++ para reabrir a lupa.

* Para mais informações sobre as funcionalidades e atalhos da lupa, poderá
  consultar as seguintes páginas:

    * [Use a Lupa para tornar as coisas mais fáceis de ver no
      ecrã](https://support.microsoft.com/pt-pt/help/11542/windows-use-magnifier-to-make-things-easier-to-see)
    * Atalhos de teclado do Windows para acessibilidade[4]


## Registro de Alterações

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/pt-pt/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.en.html
