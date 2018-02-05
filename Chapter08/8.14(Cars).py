def make_car(manufacturer, model , **other_info):
    car = {}
    car['Manufacturer'] = manufacturer
    car['Model'] = model

    for key , value in other_info.items():
        car[key] = value
    return car

car = make_car('subaru' , 'outback', color = 'blue' , tow_package =True)
print(car)