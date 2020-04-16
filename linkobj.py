class LinkObj:

    def __init__(self, url ,depthcount):
        self.url = url
        self.depthcount = depthcount

    def __eq__(self, other):
        return self.url == other.url
