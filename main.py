import pandas as pd
import mysql.connector as mysql
import csv


# obtendo conexão com o banco
def getConnection():
    conn = mysql.connect(
        host='127.0.0.1', database='percistenciadedados', user='root', password='root123')
    return conn

# inserindo dados com formatação no mySQL


def insertCsvToMySQL():
    conn = getConnection()

    with open("dados.csv") as arquivoCSV:
        dadosCSV = csv.reader(arquivoCSV, delimiter=",")
        dadosToMySQL = []

        for row in dadosCSV:
            dadosToMySQL.append((row[0], row[1], row[2]))

        sql_stm = "INSERT INTO usuarios (ano, mes, usuarios) VALUES (%s, %s, %s)"
        cur = conn.cursor()
        cur.executemany(sql_stm, dadosToMySQL)
        conn.commit()
        cur.close()
        conn.close()

# def feito para testar a conexão


def testarConnection():
    conn = mysql.connect(
        host='127.0.0.1', database='percistenciadedados', user='root', password='root123')
    print(conn.get_server_info())
    print(conn.get_server_version())


# rodando aplicacao
if __name__ == '__main__':
    insertCsvToMySQL()
