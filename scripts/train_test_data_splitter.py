print("working")

def hello():
    print("hi")

def ask_user_for_split():
    print("What percentage of the data do you want to use for training the algorithm? Put in a number between 0 and 100")
    user_input = input(">>")
    while float(user_input) > 100 or float(user_input)<0:
        print("Input must be between 0 and 100")
        print("What percentage of the data do you want to use for training the algorithm? Put in a number between 0 and 100")
        user_input = input(">>")

    return float(user_input)/100


def split_data(split,category1,category2):

    split1 = round(len(category1)*split)
    category1_train = category1[:split1]
    category1_test = category1[split1:]

    split2 = round(len(category2)*split)
    category2_train = category2[:split2]
    category2_test = category2[split2:]

    return [[category1_train,category1_test],[category2_train,category2_test]]
