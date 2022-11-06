#coding:utf-8

from time import sleep

#pour les fonction d'ajustement de nombres binaires, on pourrait factoriser ça en une seule fonction avec un paramêtre en plus 
#mais je pense pas que ça soit nécessaire pour ton devoir

def adjust_binary_number_size(a: list, required_size):
    """
    ajoute des 0 à la fin du nombre binaire (le nom de la fonction est donc un peu mal choisi mais bref)
    """
    if len(a) != required_size:
        for i in range(required_size - len(a)):
            a.append(0)
    return a

def adjust_size_deb(a: list, required_size):
    if len(a) != required_size:
        for i in range(required_size - len(a)):
            a.insert(0, 0) #met des 0 au debut de la liste 
    return a


def addition_bit(a, b):
    """
    addition de deux nombres binaires de longueur 1, on retourne aussi la retenue 
    0 + 0 = 0
    0 + 1 = 1
    1 + 0 = 1
    1 + 1 = 0 (avec 1 en retenue)    
    """
    result = a + b
    if result == 2:
        return (0, 1)
    else:
        return (result, 0)

def addition_binaire(a, b):
    """
    addition de deux nombres binaires de taille quelconque
    """
    if len(a) != len(b):
        if len(a) > len(b):
            b = adjust_size_deb(b, len(a))
        else:
            a = adjust_size_deb(a, len(b))
    retenue = 0
    result = []
    print(a, "+", b) #tu peux l'enlever c'est juste pour debugger
    for i in range(len(a)-1, -1, -1): #au lieu de retourner je parcours juste la liste à l'envers lol

        bit_result = addition_bit(a[i], b[i])
        print(i, " : ", a[i], "+", b[i], "({})".format(retenue), "=",  bit_result) #tu peux l'enlever c'est juste pour debugger
        #gestion de la retenue
        bit_retenue = addition_bit(bit_result[0], retenue)
        result.insert(0, bit_retenue[0])
        if i != 0: #on modifie pas la retenue à la fin
            retenue = bit_result[1]
    result.insert(0, retenue)
    return result


def multiplication_binaire(a, b):
    operation_list = [] #creation de la liste d'operations intermédiaires
    for bit_i in range(len(b)-1, -1, -1):
        multiplied_a = [i*b[bit_i] for i in a] #on peut le faire avec un vrai for mais je trouve que c'est plus joli comme ça
        multiplied_a = adjust_binary_number_size(multiplied_a, len(a) + (len(b)-1)-bit_i)
        operation_list.append(multiplied_a)
    
    #addition des lignes intermédiaires:
    while len(operation_list) != 1:
        sleep(0.5)
        print(operation_list) #tu peux l'enlever c'est juste pour debugger
        operation_list[0] = addition_binaire(operation_list[0], operation_list[1])
        operation_list.pop(1)
    
    return operation_list[0]

def main():
    """
    on récupère deux nombres binaires sous forme de listes
    """
    nmb1 = eval(input("nombre binaire 1 >> "))
    nmb2 = eval(input("nombre binaire 2 >> "))

    print(multiplication_binaire(nmb1, nmb2))

main()