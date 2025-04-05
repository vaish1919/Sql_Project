from database import get_connector
import matplotlib.pyplot as plt

import pandas as pd

def fetch_db():
    conn = get_connector()
    query = "select * from payment"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_html(classes="table table-striped") 

def fetch_group_by_db(column_name):
    conn = get_connector()
    query = f"select `{column_name}`, COUNT(*) AS count from payment group by `{column_name}`"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_html(classes="table table-striped")

def fetch_order_by_db(column_name):
    conn = get_connector()
    query = f"select * from payment order by `{column_name}` desc"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_html(classes="table table-striped")

def fetch_top5_db(column_name):
    conn = get_connector()
    query = f"select * from payment order by `{column_name}` desc limit 5"
    df = pd.read_sql(query, conn)
    conn.close()
    return df.to_html(classes="table table-striped")

def pie_chart(column_name):
    conn = get_connector()
    query = f"select {column_name} , count(*) as count from payment group by {column_name} limit 5"
    df = pd.read_sql(query, conn)
    conn.close()
    plt.figure(figsize=(10, 6))
    plt.pie(df['count'], labels=df[column_name], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  
    plt.savefig('static/pie_chart.png')
    plt.close()
