# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Terracognita(Package):
    """
    Reads from existing public and private cloud
    providers (reverse Terraform) and generates your infrastructure as code on
    Terraform configuration
    """

    homepage = "https://github.com/cycloidio/terracognita"
    url = "https://github.com/cycloidio/terracognita/archive/refs/tags/v0.8.4.tar.gz"

    version("0.8.4", sha256="7420694805c3ab666591b9686958eb49e61452065546f0eb315f215c8241da84")
    version("0.8.3", sha256="7713e4b93528c294db86d008a2ab09ed841984ae2d1ea6f58c3703dab3a1b21e")
    version("0.8.2", sha256="7f7a75c357250e089e8d77b10e236bf6193e9d6d5ff26b697398d00f4550d9b4")
    version("0.8.1", sha256="dff35a6913d64dbd4e0595bd15d2f2029a8605a8bf0ba32a1de95f3236d85f1c")
    version("0.8.0", sha256="ff3bcfae00d24b551bd7a3c406cb20e5a552b37b7d3baa7e73318619bb3605d8")
    version("0.7.6", sha256="bc2361718cce62fb799f8470a268b9d2af7ab95a8337bbaa05d79f4b636482d1")
    version("0.7.5", sha256="980cba1cb914c32d60b1124a8755bdba4d44608397c614ccf0d94d7e16f7a99f")
    version("0.7.4", sha256="7027103c899d29b86dd1dc72e1e2d6d685bec6311673f7fbd31c8127ccd62c82")
    version("0.7.3", sha256="9ad6d29536cd5916a407070cad2ee5f469b3b3b9e8f4de64bf5bc37e23e5b94e")

    depends_on("go@1.17:", type="build")
    depends_on("gmake@3.81", type="build")

    phases = ["build", "install"]

    def setup_build_environment(self, env):
        # Point GOPATH at the top of the staging dir for the build step.
        env.prepend_path("GOPATH", self.stage.path)

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        make("install", "PREFIX=%s" % prefix)
