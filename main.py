import sys

from package.app import App

if __name__ == "__main__":
    app = App([])
    sys.exit(app.exec_())