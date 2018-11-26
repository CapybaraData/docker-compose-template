from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    It works!!
  </body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)