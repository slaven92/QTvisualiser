import sys

from QTvisualiser.app import App

def main():
    app = App([])
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()