# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
"""

import sgtk

class ConnectionHandler(object):
    """
    """
    
    @staticmethod
    def open_connection(app):
        """
        """
        handler = ConnectionHandler(app)
        handler.do_open_connection()
 
    @staticmethod
    def connect(app):
        """
        """
        handler = ConnectionHandler(app)
        handler.do_connect()
        
    
    def __init__(self, app):
        """
        """
        self._app = app
    

    def do_connect(self):
        """
        """
        try:
            p4_fw = sgtk.platform.get_framework("tk-framework-perforce")
            p4_fw.connection.connect()
        except:
            self._app.log_exception("Failed to connect!")
            return
    
    def do_open_connection(self):
        """
        """
        try:
            p4_fw = sgtk.platform.get_framework("tk-framework-perforce")
            p4_fw.connection.connect_with_dialog()
        except:
            self._app.log_exception("Failed to Open Connection dialog!")
            return        
        
        
        