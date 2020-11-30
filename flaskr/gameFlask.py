from redis import Redis
from flask import Flask, jsonify, request

app = Flask(__name__)
r = Redis()

@app.route('/')
def home():
   return 'RetroPie DB'

@app.route('/current')
def current():
   if(r.get('end_time') == None and r.get('start_time' != None)):
      current_game = r.get('current_game')
      return jsonify(current_game.decode())
   else:
      return "There is no game being played"

if __name__ == '__main__':
   app.run(port=6379)