#list1 = [[1,2,3],[4,5,6],[7,8,9]]

#or i in list1:
#	for j in list1:
#list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#for i in range(3):
 #   for j in range(3):
  #      print(list1[i][j])

list1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
rc = input("enter row, and coloum respectively(number 1-3)")
for i in range(3):
    for j in range(3):
        print(list1[i][j], end=' ')
    print()  # Newline after each row

