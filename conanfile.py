from conans import ConanFile, CMake, tools, os

class BlackholeConan(ConanFile):
    name = "Blackhole"
    version = "1.9.0"
    description = ""
    license = "https://github.com/3Hren/blackhole/blob/master/LICENSE"
    url = "https://github.com/3Hren/blackhole"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    lib_short_name = "blackhole"
    archive_name = "{0}-{1}".format(lib_short_name, version)
    requirements = "Boost.Thread/1.65.1@bincrafters/stable"
            
    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.url, self.version))
                
    def build(self):
        cmake = CMake(self)
        conan_magic_lines = r"""project(${LIBRARY_NAME})
    INCLUDE(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    CONAN_BASIC_SETUP()"""
        tools.replace_in_file(os.path.join(self.archive_name, "CMakeLists.txt"), r"project(${LIBRARY_NAME})", conan_magic_lines)
        cmake = CMake(self)
        cmake.configure(source_dir=self.archive_name)
        cmake.build()
    
    def package(self):
        include_dir = os.path.join(self.archive_name, 'include')
        self.copy(pattern="*.h", dst="include", src=include_dir)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
            
    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
