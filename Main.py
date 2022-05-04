# Jayden McCormick
""" This is my COP 1500 integration project for Spring 2022.
My project is a basic tool for selecting hardware for building a computer. """


__author__ = "Jayden McCormick"

import time


def pause():
    """
    Used to make a short pause for the user to read what is on screen without
    getting overwhelmed by a ton of text all at once.
    """
    for timer in range(3):
        print("", end="")
        time.sleep(0.5)


def partpicker():
    """
    This function is what holds all of the actual math and input statements
    to generate what parts the user may want to consider building with.
    """
    cpubrand = 0
    amdchoice = 0
    cpuchoice = 0
    cpuprice = 0
    cpu = 0
    cpucost = 0
    coolercost = 0
    coolerreq = 0
    totalcost = 0
    wifireq = 0
    mbchoice = 0
    # All above are used to prevent errors saying they may be referenced before
    # assignment, even though the way the code is set up it would never happen.
    validation = True
    while validation:
        cpubrand = input("Choose your cpu by entering '1' or '2': ")
        try:
            if int(cpubrand) == 1:
                print("You have chosen a AMD cpu.")
                cpubrand = int(1)
                validation = False
            elif int(cpubrand) == 2:
                print("You have chosen a Intel cpu.")
                cpubrand = int(2)
                validation = False
            else:
                print("Invalid number, please try again.")
        except ValueError:
            print("Please enter the whole numbers 1 or 2.")
    # Provides confirmation of the cpu selected,
    # if incorrectly selected it allows another chance to enter
    # a valid cpu before prompting the user to exit.
    print("Alright, now lets get into a bit more detail.")
    if cpubrand == 1:
        cpu = "AMD cpu"  # Setting string
        cpuchoice = 0  # Setting cpuchoice as a variable (Intel cpu)
        print("Since you have chosen a AMD cpu, "
              "would you like a,", end=' ')
        print("lower-end ($115), mid-range ($300), "
              "or high-end cpu? ($4000)")
        print("For low-end, enter '1', mid-range: '2', "
              "high-end: '3'")
        validation = True
        while validation:
            amdchoice = input("Enter '1', '2', or '3': ")
            try:
                if int(amdchoice) == 1:
                    cpuprice = "low-end "  # Setting string
                    print("You have chosen the low-end cpu.")
                    print("The cpu is a AMD Athlon 3000G Picasso", end=' ')
                    print("3.5GHz at $114.99.", end=' ')
                    print("However, it doesn't come "
                          "with a cooler.", end=' ')
                    print("The recommended cooler would be the", end=' ')
                    print("'Cooler Master Hyper 212' at $49.99.")
                    amdchoice = int(1)
                    validation = False
                elif int(amdchoice) == 2:
                    cpuprice = "mid-range "  # Setting string
                    print("You have chosen the mid-range cpu.")
                    print("The cpu is a Ryzen 5 5600X 6-core,"
                          " 12-threads.", end=' ')
                    print("It comes with an air cooler included at $300.")
                    amdchoice = int(2)
                    validation = False
                elif int(amdchoice) == 3:
                    cpuprice = "high-end "  # Setting string
                    print("You have chosen the high-end cpu.")
                    print("The cpu is a Ryzen Threadripper 3990X", end=' ')
                    print("64-Core 2.9 GHz at $3989.99.", end=' ')
                    print("However, you will need a heavy-duty"
                          " cooling solution.", end=' ')
                    print("The best recommended would be the", end=' ')
                    print("'Thermaltake Water 3.0 "
                          "Riing 360mm' at $179.99.")
                    amdchoice = int(3)
                    validation = False
                else:
                    print("You have selected an invalid number,"
                          "please try again.")
            except ValueError:
                print("You have selected an invalid character, please "
                      "enter a whole number.")

    # Provides options, the rough cost, confirmation,
    # a chance to redo if entered incorrectly.
    # Setting up costs for later calculation.
    # Also separates AMD from Intel. Prices from
    # newegg.com, amazon.com and bestbuy.com

    if cpubrand == 2:
        cpu = "Intel cpu"  # Setting string
        amdchoice = 0  # Setting amdchoice as a varible. (AMD cpu)
        print("Since you have chosen a Intel cpu, "
              "would you like a", end=' ')
        print("lower-end ($120), mid-range ($200),"
              " or high-end ($620) cpu?")
        print("For low-end, enter '1', mid-range: '2', high-end: '3'")
        validation = True
        while validation:
            cpuchoice = input("Enter '1', '2', or '3': ")
            try:
                if int(cpuchoice) == 1:
                    cpuprice = "low-end "  # Setting string
                    print("You have chosen the low-end cpu.")
                    print("The cpu is a Intel "
                          "Pentium Gold G-6400 2-Core 4.0 GHz at 119.99")
                    print("However, it doesn't come with a cooler.")
                    print("The recommended cooler would be the", end=' ')
                    print("'Cooler Master Hyper 212' at $49.99.")
                    cpuchoice = int(1)
                    validation = False
                elif int(cpuchoice) == 2:
                    cpuprice = "mid-range "  # Setting string
                    print("You have chosen the mid-range cpu.")
                    print("The cpu is a i5-11400 "
                          "6-Core 4.4 GHz at $189.99.")
                    print("The recommended cooler would be the", end=' ')
                    print("'Cooler Master Hyper 212' at $49.99.")
                    cpuchoice = int(2)
                    validation = False
                elif int(cpuchoice) == 3:
                    cpuprice = "high-end "  # Setting string
                    print("You have chosen the high-end cpu.")
                    print("The cpu is a Core i9-12900K"
                          " 16-Core, 5.2 GHz at $619.99.")
                    print("However, you will need a heavy-duty"
                          " cooling solution.", end=' ')
                    print("The best recommended would be the", end=' ')
                    print("'Thermaltake Water 3.0 Riing' at $179.99.")
                    cpuchoice = int(3)
                    validation = False
                else:
                    print("You have selected an invalid number,"
                          "please try again.")
            except ValueError:
                print("You have selected an invalid character, please "
                      "enter a whole number.")
    if amdchoice == 1:
        cpucost = 114.99
        coolercost = 49.99
    elif amdchoice == 2:
        cpucost = 300
        coolercost = 0
    elif amdchoice == 3:
        cpucost = 3989.99
        coolercost = 179.99

    if cpuchoice == 1:
        cpucost = 119.99
        coolercost = 49.99
    elif cpuchoice == 2:
        cpucost = 189.99
        coolercost = 49.99
    elif cpuchoice == 3:
        cpucost = 619.99
        coolercost = 179.99
    # Provides options, the rough cost, confirmation,
    # a chance to redo if entered incorrectly.
    # Setting up costs for later calculation.
    # Also separates Intel from AMD. Prices from newegg.com and amazon.com
    print("You have chosen a " + cpuprice + cpu)
    # Reassures what was selected above and combines the two strings.

    print("Please note that this program ignores tax values.")
    print("Your total cost for your cpu and Cooler is:")
    print(cpucost, coolercost, sep='+')
    # The two prices assigned previously being visually added together.
    cputempcost = cpucost + coolercost
    print("$", format(cputempcost, '.2f'), sep='')
    print("Do you already have a cooler that you would like to use?")
    print("Enter '1' if you don't need a cooler,"
          " '2' if you need to buy one")
    validation = True
    while validation:
        coolerreq = input("Enter '1' or '2': ")
        try:
            if int(coolerreq) == 1:
                totalcost = cputempcost - coolercost
                print("Your new price is: $", format(totalcost, '.2f'))
                coolerreq = int(1)
                validation = False
            elif int(coolerreq) == 2:
                totalcost = cputempcost
                print("Your total cost remains at: $",
                      format(totalcost, '.2f'))
                coolerreq = int(2)
                validation = False
            else:
                print("Please enter the numbers 1 or 2")
        except ValueError:
            print("Your character is invalid, please try again.")
    roundedcost = (totalcost + 1) // 1
    print("Smallest whole dollar amount you can pay: $",
          format(roundedcost, '.2f'))
    # Showing the total cost for the cpu, to the cent
    # setting the total cost as of this point,
    # will add along as parts are configured.
    # Showing smallest possible whole dollar amount to purchase
    print("Great, now that you've selected your cpu,", end=' ')
    print("let's get onto the motherboard.")
    print("The motherboard is the main 'house'", end=' ')
    print("where all the components are seated into", end=' ')
    print("This allows them to work together.", end=' ')
    print("The motherboard is where everything is plugged into", end=' ')
    print("and how the computer is turned on.")
    print("Motherboards can come with or without WiFi.")
    print("If you already have a WiFi adaptor (usb or PCIe)", end=' ')
    print("or are able to run a ethernet cable to your computer,", end=' ')
    print("it isn't as important and not "
          "having it can save you some money.")
    print("Do you need a motherboard with "
          "WiFi? Enter '1' for yes, or '2' for no.")
    validation = True
    while validation:
        wifireq = input("Enter '1' or '2'")
        try:
            if int(wifireq) == 1:
                wifireq = int(1)
                print("You have chosen to have WiFi.")
                validation = False
            elif int(wifireq) == 2:
                wifireq = int(2)
                print("You have chosen no WiFi.")
                validation = False
            else:
                print("Please enter either 1 or 2.")
        except ValueError:
            print("Answer not recognized, please try again.")

    # Provides confirmation of selection,
    # and if incorrectly answered it allows another chance to provide an answer
    if amdchoice == 1 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif amdchoice == 1 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif amdchoice == 2 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif amdchoice == 2 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif amdchoice == 3 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif amdchoice == 3 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
        # Choosing motherboard based on user inputted cpu and
        # if they need Wi-Fi
    elif cpuchoice == 1 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif cpuchoice == 1 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif cpuchoice == 2 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        int(input("Enter '1' for low-end, '2' for higher-end."))
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif cpuchoice == 2 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif cpuchoice == 3 and wifireq == 1:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    elif cpuchoice == 3 and wifireq == 2:
        chipset = "Ex chipset."
        print("Since you have chosen the " + cpuprice + cpu, end=' ')
        print("You have a choice between a", end=' ')
        print("low-end motherboard or higher-end of the " + chipset)
        validation = True
        while validation:
            mbchoice = input("Enter '1' for low-end, '2' for"
                             " higher-end.")
            try:
                if int(mbchoice) == 1:
                    print("Test")
                    mbchoice = int(1)
                    validation = False
                elif int(mbchoice) == 2:
                    print("Test")
                    mbchoice = int(2)
                    validation = False
                else:
                    print("Please enter the numbers 1 or 2.")
            except ValueError:
                print("Invalid character, please try again.")
    # Choosing motherboard based on user inputted cpu and if
    # they need Wi-Fi
    print("Now that you have a basic outline of the hardware and prices,",
          end=' ')
    print("let's see how your budget compares to the price.")
    inpbudget = int(input("Enter your budget in whole dollars: $"))
    print("Your total cost is: $", roundedcost, sep='')
    pricediff = roundedcost - inpbudget
    # Shows difference in price between your budget and the cost of the machine
    if pricediff > 0:
        print("Your total cost minus your budget is: ", end='')
        print(roundedcost, inpbudget, sep='-')
        print("You still need to save: $", pricediff, end='')
        print(" to get this build.")
    elif pricediff <= 0:
        print("You have enough money saved for this build!")
        print("You have ", (-pricediff), sep='', end=' ')
        print("extra.")
    if coolerreq == 5:
        return coolerreq + mbchoice + amdchoice + cpuchoice
        #  Impossible to occur, but used to remove warnings that the
        #  above variables may not be used since they were used,
        #  but hidden in if/elif statements (im assuming)


