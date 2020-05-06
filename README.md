# Gdnf-cache

![gdnf-cache](./docs/imgs/gdnf-cache.gif)

## Como utilizar

Clique na aba **releases** do Github:

![Aba releases do Github](./docs/imgs/github/github-releases.png)

Ao acessar a aba releases clique na opção **Assets**:

![Opção assets do Github](./docs/imgs/github/github-assets.png)

Localize o arquivo com extensão `tar.xz` e realize o download do mesmo.

Ao concluir o download descompacte o conteúdo.

O aplicativo pode ser utilizado no local onde foi descompactado ou copiado para uma pasta de sua preferencia (aplicativo funciona como um portable).

Dentro do conteudo extraido procure pelo binario `gdnf-cache`, de 2 cliques sobre o mesmo e aguarde:

![Binario do Gdnf cache](./docs/imgs/github/binary-gdnf-cache.png)

Caso o aplicativo não inicie, abra um terminal na mesma pasta do binario (`gdnf-cache`) e execute `./gdnf-cache`:

![Executando o binario via terminal](./docs/imgs/github/terminal-run-binary.png)

Caso seja exibida alguma mensagem de erro favor reportar o erro :joy:. 

## Como desenvolver

Faça download ou clone este repositório.

Verifique se a biblioteca `python3-dnf` está instalada.

Caso não esteja:

```bash
sudo dnf install python3-dnf
```

> **OBS**: A biblioteca `dnf` que é importada em alguns scripts não funciona dentro de ambientes virtuais (pipenv, venv, etc). Utilize o interpretador Python do sistema para a execução do código.

Na função `def get_package_by_name(self, name, limit=10)` do script `ConnectSQLite.py` está sendo utilizado o parâmetro `limit` para evitar consultadas longas de mais. Edite conforme a sua necessidade.

Em sistemas baseados em GTK as bibliotecas necessárias costumam estar instaladas, caso não estejam acesse este meu outro repositório para ver como realizar a configuração do ambiente de de desenvolvimento.

- [https://github.com/natorsc/gui-python-gtk](https://github.com/natorsc/gui-python-gtk).

## Releases

- 06/05/2020 - [Gdnf cache 0.1.0](https://github.com/natorsc/gdnf-cache/releases/tag/v0.1.0) :tada:. 

## ToDo

- [x] Colocar a consulta da interface em outra thread (para não travar o loop da interface).
- [x] Modo escuro da interface (dark mode) :satisfied:.
- [x] Criar arquivo de interface para o dialogo de detalhes do pacotes.
- [x] Criar arquivo de interface para o dialogo sobre.
- [ ] Criar um controle para o parâmetro `limit`?

## Agradecimentos

Ao canal [debxp linux](https://www.youtube.com/channel/UC8EGrwe_DXSzrCQclf_pv9g) no YouTube.

Link para live onde a ideia foi exibida:

- [Live Coding #17 - Apresentando o script DNF-CACHE!](https://youtu.be/4drCw9fXfnw).

Repositório onde está sendo desenvolvido o `dnf-cache`, que é a versão cli (para se utilizar via terminal):

- [dnf-cache](https://gitlab.com/blau_araujo/dnf-cache)