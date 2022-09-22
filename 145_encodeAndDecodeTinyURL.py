class Codec:
    def __init__(self):
        self.code = {}
        self.counter = 0
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        self.code[self.counter] = longUrl
        self.counter += 1
        
        return self.counter - 1
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.code[shortUrl]