import random
class Codec:
    
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.s2l = dict()
        self.l2s = dict()
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.l2s:
            code = "".join(random.choice(self.alphabet) for _ in range(6))
            if code not in self.s2l:
                self.s2l[code] = longUrl
                self.l2s[longUrl] = code
            
        return "http://tinyurl.com/" + self.l2s[longUrl]
        
 
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl[-6:]
        return self.s2l[key]
 
# Your Codec object will be instantiated and called as such:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
raw_url = codec.decode(codec.encode(url))
print(raw_url)