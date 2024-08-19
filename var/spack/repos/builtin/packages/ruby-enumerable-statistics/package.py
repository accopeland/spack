# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class RubyEnumerableStatistics(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://rubygems.org/gems/enumerable-statistics"
    url = "https://rubygems.org/downloads/enumerable-statistics-2.0.8.gem"

    # maintainers("github_user1", "github_user2")

    license("MIT")

    version("2.0.8", sha256="1e0d69fcdec1d188dd529e6e5b2c27e8f88029c862f6094663c93806f6d313b3", expand=False)

    #depends_on("ruby@3", type=("build", "run"))
