def make_car(manufacturer_name, model_name, **car_info):
    """Builds dictionary containing info about a car"""
    car_info['manufacturer'] = manufacturer_name
    car_info['model'] = model_name
    return car_info

car = make_car('honda', 'accord', color='grey', horsepower='dunno')
print(car)