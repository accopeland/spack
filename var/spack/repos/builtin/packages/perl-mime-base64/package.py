# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PerlMimeBase64(PerlPackage):
    """"Encoding and decoding of base64 strings"""

    homepage = "https://metacpan.org/pod/MIME::Base64"
    url = "https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/MIME-Base64-3.16.tar.gz"

    version("3.16", sha256="77f73d6f7aeb8d33be08b0d8c2617f9b6c77fb7fc45422d507ca8bafe4246017")

    depends_on("perl", type=("run"))

    def configure_args(self):
        args = []
        return args