def required():
    """
    This function holds everything that was required for the project, which
    I couldn't naturally fit into the theme.
    """
    validation = True
    while validation:
        exponent = input("Enter a whole number above 0 to be squared: ")
        try:
            if int(exponent) > 0:
                square = int(exponent) ** 2
                print(square)
                validation = False
            else:
                print("Please enter a whole number above 0.")
        except ValueError:
            print("Please enter a whole number above 0. (ex: 1,2,3)")
    # Shows a number squared, and doesn't allow something that's not a number>0
    validation = True
    while validation:
        multiply = input("Enter a whole number above 0 to be "
                         "multiplied by 2: ")
        try:
            if int(multiply) > 0:
                multiplied = int(multiply) * 2
                print(multiplied)
                validation = False
            else:
                print("Please enter a whole number above 0.")
        except ValueError:
            print("Please enter a whole number above 0. (ex: 1,2,3)")
    # Shows a number multiplied by 2
    # , and doesn't allow something that's not a number>0
    validation = True
    while validation:
        division = input("Enter a whole number above 0 to be divided by 2: ")
        try:
            if int(division) > 0:
                divided = int(division) / 2
                print(divided)
                validation = False
            else:
                print("Please enter a whole number above 0.")
        except ValueError:
            print("Please enter a whole number above 0. (ex: 1,2,3)")
    # Shows a number divided by 2
    # , and doesn't allow something that's not a number>0
    validation = True
    while validation:
        modulo = input("Enter a whole number above 4 to be given the "
                       "remainder after division by 3: ")
        try:
            if int(modulo) > 4:
                percentsign = int(modulo) % 3
                print(percentsign)
                validation = False
            else:
                print("Please enter a whole number above 4.")
        except ValueError:
            print("Please enter a whole number above 4. (ex: 5,6,7)")
    # Shows a remainder from 3, and doesn't allow something
    # that's not a number>4


