from flask import Flask, render_template
from fetch import fetch_db, fetch_group_by_db, fetch_order_by_db, fetch_top5_db, pie_chart

app = Flask(__name__)


@app.route("/")
@app.route("/fetch")
def fetch():
    table_html = fetch_db()
    return render_template("index.html", table=table_html)
    

@app.route("/group/<column_name>")
def fetch_group(column_name):
    table_html = fetch_group_by_db(column_name)
    return render_template("index.html", table=table_html)

@app.route("/order/<column_name>")
def fetch_order(column_name):
    table_html = fetch_order_by_db(column_name)
    return render_template("index.html", table=table_html)

@app.route("/top5/<column_name>")
def fetch_top5(column_name):
    table_html = fetch_top5_db(column_name)
    return render_template("index.html", table=table_html)

@app.route("/pie/<column_name>")
def fetch_pie_chart(column_name):
    pie_chart()
    return render_template("image.html")
    


if __name__ == "__main__":
    app.run(debug=True)