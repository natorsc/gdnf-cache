# Gdnf-cache

![gdnf-cache](./docs/imgs/gdnf-cache.gif)

> **OBS**: Para exibir os detalhes de um determinado pacotes basta dar **2 cliques sobre a linha**.

Projeto criado a partir da ideia exibida na live do canal [debxp linux](https://www.youtube.com/channel/UC8EGrwe_DXSzrCQclf_pv9g).

Link para live onde a ideia é exibida:

- [Live Coding #17 - Apresentando o script DNF-CACHE!](https://youtu.be/4drCw9fXfnw).

Repositório da live no Gitlab:

- [dnf-cache](https://gitlab.com/blau_araujo/dnf-cache)

## Observações

A biblioteca `dnf` que é importada nos scripts do Python não funciona dentro de ambientes virtuais (pipenv, venv, etc). Deve-se utilizar o interpretador Python do sistema para execução do código.

Para instalar a mesma:

```bash
sudo dnf install python3-dnf
```

---

Chaves válidas para o `available()`:

```text
'_chksum', '_from_cmdline', '_from_repo', '_from_system', '_header',
'_is_in_active_module', '_is_local_pkg', '_pkgid', '_priv_chksum', '_priv_size',
'_repo', '_size', 'a', 'arch', 'base', 'baseurl', 'buildtime', 'changelogs',
'chksum', 'conflicts', 'debug_name', 'debugsource_name', 'description',
'downloadsize', 'e', 'enhances', 'epoch', 'evr', 'evr_cmp', 'evr_eq', 'evr_gt',
'evr_lt', 'files', 'getDiscNum', 'get_advisories', 'get_delta_from_evr', 'group',
'hdr_chksum', 'hdr_end', 'idx', 'installed', 'installsize', 'installtime',
'license', 'localPkg', 'location', 'medianr', 'name', 'obsoletes', 'packager',
'pkgdir', 'pkgtup', 'prereq_ignoreinst', 'provides', 'r', 'reason', 'recommends',
'regular_requires', 'relativepath', 'release', 'remote_location', 'repo', 'repoid',
'reponame', 'requires', 'requires_pre', 'returnIdSum', 'rpmdbid', 'size',
'source_debug_name', 'source_name', 'sourcerpm', 'suggests', 'summary',
'supplements', 'ui_from_repo', 'url', 'v', 'verifyLocalPkg', 'version'
```

---

Na função `def get_package_by_name(self, name, limit=10)` do script `ConnectSQLite.py` está sendo utilizado o parâmetro `limit` para evitar consultadas longas de mais. Edite conforme a sua necessidade.

Como não foram gerados executáveis (binários) é necessário ter as bibliotecas do GTK instaladas no sistema. Para ver como realizar a instalação acesse meu outro repositório:

- [https://github.com/natorsc/gui-python-gtk](https://github.com/natorsc/gui-python-gtk).

## ToDo

- [x] Colocar a consulta da interface em outra thread (para não travar o loop da interface).
- [x] Modo escuro da interface (dark mode) :satisfied:.
- [x] Criar arquivo de interface para o dialogo de detalhes do pacotes.
- [x] Criar arquivo de interface para o dialogo sobre.
- [ ] Criar um controle para o parametro `limit`?