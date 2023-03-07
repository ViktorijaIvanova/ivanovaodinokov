#После заполнения списков появляется меню с выбором действий:
#• Узнать, вводя название города,  сколько в нем жителей;
#• Отобразить в алфавитном порядке список городов и количество жителей;
#• Ввести кол-во жителей и вывести на экран название города, в котором наиболее приближенное  кол-во жителей;
#• Найти города в которых живет меньше, чем n жителей ;
#• Свой вариант.
def linnad():
    # Создаем пустые списки
    cities = []
    populations = []
    
    # Просим пользователя ввести количество городов
    num_linnad = int(input("sisetage arv linnas: "))
    
    # Заполняем списки данными о городах и населении
    for i in range(num_linnad):
        linnad = input(f"sisetage nimi linna{i+1}: ")
        inimesed = int(input(f"sisetage arvad inimesed{linnad}: "))
        linnad.append(linnad)
        inimesed.append(inimesed)
    
    # Возвращаем заполненные списки
    return linnad, inimesed


    
    
    
def Käkk(käsk: int, linnad: int, linnas:list, inimesed: list)->any:
    """
    """
    if käsk == "1":
        linnad= input("sisetage nimi linnas:")
        print("Inimesed {inimesed}, linnad, {linnad}")
    if käsk == "2":
        sorted_tuple=sorted(linnas.items())
        print(sorted_tuple)
    if käsk == "3":
        print(Enamus_pop)#bolshe
    if käsk == "4":
        num = int(input("Sisesta rahvaarv:"))
        print(less)
    if käsk== "5":
        täht=input("sisetage esimene täht:")
        sõna= [sõna for sõna in linnad if sõna.startswith(täht)]
    print(sõna)

def Enamus_pop(linnas):
    """
    """
    big = 0
    town = ''
    for city, pop in linnas.items():
        if pop > big:
            big = pop
            town = city 
    return f'{town} : {big}'

def less(cities, num):
    """
    """
    my_dic = {}
    for city, pop in cities.items():
        if pop < num:
            my_dic[city] = pop
    return my_dic

