from tv import TV 

def main():
    # Create TV set
    telewizor = TV()
    print("TV is created")

    # Show TV status
    print("Status:")
    telewizor.show_status()

    # Turn TV on
    print("Turning TV on...")
    telewizor.turn_on()

    # Show TV status
    print("Status:")
    telewizor.show_status()

    # Turn TV off
    print("Turning TV of...")
    telewizor.turn_off()

    # Show TV status
    print("Status:")
    telewizor.show_status()

if __name__ == "__main__":
    main()