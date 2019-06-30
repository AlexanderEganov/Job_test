from urllib import request
import re
#myurl = "https://academy.hh.ru"
myurls = ["https://repetitors.info","https://hands.ru/company/about",]
nombers=[]
it = 0
for myurl in myurls:
    otvet = request.urlopen(myurl)
    serch_text = otvet.readlines()
    iterator = 1
    List_index = []
    list_index_str = []
    for line in serch_text:
        list_index_str = []
        stroka = str(line)
        list_index_str_mos=[m.start() for m in re.finditer("495", stroka)]
        list_index_str_ru=[m.start() for m in re.finditer("800", stroka)]
        for index in list_index_str_mos:
            list_index_str.append(index)
        for index in list_index_str_ru:
            list_index_str.append(index)
        list_index_str=list(set(list_index_str))
        kolichestvo_ind = len(list_index_str)
        if list_index_str:
            for index in list_index_str:
                if stroka[index-3] == '8' or stroka[index-2] == '8' or stroka[index-1] == '8' :
                    ind_8 = stroka.index('8',index-5)
                    stroka_tel = stroka[ind_8:ind_8 + 16 : 1]
                    nomber_tel = ''
                    for char in stroka_tel:
                        if char in ('0','1','2','3','4','5','6','7','8','9'):
                            nomber_tel=nomber_tel+char
                            if len(nomber_tel) == 11:
                                nombers.append(nomber_tel)

nombers = (list(set(nombers)))
for tel in nombers:
    print(str(iterator) + " : " + tel)
    iterator+=1
input()
