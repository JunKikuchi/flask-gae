import wsgiref.handlers

from main import app

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
