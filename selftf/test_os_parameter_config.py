# use random generation
# list_setting = None

list_setting = [
#    ("NLP_transformer_XL", 1, 1, 1, 1, "dry_run",
# """{'worker_num': 5, 'ps_num': 5, 'place_pruned_graph': 0, 'optimizer': 2, 'n_partition': 1, 'max_folded_constant_in_bytes': 20725760, 'learning_rate': 0.001, 'intra_op_parallelism_threads': 14, 'inter_op_parallelism_threads': 15, 'infer_shapes': 1, 'global_jit_level': 1, 'enable_bfloat16_sendrecv': 1, 'do_function_inlining': 0, 'do_common_subexpression_elimination': 0, 'batch_size': 32, 'OMP_NUM_THREADS': 1, 'MKL_DYNAMIC': 1, 'KMP_BLOCKTIME': 357, 'KMP_AFFINITY_type': 0, 'KMP_AFFINITY_respect': 0, 'KMP_AFFINITY_permute': 1, 'KMP_AFFINITY_offset': 0, 'KMP_AFFINITY_granularity': 1}""")
#    ("NLP_bert", 1, 1, 1, 1, "mltuner",
# """{'num_cpu_per_node': 17, 'num_gpu_per_node': 0, 'num_mem_per_node': 67302588416, "ps_num": 1, "worker_num": 9, "intra_op_parallelism_threads": 1, "inter_op_parallelism_threads": 1, "n_partition": 1, "learning_rate": 0.001, "batch_size": 16, "optimizer": 2, "do_common_subexpression_elimination": 0, "max_folded_constant_in_bytes": 10485760, "do_function_inlining": 0, "global_jit_level": 0, "infer_shapes": 1, "enable_bfloat16_sendrecv": 0, "place_pruned_graph": 0,"KMP_AFFINITY_granularity": 1,"KMP_AFFINITY_respect": 1,"KMP_AFFINITY_type": 0,"KMP_AFFINITY_permute": 0,"KMP_AFFINITY_offset": 0,"KMP_BLOCKTIME": 200,"OMP_NUM_THREADS": 1,"MKL_DYNAMIC": 1}""")
## tf default config:
#    ("resnet50", 1, 1, 1, 1, "mltuner",
# """{'num_cpu_per_node': 17, 'num_gpu_per_node': 0, 'num_mem_per_node': 67302588416, 'worker_num': 9, 'ps_num': 1, 'place_pruned_graph': 0, 'optimizer': 2, 'n_partition': 1, 'max_folded_constant_in_bytes': 10485760, 'learning_rate': 0.001, 'intra_op_parallelism_threads': 0, 'inter_op_parallelism_threads': 0, 'infer_shapes': 0, 'global_jit_level': 0, 'enable_bfloat16_sendrecv': 0, 'do_function_inlining': 0, 'do_common_subexpression_elimination': 0, 'batch_size': 16, 'OMP_NUM_THREADS': 1, 'MKL_DYNAMIC': 1, 'KMP_BLOCKTIME': 200, 'KMP_AFFINITY_type': 0, 'KMP_AFFINITY_respect': 1, 'KMP_AFFINITY_permute': 0, 'KMP_AFFINITY_offset': 0, 'KMP_AFFINITY_granularity': 1}"""),
## pytorch default config:
#    ("pytorch_squeezenet", 1, 1, 1, 1, "mltuner",
# """{'num_cpu_per_node': 17, 'num_gpu_per_node': 0, 'num_mem_per_node': 67302588416, 'worker_num': 9, 'ps_num': 1, 'optimizer': 0, 'learning_rate': 0.001, 'intra_op_parallelism_threads': 2, 'inter_op_parallelism_threads': 2, 'batch_size': 1024, 'OMP_NUM_THREADS': 1, 'MKL_DYNAMIC': 1, 'KMP_BLOCKTIME': 200, 'KMP_AFFINITY_type': 0, 'KMP_AFFINITY_respect': 1, 'KMP_AFFINITY_permute': 0, 'KMP_AFFINITY_offset': 0, 'KMP_AFFINITY_granularity': 1}""")
# """
# {'ps_num': 8, 'intra_op_parallelism_threads': 13, 'inter_op_parallelism_threads': 11, 'do_common_subexpression_elimination': 0, 'max_folded_constant_in_bytes': 70629295, 'do_function_inlining': 1, 'global_jit_level': 2, 'infer_shapes': 1, 'enable_bfloat16_sendrecv': 1, 'place_pruned_graph': 1, 'KMP_AFFINITY_granularity': 1, 'KMP_AFFINITY_respect': 0, 'KMP_AFFINITY_type': 1, 'KMP_AFFINITY_permute': 10, 'KMP_AFFINITY_offset': 6, 'KMP_BLOCKTIME': 293, 'OMP_NUM_THREADS': 7, 'MKL_DYNAMIC': 0, 'MXNET_CPU_WORKER_NTHREADS': 3, 'MXNET_CPU_NNPACK_NTHREADS': 2, 'MXNET_MP_WORKER_NTHREADS': 3, 'MXNET_EXEC_ENABLE_INPLACE': 0, 'MXNET_EXEC_NUM_TEMP': 3, 'MXNET_GPU_MEM_POOL_TYPE': 0, 'MXNET_ENGINE_TYPE': 1, 'MXNET_KVSTORE_USETREE': 1, 'MXNET_UPDATE_ON_KVSTORE': 0, 'MXNET_CPU_TEMP_COPY': 4, 'MXNET_GPU_PARALLEL_RAND_COPY': 4}
# """)
## mxnet default config:
   ("mxnet_resnet20", 1, 1, 1, 1, "mltuner",
"""{'num_cpu_per_node': 17, 'num_gpu_per_node': 0, 'num_mem_per_node': 67302588416, 'worker_num': 9, 'ps_num': 1, 'learning_rate': 0.001, 'batch_size': 64, 'OMP_NUM_THREADS': 1, 'MKL_DYNAMIC': 1, 'KMP_BLOCKTIME': 200, 'KMP_AFFINITY_type': 0, 'KMP_AFFINITY_respect': 1, 'KMP_AFFINITY_permute': 0, 'KMP_AFFINITY_offset': 0, 'KMP_AFFINITY_granularity': 1, 'MXNET_CPU_WORKER_NTHREADS': 1, 'MXNET_CPU_NNPACK_NTHREADS': 4, 'MXNET_MP_WORKER_NTHREADS': 1, 'MXNET_EXEC_ENABLE_INPLACE': 1, 'MXNET_EXEC_NUM_TEMP': 1, 'MXNET_GPU_MEM_POOL_TYPE': 0, 'MXNET_ENGINE_TYPE': 1, 'MXNET_KVSTORE_USETREE': 0, 'MXNET_UPDATE_ON_KVSTORE': 1, 'MXNET_CPU_TEMP_COPY': 4, 'MXNET_GPU_PARALLEL_RAND_COPY': 4}""")

   # ("densenet121", 1, 1, 1, 1, "mltuner",
   #  """{"ps_num": 1, "worker_num": 35, "intra_op_parallelism_threads": 0, "inter_op_parallelism_threads": 0, "n_partition": 1, "learning_rate": 0.001, "batch_size": 100, "optimizer": 2, "do_common_subexpression_elimination": 0, "max_folded_constant_in_bytes": 0, "do_function_inlining": 0, "global_jit_level": 0, "infer_shapes": 0, "enable_bfloat16_sendrecv": 0, "place_pruned_graph": 0}"""
   #  ),
   # ("densenet121", 1, 1, 1, 1, "dry_run",
   #  """{"ps_num": 1, "worker_num": 35, "intra_op_parallelism_threads": 0, "inter_op_parallelism_threads": 0, "n_partition": 1, "learning_rate": 0.001, "batch_size": 100, "optimizer": 2, "do_common_subexpression_elimination": 0, "max_folded_constant_in_bytes": 0, "do_function_inlining": 0, "global_jit_level": 0, "infer_shapes": 0, "enable_bfloat16_sendrecv": 0, "place_pruned_graph": 0}"""
   #  ),
   # ("inceptionv3", 1, 1, 1, 1, "mltuner",
   #  """{"ps_num": 1, "worker_num": 35, "intra_op_parallelism_threads": 0, "inter_op_parallelism_threads": 0, "n_partition": 1, "learning_rate": 0.001, "batch_size": 100, "optimizer": 2, "do_common_subexpression_elimination": 0, "max_folded_constant_in_bytes": 0, "do_function_inlining": 0, "global_jit_level": 0, "infer_shapes": 0, "enable_bfloat16_sendrecv": 0, "place_pruned_graph": 0}"""
   #  ),
   # ("inceptionv3", 1, 1, 1, 1, "dry_run",
   #  """{"ps_num": 1, "worker_num": 35, "intra_op_parallelism_threads": 0, "inter_op_parallelism_threads": 0, "n_partition": 1, "learning_rate": 0.001, "batch_size": 100, "optimizer": 2, "do_common_subexpression_elimination": 0, "max_folded_constant_in_bytes": 0, "do_function_inlining": 0, "global_jit_level": 0, "infer_shapes": 0, "enable_bfloat16_sendrecv": 0, "place_pruned_graph": 0}"""
   #  )
]
# use random generation
# list_setting = None
##Testing for best worst
# list_setting = [
#     # LR Best
#     # ("LR", 10, 108, 10, 108, "dry_run",
#     # "{"
#     # "'optimizer': 3, "
#     # "'learning_rate': 2.4e-05, "
#     # "'batch_size': 4560,"
#     # "'ps_num': 18, "
#     # "'worker_num': 18, "
#     # "'intra_op_parallelism_threads': 12, "
#     # "'inter_op_parallelism_threads': 4, "
#     #
#     # "'do_common_subexpression_elimination': 1,"
#     # "'max_folded_constant_in_bytes': 55952477,"
#     # "'do_function_inlining': 0, "
#     # "'global_jit_level': 2, "
#     # "'infer_shapes': 1,"
#     # "'place_pruned_graph': 1, "
#     # "'enable_bfloat16_sendrecv': 0} "),
#     ("CNN", 10, 108, 10, 108, "dry_run",
#     #CNN Best
#     "{"
#     "'optimizer': 2, "
#     "'learning_rate': 0.0001, "
#     "'batch_size': 100,"
#     "'ps_num': 5, "
#     "'worker_num': 31, "
#     "'intra_op_parallelism_threads': 13, "
#     "'inter_op_parallelism_threads': 3, "
#     "'do_common_subexpression_elimination': 0,"
#     "'max_folded_constant_in_bytes': 42785965,"
#     "'do_function_inlining': 0, "
#     "'global_jit_level': 2, "
#     "'infer_shapes': 0,"
#     "'place_pruned_graph': 1, "
#     "'enable_bfloat16_sendrecv': 1} ")
# ]
## reconfig scheme 0 test
# list_setting = [
# ("LR", 10, 108, 10, 108, 0.000024, 4560, "bo", 36 - 22, 7, "RMSProp", "selftf_reconfig_0"),
# ("SVM_BIG", 10, 108, 10, 108, 0.00008, 2590, "bo", 36-14, 10, "SGD", "selftf_reconfig_0"),
# ("CNN", 10, 108, 10, 108, 0.000100, 100, "bo", 36-22, 7, "Adam", "selftf_reconfig_0"),
# ("ALEXNET_IMAGENET", 10, 10, 10, 10, 0.02, 32, "bo", 36 - 22, 7, "RMSProp_Imagenet", "selftf_reconfig_0"),
# ]

