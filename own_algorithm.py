def __compare_vectors(training_vector, test_vector):
    score = 0
    for i in range(0,len(training_vector)):
        score +=(training_vector[i] - test_vector[i])**2
    return score

def __classify_single_vector(training_vectors, test_vector, training_classifications):
    scores = []
    classifier = 0
    for vector in training_vectors:
        scores.append(__compare_vectors(vector, test_vector))
    for i in range(0,len(scores)):
        classifier += (scores[i] * training_classifications[i])
    if classifier > 0:
        return(-1)
    else:
        return(1)

def classify_multiple_vectors(training_vectors, test_vectors, training_classifications):
    classifiers = []
    for test_vector in test_vectors:
        classifiers.append(__classify_single_vector(training_vectors, test_vector, training_classifications))
    # for i in range(0,len(classifiers)-1):
    #     if classifiers[i] == -1:
    #         classifiers[i] = 0
    return classifiers

# print(classify_multiple_vectors([[0,0,0,0,0], [100,100,100,100,100]], [[1,1,1,1,1],[99,99,99,99,99]], [1,-1]))

# print(classify_single_vector([[0,0,0,0,0], [100,100,100,100,100]], [99,99,99,99,99], [1,-1]))

# print(compare_vectors([0,0,0,0,0], [2,2,2,2,2]))
