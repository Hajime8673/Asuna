class Context:
    """
    Provides a context-like access to a dictionary with support for default values.

    The Context class allows accessing dictionary values using dot notation, and provides a default value
    for non-existing keys. It also supports nested dictionaries.

    Args:
        dictionary (dict): The dictionary containing the initial values.
        **kwargs: Additional keyword arguments used to set default values for non-existing dictionary keys.

    Attributes:
        dictionary (dict): The underlying dictionary storing the values.
        default_value (any): The default value to be returned for non-existing keys.

    Examples:
        ```py
        ctx = Context({'asuna': 10})
        print(ctx.asuna)  # Output: 10
        print(ctx.sakura)  # Output: None

        ctx = Context({'asuna': 10}, default=0, miyuki=5)
        print(ctx.asuna)  # Output: 10
        print(ctx.sakura)  # Output: 0
        print(ctx.miyuki)  # Output: 5
        ```
    """

    def __init__(self, dictionary, **kwargs):
        self.dictionary = dictionary
        self.default_value = kwargs.get("default", None)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattr__(self, key):
        """
        Retrieves the value associated with the given key.

        If the key exists in the dictionary, its corresponding value is returned.
        If the key does not exist, the default value is returned.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            any: The value associated with the key, or the default value if the key does not exist.
        """
        if key in self.dictionary:
            value = self.dictionary[key]
            if isinstance(value, dict):
                return Context(value, default=self.default_value)
            return value
        return self.default_value

    def __setattr__(self, key, value):
        """
        Sets the value for the given key in the dictionary.

        If the key is 'dictionary' or 'default_value', the attribute is set directly.
        Otherwise, the key-value pair is stored in the dictionary.

        Args:
            key (str): The key to set the value for.
            value (any): The value to be associated with the key.

        Returns:
            None
        """
        if key != "dictionary" and key != "default_value":
            self.dictionary[key] = value
        else:
            super().__setattr__(key, value)
