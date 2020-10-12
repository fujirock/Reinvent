from utils.enums.component_specific_parameters_enum import ComponentSpecificParametersEnum

class SparseChemSpecificParametersEnum(ComponentSpecificParametersEnum):
    _SC_MODEL_PATH = "sc_model_path"
    _SC_CONFIG_FILE = "sc_config_file"
    _SC_MAC_CPUS = "sc_max_num_cpus"
    _SC_REF_HASH = "sc_ref_hash"
    _SC_MODEL_CONF = "sc_model_conf"
    _SC_TASK_IDS = "sc_task_ids"
    _SC_TASK_WEIGHTS = "sc_task_weights"

    # Need to stick to this pattern of getter/setter as the alternative more concise one cannot
    # be pickled for multiprocessing

    @property
    def SC_MODEL_PATH(self):
        return self._SC_MODEL_PATH

    @SC_MODEL_PATH.setter
    def SC_MODEL_PATH(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_CONFIG_FILE(self):
        return self._SC_CONFIG_FILE

    @SC_CONFIG_FILE.setter
    def SC_CONFIG_FILE(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_MAC_CPUS(self):
        return self._SC_MAC_CPUS

    @SC_MAC_CPUS.setter
    def SC_MAC_CPUS(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_REF_HASH(self):
        return self._SC_REF_HASH

    @SC_REF_HASH.setter
    def SC_REF_HASH(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_MODEL_CONF(self):
        return self._SC_MODEL_CONF

    @SC_MODEL_CONF.setter
    def SC_MODEL_CONF(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_TASK_IDS(self):
        return self._SC_TASK_IDS

    @SC_TASK_IDS.setter
    def SC_TASK_IDS(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")

    @property
    def SC_TASK_WEIGHTS(self):
        return self._SC_TASK_WEIGHTS

    @SC_TASK_WEIGHTS.setter
    def SC_TASK_WEIGHTS(self, value):
        raise ValueError("Do not assign value to a SparseChemSpecificParametersEnum field")
