"""
store main abstract behaviour for the resource 
"""
 
from abc import ABC, abstractclassmethod
    
class ResourceCredentialsValdiator(ABC):
    """ Basic representation of resource credentials validator. """
    
    def __init__(self):
        self.resource_basic_url = None
        self.user_token = None
        self.user_id = None
        
    @abstractclassmethod
    def get_credentials_from_machine_environment(self):
        pass
    
    @abstractclassmethod
    def get_user_id(self):
        pass
    
    @abstractclassmethod
    def validate_credentials(self):
        pass

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
    
