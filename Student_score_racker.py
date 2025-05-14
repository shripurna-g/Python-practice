'''
Input: List of students and their scores (name-score pairs)
Store them in a dictionary
Print:
The top scorer(s)
The average score
All names with scores above the average
🔧 Practice:
Dictionaries
Loops
Conditionals
Aggregation
'''

def score_tracker(score_list):

    student_dict = dict(score_list)

    #sort by score
    sorted_by_score = dict(sorted(student_dict.items(), key=lambda item:item[1], reverse=True))

    #Top scorer
    print(f"Top scorer:{list(sorted_by_score.keys())[0]}")

    #Average score
    avg_score = sum(student_dict.values()) / len(student_dict)
    print(f"Average score: {avg_score}")

    #Students with above average scores

    pass

if __name__ == '__main__':

    student_scores = [["Student-A",78],
                      ["Student-B",64],
                      ["Student-C",32],
                      ["Student-D",93],
                      ]

    tracker = score_tracker(student_scores)

