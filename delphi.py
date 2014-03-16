import collections
import numpy
import operator
import random


criteria = [

    'data analysis',
    'highload development',
    'network stack',
    'databases',
    'programming language profficiency',

    'microbiology',
    'virilory',
    'immunology',
    'bacteriology',
    'protein structures',

    'leadership',
    'scientific reputation',
    'time management',
    'management skills',
    'estimate salary',

]

alternatives = [
                'Tony',
                'Rudolf',
                'Kate',
                'Lee Ann',
                'Mustafa',
               ]

experts = [
           'Bill', 
           'Bob', 
           'Mary', 
           'Jack', 
           'Dave',
          ]


def generate_criteria_weights(criteria):

    criteria_weights = collections.defaultdict(dict)
    criteria_weights_mean = {}
 
    for criterion in criteria:
        for expert in experts:
            criteria_weights[criterion][expert] = random.randint(1, 100)
        criteria_weights_mean[criterion] = numpy.mean(criteria_weights[criterion].values())

    return criteria_weights_mean

def generate_expert_scores():

    expert_scores = collections.defaultdict(lambda : collections.defaultdict(dict))

    for criterion in criteria:
        for alternative in alternatives:
            for expert in experts:                    
                expert_scores[criterion][alternative][expert] = random.randint(0, 10)
   
    return expert_scores    


def get_average_scores(expert_scores):

    average_scores = collections.defaultdict(dict)

    for criterion in criteria:
        for alternative in alternatives:
            scores = expert_scores[criterion][alternative].values()

            average_scores[criterion][alternative] = numpy.mean(scores)

    return average_scores

def normalize_expert_scores(expert_scores, average_scores):

    total_distance_before = 0 
    total_distance_after = 0 

    for criterion in criteria:
        for alternative in alternatives:
            for expert in experts:       

                expert_score = expert_scores[criterion][alternative][expert]      
                average_scrore = average_scores[criterion][alternative]       

                distance_from_mean = average_scrore - expert_score
                total_distance_before += abs(distance_from_mean)

                smooth_coefficient = distance_from_mean / random.randint(1, 10)
                expert_scores[criterion][alternative][expert] += smooth_coefficient
                total_distance_after += abs(distance_from_mean) - abs(smooth_coefficient)
    
    return expert_scores

def get_result_rating(average_expert_scores, criteria_weights):

    result_rating = collections.defaultdict(float)
  
    for alternative in alternatives:
        for criterion in criteria:
            expert_score = average_expert_scores[criterion][alternative]
            criteria_weight = criteria_weights[criterion]
            result_rating[alternative] += expert_score * criteria_weight

    return sorted(result_rating.iteritems(), key=operator.itemgetter(1), reverse=True)


if __name__ == '__main__':

    criteria_weights = generate_criteria_weights(criteria)
                                    
    expert_scores = generate_expert_scores()
    average_scores = get_average_scores(expert_scores)

    #First round of normalization/smoothing
    normalized_expert_scores_1 = normalize_expert_scores(expert_scores, average_scores)
    average_scores = get_average_scores(normalized_expert_scores_1)

    #Second round of normalization/smoothing
    normalized_expert_scores_2 = normalize_expert_scores(normalized_expert_scores_1, average_scores)
    average_scores = get_average_scores(normalized_expert_scores_2)

    result_rating = get_result_rating(average_scores, criteria_weights)

    print('Best choice is {0}.\nRating:'.format(result_rating[0][0]))
    for alternative, rating in result_rating:
        print('    {0} {1}'.format(alternative, int(rating)))

        


 