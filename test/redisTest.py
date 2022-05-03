import redis
import os

r = redis.from_url("redis://:p02c792e2cb6c84b316c095b0ab525168b4cc243b7de1f92943081f1ebd3579e2@ec2-18-205-76-248.compute-1.amazonaws.com:28339")
r.set("Message", "hello World")
msg = r.get("Message")
print(msg)