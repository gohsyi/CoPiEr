include(CTest)

#
# define the instance sets
#
# semicolon '\;' is used to split an instance and its optimal objective value
# For infeasible instances, '+infinity' is used (or '-infinity' in case of maximization)
#

#
# CP instances
#
set(instances_CP
    "instances/CP/linking.cip\;2"
    "instances/CP/j301_2.cip\;47"
    "instances/CP/disj_conj_rail.cip\;1324.43557422969"
    "instances/CP/stein27_super.cip\;1"
    )

set(settings_default
    "default"
)
#
# settings to run a whole test. In order to run a sub-suite, use -R
#
set(settings_MIP
    "default"
    "separating_off"
    "presolving_off"
    "heuristics_off"
    "separating_fast"
    "presolving_fast"
    "heuristics_fast"
    "separating_aggressive"
    "presolving_aggressive"
    "heuristics_aggressive"
    "allaggr"
    "cgmip"
    "cgmipstrong"
    "convertinttobin"
    "fullstrongbfs"
    "indicatorlogicor"
    "mostinf"
    "distribution"
    "oddcylcelift"
    "oddcylce"
    "oddcylceliftheur"
    "indicatorsepa"
    "proporbit"
    "allfull"

    "cgmipviol"
#    "dynamic"
    "heurlprows"
    "intobj"
#    "nologicor"
    "presolaggr"
    "pscost"
    "setppclifting"
    "xorsepaparity"
#    "cloud"
#    "feaspump20"
    "indicatoralterlp"
    "leastinf"
    "presolfast"
    "randomhybrid"
    "uct_breadth_dualval"
    "alldisp"
    "vbcvisualization"
    "bakvisualization"
    "solvingphases"
)

set(settings_MINLP
    "default"
    "undercover1"
    "undercover2"
    "rensnlp"
    "nlpdiving2"
    "nlpdiving3"
    "nlpdiving1-relprop"
#    "nlpdivingsolvesubmip"
    "nlpdiving4"
)
set(settings_Bivariate
    "default"
    "bivariate"
)

#
# Indicator instances
#
set(instances_Indicator
    "instances/Indicator/mcf128-4-1.lp\;14"
    "instances/Indicator/mcf64-4-1.lp\;10"
)


#
# MIP instances
#
set(instances_MIP
    "instances/MIP/bell5.mps\;8966406.49"
    "instances/MIP/blend2.mps\;7.598985"
#    "instances/MIP/dcmulti.mps\;188182"
    "instances/MIP/egout.mps\;568.1007"
    "instances/MIP/enigma.mps\;0"
    "instances/MIP/flugpl.mps\;1201500"
    "instances/MIP/gt2.mps\;21166"
    "instances/MIP/lseu.mps\;1120"
    "instances/MIP/MANN_a9.clq.lp\;16"
    "instances/MIP/misc03.mps\;3360"
    "instances/MIP/p0033.osil\;3089"
    "instances/MIP/p0548.mps\;8691"
    "instances/MIP/rgn.mps\;82.1999974"
    "instances/MIP/stein27.fzn\;18"
    "instances/MIP/stein27_inf.lp\;+infinity"
    "instances/MIP/vpm2.fzn\;13.75"
    )

#
# add additional ZIMPL instances if the configuration uses ZIMPL
#
if(ZIMPL AND ZIMPL_FOUND)

list(APPEND
    instances_Indicator
    "/instances/Indicator/indicatortest.zpl\;-2"
    "../check/instances/Indicator/mcf64-4-1.zpl\;10"
    )
#
# this instance was part of the original coverage tests. However, it causes
# a significant overhead without providing relevant benefit.
#
#list(APPEND
#    instances_MIP
#    "instances/MIP/rocII_2_11.zpl\;+4.61527698552400e+00"
#    )

endif()
#
# MINLP instances
#
set(instances_MINLP
    "instances/MINLP/bip_cross_min.10.10.10.1.pip\;1"
    "instances/MINLP/circle.cip\;4.57424778"
    "instances/MINLP/ex1266.mps\;16.3"
    "instances/MINLP/m3.osil\;37.8"
    "instances/MINLP/parincQuadratic.osil\;49920.5564"
    "instances/MINLP/tltr.mps\;48.0666666667"
    )
