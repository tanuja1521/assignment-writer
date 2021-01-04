from PIL import Image

from fpdf import FPDF

img=Image.open("images/bg.png")
sizeOfSheet=img.width - 100
sheetLen = img.height - 100
print(sheetLen)
gap,_= 100,100
allowedchar='ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm(),.?;1234567890-'
def Write(char):
    global gap,_
    if char=='\n':
        pass
    else:
        char.lower()
        cases=Image.open("images/%s.png"%char)
        img.paste(cases,(gap,_))
        size=cases.width
        gap+=size
        del cases
if __name__=='__main__':

    try:
        with open("output/example.txt",'r') as file:
            i = 0
            data=file.read().replace('\n','#')
            l=len(data)
            nn=-(len(data)//-650)
            print(nn)
            wordlist=data.split(' ')
            for word in wordlist:
                if gap > sizeOfSheet-70*(len(word)):
                    gap=100
                    if _+200 < sheetLen:
                        _+=150
                    else:
                        img.save("output/%dout.png"%i)
                        i += 1
                        img1=Image.open("images/bg.png")
                        img=img1
                        gap,_= 100,100 

                for letter in word:
                    if letter in allowedchar:
                        if letter.islower():
                            pass
                        elif letter.isupper():
                            letter.lower()
                            letter+='upper'
                        elif letter=='?':
                            letter="question"
                        Write(letter)
                    elif letter =='#':
                        gap=100
                        if _+200 < sheetLen:
                            _+=150
                        else:
                            img.save("output/%dout.png"%i)
                            i += 1
                            img1=Image.open("images/bg.png")
                            img=img1
                            gap,_= 100,100 
                Write('space')
            img.save("output/%dout.png"%i)
            i += 1
            img1=Image.open("images/bg.png")
            img=img1
            gap,_= 100,100     
               

    except ValueError as E:
        print("{}\nTry again",format(E))
    imageList=[]
    for i in range(0,i):
        imageList.append("output/%dout.png"%i)

    cover=Image.open(imageList[0])
    width,height=cover.size
    pdf=FPDF(unit="pt",format=[width,height])
    for i in range(0,len(imageList)):
        pdf.add_page()
        pdf.image(imageList[i],0,0)
    pdf.output("output/new.pdf","F")
               