nilai = [75, 55, 80, 60, 45, 90] 
Lulus = []

for x in nilai:
    if x >= 60:
        Lulus.append (x)
print(f"Nilai lulus = {Lulus}")
print (f"Jumlah lulus = {len(Lulus)}")