set(instances_Bivariate
    "instances/Bivariate/st_qpk1.osil\;-3"
    "instances/Bivariate/nvs01.osil\;12.4696688"
   )
#
# PseudoBoolean instances
#
set(instances_PseudoBoolean
    "instances/PseudoBoolean/factor-mod-size=9-P0=67-P1=349-P2=67-P3=499-P4=79-P5=347-P6=307-B.opb\;3"
    "instances/PseudoBoolean/normalized-bsg_10_4_5.opb\;-4"
    "instances/PseudoBoolean/normalized-mds_10_4_3.opb\;2"
    "instances/PseudoBoolean/normalized-mds_50_25_5.opb\;3"
    "instances/PseudoBoolean/normalized-t2001.13queen13.1111218308.opb\;+infinity"
    "instances/PseudoBoolean/normalized-t2001.13queen13.1110976730--soft-33-100-0.wbo\;4"
    "instances/PseudoBoolean/wheel010.lap.opb.pre.cip\;25"
    )

#
# Semicontinuous instances
#
set(instances_Semicontinuous
#    "instances/Semicontinuous/meanvarxsc.lp\;14.36918"
    "instances/Semicontinuous/semicon1.mps\;1.1"
    )
#
# SAT instance(s)
#
set(instances_SAT
    "instances/SAT/bart10.shuffled.cnf\;0"
    )

#
# SOS instances
#
set(instances_SOS
    "instances/SOS/findRoot.lp\;1.0"
    "instances/SOS/pcu_0.01.lp\;0.167527525"
    "instances/SOS/pcu_0.1.lp\;0.185145653"
    "instances/SOS/sparse2.lp\;26.0"
    "instances/SOS/tpesc.lp\;54027.1672208127"
    )

#
# Orbitope instances
#
set(instances_Orbitope
    "instances/Orbitope/packorb_1-FullIns_3.cip\;28"
    "instances/Orbitope/partorb_1-FullIns_3.cip\;4"
    )

#
# available reader file extensions for SCIP readers
#
set(scip_reader_extensions
    "cip"
    "gms"
    "ppm"
    "pbm"
    "ccg"
#    "opb"
    "pip"
    "rlp"
#    "mps"
    "lp"
    )

#
# add a test to build the SCIP binary that all further tests depend on
#
add_test(NAME scip-build
        COMMAND ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target scip
        )

#
# avoid that several build jobs try to concurrently build the SCIP library
# note that this ressource lock name is not the actual libscip target
#
set_tests_properties(scip-build
                    PROPERTIES
                        RESOURCE_LOCK libscip
                    )


#
# macro to split an instance into its relevant information
# - path
# - optval
# - basename
#
macro(split_instance instance)
    list(GET instance 0 path)
    list(GET instance 1 optval)
    get_filename_component(basename ${path} NAME)
endmacro(split_instance)

macro(add_instancetests instances settings prefix)
#
# loop over the instances
#
    foreach(instance ${${instances}})
        split_instance(instance)
        #
        # loop over all settings
        #
        foreach(setting ${${settings}})
            #
            # treat the instance as a tuple (list) of two values
            #
            add_test(NAME ${prefix}-${setting}-${basename}
                    COMMAND $<TARGET_FILE:scip> -f ${PROJECT_SOURCE_DIR}/check/${path} -s ${PROJECT_SOURCE_DIR}/coverage/settings/${setting}.set -o ${optval} ${optval}
                    )
            set_tests_properties(${prefix}-${setting}-${basename}
                                PROPERTIES
                                    PASS_REGULAR_EXPRESSION "Validation         : Success"
                                    DEPENDS scip-build
                                )
        endforeach(setting)
    endforeach(instance)
endmacro(add_instancetests)

add_instancetests(instances_CP settings_default "CP")
add_instancetests(instances_Indicator settings_default "Indicator")
add_instancetests(instances_MIP settings_MIP "MIP")
add_instancetests(instances_MINLP settings_MINLP "MINLP")
add_instancetests(instances_Bivariate settings_Bivariate "Bivariate")
add_instancetests(instances_PseudoBoolean settings_default "PseudoBoolean")
add_instancetests(instances_Semicontinuous settings_default "Semicontinuous")
add_instancetests(instances_SAT settings_default "SAT")
add_instancetests(instances_SOS settings_default "SOS")
add_instancetests(instances_Orbitope settings_default "Orbitope")