#CNN Reconfiguration test

#
# list_setting = [
#     ("CNN", 10, 108, 10, 108, 0.000100, 100, "bo", 36-22, 7, "Adam", "selftf_reconfig_0"),
#     ("LR", 10, 108, 10, 108, 0.000024, 4560, "bo", 36 - 22, 7, "RMSProp", "selftf_reconfig_0"),
#     ("ALEXNET_IMAGENET", 10, 10, 10, 10, 0.02, 32, "bo", 36 - 22, 7, "RMSProp_Imagenet", "selftf_reconfig_0"),
# ]
#
# list_setting = [
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36 - 22, 7, "RMSProp", "selftf_reconfig_0")
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36 - 22, 7, "RMSProp", "selftf")
# ]
#
# list_setting = [
#     ("CNN", 10, 108, 10, 108, 0.000100, 100, "bo", 36-22, 7, "Adam", "selftf_reconfig_0"),
#     ("CNN", 10, 108, 10, 108, 0.000100, 100, "bo", 36-22, 7, "Adam", "selftf"),
# ]


# #INCEPTION BO Testing
# list_setting = [
#     ("INCEPTION", 10, 200, 10, 200, 0.045, 10, "bo", 36-31, 3, "RMSProp", "dry_run"),
#     ("INCEPTION", 10, 200, 10, 200, 0.045, 10, "bo", 36-31, 14, "RMSProp", "dry_run"),
#     ("INCEPTION", 10, 200, 10, 200, 0.045, 10, "bo", 36-29, 1, "RMSProp", "dry_run"),
#     ("INCEPTION", 10, 200, 10, 200, 0.045, 10, "bo", 36-30, 1, "RMSProp", "dry_run"),
# ]

