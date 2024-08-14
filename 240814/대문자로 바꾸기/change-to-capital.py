lower = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
upper = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
for _ in range(5):
    arr = input().split()
    for i in range(3):
        print(upper[lower.index(arr[i])], end=" ")
    print()