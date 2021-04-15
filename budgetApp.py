
class Budget:

    def __init__(self, food_balance, clothing_balance, entertainment_balance):
        self.food_balance = food_balance
        self.clothing_balance = clothing_balance
        self.entertainment_balance = entertainment_balance
    
    def init_session(self):
        print('WELCOME TO ***MY BUDGET*** APP')
        print('THE APP THAT MAKES YOU SPEND WISELY :)')
        print('BUDGET ON.')
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT')
        print('4. BALANCE')
        print('5. EXIT')
        
        try:
            output = int(input('CHOOSE AN OPTION: '))
            if output == 1:
                print(" ")
                self.food()

            elif output == 2:
                print(" ")
                self.clothing()

            elif output == 3:
                print(" ")
                self.entertainment()

            elif output == 4:
                print(' ')
                self.balance()

            elif output == 5:
                print("THANK YOU FOR USING OUR SERVICE.")
                exit()

            elif output != 1 or 2 or 3 or 4 or 5:
                print(" ")
                print('CHOOSE FROM AVAILABLE OPTIONS')
                print(" ")
                self.init_session()

        except ValueError:
            print(" ")
            print('NUMBERS ONLY.CHOOSE FROM AVAILABLE OPTIONS')
            print(" ")
            self.init_session()


    def food(self):
        name = 'FOOD'
        print('FOOD CATEGORY')
        print('1. DEPOSIT')
        print('2. WITHDRAW')
        print('3. TRANSFER') 
        print('4. RETURN TO MAIN MENU')
        try:
            output_food = int(input('CHOOSE AN OPTION: '))
            if output_food ==1:
                print(" ")
                if self.deposit_session(self.food_balance,name) == True:
                    print(" ")
                    self.food()
                else:
                    print(" ")
                    self.food()

            elif output_food == 2:
                print(" ")
                if self.withdrawal_session(self.food_balance,name) == True:
                    print(" ")
                    self.food()
                else:
                    print(" ")
                    self.food()

            elif output_food == 3:
                print(" ")
                self.transfer_session(self.food_balance,name)
                print(" ")
                self.food()

            elif output_food ==4:
                print(" ")
                self.init_session()

            elif output_food != 1 or 2 or 3 or 4 or 5:
                print(" ")
                print("CHOOSE FROM THE AVAILABLE OPTIONS")
                self.food()

        except ValueError:
            print(" ")
            print("NUMBERS ONLY. CHOOSE FROM AVAILABLE OPTIONS.")
            print(" ")
            self.food()


    def clothing(self):
        name = 'CLOTHING'
        print('CLOTHING CATEGORY')
        print('1. DEPOSIT')
        print('2. WITHDRAW')
        print('3. TRANSFER')
        print('4. RETURN TO MAIN MENU')
        try:
            output_clothing = int(input('CHOOSE AN OPTION: '))
            if output_clothing ==1:
                if self.deposit_session(self.clothing_balance,name) == True:
                    print(" ")
                    self.clothing()
                else:
                    print(" ")
                    self.clothing()

            elif output_clothing ==2:
                print(" ")
                if self.withdrawal_session(self.clothing_balance,name) == True:
                    print(" ")
                    self.clothing()
                else:
                    print(" ")
                    self.clothing()

            elif output_clothing == 3:
                print(" ")
                self.transfer_session(self.clothing_balance,name)
                print(" ")
                self.clothing()

            elif output_clothing == 4:
                print(" ")
                self.init_session()

            elif output_clothing != 1 or 2 or 3 or 4 or 5:
                print(" ")
                print("CHOOSE FROM AVAILABLE OPTIONS")
                print(" ")
                self.clothing()

        except ValueError:
            print(" ")
            print("NUMBERS ONLY. CHOOSE FROM AVAILABLE OPTIONS.")
            print(" ")
            self.clothing()


    def entertainment(self):
        name = 'ENTERTAINMENT'
        print('ENTERTAINMENT CATEGORY')
        print('1. DEPOSIT')
        print('2. WITHDRAW')
        print('3. TRANSFER')
        print('4. RETURN TO MAIN MENU')
        try:
            output_entertainment = int(input('CHOOSE AN OPTION: '))
            if output_entertainment ==1:
                if self.deposit_session(self.entertainment_balance,name) == True:
                    print(" ")
                    self.entertainment()
                else:
                    print(" ")
                    self.entertainment()

            elif output_entertainment ==2:
                if self.withdrawal_session(self.entertainment_balance,name) == True:
                    print(" ")
                    self.entertainment()
                else:
                    print(" ")
                    self.entertainment()

            elif output_entertainment == 3:
                self.transfer_session(self.entertainment_balance, name )
                print(" ")
                self.entertainment()

            elif output_entertainment == 4:
                print(" ")
                self.init_session()

            elif output_entertainment != 1 or 2 or 3 or 4 or 5:
                print(" ")
                print("CHOOSE FROM AVAILABLE OPTIONS")
                print(" ")
                self.entertainment()

        except ValueError:
            print(" ")
            print("NUMBERS ONLY. CHOOSE FROM AVAILABLE OPTIONS.")
            print(" ")
            self.entertainment()


    def deposit_session(self,deposit_sections,name):
        try:
            deposit= int(input("WHAT'S YOUR BUDGET FOR %s: " %name))
            deposit_sections.append(deposit)
            i = 0
            for deposit_section in deposit_sections:
                i+=deposit_section
            print("ACCOUNT_BALANCE %s: " %i)
            print('DEPOSIT SUCCESSFUL')
            return True
        except ValueError:
            print("NUMBERS ONLY")
            

    def withdrawal_session(self, withdrawal_sections,name):
        try:
            withdraw = int(input("HOW MUCH WILL LIKE TO WITHDRAW: "))
            i = 0
            for withdrawal_section in withdrawal_sections:
                i+=withdrawal_section
            new_balance = i - withdraw
            if new_balance > 0:
                withdrawal_sections = new_balance
                print("ACCOUNT_BALANCE %s: " %withdrawal_sections)
                print('WITHDRAWAL SUCCESSFUL')
                return True
            elif new_balance < 0:
                print("INSUFFICIENT FUNDS. MAKE A DEPOSIT")
                self.init_session()
        except ValueError:
            print("ENTER AMOUNT YOU WANT TO WITHDRAW IN NUMBERS")
    

    def transfer_session(self, sections, name):
        print("TRANSFER CATEGORY")
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT')
        try:
            transfer_to= int(input("ENTER THE NUMBER OF THE CATEGORY YOU WANT TO TRANSFER FROM: "))
            if transfer_to == 1:
                transfer_to = self.food_balance
                transfer_name = 'FOOD'
            elif transfer_to == 2:
                transfer_to = self.clothing_balance
                transfer_name = 'CLOTHING'
            elif transfer_to == 3:
                transfer_to = self.entertainment_balance
                transfer_name = 'ENTERTAINMENT'
            elif transfer_to != 1 or 2 or 3:
                print("CHOOSE FROM THE AVAILABLE OPTIONS")
                self.transfer_session(sections, name)

            transfer_how_much = int(input("ENTER HOW MUCH YOU WILL LIKE TO TRANSFER: "))
            for balance in sections:
                sections = balance
            transfer = sections - transfer_how_much
            if transfer > 0:
                sections = transfer
                for balance in transfer_to:
                    transfer_to = balance
                transfer_success = transfer_to + transfer_how_much
                transfer_to = transfer_success
                print("TRANSFER SUCCESSFUL")
                print("ACCOUNT BALANCE UPDATED")
                print("BALANCE FOR %s: %d" %(name, sections))
                print("BALANCE FOR %s: %d" %(transfer_name, transfer_to))
            else:
                print("INSUFFICIENT FUNDS. RETURN TO MAIN MENU AND MAKE A DEPOSIT")
                self.init_session()

        except ValueError:
            print("NUMBERS ONLY. CHOOSE FROM AVAILABLE OPTIONS")
            self.init_session()

        
    def balance(self):
        print("BALANCE CATEGORY")
        print('1. FOOD')
        print('2. CLOTHING')
        print('3. ENTERTAINMENT')
        print('4. RETURN TO MAIN MENU')
        try:
            bal = int(input("ENTER A CATEGORY(NUMBER) TO CHECK BALANCE: "))
            if bal == 1:
                print(' ')
                f = 0
                for f_bal in self.food_balance:
                    f+=f_bal
                print("BALANCE FOR FOOD CATEGORY: %d" %f)
                print(' ')
                self.food()

            elif bal == 2:
                print(' ')
                c = 0
                for c_bal in self.clothing_balance:
                    c+=c_bal
                print("BALANCE FOR CLOTHING CATEGORY: %d" %c)
                print(' ')
                self.clothing()

            elif bal == 3:
                print(' ')
                e = 0
                for e_bal in self.entertainment_balance:
                    e+=e_bal
                print("BALANCE FOR ENTERTAINMENT CATEGORY: %d" %e)
                print(' ')
                self.entertainment()

            elif bal == 4:
                print(' ')
                self.init_session()

            elif bal != 1 or 2 or 3 or 4:
                print(' ')
                print("INVALID OPTION. CHOOSE FROM AVAILABLE OPTIONS. NUMBERS ONLY")
                self.balance()

        except ValueError:
            print(' ')
            print("CHOOSE FROM AVAILABLE OPTIONS. ENTER NUMBERS ONLY")
            self.balance()
            print(' ')



obj = Budget([0],[0],[0])
obj.init_session()