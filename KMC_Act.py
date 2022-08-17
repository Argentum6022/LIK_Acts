from docxtpl import DocxTemplate
import datetime
import os

def kmc():
    #Ввод данных
    file_path=str(input('Введите путь папки: '))
    date=str(input('Введите дату и время получения реагента: '))
    date_test_start=str(input('Введите дату начала испытаний: '))
    date_test_end=str(input('Введите дату окончания испытаний: '))
    number=str(input('Введите входящий номер реагента: '))
    customer=str(input('Введите название фирмы заказчика: '))
    receiving=str(input('Введите способ получения:'))
    brand_of_reagent=str(input('Введите марку реагента:'))
    batch_number1=str(input('Введите номер партии первого реагента: '))
    batch_number2=str(input('Введите номер партии второго реагента: '))
    manufacturer=str(input('Введите название фирмы производителя:'))
    well=str(input('Введите место отбора пробы: '))
    date_on_well=str(input('Введите дату и время отбора пробы: '))
    seal1=str(input('Введите номер пломбы первого реагента: '))
    seal2=str(input('Введите номер пломбы второго реагента: '))
    dop_acts=list(map(str,input('Введите названия сопроводительных документов через запятую,'
                           ' если таковые отсутствуют, поставьте \"-\": ').split(',')))

    #Создание новой папки
    file_path=file_path.replace('\\','\\\\')
    os.chdir(file_path)
    os.mkdir(number)

    #Определние текущей даты
    date_now=datetime.date.today()
    date_now=date_now.strftime('%d.%m.%Y')

    #Заполнение акта приёма
    doc = DocxTemplate(f"{file_path}\\Исходный Акт приёма КМЦ.docx")
    if dop_acts[0]=='-':
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,
                    'date_on_well' : date_on_well,'seal1' : seal1,'seal2' : seal2,'doc1':'-','doc2':'-',
                    'batch_number1':batch_number1,'batch_number2':batch_number2,
                    'brand_of_reagent':brand_of_reagent}
    elif len(dop_acts)==1:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,
                    'date_on_well' : date_on_well,'seal1' : seal1,'seal2' : seal2,'doc1':'-','doc2':'-',
                    'batch_number1':batch_number1,'batch_number2':batch_number2,
                    'brand_of_reagent':brand_of_reagent}
    else:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,
                    'date_on_well' : date_on_well,'seal1' : seal1,'seal2' : seal2,'doc1':'-','doc2':'-',
                    'batch_number1':batch_number1,'batch_number2':batch_number2,
                    'brand_of_reagent':brand_of_reagent}
    doc.render(context)
    doc.save(f"{file_path}\\{number}\\{number} Акт приёма материалов.docx")


    #Заполнение акта исследования первого реагента
    doc = DocxTemplate(f"{file_path}\\Исходный КМЦ 1.docx")
    if dop_acts[0]=='-':
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal1' : seal1,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number1': batch_number1,'manufacturer':manufacturer}
    else:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal1' : seal1,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number1': batch_number1,'manufacturer':manufacturer}
    doc.render(context)
    doc.save(f"{file_path}\\{number}\\{number}-1 КМЦ.docx")

    #Заполнение акта исследования второго реагента
    doc = DocxTemplate(f"{file_path}\\Исходный КМЦ 2.docx")
    if dop_acts[0]=='-':
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal2' : seal2,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number2': batch_number2,'manufacturer':manufacturer}
    else:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal2' : seal2,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number2': batch_number2,'manufacturer':manufacturer}
    doc.render(context)
    doc.save(f"{file_path}\\{number}\\{number}-2 КМЦ.docx")