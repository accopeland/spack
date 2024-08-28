# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Dust(Package):
    """du + rust = dust. Like du but more intuitive."""

    homepage = "https://github.com/bootandy/dust"
    url = "https://github.com/bootandy/dust/archive/v0.7.5.tar.gz"

    maintainers("fangohr")

    license("Apache-2.0")

    version("1.1.1", sha256="98cae3e4b32514e51fcc1ed07fdbe6929d4b80942925348cc6e57b308d9c4cb0")
    version("1.1.0", sha256="2429b4ac76ad8520b99e7167dbb70c8e0088b5fad2c79f799e22b7d137d5fc33")
    version("1.0.0", sha256="34b72116ab6db9bdb97bc1e49dadf392a1619838204b44b0a4695539d54ffbe8")
    version("0.9.0", sha256="70efd66e662fcd93bbc6cf2f8c3104a1de7e52090f709e9040a34bdc7c72ea9c")
    version("0.8.6", sha256="feede818e814011207c5bfeaf06dd9fc95825c59ab70942aa9b9314791c5d6b6")
    version("0.8.5", sha256="0eff8b1b4e53f5ec2ffc0cfb9e5500bf27a9a5a68b1ff115c98facb4d20a7b7c")
    version("0.8.4", sha256="611f2da80ef5b1d4423bcda159a65e9436692357b686b91b1dd8245a76eed589")
    version("0.8.3", sha256="1e07203546274276503a4510adcf5dc6eacd5d1e20604fcd55a353b3b63c1213")
    version("0.8.2", sha256="890972fbf1a7f0a336c0f20e1e9ecc756c62d3debd75d22b596af993a3d8af01")
    version("0.8.1", sha256="9f3b5e93c62bb54139479ac4396549fc62389ac9a7d300b088cdf51cd0e90e22")
    version("0.7.5", sha256="f892aaf7a0a7852e12d01b2ced6c2484fb6dc5fe7562abdf0c44a2d08aa52618")

    depends_on("rust")

    sanity_check_is_file = [join_path("bin", "dust")]

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", ".")

    @run_after("install")
    def check_install(self):
        print("Attempt to call 'dust' with '--version'")
        dust = Executable(join_path(self.spec["dust"].prefix.bin, "dust"))
        output = dust("--version", output=str.split)
        print("stdout received fromm dust is '{}".format(output))
        assert "Dust " in output

    def test_run(self):
        """check dust can execute (with option '--version')"""
        dust = which(self.prefix.bin.dust)
        out = dust("--version", output=str.split, error=str.split)
        assert "Dust " in out
