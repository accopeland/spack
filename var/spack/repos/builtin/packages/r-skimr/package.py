# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RSkimr(RPackage):
    """A simple to use summary function that can be used with pipes and displays nicely in the console. The default summary statistics may be modified by the user as can the default formatting. Support for data frames and vectors is included, and users can implement their own skim methods for specific object types as described in a vignette. Default summaries include support for inline spark graphs. Instructions for managing these on specific operating systems are given in the "Using skimr" vignette and the README."""

    homepage = "https://cran.r-project.org/web/packages/skimr/index.html"
    cran = "skimr"

    version("2.1.5", sha256="06f3a3ea1d16f48f7b91312182bbe05bfa25af5116985a3723ff9acadd168387")
    version("2.1.4", sha256="6f6e65a43d764f9689f03617747f56e5804a7bf93fc83a3e86522344e051d5f5")
    version("2.1.3", sha256="41510c514ce65c86642b0165e3fb03b0fad17e58eb95f29a00a6261568a0050b")
    version("2.1.2", sha256="f0e70fe8c6ebd365fbb091fd0f3805749a6e73f77eca595c0a343058926bcc14")
    version("2.1.1", sha256="500758a029d6c8fd3e5d1463e91cebe9420cd1be1349824c2bb7b8f295f45a5c")
    version("2.1", sha256="256eafa98cd810e185b29f2fee63184d8eb17a6e8591ffcef30878c4ff3288a1")
    version("2.0.2", sha256="93d2d4684423c737f965030d1436887f295836c87665c37bf0efd7f0ea73208c")
    version("2.0.1", sha256="e9d28b6d2b339e75a46bab5e9c584fe227558b02acc19f2a4e98b3e914e599ed")
    version("2.0", sha256="e441f115412a699377e1c13d0b49ec74d73fcf3f5e25ba6db8b2b121a9e63b8b")
    version("1.0.7", sha256="693aa28a1390941000e1051cd68bcfe1fe86241b19dee3a831ff54d23792757d")

    depends_on("r", when="@3.1.2:", type=("build", "run"))
    depends_on("r-cli", type="run")
    depends_on("r-dplyr", when="@0.8.0:", type="run")
    depends_on("r-knitr", when="@1.2:", type="run")
    depends_on("r-magrittr", when="@1.5:", type="run")
    depends_on("r-pillar", when="@1.6.4:", type="run")
    depends_on("r-purrr", type="run")
    depends_on("r-repr", type="run")
    depends_on("r-rlang", when="@0.3.1:", type="run")
    #depends_on("r-stats", type="run")
    depends_on("r-stringr", when="@1.1:", type="run")
    depends_on("r-tibble", when="@2.0.0:", type="run")
    depends_on("r-tidyr", when="@1.0:", type="run")
    depends_on("r-tidyselect", when="@1.0.0:", type="run")
    depends_on("r-vctrs", type="run")

    def configure_args(self):
        args = []
        return args
