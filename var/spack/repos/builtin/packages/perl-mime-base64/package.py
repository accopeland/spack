# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class PerlMimeBase64(PerlPackage):
    """functions to encode and decode strings into and from the base64 encoding specified in RFC 2045 - MIME (Multipurpose Internet Mail Extensions). 
    The base64 encoding is designed to represent arbitrary sequences of octets in a form that need not be humanly readable. 
    A 65-character subset ([A-Za-z0-9+/=]) of US-ASCII is used, enabling 6 bits to be represented per printable character."""

    homepage = "https://metacpan.org/pod/MIME::Base64::Perl"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GAAS/MIME-Base64-Perl-1.00.tar.gz"

    license("APACHE")

    version("1.00", sha256="f78c7ab62043518c31f733344a617ee22b04218c3ebadf796e73338acbb2f2ab")

    #depends_on("perl-module-build", type="build")
    #depends_on("perl", type="run")
