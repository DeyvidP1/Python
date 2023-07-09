def slope_style_score(score):
    score = score[1:-1]

    average_score = sum(score) / len(score)
    
    final_score = round(average_score, 2)

    return final_score
    final_score = slope_style_score(scores)
    print(final_score)
    pass



print (slope_style_score([60, 70, 80, 90, 100]))

