# Creator: Mark Hunter
# Date: December 7th, 2021
# Purpose: This program is designed to input and track insurance policy statements for the One Stop Insurance Company

# We honestly only need to run this import statement once, so that's why it's here!
import datetime
while True:
    # Getting our constants and function here!
    # This ones to make sure we don't enter a fake province later!
    PROVINCE_LIST = ("AB", "SK", "PE", "NL", "QC", "ON", "MB", "NS", "BC", "YT", "NU")
    f = open("OSICDef.dat", "r")
    POLICY_NUM = int(f.readline())
    BASIC_PREM = float(f.readline())
    DISCOUNT = float(f.readline())
    EXTRA_COVERAGE = float(f.readline())
    GLASS_COVERAGE = float(f.readline())
    LOANER_COVERAGE = float(f.readline())
    HST_RATE = float(f.readline())
    PROCESS_FEE = float(f.readline())
    f.close()

    # Gotta get personal information somehow, here's a legal way!
    print('Lets enter our personal information first!')
    print('(Note: Every comma will be replaced by a space to prevent this program from breaking)')
    print('-----')
    while True:
        first_name = input('Enter your first name (Type END to stop entering data and view current data): ')
        first_name = first_name.capitalize()
        first_name = first_name.replace(',', ' ')
        if first_name == '':
            print('Invalid Entry! You cannot leave this information blank!')
        else:
            break

    if first_name.upper() == 'END':
        print('-----')
        break

    while True:
        last_name = input('Enter your last name: ')
        last_name = last_name.capitalize()
        last_name = last_name.replace(',', ' ')
        if last_name == '':
            print('Invalid Entry! You cannot leave this information blank!')
        else:
            break

    while True:
        address = input('Please enter your home address (Example: 19 Eighty-Four Drive): ')
        address = address.replace(',', ' ')
        if address == (''):
            print("Invalid entry! You cannot leave this information blank!")
        else:
            break

    while True:
        city = input('Please enter your city: ')
        city = city.replace(',', ' ')
        if city == (''):
            print('Invalid entry! You cannot leave this information blank!')
        else:
            break

    while True:
        province = input("Please enter your province (XX): ")
        province = province.upper()
        if len(province) != 2:
            print("Invalid entry! Province must be entered using this format (XX)")
        # No fake provinces allowed!
        elif province in PROVINCE_LIST:
            break
        else:
            print("Invalid entry! Province must be a valid province. Refer to the key below")
            print("(AB, SK, PE, NL, QC, ON, MB, NS, BC, YT, NU)")

    while True:
        postal = input("Please enter your postal code (XXXXXX): ")
        postal = postal.upper()
        postal = postal.replace(',', ' ')
        if len(postal) != 6:
            print("Invalid entry: Information must be 6 characters!")
        else:
            break

    while True:
        phone = input("Please enter your phone number (9999999999): ")
        if len(phone) != 10:
            print("Invalid entry: Information must be 10 digits")
        elif phone.isdigit() == False:
            print("Invalid entry: Information must be 10 digits")
        else:
            phone = "(" + phone[0:3] + ") " + phone[3:6] + "-" + phone[6:]
            break

    # Time for the insurance information. Remember, the more coverage, the more money for us!
    # I love capitalism.
    insurance_premium = 0
    print('-----')
    print('Now we shall enter our insurance information!')
    print('-----')

    # Every car after the first gets a 25% discount! Base premium only, read the fine print.
    # This is information we need for our data table, so I'm gonna calculate it early.
    while True:
        try:
            car_amount = int(input('How many cars are you signing up for this insurance plan?: '))
        except:
            print("Invalid Entry! Value cannot be below 0 or a decimal!")
        else:
            if car_amount == 1:
                insurance_premium = BASIC_PREM
                break
            elif car_amount > 1:
                insurance_premium = BASIC_PREM * car_amount
                discounted_cars = (car_amount * BASIC_PREM) - BASIC_PREM
                discounted_price = discounted_cars * DISCOUNT
                insurance_premium = insurance_premium - discounted_price
                break
            else:
                print("Invalid Entry! Value cannot be below 0 or a decimal!")

    # In case your wondering why we don't calculate anything for these, that's because we don't need the extra charge
    # information right now! We'll be using the answers for calculations later.
    while True:
        extra_liability = input("Would you like extra liability? (Y/N): ")
        extra_liability = extra_liability.upper()
        if extra_liability == 'Y' or extra_liability == 'N':
            break
        else:
            print("Invalid Entry! Please enter either Y or N!")

    while True:
        glass_coverage = input("Would you like glass coverage? (Y/N): ")
        glass_coverage = glass_coverage.upper()
        if glass_coverage == 'Y' or glass_coverage == 'N':
            break
        else:
            print("Invalid Entry! Please enter either Y or N!")

    while True:
        loaner_car = input("Are these loaner cars? (Y/N): ")
        loaner_car = loaner_car.upper()
        if loaner_car == 'Y' or loaner_car == 'N':
            break
        else:
            print("Invalid Entry! Please enter either Y or N!")

    while True:
        payment_plan = input("Select a plan, Full or Monthly (F/M): ")
        payment_plan = payment_plan.upper()
        if payment_plan == 'F' or payment_plan == 'M':
            break
        else:
            print("Invalid Entry! Please enter either F or M!")

    # Need to save our data. This will be stored in a database called Policies.dat, as shown there.
    f = open("Policies.dat", "a")
    f.write(
        f"{POLICY_NUM}, {first_name}, {last_name}, {address}, {city}, {province}, {postal}, {phone}, {car_amount}, "
        f"{extra_liability}, {glass_coverage}, {loaner_car}, {payment_plan}, {insurance_premium}\n")
    f.close()

    # Just keeping our constant table up to date and automating for the next policy number!
    POLICY_NUM = POLICY_NUM + 1
    f = open("OSICDef.dat", "w")
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASIC_PREM:,.2f}\n")
    f.write(f"{DISCOUNT:,.2f}\n")
    f.write(f"{EXTRA_COVERAGE:,.2f}\n")
    f.write(f"{GLASS_COVERAGE:,.2f}\n")
    f.write(f"{LOANER_COVERAGE:,.2f}\n")
    f.write(f"{HST_RATE:,.2f}\n")
    f.write(f"{PROCESS_FEE:,.2f}\n")
    f.close()

