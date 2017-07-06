import random

def ask_user_for_sample_size():
    print("What size of sample (%) do you want to use for training the algorithm? Put in a number between 0 and 100")
    user_input = input(">>")
    while float(user_input) > 100 or float(user_input)<0:
        print("Input must be between 0 and 100")
        print("What percentage of the data do you want to use for training the algorithm? Put in a number between 0 and 100")
        user_input = input(">>")

    return float(user_input)/100

def sample_data(sample_size, category1_training, category2_training):
    sample_size1 = sample_size * len(category1_training)
    sample_size2 = sample_size * len(category2_training)
    sample_category1 = random.sample(category1_training, int(sample_size1))
    sample_category2 = random.sample(category2_training, int(sample_size2))
    return [sample_category1, sample_category2]
