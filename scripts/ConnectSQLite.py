# -*- coding: utf-8 -*-
"""Database.

Para visualizar ou manipular o banco SQLite pode-se utilizar a ferramenta:

- [DB Browser for SQLite](https://sqlitebrowser.org/).
"""

import sqlite3


class ConnectDB:
    def __init__(self, dbpath):
        # Criando conexão.
        self.con = sqlite3.connect(dbpath, check_same_thread=False)
        self.cur = self.con.cursor()
        # self.drop_table(table='available')
        if not self.table_exists(table='available'):
            self.create_table()

    def table_exists(self, table):
        query = 'SELECT name FROM sqlite_master WHERE type="table" AND name = ?;'
        result = self.cur.execute(query, (table,))
        return result.fetchone()

    def drop_table(self, table):
        """Remover tabela.
        :param table: (str) Nome da tabela que se deseja remover.
        """
        query = f'DROP TABLE IF EXISTS `{table}`;'
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao remover a tabela [x]: {e}')
        else:
            # Commit para registrar a operação/transação no banco.
            self.con.commit()
            print('\n[!] Tabela removida com sucesso [!]')

    def create_table(self):
        """Cria a tabela caso a mesma não exista."""
        query = '''CREATE TABLE IF NOT EXISTS `available` (
            arch text,
            description text,
            license text,
            pkg_name text,
            reponame text,
            summary text,
            version text
            );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela criada com sucesso [!]')

    def insert_dnf_metadata(self, data):
        """Adiciona varias linhas na tabela.

        Desta forma não se faz necessário um laço de repetição com
        vários ``inserts``.

        :param data: (list or tuple) Lista de tuplas contendo os
        dados ou uma tupla de tuplas contendo os dados.
        """
        query = '''INSERT INTO `available` 
                (arch, description, license, pkg_name, reponame, summary, version) 
                VALUES (?, ?, ?, ?, ?, ?, ?);'''
        try:
            self.cur.executemany(query, data)
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao inserir os registros [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registros inseridos com sucesso [!]')

    def get_package_by_name(self, name, limit=10):
        """Consulta todos os registros da tabela.
        Utilizando ``limit`` para evitar consultas longas de mais.

        :param name: Nome do pacote que se deseja pocurar.
        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.

        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = '''SELECT pkg_name, group_concat(arch) FROM `available` 
        WHERE pkg_name LIKE "%"||?||"%" 
        GROUP BY pkg_name LIMIT ?;'''
        self.cur.execute(query, (name, limit))
        return self.cur.fetchall()


if __name__ == "__main__":
    DB_DEV = '../data/db-dev.sqlite3'
    # db = ConnectDB(dbpath=DB_DEV)
    #
    # packages = db.get_package_by_name(name='pycharm')
    # print(packages)
