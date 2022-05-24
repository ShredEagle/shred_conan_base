import os
from conans import ConanFile

def shred_basic_layout(conanfile, src_folder="."):
    conanfile.folders.build = "build_ws"
    if conanfile.settings.get_safe("build_type"):
        conanfile.folders.build = os.path.join(conanfile.folders.build, str(conanfile.settings.build_type))
    conanfile.folders.generators = os.path.join(conanfile.folders.build, "conan")
    conanfile.cpp.build.bindirs = ["."]
    conanfile.cpp.build.libdirs = ["."]
    conanfile.folders.source = src_folder

class ShredBaseConanFile(object):
    def layout(self):
        shred_basic_layout(self)

class ShredConanBase(ConanFile):
    name = "shred_conan_base"
    version = "0.0.1"
