from appwrite.service import Service


class Database(Service):

    def list_collections(self, search='', limit=25, offset=0, order_type='ASC'):
        """List Collections"""
        pass

    def create_collection(self, name, read="[]", write="[]", rules="[]"):
        """Create Collection"""
        pass

    def list_documents(self, collection_id, filters="[]", offset=0, limit=50, order_field='$uid', order_type='ASC', order_cast='string', search='', first=0, last=0):
        """List Documents"""
        pass

    def create_document(self, collection_id, data, read="[]", write="[]", parent_document='', parent_property='', parent_property_type='assign'):
        """Create Document"""
        pass

    def delete_collection(self, collection_id):
        """Delete Collection"""
        pass

    def get_document(self, collection_id, document_id):
        """Get Document"""
        pass

    def update_document(self, collection_id, document_id, data, read="[]", write="[]"):
        """Update Document"""
        pass

    def delete_document(self, collection_id, document_id):
        """Delete Document"""
        pass
