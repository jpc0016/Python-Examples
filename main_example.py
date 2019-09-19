# Use case of __main__ parameter
#
# define main function below
def main():
    print("\nHello main function!\n")

# When this file is run as the main program, the special variable __name__ is
# set to "__main__"
if __name__ == "__main__":
    main()


print("\nHello everyone else!\n")
