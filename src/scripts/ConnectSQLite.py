# -*- coding: utf-8 -*-
"""."""
import sqlite3


class ConnectDB:
    def __init__(self, dbpath):
        self.con = sqlite3.connect(dbpath)
        self.cur = self.con.cursor()

    def table_exists(self, table):
        # query = 'SELECT name FROM sqlite_master WHERE type="table" AND name = ?;'
        query = 'SELECT name FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%";'
        # result = self.cur.execute(query, (table,))
        result = self.cur.execute(query, )
        # return result.fetchone()
        return result.fetchall()

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
            self.con.commit()
            print(f'\n[!] Tabela |{table}| removida com sucesso [!]')

    def create_table_available(self):
        query = '''CREATE TABLE IF NOT EXISTS `available` (
            arch text,
            description text,
            license text,
            pkg_name text,
            release text,
            reponame text,
            summary text,
            version text
            );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela available criada com sucesso [!]')

    def create_table_installed(self):
        query = '''CREATE TABLE IF NOT EXISTS `installed` (
            pkg_name text,
            installed bool
            );'''
        try:
            self.cur.execute(query)
        except Exception as e:
            print(f'\n[x] Falha ao criar a tabela [x]: {e}')
        else:
            print('\n[!] Tabela installed criada com sucesso [!]')

    def insert_dnf_available(self, data):
        """Adiciona varias linhas na tabela.

        Desta forma não se faz necessário um laço de repetição com
        vários ``inserts``.

        :param data: (list or tuple) Lista de tuplas contendo os
        dados ou uma tupla de tuplas contendo os dados.
        """
        query = '''INSERT INTO `available` 
                (arch, description, license, pkg_name, release, reponame, summary, version) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''
        try:
            self.cur.executemany(query, data)
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao inserir os registros na tabela |available| [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registros inseridos com sucesso na tabela |available| [!]')

    def insert_dnf_installed(self, data):
        """."""
        query = '''INSERT INTO `installed` 
                (pkg_name, installed) 
                VALUES (?, ?);'''
        try:
            self.cur.executemany(query, data)
        except Exception as e:
            self.con.rollback()
            print('\n[x] Falha ao inserir os registros na tabela |installed| [x]')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
        else:
            self.con.commit()
            print('\n[!] Registros inseridos com sucesso na tabela |installed| [!]')

    def get_packages_by_name(self, name, limit):
        """Consulta todos os registros da tabela.
        Utilizando ``limit`` para evitar consultas longas de mais.

        :param name: Nome do pacote que se deseja pocurar.
        :param limit: (int) Parâmetro que limita a quantidade de
        registros que serão exibidos.

        :return: É retornada uma lista (list) de tuplas (tuple)
        contendo os dados.
        Se não houver dados é retornada uma lista vazia ``[]``.
        """
        query = '''SELECT group_concat(DISTINCT arch), description, license, 
        pkg_name, release, group_concat(DISTINCT reponame), summary, version 
        FROM `available` 
        WHERE pkg_name LIKE "%"||?||"%" 
        GROUP BY pkg_name LIMIT ?;'''
        self.cur.execute(query, (name, limit))
        return self.cur.fetchall()

    def get_package_installed(self, name):
        query = '''SELECT  pkg_name, installed
        FROM `installed` 
        WHERE pkg_name = ?;'''
        self.cur.execute(query, (name,))
        return self.cur.fetchone()


if __name__ == "__main__":
    db = ConnectDB()
