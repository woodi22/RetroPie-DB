from redis import Redis

r = Redis()

current_game = input("Current Game: ")
start_time = r.time
end_time = r.time

r.set('current_game', current_game)
r.set('start_time', start_time)
r.set('end_time', end_time)
