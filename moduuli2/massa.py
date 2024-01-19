leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))
leiviskät_nauloiksi = leiviskät * 20
naulat_yhteensä = leiviskät_nauloiksi + naulat
naulat_luodeiksi = naulat_yhteensä * 32
luodit_yhteensä = naulat_luodeiksi + luodit
luodit_grammoiksi = float(luodit_yhteensä) * 13.3
kilogrammat = int(luodit_grammoiksi // 1000)
grammat = luodit_grammoiksi % 1000
print(f"Massa nykymittojen mukaan:\n{kilogrammat:}kg " "ja" f"{grammat: .2f}g")

