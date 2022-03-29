# Lupa do Windows (Windows Magnifier) #

* Autor: Cyrille Bougot
* Compatibilidade com NVDA: 2018.3 e além
* Baixe a [versão estável][1]
* Baixe a [versão em desenvolvimento][2]

Este complemento melhora o uso da Lupa do Windows com NVDA.


## Recursos

* Permite informar o resultado de alguns comandos de teclado nativo da Lupa.
* Permite reduzir os casos em que os comandos de navegação em tabelas entram
  em conflito com os comandos da Lupa.
* Adiciona alguns atalhos de teclado para alternar várias opções da Lupa.


## Configurações

O painel de configuração do complemento Lupa do Windows permite configurar como o NVDA reage aos comandos nativos da Lupa do Windows.
Você pode querer ter mais ou menos comandos informados de acordo com o que você consegue ver.
Este painel pode ser aberto escolhendo Preferências -> Configurações no menu NVDA e então selecionando a categoria Lupa do Windows na janela de Configurações.
O atalho de teclado NVDA+Windows+O depois O também permite abrir este painel de configurações diretamente.

O painel contém as seguintes opções:

* Relatar movimentos da visualização: controla o que é informado quando você
  move a visualização com os comandos Control+Alt+Setas. As três opções são:
  
    * Desativado: Nada é relatado.
    * Com voz: uma mensagem de voz indica a posição da visualização ampliada
      na dimensão em que a visualização está sendo movida.
    * Com tons: um tom é reproduzido e sua altura indica a posição da
      visualização ampliada na dimensão em que a visualização está sendo
      movida.
  
  Essa opção afeta apenas o modo de visualização cheia.
  
* Relatar ativação ou desativação: Se marcada, o estado da lupa é informado
  quando você usa os comandos Windows++ ou Windows+Esc para ativá-la ou
  desativá-la.
* Relatar ampliação: Se marcada, o nível de ampliação da Lupa é informado
  quando você usa os comandos de zoom Windows++ ou Windows+-.
* Relatar inversão de cores: Se marcada, o estado de inversão de cores é
  rinformado quando você usa o comando de alternância control+Alt+I.
* Relatar mudança da visualização: Se marcada, o tipo de visualização é
  informado quando você usa um comando que altera o tipo da visualização
  (Control+Alt+M, Control+Alt+F, Control+Alt+D, Control+Alt+L)
* Relatar redimensionamento de lente ou janela acoplada: Se marcada, uma
  mensagem é relatada quando você usa os comandos de redimensionamento
  (Alt+Shift+Setas). No modo de janela acoplada, a altura ou largura é
  informada. No modo de lente, a nova dimensão não pode ser informada por
  enquanto. Estes comandos de redimensionamento não parecem estar
  disponíveis em todas as versões do Windows; se a sua versão do Windows não
  os suportar, você deve manter esta opção desmarcada.
* Em documentos e visualizações de listas, passar atalhos control+alt+setas
  para a Lupa do Windows: Há três opções possíveis:
  
    * Nunca: O comando não é passado para a Lupa do Windows e a navegação
      padrão de tabela do NVDA pode operar. Quando usado em documentos fora
      de uma tabela, o comando Control+Alt+Seta relata uma mensagem de erro
      "Não está numa tabela". Esse é o comportamento padrão do NVDA sem este
      complemento.
    * Somente quando não estiver em tabela: Em tabela ou em visualizações de
      lista, os comandos Control+Alt+Seta executam a navegação padrão de
      tabela. Quando usados em documentos fora duma tabela, os comandos
      Control+Alt+Seta executam comandos padrões de movimento da
      visualização da Lupa. Se você ainda deseja mover a visualização da
      Lupa do Windows enquanto está na tabela ou na visualização de lista,
      você precisará pressionar NVDA+F2 antes de usar os comandos
      Control+Alt+Seta. Essa opção é o melhor meio-termo se você deseja usar
      Control+Alt+Seta para ampliação e navegação de tabela.
    * Sempre: Os comandos Control+Alt+Seta movem a visualização da Lupa em
      qualquer caso. Esta opção pode ser útil se você não usar
      Control+Alt+Seta para navegar em tabela, por exemplo, porque alterou
      os atalhos de navegação em tabelas no NVDA ou porque utiliza
      exclusivamente o complemento [Navegação fácil em tabelas (Easy table
      navigator)][5] para navegação nas tabelas.


## Comandos adicionados por este complemento

Além dos comandos nativos da Lupa, este complemento fornece comandos
adicionais que permitem controlar as opções da Lupa sem abrir sua página de
configuração. Todos os comandos adicionados para controlar as opções da Lupa
são acessíveis através do comando de camada Lupa NVDA+Windows+O:

* NVDA+Windows+O depois C: Ativa ou desativa o rastreamento do cursor.
* NVDA+Windows+O depois F: Ativa ou desativa o rastreamento do foco.
* NVDA+Windows+O depois M: Ativa ou desativa o rastreamento do mouse.
* NVDA+Windows+O depois T: Ativa ou desativa o rastreamento totalmente.
* NVDA+Windows+O depois S: Ativa ou desativa a suavização.
* NVDA+Windows+O depois R: Alterna entre os modos de rastreamento do mouse
  (no limite da tela ou centralizado na tela); esse recurso está disponível
  apenas no Windows 10 compilação 17643 ou superior.
* NVDA+Windows+O depois X: Alterna entre os modos de rastreamento do cursor
  de texto (no limite da tela ou centralizado na tela); esse recurso está
  disponível apenas no Windows 10 compilação 18894 ou superior.
* NVDA+Windows+O depois V: Coloca o cursor do mouse no centro da
  visualização ampliada (comando disponível apenas na visualização em tela
  cheia).
* NVDA+Windows+O depois O: Abre as configurações do complemento Lupa do
  Windows.
* NVDA+Windows+O depois H: Exibe a ajuda sobre os comandos de camada Lupa.

Não há comando (gesto) direto padrão para cada comando, mas você pode
atribuir um normalmente no diálogo definir comandos (gesto de entrada), se
desejar. Da mesma forma, você também pode modificar ou excluir o gesto de
acesso à camada Lupa (NVDA+Windows+O). Ainda assim, você não pode modificar
a tecla de atalho dos subcomandos da camada Lupa.


## Comandos nativos da Lupa

O resultado dos seguintes comandos nativos da Lupa pode ser relatado por
este complemento, de acordo com sua configuração:

* Iniciar Lupa: Windows++ (no teclado alfanumérico ou no teclado numérico)
* Sair da Lupa: Windows+Esc
* Ampliar: Windows++ (no teclado alfanumérico ou no teclado numérico)
* Diminuir ampliação: Windows+- (no teclado alfanumérico ou no teclado
  numérico)
* Alternar inversão de cores: Control+Alt+I
* Selecionar visualização acoplada: Control+Alt+D
* Selecionar visualização em tela cheia: Control+Alt+F
* Selecionar visualização de lente: Control+Alt+L
* Circuitar através dos três tipos de visualização: Control+Alt+M
* Redimensionar a lente com o teclado: Shift+Alt+seta para
  Esquerda/Direita/Cima/Baixo. Nota: embora isso não pareça estar
  documentado, este atalho parece ter sido retirado em versões recentes do
  Windows, como o Windows 2004.
* Mover a visualização ampliada: Control+Alt+Setas (a informação afeta
  apenas o modo de tela cheia)

Aqui está também uma lista de outros comandos nativos da Lupa, apenas para
informação:

* Control+Alt+rodinhaDeRolagemDoMouse: Aumenta e diminui a ampliação usando
  a rodinha de rolagem do mouse.
* Control+Windows+M: Abre a janela de configurações da Lupa.
* Control+Alt+R: Redimensiona a lente com o mouse.
* Control+Alt+Espaço: Mostra rapidamente toda a área de trabalho ao usar a
  visualização em tela cheia.

Nenhum dos comandos nativos da Lupa podem ser modificados.


## Notas

* Para computadores equipados com uma placa de vídeo Intel, control+alt+seta
  (esquerda/direita/cima/baixo) também são atalhos para modificar a
  orientação da tela. Esses atalhos são habilitados por padrão e entram em
  conflito com os atalhos da Lupa do Windows para mover a visualização. Você
  precisará desabilitá-los para poder usá-los na Lupa. Eles podem ser
  desabilitados no painel de controle Intel ou no menu Intel presente na
  bandeja do sistema (área de notificação).
* Dependendo da sua versão do Windows, Alt+Shift+Seta são atalhos da Lupa do
  Windows para redimensionar a visualização ampliada (lente ou
  acoplada). Quando a Lupa está ativa (mesmo no modo de tela cheia), esses
  atalhos são capturados pela Lupa e não podem ser passados para o
  aplicativo, mesmo se antes você pressionar NVDA+F2. Para usar esses
  atalhos no aplicativo atual, você precisa sair da Lupa (Windows+Esc) e
  reabri-la depois (Windows++). Por exemplo, no Ms Word, para diminuir o
  nível do título:
  
    * Pressione Windows+Esc para sair da Lupa.
    * Pressione Alt+Shift+SetaParaDireita para diminuir o nível do título
      atual.
    * Pressione Windows++ para reabrir a Lupa.

* Para mais informações sobre os recursos e atalhos da Lupa do Windows, pode
  consultar as seguintes páginas:

    * [Usar a Lupa para facilitar a visualização dos itens na
      tela](https://support.microsoft.com/pt-br/windows/usar-a-lupa-para-facilitar-a-visualiza%C3%A7%C3%A3o-dos-itens-na-tela-414948ba-8b1c-d3bd-8615-0e5e32204198)
    * [Atalhos de teclado de acessibilidade do Windows][4]


## Registro de alterações (Change log)

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=winmag

[2]: https://addons.nvda-project.org/files/get.php?file=winmag-dev

[4]: https://support.microsoft.com/pt-br/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.pt_BR.html