# #LR BO Testing
# list_setting = [
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36-22, 7, "RMSProp", "dry_run"),
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36-26, 10, "RMSProp", "dry_run"),
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36-20, 7, "RMSProp", "dry_run"),
#     ("LR", 10, 200, 10, 200, 0.000024, 4560, "bo", 36-34, 6, "RMSProp", "dry_run"),
# ]

# #SVM BO Testing
# list_setting = [
#     ("SVM", 10, 200, 10, 200, 0.00008, 2590, "bo", 36-14, 10, "SGD", "dry_run"),
#     ("SVM", 10, 200, 10, 200, 0.00008, 2590, "bo", 36-12, 15, "SGD", "dry_run"),
#     ("SVM", 10, 200, 10, 200, 0.00008, 2590, "bo", 36-15, 8, "SGD", "dry_run"),
#     ("SVM", 10, 200, 10, 200, 0.00008, 2590, "bo", 36-15, 15, "SGD", "dry_run"),
#
# ]
# list_setting = [
#
#     # BaseRun for LR
#
#     ("CNN", 10, 200, 10, 200, 0.00006, 1500, "bo", 29, 4, "Momentum", "selftf"),
#     ("CNN", 10, 200, 10, 200, 0.00009, 3900, "bo", 18, 9, "RMSProp", "selftf"),
#     ("CNN", 10, 200, 10, 200, 0.00007, 2700, "bo", 19, 5, "Adam", "selftf"),
#     ("CNN", 10, 200, 10, 200, 0.00007, 2700, "bo", 19, 5, "Adam", "selftf"),
#     ("CNN", 10, 200, 10, 200, 0.00008, 2700, "bo", 19, 5, "Adam", "selftf"),
# ]

