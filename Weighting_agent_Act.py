from docxtpl import DocxTemplate
import datetime
import os
def wa():
    #Ввод данных
    file_path=str(input('Введите путь папки: '))
    date=str(input('Введите дату и время получения реагента: '))
    date_test_start=str(input('Введите дату начала испытаний: '))
    date_test_end=str(input('Введите дату окончания испытаний: '))
    number=str(input('Введите входящий номер реагента: '))
    customer=str(input('Введите название фирмы заказчика: '))
    receiving=str(input('Введите способ получения:'))
    brand_of_reagent=str(input('Введите марку реагента:'))
    batch_number=str(input('Введите номер партии: '))
    manufacturer=str(input('Введите название фирмы производителя:'))
    well=str(input('Введите место отбора пробы: '))
    date_on_well=str(input('Введите дату и время отбора пробы: '))
    seal=str(input('Введите номер пломбы: '))
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
    doc = DocxTemplate(f"{file_path}\\Исходный_Акт приёма утяжелитель.docx")
    if dop_acts[0]=='-':
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,
                    'date_on_well' : date_on_well,'seal' : seal,'doc1':'-','doc2':'-',
                    'batch_number':batch_number,'brand_of_reagent':brand_of_reagent}
    elif len(dop_acts)==1:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,
                    'date_on_well' : date_on_well,'seal' : seal,'doc1':'-','doc2':'-',
                    'batch_number':batch_number,'brand_of_reagent':brand_of_reagent}
    else:
        context = {'date': date, 'number': number, 'customer': customer,
                   'receiving': receiving, 'well': well,
                   'date_on_well': date_on_well, 'seal': seal, 'doc1': '-', 'doc2': '-',
                   'batch_number': batch_number, 'brand_of_reagent': brand_of_reagent}
    doc.render(context)
    doc.save(f"{file_path}\\{number}\\{number} Акт приёма материалов.docx")


    #Заполнение акта исследования
    doc = DocxTemplate(f"{file_path}\\Исходный утяжелитель.docx")
    if dop_acts[0]=='-':
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal' : seal,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number': batch_number,'manufacturer':manufacturer}
    else:
        context = { 'date' : date,'number' : number,'customer' : customer,
                    'receiving' : receiving,'well' : well,'date_on_well' : date_on_well,
                    'seal' : seal,'now_date':date_now,'doc1':'-','date_test_start':date_test_start,
                    'date_test_end':date_test_end,'brand_of_reagent': brand_of_reagent,
                    'batch_number': batch_number,'manufacturer':manufacturer}
    doc.render(context)
    doc.save(f"{file_path}\\{number}\\{number} утяжелитель.docx")