# Now we can do our receipt calculations and combining the names to create a full name.
# I prefer it that way.
    full_name = f'{first_name} {last_name}'
    extra_charge = 0

    if extra_liability == 'Y':
        extra_charge = extra_charge + (car_amount * EXTRA_COVERAGE)

    if glass_coverage == 'Y':
        extra_charge = extra_charge + (car_amount * GLASS_COVERAGE)

    if loaner_car == 'Y':
        extra_charge = extra_charge + (car_amount * LOANER_COVERAGE)

# Receipt time!

    # Bro what's the date?
    date = datetime.datetime.now()
    date = date.strftime("%b %d, %Y")

    # Calculations!
    insurance_premium_hst = insurance_premium * HST_RATE
    insurance_premium_total = insurance_premium + insurance_premium_hst
    extra_charge_hst = extra_charge * HST_RATE
    extra_charge_total = extra_charge + extra_charge_hst
    subtotal = insurance_premium + extra_charge
    total_hst = insurance_premium_hst + extra_charge_hst
    total = insurance_premium_total + extra_charge_total

    # ...Formatting...
    car_amount_str = f'{car_amount}'
    car_amount_pad = f'{car_amount_str:>4}'
    insurance_premium_str = f'${insurance_premium:,.2f}'
    insurance_premium_pad = f'{insurance_premium_str:>10}'
    insurance_premium_hst_str = f'${insurance_premium_hst:,.2f}'
    insurance_premium_hst_pad = f'{insurance_premium_hst_str:>10}'
    insurance_premium_total_str = f'${insurance_premium_total:,.2f}'
    insurance_premium_total_pad = f'{insurance_premium_total_str:>10}'

    extra_charge_str = f'${extra_charge:,.2f}'
    extra_charge_pad = f'{extra_charge_str:>10}'
    extra_charge_hst_str = f'${extra_charge_hst:,.2f}'
    extra_charge_hst_pad = f'{extra_charge_hst_str:>10}'
    extra_charge_total_str = f'${extra_charge_total:,.2f}'
    extra_charge_total_pad = f'{extra_charge_total_str:>10}'

    subtotal_str = f'${subtotal:,.2f}'
    subtotal_pad = f'{subtotal_str:>10}'
    total_hst_str = f'${total_hst:,.2f}'
    total_hst_pad = f'{total_hst_str:>10}'
    total_str = f'${total:,.2f}'
    total_pad = f'{total_str:>10}'

    print('One Stop Insurance Company Reciept')
    print(f'Current Date: {date}')
    print('')
    print('Customer Information')
    print(f'    {full_name}')
    print(f'    {city}, {address}')
    print(f'    {postal}, {province}')
    print('')
    print(f'Phone Number: {phone}')
    print('[======================================]')
    print(f'Cars Insured:                    {car_amount_pad}')
    print(f'                              -------')
    print(f'Insurance Premium:         {insurance_premium_pad}')
    print(f'HST:                       {insurance_premium_hst_pad}')
    print(f'Total:                     {insurance_premium_total_pad}')
    print(f'                              -------')
    print(f'Extra Charges:             {extra_charge_pad}')
    print(f'HST:                       {extra_charge_hst_pad}')
    print(f'Total:                     {extra_charge_total_pad}')
    print(f'                              -------')
    print(f'Subtotal:                  {subtotal_pad}')
    print(f'Total HST:                 {total_hst_pad}')
    print(f'Total:                     {total_pad}')
    print('[======================================]')
    print('Thank you for choosing One Stop Insurance!')
    print("   If you don't stop, we'll cover you!    ")
    print('-----')
    print('Data has been saved! Reciept is just above!')
    print('-----')
    print('Welcome back!')

    # The code below will only run after we type END in the first_name input above!

