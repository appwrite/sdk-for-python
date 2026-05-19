from enum import Enum

class ProjectProtocolId(Enum):
    REST = "rest"
    GRAPHQL = "graphql"
    WEBSOCKET = "websocket"
