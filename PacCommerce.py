from tabulate import tabulate
from math import sqrt

data = {
    "Sumbul":"Platinum",
    "Ana":"Gold",
    "Cahya":"Platinum"
}

benefit = {
    "Membership":["Platinum","Gold","Silver"],
    "Discount":[0.15,0.1,0.08],
    "Another Benefit":["Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%",
                       "Benefit Silver + Voucher Ojek Online","Voucher Makanan"]
}

requirement = {
    "Membership":["Platinum","Gold","Silver"],
    "Monthly Expense (juta)":[8,6,5],
    "Monthly Income (juta)":[15,10,7]
}


class Membership:

    def show_benefit():
        print("Benefit Membership PacCommerce\n")
        print(tabulate(benefit,headers="keys",tablefmt="github",numalign="center"))
    
    def show_requirements():
        print("Requirements Membership PacCommerce\n")
        print(tabulate(requirement,headers="keys",tablefmt="github",numalign="center"))

    def predict_membership(monthly_expense,monthly_income):
        prediction=[]
        r_p = sqrt((monthly_expense - requirement["Monthly Expense (juta)"][0])**2 + (monthly_income - requirement["Monthly Income (juta)"][0])**2)
        prediction.append(r_p)
        r_g = sqrt((monthly_expense - requirement["Monthly Expense (juta)"][1])**2 + (monthly_income - requirement["Monthly Income (juta)"][1])**2)
        prediction.append(r_g)
        r_s = sqrt((monthly_expense - requirement["Monthly Expense (juta)"][2])**2 + (monthly_income - requirement["Monthly Income (juta)"][2])**2)
        prediction.append(r_s)
        # print(prediction)
        prediction_value=min(prediction)
        if prediction_value == prediction[0]:
            print(requirement["Membership"][0])
        elif prediction_value == prediction[1]:
            print(requirement["Membership"][1])
        elif prediction_value == prediction[2]:
            print(requirement["Membership"][2])
        # print(min(prediction))

    def calculate_price(membership,list_harga_barang):
        if membership == benefit["Membership"][0]:
            final_price = sum(list_harga_barang) - (sum(list_harga_barang)*benefit["Discount"][0])
        elif membership == benefit["Membership"][1]:
            final_price = sum(list_harga_barang) - (sum(list_harga_barang)*benefit["Discount"][1])
        elif membership == benefit["Membership"][2]:
            final_price = sum(list_harga_barang) - (sum(list_harga_barang)*benefit["Discount"][2])
            
        print(final_price)

# Membership.show_benefit()
# Membership.show_requirements()
Membership.predict_membership(9,18)
# Membership.calculate_price(data["Ana"],[150_000, 200_000, 400_000])