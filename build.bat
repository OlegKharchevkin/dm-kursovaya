@mkdir build
@cd build
@title Cmake
@cmake .. -G "Unix Makefiles"  
@cmake --build . --config Release 
@cd ..
@title Pyinstallers
@pyinstaller make/make.spec --log-level WARN 