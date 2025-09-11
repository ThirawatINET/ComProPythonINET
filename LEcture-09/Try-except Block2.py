filename = input("Enter a filename: ") #รับfilename
try: #ถ้าเปิดไฟล์ไม่ได้ ทำ line 8
        #ถ้าเปิดได้ line 4
    infile = open(filename, "r") 
    contents = infile.read() #ถ้าทำได้ทำอันนี้
    print(contents)
    infile.close()
except IOError: #ทำอันนี้ต่อ
    print("An error occurred trying to read")
    print("the file", filename)

print("End of Program")