def main():
    """
    The main function is the function that calls upon all the other functions.
    """
    # Setting some future variables as 0s, to ensure everything runs smoothly
    hello = "Hello "
    print(hello * 2)  # The only use I could think of, for now at least,
    # where string repetetion would be useful. A double "Hello" intro.
    print("Welcome to the computer hardware selector.")
    pause()
    print("Before we get into the actual project, let's get through what I "
          "couldn't naturally fit into the project that are required.")
    pause()
    required()
    pause()
    print("Now let's get into the actual project!")
    print("First, let's choose a cpu as it will determine the chipset"
          " to pick.")
    pause()
    print("The cpu is essentially the brains of the computer.", end=' ')
    print("It handles all the processing done, and is a very important part.")
    pause()
    print("Enter '1' to choose an AMD Ryzen cpu.")
    print("These are recommended for higher end, multi-use builds.", end=' ')
    print("They perform very well for gaming, editing, design, and other"
          " tasks.")
    pause()
    print("Enter '2' to choose an Intel cpu.")
    print("These are recommended for lower end builds.", end=' ')
    print("They are mainly useful for general computing and gaming.")
    pause()
    partpicker()
    pause()
    print("You have reached the end of my project!")
    print("I happened to have all things necessary for the assignment")
    print("before having to go through and research chipsets and plug them in "
          "(sigh of relief) so I'm not sure if I'll come back to this or not")
    pause()
    validation = True
    while validation:
        adios = input("Enter '1' to exit: ")
        try:
            if int(adios) == 1:
                validation = False
                quit()
            else:
                print("I said, Enter '1' to exit: ")
        except ValueError:
            print("It's too late to try to crash the program!")
    # Shows ending for now, quits program.


if __name__ == "__main__":
    main()
