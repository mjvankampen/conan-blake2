from conans import ConanFile, CMake, tools


class Blake2Conan(ConanFile):
    name = "blake2"
    version = "20190808"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Blake2 here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "arch"
    options = {"shared": [True, False],
               "enable_xop": [True, False],
               "isa_extension": ["Best", "SSE2", "SSSE3", "SSE4.1", "AVX", "AVX2", "Neon", "None"]}
    default_options = {"shared": "False", "enable_xop": "False", "isa_extension": "Best"}
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="blake2")
        git.clone("https://github.com/mjvk/BLAKE2.git","cmake")
        git.checkout("8c4d6b9efb55fa8731fab851aec7ff160a3eb5b9")
    
    def configure(self):
        if self.settings.compiler == "Visual Studio":
            raise Exception("Visual studio is not supported as a compiler as it misses some POSIX features, try mingw on windows!")
            
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["ISA_EXTENSION"] = self.options.isa_extension
        cmake.definitions["XOP_ENABLED"] = self.options.enable_xop
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

