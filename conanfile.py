from conans import ConanFile, CMake, tools
import os


class Blake2Conan(ConanFile):
    name = "blake2"
    version = "20200315"
    license = "MIT"
    author = "mjvk"
    url = "https://github.com/mjvk/conan-blake2"
    homepage = "https://blake2.net"
    description = "Libraries and executables to generate a blake2 hash"
    topics = ("blake2", "hashing", "<and here>")
    settings = "os", "compiler", "arch"
    options = {"shared": [True, False],
                "b2sum": [True, False],
                "blake2": [True, False],
               "enable_xop": [True, False],
               "isa_extension": ["Best", "SSE2", "SSSE3", "SSE4.1", "AVX", "AVX2", "Neon", "None"],
               "options_from_context": [True, False]}
    default_options = {"shared": "False", "enable_xop": "False", "isa_extension": "Best", "b2sum": "True", "blake2": "True", "options_from_context": "True"}
    generators = "cmake"
    _cmake = None
    
    def configure(self):
        # Detect if host or build context
        if self.options.options_from_context:
            settings_target = getattr(self, 'settings_target', None)
            self.options.b2sum = settings_target is not None
            self.options.blake2 = settings_target is None
        del self.options.options_from_context    
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd
        
    def source(self):
        git = tools.Git(folder="blake2")
        git.clone("https://github.com/mjvk/BLAKE2.git","cmake")
        git.checkout("b4809c7454de692e803af74c62c66d67b0999113")
            
    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.definitions["ISA_EXTENSION"] = self.options.isa_extension
        self._cmake.definitions["XOP_ENABLED"] = self.options.enable_xop
        self._cmake.definitions["BUILD_B2SUM"] = self.options.b2sum
        self._cmake.configure(source_folder="blake2")
        return self._cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        if self.options.blake2:
            self.cpp_info.libs = ["blake2b", "blake2bp", "blake2s", "blake2sp", "blake2xb", "blake2xs"]
        if self.options.b2sum:
            self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))

