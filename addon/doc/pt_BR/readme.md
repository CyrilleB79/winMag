# Lupa do Windows (Windows Magnifier) #

* Autor: Cyrille Bougot
* Compatibilidade com NVDA: 2019.2.1 e posterior
* Baixe a [versão estável][1]

Este complemento melhora o uso da Lupa do Windows com NVDA.


## Recursos

* Permite informar o resultado de alguns comandos de teclado nativo da Lupa.
* Permite reduzir os casos em que os comandos de navegação em tabelas entram
  em conflito com os comandos da Lupa.
* Adiciona alguns atalhos de teclado para alternar várias opções nativas da
  Lupa.
* Permite salvar e restaurar os parâmetros de configuração da Lupa.
* Adiciona alguns recursos extras que não são fornecidos pela Lupa do
  Windows (mouse para visualizar, janela da Lupa não na parte superior)

## Configurações

O painel de configuração do complemento Windows Magnifier permite configurar
como o NVDA reage aos comandos nativos do Windows Magnifier.  Você pode
desejar que mais ou menos comandos sejam relatados de acordo com o que você
consegue ver.  O painel também contém uma opção para modificar o
comportamento da janela de controle da Windows Magnifier.

Esse painel pode ser aberto escolhendo Preferências -> Configurações no menu NVDA e, em seguida, selecionando a categoria Windows Magnifier na janela Configurações.
O atalho de teclado NVDA+Windows+O e depois O também permite abrir esse painel de configurações diretamente.

O painel contém as seguintes opções:

* Relatar movimentos da visualização: controla o que é informado quando você
  move a visualização com os comandos Control+Alt+Setas. As três opções são:
  
    * Desativado: Nada é relatado.
    * Com voz: uma mensagem de voz indica a posição da visualização ampliada
      na dimensão em que a visualização está sendo movida.
    * Com tons: um tom é reproduzido e sua altura indica a posição da
      visualização ampliada na dimensão em que a visualização está sendo
      movida.
  
  Essa opção não afeta o modo de exibição encaixado.

* Relatar bordas da tela: controla o que é relatado quando você alcança as
  bordas da tela ao mover a exibição com os comandos Control+Alt+Setas.  As
  três opções são: Desligado, Com fala e Com tons.  Essa opção não afeta o
  modo de exibição encaixado.
* Volume dos tons que informam a posição da visualização: permite definir o
  volume dos tons se você tiver selecionado informar os movimentos da
  visualização ou as bordas da tela com tons.
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
  
    * Nunca: O comando não é passado para o Windows Magnifier e a navegação
      padrão na tabela do NVDA pode funcionar.  Quando usado em documentos
      fora de uma tabela, o comando Control+Alt+Seta informa uma mensagem de
      erro “Não está em uma tabela”.  Esse é o comportamento padrão do NVDA
      sem esse complemento.  Você ainda pode usar NVDA+Windows+O e depois as
      setas para mover a exibição ampliada.
    * Somente quando não estiver em uma tabela: Em exibições de tabela ou de
      lista, os comandos Control+Alt+Seta executam a navegação padrão na
      tabela.  Quando usados em documentos fora de uma tabela, os comandos
      Control+Alt+Seta executam comandos padrão de movimentação da
      visualização da Lupa.  Se ainda quiser mover o modo de exibição da
      Lupa do Windows enquanto estiver na tabela ou no modo de exibição de
      lista, será necessário pressionar NVDA+F2 antes de usar os comandos
      Control+Alt+Seta ou, alternativamente, usar NVDA+Windows+O e, em
      seguida, as setas.  Essa opção é o melhor compromisso se você quiser
      usar Control+Alt+Seta para a navegação na lupa e na tabela.
    * Sempre: Os comandos Control+Alt+Seta movem a visualização da Lupa em
      qualquer caso. Esta opção pode ser útil se você não usar
      Control+Alt+Seta para navegar em tabela, por exemplo, porque alterou
      os atalhos de navegação em tabelas no NVDA ou porque utiliza
      exclusivamente o complemento [Navegação fácil em tabelas ][5] para
      navegação nas tabelas.

* Manter a janela de comando da Lupa do Windows sempre na parte superior: Se
  desmarcada, a janela de controle da Lupa não será mantida sempre em cima
  de outras janelas.

## Comandos adicionados por este complemento

Além dos comandos nativos da Lupa, esse complemento fornece comandos
adicionais:

* Comandos que permitem controlar as opções da Lupa sem abrir sua página de
  configuração.
* Comandos extras específicos para esse complemento.

Todos esses comandos adicionais podem ser acessados por meio do comando de
camada da lupa NVDA+Windows+O:

* NVDA+Windows+O depois C: Ativa ou desativa o rastreamento do cursor.
* NVDA+Windows+O depois F: Ativa ou desativa o rastreamento do foco.
* NVDA+Windows+O depois M: Ativa ou desativa o rastreamento do mouse.
* NVDA+Windows+O então T: ativa ou desativa o rastreamento globalmente.
  Quando o rastreamento é ativado novamente, ele é definido para a última
  configuração de rastreamento ativa antes de ser desativado.
* NVDA+Windows+O depois S: Ativa ou desativa a suavização.
* NVDA+Windows+O e depois R: Alterna entre os modos de rastreamento do
  ponteiro do mouse (dentro da borda da tela ou centralizado na tela); esse
  recurso só está disponível no Windows 10 build 17643 ou superior.
