from visa_approval.logger import logging
from visa_approval.exception import visaapprovalException
import sys

logging.info("Wellcome to our custom logger")


try:
    a = 2/0
except Exception as e:
    raise visaapprovalException(e, sys)