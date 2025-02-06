# write your code here!
#RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
#ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
#NL – Honduran Lempira; 1 conicoin = 0.17 HNL;
#AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
#MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.
def currency_converted_list(amount: float):
    currencies = ["RUB", "ARS", "NL", "AUD", "MAD"]
    rates = [2.98, 0.82, 0.17, 1.9622, 0.208]
    for i in range(len(currencies)):
        converted = ""
        for j in range(len(rates)): 
            converted = f"I will get {round((rates[j] * amount), 2)} {currencies[i]} from the sale of {amount} conicoins"
        print(converted)
coni = float(input("Please, enter the number of conicoins you have: "))
print(f"{currency_converted_list(coni)}")
