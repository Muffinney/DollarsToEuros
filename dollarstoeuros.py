while True:
    # Asks for dollar amount
    dollar = float(input("Enter dollar amount to be converted: "))

    # Conversion amount
    euros = dollar * .94540

    # Output euro amount
    print("You have €" + str(round(euros, 2)))

    # Asks if user wants to continue
    convert = input("Would you like to convert dollars to euros? ")
    if convert == "no":
        break