from ..service import Service
from urllib.parse import quote
from typing import Any, Dict, List, Optional, Union
from ..exception import AppwriteException
from appwrite.utils.deprecated import deprecated
from ..enums.embedding_model import EmbeddingModel
from ..models.embedding_list import EmbeddingList

class Embeddings(Service):

    def __init__(self, client) -> None:
        super(Embeddings, self).__init__(client)

    def create_text_embeddings(
        self,
        texts: List[str],
        model: Optional[EmbeddingModel] = None
    ) -> EmbeddingList:
        """
        Generate vector embeddings for an array of text using the selected embedding model. Use the returned vectors to power semantic search and similarity queries against your vector collections.
        

        Parameters
        ----------
        texts : List[str]
            Array of text to generate embeddings.
        model : Optional[EmbeddingModel]
            The embedding model to use for generating vector embeddings.
        
        Returns
        -------
        EmbeddingList
            API response as a typed Pydantic model
        
        Raises
        ------
        AppwriteException
            If API request fails
        """

        api_path = '/embeddings/text'
        api_params = {}
        if texts is None:
            raise AppwriteException('Missing required parameter: "texts"')


        api_params['texts'] = self._normalize_value(texts)
        if model is not None:
            api_params['model'] = self._normalize_value(model)

        response = self.client.call('post', api_path, {
            'X-Appwrite-Project': self.client.get_config('project'),
            'content-type': 'application/json',
            'accept': 'application/json',
        }, api_params)

        return self._parse_response(response, model=EmbeddingList)

