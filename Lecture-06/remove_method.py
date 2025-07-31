fruirs_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
while "apple" in fruirs_with_duplicates:
    fruirs_with_duplicates.remove("apple")
print(f"Fruirs after remove: {fruirs_with_duplicates}")

#ใช้ while เพราะรู้ว่าจะLoopกี่รอบ 
#remove ลบ apple ทำไมเรื่อยๆจน apple หมด