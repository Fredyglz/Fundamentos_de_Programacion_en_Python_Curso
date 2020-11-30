usd = 230 
eur = 320

# 1 usd == 0.85 eur
eur_a_usd = 320 * 1 / 0.85
usd_a_eur = 230 * 0.85 / 1

print("Dolares y Euros")
print(eur, " euros son ", round(eur_a_usd, 4), " dolares ")
print(usd, " dolares son ", round(usd_a_eur, 4), " euros ")
