#!/usr/bin/env python
# -*- coding: utf-8 -*-
from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(build_type=["Release"])
    builder.add_common_builds(pure_c=True)
    builder.run()