"""
store main abstract behaviour for the resource 
"""
 
from abc import ABC, abstractclassmethod


class ResourceCredentialsValidator(ABC):
    """ Basic representation of resource credentials validator. """
    
    def __init__(self):
        self.resource_basic_url = None
        self.user_token = None
        self.user_id = None
    
    @classmethod
    def get_user_id(self):
        ...

    @classmethod
    def validate_credentials(self):
        ...


class ContentUploader(ABC):
    """ Basic representation of content uploader. """
    
    def __init__(self):
        self.resource_basic_url = None
        self.content_path = None
    
    @abstractclassmethod    
    def read_content(self):
        pass
    
    @abstractclassmethod    
    def publicsh_draft_content(self, data):
        pass
    
