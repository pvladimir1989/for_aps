import csv
import json
import os

import pandas as pd
import psycopg2
from elasticsearch import Elasticsearch

from dotenv import load_dotenv

load_dotenv()

INDEX = "posts"
SERVER_POSTGRES_CONNECTION = os.getenv("SERVER_POSTGRES_CONNECTION", None)


def df2elastic_converter(df):
    for record in df.to_dict(orient="records"):
        yield '{ "index" : { "_index" : "%s", "_type" : "%s" }}' % (INDEX, "record")
        yield json.dumps(record, default=int)


def elastic_insert_logic(file_name: str):
    """ в Elastic"""
    df = pd.read_csv(file_name, usecols=[0])
    df["id"] = df.index + 1

    # Добавляем все в новый индекс INDEX
    e = Elasticsearch("http://es01:9200")
    if e.indices.exists(INDEX):
        e.indices.delete(index=INDEX)
    e.indices.create(index=INDEX)

    r = e.bulk(df2elastic_converter(df))
    if not r["errors"]:
        print("Успешно")
    else:
        print("Ошибка")


def postgres_insert_logic(file_name: str):
    """Добавление данных в Postgres"""
    conn = psycopg2.connect(SERVER_POSTGRES_CONNECTION)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS posts;")
    cur.execute("""CREATE TABLE posts(
        id SERIAL PRIMARY KEY,
        rubrics text[] NOT NULL,
        text text NOT NULL,
        created_date date NOT NULL
    )
    """)

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            sql = "INSERT INTO posts (rubrics, text, created_date) VALUES  (%s, %s, %s)"
            cur.execute(sql, (eval(row[2]), row[0], row[1]))

    conn.commit()
    print("Успешно записал данные в postgres")


def main():
    file_name = "./posts.csv"
    postgres_insert_logic(file_name)
    elastic_insert_logic(file_name)


if __name__ == "__main__":
    main()
