def what_is_my_sign(day, month):
    zodiac_signs = {
        (3, 21): 'Aries',
        (4, 21): 'Taurus',
        (5, 22): 'Gemini',
        (6, 22): 'Cancer',
        (7, 23): 'Leo',
        (8, 23): 'Virgo',
        (9, 24): 'Libra',
        (10, 24): 'Scorpio',
        (11, 23): 'Sagittarius',
        (12, 22): 'Capricorn',
        (1, 21): 'Aquarius',
        (2, 20): 'Pisces',
    }
    
    for date in zodiac_signs:
        if (month == date[0] and day > date[1]) or (month == date[0] + 1 and day < date[1]):
            return zodiac_signs[date]
    
    pass

print(what_is_my_sign(29, 1))