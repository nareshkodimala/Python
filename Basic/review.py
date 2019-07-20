from PIL import Image
ref=Image.open("newimage.jpg")
ref1=ref.resize((4000,3000))
print(ref1.size)
ref1.show()
ref1.save("newimage.jpg")


from PIL import Image
ref=Image.open("newfile1.jpg")
ref1=ref.convert("L")
ref1.show()
ref1.save("newfile.jpg")
