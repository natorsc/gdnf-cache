# -*- coding: utf-8 -*-
""".
O pacote `dnf` não funciona em ambientes virtuais, deve-se utilizar o
interpretador Python do sistema!
"""

from dnf import Base


def get_dnf_metadata():
    base = Base(0)
    base.read_all_repos()
    base.fill_sack()
    q = base.sack.query()
    q_available = q.available()
    available_packages = q_available.run()
    data = [(pkg.arch, pkg.description, pkg.license, pkg.name, pkg.reponame,
             pkg.summary, pkg.version) for pkg in available_packages]
    return data


if __name__ == '__main__':
    from ConnectSQLite import ConnectDB

    print('Criando/conectando no banco de desenvolvimento.')
    DB_DEV = '../data/db-dev.sqlite3'
    db = ConnectDB(dbpath=DB_DEV)
    #
    # print('Coletando dnf metadata...')
    # data = get_dnf_metadata()
    # db.insert_dnf_metadata(data=data)
    #
    # print('Dados inseridos')
