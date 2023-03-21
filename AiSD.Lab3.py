# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
# заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# 10.	Формируется матрица F следующим образом: если в С количество минимальных чисел в нечетных столбцах в области 2 больше,чем количество максимальных чисел в
#четных строках в области 1, то поменять в С симметрично области 1 и 2 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
#После чего вычисляется выражение: A*А+(K*AT). Выводятся по мере формирования А, F и все матричные операции последовательно.

#                       4
#   D   E           3       2
#   C   B               1

from math import ceil, floor
import random

def printMatrix(matrix): # функция вывода матрицы
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
          print ("{:5d}".format(matrix[i][j]), end="")
      print()
n = int(input('Введите число число N, большее или равное 5: '))
while n < 5:  # ошибка в случае введения слишком малого порядка матрицы
    n = int(input("Введите число N, большее или равное 5: "))
k = int(input('Введите число число K: '))

# ниже создание и вывод матрицы А(N,N) c диапазоном значений от -10 до 10
A = [ [ random.randint(-10, 10) for j in range(n)] for i in range(n) ]
print('\nМатрица А:')
printMatrix(A)

F = [[elem for elem in raw] for raw in A]         # создание матрицы F, на данный момент равной матрице A
F_dump = [[elem for elem in raw] for raw in F]        # резервная копия матрицы F для дальнейших операций

submatrix_order = ceil(n/2) # определение порядка подматрицы

# вычленяем матрицу C через срезы
# проверка n на четность нужна для корректного среза(чтобы матрица А делилась на равные 4 подматрицы)

if n %2 == 0:
    c = [F[i][submatrix_order:n] for i in range(0,submatrix_order)]
else:
    c = [F[i][submatrix_order-1:n] for i in range(0, submatrix_order)]

#ниже ищем кол-во минимальных чисел в нечётных столбцах в области 2 в С
minlist = []
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i >= j) and ((i + j + 1) >= submatrix_order) and (j+1) % 2 != 0:
            minlist.append(c[i][j])
minvalue = minlist.count(min)

#ниже ищем количество максимальных чисел в четных строках в области 1
maxlist = []
for i in range(submatrix_order):
    for j in range(submatrix_order):
        if (i <= j) and ((i + j + 1) >= submatrix_order) and (i+1) % 2 == 0:
            maxlist.append(c[i][j])
maxvalue = maxlist.count(max)
#ниже выполнение инструкций по условию
if minvalue > maxvalue:
    print('\nВ C кол-во минимальных чисел в нечётных столбцах в области 2 больше, \n'
          'чем кол-во максимальных чисел в чётных строках в '
          'области 1, значит меняем\nв C симметрично области 1 и 2 места\n')
    for i in range(submatrix_order, n):
        for j in range(submatrix_order, n):
            if i >= j:
                F_dump[i][j] = F[submatrix_order - j - 1][submatrix_order - i -1]
    print("Матрица F:")
    F = F_dump
    printMatrix(F)
else:
    print('\nВ С кол-во минимальных чисел в нечётных столбцах в области 2 меньше или равно, \n'
          'чем кол-во максимальных чисел в чётных строках в '
          'области 1, значит меняем\nв C и Е местами несимметрично\n')
    for i in range(ceil(n / 2), n):
        for j in range(ceil(n / 2)):
            F[i][j] = F_dump[i - floor(n / 2)][floor(n / 2) + j]
            F[i - floor(n / 2) ][floor(n / 2) + j] = F_dump[i][j]
    print("Матрица F:")
    printMatrix(F)


AA = [[0 for i in range(n)] for j in range(n)] #заготовка под результат умножения матрицы А на саму себя
for i in range(n):      #производим умножение двух матриц
    for j in range(n):
        for l in range(n):
            AA[i][j] += A[i][l] * A[l][j]
print('\nРезультат умножения матрицы А на матрицу А:')
printMatrix(AA)

AT = [[0 for i in range(n)] for j in range(n)]          # заготовка под транспонированную матрицу A
for i in range(n):  # произведение транспонирования матрицы A
    for j in range(n):
        AT[i][j] = A[j][i]
print("\nМатрица A транспонированная:")
printMatrix(AT)

KAT = [[0 for i in range(n)] for j in range(n)]
for i in range(n):  # умножегие транспонированной матрицы А на кэфф К
    for j in range(n):
        KAT[i][j] = AT[i][j] * k
print("\nРезультат умножения коэффициента K на матрицу AT:")
printMatrix(KAT)

matrix_result = [[0 for i in range(n)] for j in range(n)]      # заготовка под конечный результат
for i in range(n):              #разность между двух матриц
    for j in range(n):
        matrix_result[i][j] = AA[i][j] + KAT[i][j]
print("\nКонечный результат AA + KAT:")
printMatrix(matrix_result)

print("\nРабота программы завершена")



