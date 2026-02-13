from flask import FLASK

app = FLASK(__name__)

def normal_function():
  return "This will deploy on the agent server"

@app.route("/")
def home():
  return normal_function()

if __name_ == "__main__"
  app.run(host="0.0.0.0", port=5000)
