class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = '/'
        self.handler = None
        self.next = {}

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        cur_node = self.next
        paths = paths.split('/')
        for path in paths:
            cur_node.insert(RouteTrieNode(path))
            cur_node = cur_node.next[path]
        cur_node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths == '/':
            return self.handler
        paths = paths.split('/')

        cur_node = self
        for path in paths:
            cur_node = cur_node.next
            cur_node = cur_node[path]


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, val=''):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.next = {}
        self.value = val

    def insert(self, path, handler=None):
        # Insert the node as before
        self.next[path] = self.next.get(path, RouteTrieNode(path))
        self.next[path].handler = handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, error):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = '/'
        self.handler = root_handler
        self.error = error
        self.next = {}

    def add_handler(self, path, path_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        if path == self.root:
            self.handler = path_handler
        else:
            path = self.split_path(path)
            cur_node = self.next
            i = 1
            for p in path:
                if not p:
                    continue
                if i:
                    i = 0
                    cur_node[p] = cur_node.get(p, RouteTrieNode(p))
                    cur_node = cur_node[p]
                else:
                    cur_node.insert(p, path_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if path == '/':
            return self.handler
        path = self.split_path(path)
        cur_node = self
        # print(path)
        for p in path:
            if p:
                # print(p, cur_node.next)
                if p in cur_node.next:
                    # print(cur_node, 'curr')
                    cur_node = cur_node.next
                    cur_node = cur_node[p]
                else:
                    return self.error

        handler = cur_node.handler
        if handler:
            return handler
        else:
            return 'not found'

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one