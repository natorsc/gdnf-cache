# Gdnf-cache

![gdnf-cache](./docs/imgs/gdnf-cache.gif)

Projeto criado a partir da ideia exibida na live do canal [debxp linux](https://www.youtube.com/channel/UC8EGrwe_DXSzrCQclf_pv9g).

Link para live onde a ideia é exibida:

- [Live Coding #17 - Apresentando o script DNF-CACHE!](https://youtu.be/4drCw9fXfnw).

Link para o repositório no Gitlab:

- [dnf-cache](https://gitlab.com/blau_araujo/dnf-cache)

## Observações

A biblioteca `dnf` que é importada nos scripts do Python não funciona dentro de ambientes virtuais (pipenv, venv, etc). Deve-se utilizar o interpretador Python do sistema para execução do código.

Para instalar a mesma:

```bash
sudo dnf install python3-dnf
```

Na função `def get_package_by_name(self, name, limit=10)` do script `ConnectSQLite.py` está sendo utilizado o parametro `limit` para evitar consultadas longas de mais. Edite conforme a sua necessidade.

Como não foram gerados executáveis (binários) é necessário ter as bibliotecas do GTK instaladas no sistema. Para ver como realizar a instalação acesse meu outro repositório:

- [https://github.com/natorsc/gui-python-gtk](https://github.com/natorsc/gui-python-gtk).
