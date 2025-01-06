from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck


class logConnectionsCheck(BaseResourceCheck):
    def __init__(self):
        name = "log_connections must be enabled."
        id = "CKV_AZURE_david"
        supported_resources = ("azurerm_postgresql_flexible_server_configuration",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)
    
    def scan_resource_conf(self, conf):
        
        if conf.get('name', [None])[0] == "log_checkpoints":
            if conf.get('value', [None])[0] == "off":
                return CheckResult.PASSED
            return CheckResult.FAILED
        
        # if conf.get('name', [None])[0] == "log_disconnections":
        #     if conf.get('value', [None])[0] == "on":
        #         return CheckResult.PASSED
        #     return CheckResult.FAILED
        
        # if conf.get('name', [None])[0] == "connection_throttle.enable":
        #     if conf.get('value', [None])[0] == "on":
        #         return CheckResult.PASSED
        #     return CheckResult.FAILED
        
        # if conf.get('name', [None])[0] == "logfiles.retention_days":
        #     value = conf.get('value', [None]) [0]
        #     if value is not None and int(value) > 3:
        #         return CheckResult.PASSED
        #     return CheckResult.FAILED
        
        return None

check = logConnectionsCheck()