#
# test writing and reading solutions
#
foreach(instance ${instances_MINLP})
    split_instance(instance)
    #
    # configure the batch file for this test by substituting placeholders in the in.file
    #
    configure_file(interactiveshell/solutiontest.bat.in interactiveshell/solutiontest-${basename}.bat)
        add_test(NAME MINLP-solutiontest-${basename}
                COMMAND $<TARGET_FILE:scip> -b ${PROJECT_BINARY_DIR}/check/interactiveshell/solutiontest-${basename}.bat
                )
        set_tests_properties(MINLP-solutiontest-${basename}
                            PROPERTIES
                                PASS_REGULAR_EXPRESSION "Validation         : Success"
                                DEPENDS scip-build
                            )
endforeach(instance)


#
# test writing and reading from and to different file extensions for MIP
#
foreach(instance ${instances_MIP})
    split_instance(instance)
    foreach(extension ${scip_reader_extensions})
        #
        # configure the batch file for this test by substituting placeholders in the in.file
        #
        configure_file(interactiveshell/readertest.bat.in interactiveshell/readertest-${extension}-${basename}.bat)
        add_test(NAME MIP-readertest-${extension}-${basename}
                COMMAND $<TARGET_FILE:scip> -b ${PROJECT_BINARY_DIR}/check/interactiveshell/readertest-${extension}-${basename}.bat
                )
        set_tests_properties(MIP-readertest-${extension}-${basename}
                            PROPERTIES
                                PASS_REGULAR_EXPRESSION "Validation         : Success"
                                DEPENDS scip-build
                            )
    endforeach(extension)
endforeach(instance)

#
# add tests for the tpi
#
if(NOT ${TPI} STREQUAL "none")
    foreach(instance ${instances_MIP})
    split_instance(instance)
        #
        # configure the batch file for this test by substituting placeholders in the in.file
        #
        configure_file(interactiveshell/concurrentsolve.bat.in interactiveshell/concurrentsolve-${basename}.bat)
        add_test(NAME MIP-concurrentsolve-${basename}
                COMMAND $<TARGET_FILE:scip> -b ${PROJECT_BINARY_DIR}/check/interactiveshell/concurrentsolve-${basename}.bat
                )
        set_tests_properties(MIP-concurrentsolve-${basename}
                            PROPERTIES
                                PASS_REGULAR_EXPRESSION "Validation         : Success"
                                DEPENDS scip-build
                            )
    endforeach(instance)
endif()

#
# add tests that read partial solutions
#
foreach(instance ${instances_MIP})
    split_instance(instance)
    #
    # if there is a partial solution file in mipstarts, we add a test
    #
    if( EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/mipstarts/${basename}.mst" )
        #
        # configure the template batch file and store it under the binary (build) directory
        #
        configure_file(interactiveshell/mipstarts.bat.in interactiveshell/MIP-mipstart-${basename}.bat)

        #
        # add test that executes the configured batch file and greps the validation expression
        #
        add_test(NAME MIP-mipstart-${basename}
                COMMAND $<TARGET_FILE:scip> -b interactiveshell/MIP-mipstart-${basename}.bat
                )
        set_tests_properties(MIP-mipstart-${basename}
                            PROPERTIES
                                PASS_REGULAR_EXPRESSION "Validation         : Success"
                                DEPENDS scip-build
                            )
    endif()
endforeach(instance)

#
# interactive shell test.
# We substitute first path placeholders in the .in file, which creates a new file under the binary directory
# Then run SCIP to execute the list of commands defined there.
#
set(shell_tmp_dir ${PROJECT_BINARY_DIR}/check/temp)
file(MAKE_DIRECTORY ${shell_tmp_dir})

configure_file(interactiveshell/interactiveshell.bat.in interactiveshell/interactiveshell.bat)

add_test(NAME interactiveshell
        COMMAND $<TARGET_FILE:scip> -b ${PROJECT_BINARY_DIR}/check/interactiveshell/interactiveshell.bat
        )
set_tests_properties(interactiveshell
                    PROPERTIES
                        PASS_REGULAR_EXPRESSION "increased branching priority of new binary variables"
                        DEPENDS scip-build
                    )

add_custom_target(check
                COMMAND ${CMAKE_CTEST_COMMAND} -R "-default" --schedule-random
                DEPENDS scip
                )
