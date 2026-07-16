bank = 0
storage = int(input("วันนี้เก็บกี่ร้าน:"))

for I in range(1,storage + 1):
    shop1 = int(input("เก็บเงิน"))
    bank = shop1 + bank 
print(f"เก็บครบ {storage} ยอดเงินจำนวน {bank}")