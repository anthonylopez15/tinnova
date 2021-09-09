import logging

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError, TransportError
from fastapi import HTTPException

from app.constants import ELASTICSEARCH_HOST


class ElasticConnection(object):
    def __init__(self, index):
        self.client = Elasticsearch(F"{ELASTICSEARCH_HOST}")
        self.index = index

    def search(self, body=None, fields=None, scroll=None):
        if fields is None:
            fields = []
        try:
            response = self.client.search(
                index=self.index, body=body, _source=fields, scroll=scroll
            )
            return response
        except ConnectionError as connection:
            raise HTTPException(status_code=connection.status_code,
                                detail=connection.info['error']["reason"])
        except TransportError as error:
            raise HTTPException(status_code=error.status_code,
                                detail=error.info['error']["reason"])

    def post(self, document):
        try:
            document = self.client.index(
                index=self.index, body=document, refresh=True
            )
            return document
        except ConnectionError as connection:
            raise HTTPException(status_code=connection.status_code,
                                detail=connection.info['error']["reason"])
        except TransportError as error:
            raise HTTPException(status_code=error.status_code,
                                detail=error.info['error']["reason"])

    def update(self, document_id, body):
        try:
            response = self.client.update(index=self.index,
                                          id=document_id,
                                          body={"doc": body},
                                          refresh=True)
            return response

        except ConnectionError as connection:
            raise HTTPException(status_code=connection.status_code,
                                detail=connection.info['error']["reason"])
        except TransportError as error:
            raise HTTPException(status_code=error.status_code,
                                detail=error.info['error']["reason"])

    def delete(self, body=None):
        try:
            return self.client.delete_by_query(index=self.index, body=body, refresh=True)

        except ConnectionError as connection:
            raise HTTPException(status_code=connection.status_code,
                                detail=connection.info['error']["reason"])
        except TransportError as error:
            raise HTTPException(status_code=error.status_code,
                                detail=error.info['error']["reason"])

