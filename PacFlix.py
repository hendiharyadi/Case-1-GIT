from tabulate import tabulate


data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}
 

plans = {
    "Basic Plan":[True, True, True, False, False, 1, "3rd party Movie only", 120_000],
    "Standard Plan":[True, True, True, True, False, 2, "Basic Plan Content + Sports", 160_000],
    "Premium Plan":[True, True, True, True, True, 4, "Basic Plan + Standard Plan + PacFlix Original Series", 200_000],
    "Services":["Bisa Stream", "Bisa Download", "Kualitas SD", "Kualitas HD", "Kualitas UHD", "Number of Devices", "Jenis Konten", "Harga"]
}


plans_sorted={}


class User:

    def check_benefit():
        print("PacFlix Plan List\n")
        print(tabulate(plans,headers="keys"))

    def check_plan(username):
        for name,plan in data.items():
            if name == username:
                for list,benefits in plans.items():
                    if plan[0] == list:
                        plans_sorted[list] = benefits
                        print(list)
                        print(f'{plan[1]} Bulan\n')
                        print(f'{list} PacFlix Benefit List') 

                    if list == "Services":
                        plans_sorted[list] = benefits
                        print(tabulate(plans_sorted,headers="keys"))

    def upgrade_plan(username,current_plan,new_plan):
        for name,plan in data.items():
            if name == username and plan[0] == current_plan:
                    if plan[1] > 12:
                        disc = plans[new_plan][-1] * 0.05
                        final_price = plans[new_plan][-1] - disc
                    else:
                        final_price = plans[new_plan][-1]              
                    
                    print(final_price)


class NewUser:

    def pick_plan(new_plan,code_referral):
        referral_code_exists = False

        for name,plan in data.items():
            if code_referral == plan[-1]:
                print("referral code exist")
                disc = plans[new_plan][-1] * 0.04
                final_price = plans[new_plan][-1] - disc
                referral_code_exists = True
                break

        if not referral_code_exists:
            raise Exception("referral code doesn't exist")
            
        print(final_price)

# User.check_benefit()

# User.check_plan("Shandy")

# User.upgrade_plan("Cahya","Standard Plan","Premium Plan")

# NewUser.pick_plan("Basic Plan","shandy-2134")
