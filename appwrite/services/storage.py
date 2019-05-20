from appwrite.service import Service


class Storage(Service):

    def list_files(self, search='', limit=25, offset=0, order_type='ASC'):
        """List Files"""
        pass

    def create_file(self, files, read="[]", write="[]", folder_id=''):
        """Create File"""
        pass

    def get_file(self, file_id):
        """Get File"""
        pass

    def delete_file(self, file_id):
        """Delete File"""
        pass

    def get_file_download(self, file_id):
        """Download File"""
        pass

    def get_file_preview(self, file_id, width=0, height=0, quality=100, background='', output=''):
        """Preview File"""
        pass

    def get_file_view(self, file_id, as=''):
        """View File"""
        pass