# This is to establish these variables in the first place, otherwise the program will crash if they can't find it later.
overall_insurance_premium = 0
overall_extra_charge = 0
overall_total_premium = 0
policy_sum = 0

# Bro what's the date? Again.
date = datetime.datetime.now()
date = date.strftime("%b %d, %Y")

# Setting up our report base here.
print('One Stop Insurance Company')
print(f'Policy Listing As Of {date}')
print(' ')
print("POLICY        CUSTOMER        INSURANCE      EXTRA        TOTAL")
print("NUMBER          NAME           PREMIUM       CHARGE      PREMIUM")
print("[===================================================================]")
# So much computing happens beyond here. This is why we don't calculate earlier! We really only need the info now.
# Oh, almost forgot! This is a loop designed to read every policy within our database and display it in a report!
f = open("Policies.dat", "r")
for PolicyLine in f:
    PolicyData = PolicyLine.split(',')
    customer_num = PolicyData[0].strip()
    first_name = PolicyData[1].strip()
    last_name = PolicyData[2].strip()
    car_amount = int(PolicyData[8].strip())
    extra_liability = PolicyData[9].strip()
    glass_coverage = PolicyData[10].strip()
    loaner_car = PolicyData[11].strip()
    payment_plan = PolicyData[12].strip()
    insurance_premium = float(PolicyData[13].strip())

    # The reason this variable is set up down here is to refresh every loop for the next policy.
    extra_charge = 0
    # This is counting how many policies we have. Will display later!
    policy_sum = policy_sum + 1
    # And now I'm just gonna combine the first and last name to make a...Full name! I AM A GENIUS!
    full_name = f'{first_name} {last_name}'

    # If statements are handy. We don't need any elif's or elses for these, as they'll just pass by if the value is N
    # and go straight to the next line of code.

    if extra_liability == 'Y':
        extra_charge = extra_charge + (car_amount * EXTRA_COVERAGE)

    if glass_coverage == 'Y':
        extra_charge = extra_charge + (car_amount * GLASS_COVERAGE)

    if loaner_car == 'Y':
        extra_charge = extra_charge + (car_amount * LOANER_COVERAGE)

    # And this is our total cost for the customers insurance!
    total_premium = insurance_premium + extra_charge

    # Just like the policy number, we're adding up to display this at the end!
    overall_insurance_premium = overall_insurance_premium + insurance_premium
    overall_extra_charge = overall_extra_charge + extra_charge
    overall_total_premium = overall_total_premium + total_premium

    # This is to format so the charts all in order. I will admit though, if a name is way too long, the graph will
    # become unaligned. However, this should be rare anyways.
    customer_num_str = f'{customer_num}'
    customer_num_pad = f'{customer_num_str:>6}'
    full_name_str = f'{full_name}'
    full_name_pad = f'{full_name_str:>18}'
    insurance_premium_str = f'${insurance_premium:,.2f}'
    insurance_premium_pad = f'{insurance_premium_str:>10}'
    extra_charge_str = f'${extra_charge:,.2f}'
    extra_charge_pad = f'{extra_charge_str:>10}'
    total_premium_str = f'${total_premium:,.2f}'
    total_premium_pad = f'{total_premium_str:>10}'

    # Finally, we'll enter the information into the graph!
    print(f'{customer_num_pad} {full_name_pad}    {insurance_premium_pad}  {extra_charge_pad}      {total_premium_pad}')

