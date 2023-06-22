from my_functions import my_func
import json
import classes_object



with open ("test_file.csv",'w',encoding = "utf-8") as f:
    f.write(my_func())




my_dictionary = {'apples':['jona gold','ingrid marie','granny smith'],'prices':[10,12,15]}


with open("test.json",'w',encoding = "utf-8") as f:
    json.dump(my_dictionary,f)




ferrari = classes_object.Cars('F1','Ferrari',250)



print(ferrari.make)
print(classes_object.lambo.make)