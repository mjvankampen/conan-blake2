from conans import ConanFile, CMake, tools


class Blake2Conan(ConanFile):
    name = "blake2"
    version = "20190928"
    license = "MIT"
    author = "mjvk"
    url = "https://github.com/mjvk/conan-blake2"
    homepage = "https://blake2.net"
    description = "Libraries and executables to generate a blake2 hash"
    topics = ("blake2", "hashing", "<and here>")
    settings = "os", "compiler", "arch"
    options = {"shared": [True, False],
                "build_b2sum": [True, False],
               "enable_xop": [True, False],
               "isa_extension": ["Best", "SSE2", "SSSE3", "SSE4.1", "AVX", "AVX2", "Neon", "None"]}
    default_options = {"shared": "False", "enable_xop": "False", "isa_extension": "Best", "build_b2sum": "False"}
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="blake2")
        git.clone("https://github.com/mjvk/BLAKE2.git","cmake")
        git.checkout("66a29ca6c5f413564ac1a138c315a5fd4954d14e")
    
    def configure(self):
        if self.settings.compiler == "Visual Studio" and self.options.build_b2sum == True:
            raise Exception("Visual studio is not supported as a compiler as it misses some POSIX features, try mingw on windows!")
            
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ISA_EXTENSION"] = self.options.isa_extension
        cmake.definitions["XOP_ENABLED"] = self.options.enable_xop
        cmake.definitions["BUILD_B2SUM"] = self.options.build_b2sum
        cmake.configure(source_folder="blake2")
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["blake2"]

