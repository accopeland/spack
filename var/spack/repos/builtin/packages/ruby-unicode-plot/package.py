# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RubyUnicodePlot(RubyPackage):
    """Plot your data by Unicode characters"""

    homepage = "https://github.com/red-data-tools/unicode_plot.rb"
    #url = "https://github.com/red-data-tools/unicode_plot.rb.git"
    url = "https://rubygems.org/downloads/unicode_plot-0.0.5.gem"

    # maintainers("github_user1", "github_user2")

    license("MIT")

    version("0.0.5", sha256="91ce6237bca67a3b969655accef91024c78ec6aad470fcddeb29b81f7f78f73b", expand=False)

    depends_on("ruby-enumerable-statistics", type=("build", "run")) # @2.0.1
