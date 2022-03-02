cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars) -> str:
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars) -> list:
    """return a list of matching models (original ordering)"""
    return [car_list[0] for car_list in cars.values()]


def get_all_matching_models(cars=cars, grep='trail') -> list:
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return sorted([car for car_list in cars.values() for car in car_list if grep.lower() in car.lower()])


def sort_car_models(cars=cars) -> dict:
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {name: sorted(car_list) for name, car_list in cars.items()}