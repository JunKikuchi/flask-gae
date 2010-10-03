import wsgiref.handlers
import sys

if 'lib' not in sys.path:
  sys.path[0:0] = ['lib', 'distlib', 'distlib.zip']

from main import app

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
