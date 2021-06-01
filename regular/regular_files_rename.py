import shutil
import os
import re

date_pattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

for amer_file_name in os.listdir('./files'):
    mo = date_pattern.search(amer_file_name)
    if mo == None:
        continue
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)

    euro_file_name = before_part + day_part + '-' + \
        month_part + '-' + year_part + after_part

    abs_working_dir = os.path.abspath('./files')
    amer_file_name = os.path.join(abs_working_dir, amer_file_name)
    euro_file_name = os.path.join(abs_working_dir, euro_file_name)
    shutil.move(amer_file_name, euro_file_name)
