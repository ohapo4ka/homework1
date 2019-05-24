def school_mean(school_data):
    score_sum = 0
    kid_num = 0
    for school_class in school_scores:
        for kid_score in school_class['scores']:
            score_sum += kid_score
            kid_num += 1

    return score_sum // kid_num

def class_mean(class_scores):
    score_sum = 0
    kid_num = 0
    for kid_score in class_scores:
        score_sum += kid_score
        kid_num += 1

    return score_sum // kid_num

school_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [3,3,5,2,2,5]},
    {'school_class': '4c', 'scores': [2,4,5,3,1,3,5,4]},
]

print('School mean score:', school_mean(school_scores))

for class_data in school_scores: 
    cls_name = class_data['school_class']
    cls_mean = class_mean(class_data['scores'])
    print('Mean for class', cls_name, ':', cls_mean)