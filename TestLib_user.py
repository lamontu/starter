# -*- coding: utf-8 -*-

from imp import reload
import TestLib

print(TestLib.lib_func(120))
print()

reload(TestLib)
