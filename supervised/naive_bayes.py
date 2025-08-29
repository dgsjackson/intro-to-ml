#Emails
#(Contains errors, Contains links, Is it a scam?)
data = [("No", "No", "No"),
("Yes", "Yes", "Yes"),
("Yes", "Yes", "Yes"),
("No", "No", "No"),
("No", "Yes", "No"),
("Yes", "Yes", "Yes"),
("Yes", "No", "No"),
("No", "Yes", "No"),
("Yes", "No", "Yes"),
("No", "Yes", "No")]

def p_class(cls, data):
    total = len(data)
    count = len(list(filter(lambda x: x[-1] == cls, data)))
    return count/total

def p_point_given_class(point, cls, data):
    p_point = 1
    for i, val in enumerate(point):
        match = 0
        cls_total = 0
        for item in data:
            if item[-1] == cls:
                cls_total += 1
                if item[i] == val:
                    match += 1
        p_point *= match/cls_total
    return p_point

def classify(point, data):
    classes = set(x[-1] for x in data)
    prob_max = 0
    argmax_class = None
    for cls in classes:
        prob = p_point_given_class(point, cls, data) * p_class(cls, data)
        if argmax_class == None or prob > prob_max:
            argmax_class = cls
            prob_max = prob
    return argmax_class


print(classify(("No", "No"), data))
print(classify(("Yes", "Yes"), data))
print(classify(("Yes", "No"), data))
print(classify(("No", "Yes"), data))