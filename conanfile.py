from conans import ConanFile, CMake, tools


class Blake2Conan(ConanFile):
    name = "blake2"
    version = "20190808"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Blake2 here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        git = tools.Git(folder="blake2")
        git.clone("https://github.com/mjvk/BLAKE2.git","cmake")
        git.checkout("f4b17ee47227e8ef7347846abef4c160511d1880")
    
    def configure(self):
        if self.settings.compiler == "Visual Studio":
            raise Exception("Visual studio is not supported as a compiler as it misses some POSIX features, try mingw on windows!")
            
    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="blake2")
        return cmake
        
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["blake2"]