# Just closing up what we opened earlier. Also, loops gone! We entered all the policy information!
f.close()
# MORE FORMATTING!
policy_sum_str = f'{policy_sum}'
policy_sum_pad = f'{policy_sum:>3}'
overall_insurance_premium_str = f'${overall_insurance_premium:,.2f}'
overall_insurance_premium_pad = f'{overall_insurance_premium_str:>10}'
overall_extra_charge_str = f'${overall_extra_charge:,.2f}'
overall_extra_charge_pad = f'{overall_extra_charge_str:>10}'
overall_total_premium_str = f'${overall_total_premium:,.2f}'
overall_total_premium_pad = f'{overall_total_premium_str:>10}'
# And this is the overall information we'll put on the lower exterior of the graph!
print("[===================================================================]")
print(f'Total Policies: {policy_sum_pad}           {overall_insurance_premium_pad}   {overall_extra_charge_pad}'
      f'     {overall_total_premium_pad}')

# Slick border design.
print(' ')
print('-----')
print(' ')

# Graph Numba 2, Monthly Payers Only!
# And of course, resetting old values, but also a few newcomers! Say hello!
overall_total_premium = 0
overall_hst = 0
overall_total_cost = 0
overall_monthly_payment = 0
policy_sum = 0

# Setting up our new report!
print('One Stop Insurance Company')
print(f'Monthly payment listing as of {date}')
print(' ')

