#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class BlackholeConan(ConanFile):
    name = "blackhole"
    version = "1.9.0"
    description = "Blackhole is an attribute-based logger with strong focus on performance"
    url = "https://github.com/bincrafters/conan-blackhole"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = (
        "Boost.Thread/1.65.1@bincrafters/stable", 
        "Boost.System/1.65.1@bincrafters/stable",
        "cmake_findboost_modular/0.1.0@bincrafters/stable"
     )
     
    def source(self):
        source_url = "https://github.com/3Hren/blackhole"
        extracted_dir = "{0}-{1}".format(self.name, self.version)
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        os.rename(extracted_dir, self.source_subfolder)
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        cmake.build()
        cmake.install()

    def package(self):
        include_dir = os.path.join(self.source_subfolder, 'include')
        self.copy(pattern="*.h", dst="include", src=include_dir)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
            
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
