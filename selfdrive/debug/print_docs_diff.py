print("Start of print_docs_diff")
import os
from common.basedir import BASEDIR
print(BASEDIR)

# TODO: if we can easily parse the stars from the generated CARS.md file, do that instead
os.environ['PYTHONPATH'] = os.path.join(BASEDIR, "openpilot_pr_base")
print(os.environ['PYTHONPATH'])

from openpilot_pr_base.selfdrive.car import docs as old_docs
from selfdrive.car import docs as new_docs
from selfdrive.car.docs_definitions import Column

print('All car info:')
# print(old_docs.get_all_car_info())


def pretty_row(row, exclude=[Column.MAKE, Column.MODEL]):
  return {k.value: v for k, v in row.items() if k not in exclude}


old_car_info = {f'{i.make} {i.model}': i for i in old_docs.get_all_car_info()}
new_car_info = {f'{i.make} {i.model}': i for i in new_docs.get_all_car_info()}

added_cars = set(new_car_info)  #  - set(old_car_info)
deleted_cars = set(old_car_info) - set(new_car_info)

if len(added_cars):
  print('This PR adds these car entries:')
  for k in added_cars:
    car_info = new_car_info[k]
    print('{}: {}'.format(k, pretty_row(car_info.row)))

if len(deleted_cars):
  print('This PR removes these car entries:')
  for k in deleted_cars:
    car_info = old_car_info[k]
    print('{}: {}'.format(k, pretty_row(car_info.row)))

# for new_car, new_car_info in new_car_info.items():
#   if new_car in old_car_info and new_car.row != old_car_info[new_car].row:
#     print('Diff in car: {}'.format(new_car.row))

# diffs = []
# for car_info in get_all_car_info():