print("POLICY           CUSTOMER             TOTAL                       TOTAL        MONTHLY")
print("NUMBER             NAME              PREMIUM          HST         COST         PAYMENT")
print('[======================================================================================]')
f = open("Policies.dat", "r")
for PolicyLine in f:
    # Getting values again...
    PolicyData = PolicyLine.split(',')
    customer_num = PolicyData[0].strip()
    first_name = PolicyData[1].strip()
    last_name = PolicyData[2].strip()
    car_amount = int(PolicyData[8].strip())
    extra_liability = PolicyData[9].strip()
    glass_coverage = PolicyData[10].strip()
    loaner_car = PolicyData[11].strip()
    payment_plan = PolicyData[12].strip()
    insurance_premium = float(PolicyData[13].strip())

    # Refresh and name science once more.
    extra_charge = 0
    full_name = f'{first_name} {last_name}'
    # Stop right there! You must prove that you are a policy with monthly payments to get into the Cool Kids Club!
    while True:
        # Thank you for your proof and have a wonderful day!
        if payment_plan == 'M':
            # Attention everyone! We now have a new member to the Cool Kids Club!
            policy_sum = policy_sum + 1

            # Lets get your extra calculations calculated, shall we?
            if extra_liability == 'Y':
                extra_charge = extra_charge + (car_amount * EXTRA_COVERAGE)

            if glass_coverage == 'Y':
                extra_charge = extra_charge + (car_amount * GLASS_COVERAGE)

            if loaner_car == 'Y':
                extra_charge = extra_charge + (car_amount * LOANER_COVERAGE)

            # To your left, even more calculations to dive into!
            total_premium = insurance_premium + extra_charge
            hst = total_premium * HST_RATE
            total_cost = total_premium + hst
            monthly_payment = (total_cost + PROCESS_FEE) / 12

            # And to your right we have...More calculations...But for the future!
            overall_total_premium = overall_total_premium + total_premium
            overall_hst = overall_hst + hst
            overall_total_cost = overall_total_cost + total_cost
            overall_monthly_payment = overall_monthly_payment + monthly_payment

            # Sadly, we gotta do all this work, but let me tell you, it's to make sure you look great on our report!
            # Uh, I mean Cool Kids Club member list! Yeah!
            customer_num_str = f'{customer_num}'
            customer_num_pad = f'{customer_num_str:>6}'
            full_name_str = f'{full_name}'
            full_name_pad = f'{full_name_str:>18}'
            total_premium_str = f'${total_premium:,.2f}'
            total_premium_pad = f'{total_premium_str:>10}'
            hst_str = f'${hst:,.2f}'
            hst_pad = f'{hst_str:>10}'
            total_cost_str = f'${total_cost:,.2f}'
            total_cost_pad = f'{total_cost_str:>10}'
            monthly_payment = f'${monthly_payment:,.2f}'
            monthly_payment_pad = f'{monthly_payment:>10}'

            # You are now registered as a member of the Cool Kids Club! Have a great day! Next!
            print(f'{customer_num_pad}   {full_name_pad}         {total_premium_pad}    {hst_pad}    '
                  f'{total_cost_pad}  {monthly_payment_pad}')
            break
        else:
            # No monthly payment? No entering the Cool Kids Club! Get out!
            break

# Welp, that's all our members accounted for! Time to close up the data table!
f.close()
# we now return to your regularly scheduled formatting.
policy_sum_str = f'{policy_sum}'
policy_sum_pad = f'{policy_sum:>3}'
overall_total_premium_str = f'${overall_total_premium:,.2f}'
overall_total_premium_pad = f'{overall_total_premium_str:>10}'
overall_hst_str = f'${overall_hst:,.2f}'
overall_hst_pad = f'{overall_hst_str:>10}'
overall_total_cost_str = f'${overall_total_cost:,.2f}'
overall_total_cost_pad = f'{overall_total_cost_str:>10}'
overall_monthly_payment_str = f'${overall_monthly_payment:,.2f}'
overall_monthly_payment_pad = f'{overall_monthly_payment_str:>10}'

# And now, the bottom of the graph.
print("[======================================================================================]")
print(f'Total Policies: {policy_sum_pad}                  {overall_total_premium_pad}     {overall_hst_pad}'
      f'   {overall_total_cost_pad}   {overall_monthly_payment_pad}')

# And finally, we are done! This input statement is used to keep the program open until the user decides to close it.
print('-----')
input('Thank you for using this service! When you are ready to exit, press enter!')
