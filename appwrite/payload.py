from typing import Optional, Dict, Any
import os, json

class Payload:
    size: int
    filename: Optional[str] = None

    _path: Optional[str] = None 
    _data: Optional[bytes] = None

    def __init__(self, path: Optional[str] = None, data: Optional[bytes] = None, filename: Optional[str] = None):
        if not path and not data:
            raise ValueError("One of path or data must be provided")

        self._path = path
        self._data = data

        self.filename = filename
        if not self._data:
            self.size = os.path.getsize(self._path)
        else:
            self.size = len(self._data)
  
    def to_binary(self, offset: Optional[int] = 0, length: Optional[int] = None) -> bytes:
        if not length:
            length = self.size
        
        if not self._data:
            with open(self._path, 'rb') as f:
                f.seek(offset)
                return f.read(length)
        
        return self._data[offset:offset + length]
    
    def to_string(self) -> str:
        return str(self.to_binary())

    def to_json(self) -> Dict[str, Any]:
        return json.loads(self.to_string())
    
    def to_file(self, path: str) -> None: # in the client SDKs, this is def to_file() -> File:
        with open(path, 'wb') as f:
            return f.write(self.to_binary())

    @classmethod
    def from_binary(cls, data: bytes, filename: Optional[str] = None) -> 'Payload':
        return cls(data=data, filename=filename)

    @classmethod
    def from_string(cls, data: str) -> 'Payload':
        return cls(data=data.encode())
       
    @classmethod
    def from_file(cls, path: str, filename: Optional[str] = None) -> 'Payload':
        if not os.path.exists(path):
            raise FileNotFoundError(f"File {path} not found")
        if not filename:
            filename = os.path.basename(path)
        return cls(path=path, filename=filename)

    @classmethod
    def from_json(cls, json: Dict[str, Any]) -> 'Payload':
        return cls(data=json.dumps(json))