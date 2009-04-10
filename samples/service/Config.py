#------------------------------------------------------------------------------
# Config.py
#   This file defines information about the service. The following four
# attributes are expected to be defined and if they are not an exception will
# be thrown when attempting to create the service:
#
#   NAME
#       the name to call the service with one %s place holder that will be used
#       to identify the service further.
#
#   DISPLAY_NAME
#       the value to use as the display name for the service with one %s place
#       holder that will be used to identify the service further.
#
#   MODULE_NAME
#       the name of the module implementing the service.
#
#   CLASS_NAME
#       the name of the class within the module implementing the service. This
#       class should accept no parameters in the constructor. It should have a
#       method called "Initialize" which will accept the configuration file
#       name. It should also have a method called "Run" which will be called
#       with no parameters when the service is started. It should also have a
#       method called "Stop" which will be called with no parameters when the
#       service is stopped using the service control GUI.
#------------------------------------------------------------------------------

NAME = "cx_FreezeSampleService%s"
DISPLAY_NAME = "cx_Freeze Sample Service - %s"
MODULE_NAME = "ServiceHandler"
CLASS_NAME = "Handler"