#     ("SVM", 10, 72, 10, 72, 0.00008, 2700, "bo", 19, 5, "Adam", "dry_run"),
#     ("SVM", 10, 72, 10, 72, 0.00004, 2700, "bo", 19, 5, "Adam", "dry_run"),
#     ("SVM", 10, 72, 10, 72, 0.00008, 2700, "bo", 19, 5, "Adam", "dry_run"),
#     #
#     # ("LR", 20, 36, 20, 36, 0.0001, 2000, "bo"),
#     # ("LR", 20, 36, 20, 36, 0.0001, 2000, "bo"),
#     # ("LR", 20, 36, 20, 36, 0.0001, 2000, "bo"),
#
#     # ("CNN", 20, 36, 20, 36, 0.0002, 100, "bo"),
#     # ("CNN", 20, 36, 20, 36, 0.0002, 100, "bo"),
#     # ("CNN", 20, 36, 20, 36, 0.0002, 100, "bo"),
#
#     # Fig 14
#     # ("LR", 20, 60, 100, 500, 0.0001, 2000, "old"),
#
#     # Fig 13
#     # ("LR", 10, 60, 100, 500, 0.001, 1000, "bo"),
#     # ("LR", 15, 60, 100, 500, 0.001, 1000, "bo"),
#     # ("LR", 25, 60, 100, 500, 0.001, 1000, "bo"),
#     # ("LR", 20, 40, 100, 500, 0.001, 1000, "bo"),
#     # ("LR", 20, 80, 100, 500, 0.001, 1000, "bo"),
#     # ("LR", 20, 100, 100, 500, 0.001, 1000, "bo"),
#
#     # # Fig 15 SVM
#     # ("SVM", 20, 60, 100, 500, 0.00005, 2000, "bo"),
#     # ("SVM", 20, 60, 100, 500, 0.00015, 2000, "bo"),
#     # ("SVM", 20, 60, 100, 500, 0.00020, 2000, "bo"),
#     #
#     # # Fig 15 CNN
#     # ("CNN", 20, 60, 100, 500, 0.0002, 100, "bo"),
#     # ("CNN", 20, 60, 100, 500, 0.0003, 100, "bo"),
#     # ("CNN", 20, 60, 100, 500, 0.0004, 100, "bo"),
#     #
#     # # Fig 16 SVM
#     # ("SVM", 20, 60, 100, 500, 0.0001, 200, "bo"),
#     # ("SVM", 20, 60, 100, 500, 0.0001, 300, "bo"),
#     # ("SVM", 20, 60, 100, 500, 0.0001, 400, "bo"),
#     #
#     # # Fig 16 CNN
#     # ("CNN", 20, 60, 100, 500, 0.0001, 2500, "bo"),
#     # ("CNN", 20, 60, 100, 500, 0.0001, 3000, "bo"),
#     # ("CNN", 20, 60, 100, 500, 0.0001, 3500, "bo"),
#
# ]
