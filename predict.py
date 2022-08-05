#fastTextで学習
import fasttext as ft

model = ft.train_supervised("model.txt", label_prefix='__label__',epoch=1000, loss="hs")
model.save_model("model.bin")

with open('./result.disticted.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.replace('\n', '')
        result = model.predict(line)
        if result[0][0]=="__label__1":
            with open('result.txt', 'a', encoding='UTF-8') as f: 
                print(line + ':' + result[0][0] + ':' + str(result[1][0]))
                f.write(line + "\n")


   

