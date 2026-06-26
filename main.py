import sys

def main():
    if "--ui" in sys.argv:
        print("Launching UI...")

    else:
        print("CLI mode...")


if __name__ == "__main__":
    main()