* NVDA+Windows+O depois X: Alterna entre os modos de rastreamento do cursor
  de texto (no limite da tela ou centralizado na tela); esse recurso está
  disponível apenas no Windows 10 compilação 18894 ou superior.
* NVDA+Windows+O e, em seguida, shift+P: salva os parâmetros de configuração
  atuais da lupa na configuração do NVDA.
* NVDA+Windows+O e depois P: Restaura os parâmetros de configuração atuais
  da lupa a partir da configuração do NVDA.  Se nenhum parâmetro de
  configuração tiver sido salvo anteriormente na configuração do NVDA, os
  parâmetros de configuração padrão do Windows Magnifier serão restaurados.
* NVDA+Windows+O e depois Setas: Mover a visualização ampliada.
* NVDA+Windows+O e V: move o cursor do mouse para o centro da visualização
  ampliada (comando não disponível no modo de visualização encaixada).
* NVDA+Windows+O e depois W: Ativa ou desativa o modo que permite manter a
  janela de controle do Windows Magnifier sempre em cima das outras.  Esse
  recurso está disponível somente para as versões instaladas do NVDA.
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
* Redimensione a lente com o teclado: Shift+Alt+Esquerda/Direita/Seta para
  cima/para baixo Observação: embora isso não pareça estar documentado, esse
  atalho parece ter sido retirado das versões recentes do Windows, como o
  Windows 10 2004.
* Mover a visualização ampliada: Control+Alt+Setas

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

* Esse complemento não foi testado em ambiente de várias telas e é possível
  que alguns recursos não estejam funcionando nesse ambiente.  Se você
  estiver usando um ambiente com várias telas e quiser que ele seja
  suportado, entre em contato comigo para que ele seja implementado.
* De modo geral, não hesite em entrar em contato comigo na [página do
  GitHub][3] deste complemento ou diretamente por e-mail.


## Registro de alterações (Change log)

### Versão 3.5

* Prepara a compatibilidade com o NVDA 2024.1.
* Resolve possíveis problemas de segurança relacionados ao
  [GHSA-xg6w-23rw-39r8][8] ao usar o complemento com versões mais antigas do
  NVDA. No entanto, é recomendável usar o NVDA 2023.3.3 ou superior.
* Nota: De agora em diante, as atualizações de tradução não aparecerão mais
  no registro de alterações.

### Versão 3.4

* O comando “mover o mouse para visualizar” funciona novamente
* Localizações atualizadas.

### Versão 3.3

* Compatibilidade reduzida para NVDA 2019.2.1 e posteriores.  As últimas
  versões compatíveis com o NVDA 2018.3 são a [3.2][7] (parcialmente
  compatível) e a [1.1][6] (totalmente compatível)
* Corrigido um bug no painel de configurações com o NVDA 2019.2.1.

### Versão 3.2

* Removido o canal de desenvolvimento.
* Localizações atualizadas.

### Versão 3.1

* Foi corrigido um problema que impedia que a janela de comando da Lupa
  fosse restaurada na parte superior.
* Foi corrigido um problema que impedia a execução do complemento no NVDA
  2019.2.1.
* Localizações atualizadas.

### Versão 3.0

* Pressionar os botões de zoom na janela da Lupa (com o teclado) agora
  informa o novo nível de zoom.
* O parâmetro que controla se a janela de controle da Lupa permanece sempre
  na parte superior agora está armazenado na configuração; isso significa
  que esse parâmetro é lembrado ao reiniciar o NVDA e pode ser ativado ou
  não, dependendo do perfil ativo.
* Foi corrigido um erro que causava a desativação inesperada da cortina de
  tela ao usar os comandos mover para visualização ou mover visualização.
* A configuração da opção alwaysOnTop agora será respeitada também ao
  alterar o modo de ampliação.
* Adição da capacidade de salvar e restaurar a configuração do Windows
  Magnifier na configuração do NVDA.
* Compatibilidade com o NVDA 2023.1.
* Esclarecer qual tipo de rastreamento é reativado quando ele é ativado
  novamente.
* Localizações atualizadas.

### Versão 2.0

* A visualização pode ser movida com as setas enquanto estiver na camada
  Windows Magnifier.
* Capacidade de manter a janela de comandos da lupa sempre na parte superior
  ou não.
* Adição do recurso “Reportar bordas da tela”.
* Configuração do volume dos tons ao usar os comandos de exibição de
  movimento.
* Os movimentos de visualização de relatórios e os comandos de mouse para
  visualização agora são suportados no modo Lente.
* Compatibilidade com o NVDA 2022.1.
* Foi corrigido um erro que às vezes informava incorretamente que a lupa não
  estava funcionando na chamada do script.
* O lançamento agora é realizado graças a uma ação do GitHub em vez do
  appVeyor.
* Localizações atualizadas.

### Versão 1.1

* Adicionadas localizações.

### Versão 1.0

* Versão inicial.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=winmag

[3]: https://github.com/CyrilleB79/winMag

[4]: https://support.microsoft.com/pt-br/help/13810

[5]: https://addons.nvda-project.org/addons/easyTableNavigator.pt_BR.html

[6]:
https://github.com/CyrilleB79/winMag/releases/download/V1.1/winMag-1.1.nvda-addon

[7]:
https://github.com/CyrilleB79/winMag/releases/download/V3.2/winMag-3.2.nvda-addon

[8]:
https://github.com/nvaccess/nvda/security/advisories/GHSA-xg6w-23rw-39r8#event-132994
