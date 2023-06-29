import os

def enter_log():
    date = input("Date: ")
    title = input("Log Title: ")
    text = input("Text of Log: ")

    filename = "logs/log_" + date + ".txt"
    with open(filename, 'w') as f:
        f.write("Date: " + date + "\n")
        f.write("Log Title: " + title + "\n")
        f.write("Text of Log: " + text + "\n")

    print("\nLog is saved.\n")

def list_logs():
    print("\nListing all saved logs:\n")
    my_logs = os.listdir("logs")
    for log in my_logs:
        print(log)
    print()

def open_log():
    log_name = input("Which log to open: ")
    filepath = "logs/" + log_name + ".txt"
    if os.path.isfile(filepath):
        print("\nReading log " + log_name + ":\n")
        with open(filepath, 'r') as f:
            print(f.read())
    else:
        print("\nLog does not exist.\n")

def main():
    while True:
        print("Welcome Captain!\n")
        print("How should I be of service?\n")
        print("(Select options 1 - 4)\n")
        print("--------------------------------------------\n")
        print("1. Enter a New log.\n")
        print("2. List all saved logs.\n")
        print("3. Open log.\n")
        print("4. Exit Captains Logs.\n")
        print("--------------------------------------------\n")

        choice = input("Your choice: ")

        if choice == '1':
            enter_log()
        elif choice == '2':
            list_logs()
        elif choice == '3':
            open_log()
        elif choice == '4':
            print("\nExiting Captains Logs...\n")
            break
        else:
            print("\nInvalid choice, please try again.\n")

if __name__ == "__main__":
    if not os.path.exists('logs'):
        os.makedirs('logs')
    main()
