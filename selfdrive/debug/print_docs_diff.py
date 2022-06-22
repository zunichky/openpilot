print("Start of print_docs_diff")
import os
from common.basedir import BASEDIR
print(BASEDIR)

os.environ['PYTHONPATH'] = os.path.join(BASEDIR, "openpilot_pr_base")
print(os.environ['PYTHONPATH'])

from openpilot_pr_base.selfdrive.car.docs import get_all_car_info

print('All car info:')
print(get_all_car_info())
