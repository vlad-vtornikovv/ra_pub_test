import zmq
import argparse
from time import sleep
from utils import getTimestamp

TIMEOUT = .5
TOPIC_NAME = '/timestamp'

def main(ip='0.0.0.0', port=5551):
  addr = f'tcp://{ip}:{port}'

  print(f'Publisher is running on {addr}')

  ctx = zmq.Context()
  publisher = ctx.socket(zmq.PUB)
  publisher.bind(addr)

  while True:
    try:
      sleep(TIMEOUT)
      publisher.send_multipart([
        bytes(TOPIC_NAME, 'utf-8'),
        b'%f' % getTimestamp(),
      ])
    except KeyboardInterrupt:
      break

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--ip', default=argparse.SUPPRESS, help='IP of (Docker) machine')
  parser.add_argument('--port', default=argparse.SUPPRESS, help='Port of (Docker) machine')

  args, _ = parser.parse_known_args()
  main(**vars(args))