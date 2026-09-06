class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for character in word.lower():

            if character not in current.children:
                current.children[character] = TrieNode()

            current = current.children[character]

        current.is_end_of_word = True

    def search(self, word):
        node = self._find_node(word)

        return node is not None and node.is_end_of_word

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix):
        node = self._find_node(prefix)

        if node is None:
            return []

        results = []

        self._collect_words(node, prefix.lower(), results)

        return results

    def _find_node(self, text):
        current = self.root

        for character in text.lower():

            if character not in current.children:
                return None

            current = current.children[character]

        return current

    def _collect_words(self, node, current_word, results):
        if node.is_end_of_word:
            results.append(current_word)

        for character, child in node.children.items():
            self._collect_words(
                child,
                current_word + character,
                results
            )


if __name__ == "__main__":

    trie = Trie()

    words = [
        "cloud",
        "cloud computing",
        "cloud engineer",
        "computer",
        "compute",
        "container",
        "continuous integration",
        "continuous deployment"
    ]

    for word in words:
        trie.insert(word)

    prefixes = [
        "cl",
        "comp",
        "cont"
    ]

    for prefix in prefixes:
        print(f"\nAutocomplete for '{prefix}':")
        print(trie.autocomplete(prefix))

    print("\nExact search:")
    print("cloud:", trie.search("cloud"))
    print("cloud engineer:", trie.search("cloud engineer"))
    print("cloud security:", trie.search("cloud security"))