from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import TEST_DATA
import random
import pytest


def load_stack_info(stack=None):
    stacks = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPX_SUPPORT_TEST_STACK))
    if stack is not None:
        target_stack = stack
    else:
        target_stack = stacks["default_stack"]
    for stack in stacks["stacks"]:
        if stack["stack"] == target_stack:
            return stack