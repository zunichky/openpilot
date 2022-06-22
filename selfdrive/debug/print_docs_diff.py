import os
from common.basedir import BASEDIR

os.environ['PYTHONPATH'] = os.path.join(BASEDIR, "openpilot_pr_base")

from openpilot_pr_base.selfdrive.car.docs import get_all_car_info

print(get_all_car_info())

