from app import create_app

application = create_app()

import scheduler

if __name__ == '__main__':
    application.run(debug=True)
