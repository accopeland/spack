# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RubyEnumerableStatistics(RubyPackage):
    """Library providing statistics features for Enumerable"""

    homepage = "https://github.com/mrkn/enumerable-statistics"
    url = "https://rubygems.org/downloads/enumerable-statistics-2.0.8.gem"
    git = "https://github.com/mrkn/enumerable-statistics.git"  # https://github.com/mrkn/enumerable-statistics/releases/tag/v2.0.8 commit=44d6876 tag="v2.0.8"

    license("MIT")

    version("2.0.8", sha256="1e0d69fcdec1d188dd529e6e5b2c27e8f88029c862f6094663c93806f6d313b3", expand=False)
    #version("2.0.8", tag="v2.0.8")
