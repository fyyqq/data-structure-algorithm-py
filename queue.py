from collections import defaultdict, Counter, OrderedDict, deque, namedtuple 

user = defaultdict(list) # any type
user["name"].append("Afiq")
user["age"].append(20)

counter = Counter({"name" : "lishaazhn", "age" : 20})

orders = OrderedDict()
orders["name"] = "Sarah"
orders["age"] = 20

deque = deque()
deque.append('a')
deque.append('b')
deque.append('c')
deque.popleft()

nTuple = namedtuple('Point', 'a b c d e')
z = nTuple(1, 2, 3, 4, 5)