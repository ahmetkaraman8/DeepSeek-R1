def categorize_age(age):
    if 0 <= age < 18:
        return 'Çocuk'
    elif 18 <= age <= 35:
        return 'Genç Yetişkin'
    elif 36 <= age <= 60:
        return 'Yetişkin'
    elif age > 60:
        return 'Yaşlı'
