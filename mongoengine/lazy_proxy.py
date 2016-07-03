from peak.util.proxies import LazyWrapper


class DocumentLazyProxy(LazyWrapper):
    """Lazy proxy for Document that allows to access the id attribute
    without dereferencing
    """
    def __init__(self, dereferencer, id_):
        """Constructor

        :param dereferencer: function that dereferences
            a document to be proxied
        :param id_: the id of the object
        """
        LazyWrapper.__init__(self, dereferencer)
        object.__setattr__(self, 'id', id_)

    def __repr__(self):
        """Overriden to avoid dereferencing while debugging"""
        return '{} ({})'.format(str(type(self)), self.id)
