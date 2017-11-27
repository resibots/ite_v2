import sys
sys.path.insert(0, sys.path[0]+'/waf_tools')

import os
import limbo

def options(opt):
    opt.load('hexapod_dart')
    opt.load('dart')
    opt.load('boost')

def configure(conf):
    conf.load('hexapod_dart')
    conf.load('dart')
    conf.load('boost')
    # In boost you can use the uselib_store option to change the variable the libs will be loaded
    boost_var = 'BOOST_ITE'
    conf.check_boost(lib='regex system serialization', min_version='1.46', uselib_store=boost_var)

    conf.check_dart()
    conf.check_hexapod_dart()

    conf.env.LIB_THREADS = ['pthread']


def build(bld):
    hexa_libs = 'HEXAPOD_CONTROLLER DART EIGEN BOOST_ITE BOOST LIMBO LIBCMAES NLOPT '
    hexa_graphic_libs = 'DART_GRAPHIC ' + hexa_libs

    cxxflags = bld.get_env()['CXXFLAGS']


    if bld.get_env()['BUILD_GRAPHIC'] == True:
      limbo.create_variants(bld,
                            source = 'hexapod.cpp',
                            uselib_local = 'limbo',
                            uselib = hexa_graphic_libs,
                            includes=". ../../src ../ ./include",
                            cxxflags = cxxflags,
                            variants = ['GRAPHIC'])

    limbo.create_variants(bld,
                          source = 'hexapod.cpp',
                          uselib_local = 'limbo',
                          uselib = hexa_libs,
                          includes=". ../../src ../ ./include",
                          cxxflags = cxxflags,
                          variants = ['SIMU'])

