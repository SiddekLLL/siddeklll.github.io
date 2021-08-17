import base64
f=open('categories.png','rb') 
ls_f=base64.b64encode(f.read()) 
f.close()
code_1 = open('image_1.txt','wb')
code_1.write(ls_f) 
code_1.close()
# print(ls_f)