
import subprocess

def run_command(cmd_list):
    result = subprocess.run(cmd_list, capture_output=True, text=True)
    if result.stdout:
        print("✅ Output:\n", result.stdout)
    if result.stderr:
        print("❌ Error:\n", result.stderr)

def show_menu():
    print("\n=== Linux Command Menu ===")
    print("1. Show Disk Usage")
    print("2. Show IP Address")
    print("3. List Files in Current Directory")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        run_command(['df', '-h'])
    elif choice == "2":
        run_command(['ip', 'a'])  # Or use ['ifconfig'] if installed
    elif choice == "3":
        run_command(['ls', '-l'])
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
