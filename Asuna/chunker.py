class Chunker:
    def chunk(input_list, chunk_size):
        """
        Chunk a list into smaller sublists of the specified length.

        :param input_list: The list to be chunked.
        :param chunk_size: The length of each chunk.
        :return: A list of chunks.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk size must be a positive integer.")

        chunks = []
        for i in range(0, len(input_list), chunk_size):
            chunk = input_list[i:i + chunk_size]
            chunks.append(chunk)

        return chunks

    def multi_chunk(*lists, chunk_size, default_value=None):
        """
        Chunk multiple lists by extracting one item from each list and forming sets.
        If a list runs out of items, use the default_value to fill in.

        :param lists: Multiple input lists.
        :param chunk_size: The length of each chunk.
        :param default_value: The value to use for lists that run out of items.
        :return: A list of chunks.
        """
        if chunk_size <= 0:
            raise ValueError("Chunk size must be a positive integer.")

        chunks = []
        num_lists = len(lists)

        for i in range(0, len(lists[0]), chunk_size):
            chunk = []

            for j in range(num_lists):
                if i < len(lists[j]):
                    chunk.append(lists[j][i])
                else:
                    chunk.append(default_value)

            chunks.append(chunk)

        return chunks

