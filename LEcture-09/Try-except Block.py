try:#คาดว่า x = 1/0 จะ Error จะไปทำคำสั่ง exceptต่อ
    x = 1 / 0
except ZeroDivisionError as e: 
    print(f"Error: {e}")
print("End of Program") #ถ้าไม่ก็ end หรือถ้าจบ Error แล้วก็ end