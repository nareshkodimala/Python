from PIL import Image
ref=Image.open("newfile.jpg")
ref1=ref.convert("L")
ref1.show()


from PIL import Image
ref=Image.open("newfile1.jpg")
ref1=ref.convert("L")
ref1.show()



from PIL import Image
ref=Image.open("newfile.jpg")
ref1=ref.resize((500,600))
print(ref1.size)
ref1.show()
ref1.save("newfile.jpg")
