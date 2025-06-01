#Cameron Mendez
#Module1.3
#06/01/2025
#Bottles of Beer on the Wall


#Define countdown function
def countdown(bottles):
    bottles = int(bottles)

    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(
            f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n")
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.\n")


#Main program
def main():
    num_bottles = input("How many bottles of beer are on the wall? ")
    countdown(num_bottles)
    print("Go on a beer run and buy some more..")


#Run the main function
if __name__ == "__main__":
    main()

# Keep the program window open when opened in folder
input("\nPress Enter to exit...")