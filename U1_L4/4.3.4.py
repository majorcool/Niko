def define_city(city,country="DE"):
    if city == "Beijing" and country == "China":
        return 'YES'
    return 'NO'
print(define_city("Beijing","China"))
print(define_city("IDK"))
print(define_city("IDK2"))