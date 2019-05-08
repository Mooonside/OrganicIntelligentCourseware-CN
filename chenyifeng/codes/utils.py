from collections import Counter

import numpy as np


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.degree = 0
        self.nodes_out = Counter()

    def link_it_to(self, node_):
        self.degree += 1
        self.nodes_out[node_.idx] += 1

    def not_link_to(self, node_):
        if node_.idx in self.nodes_out:
            self.nodes_out.pop(node_.idx)
            return 1
        # no such link exists
        return 0

    def remove(self):
        self.degree = 0
        self.nodes_out.clear()

    def __repr__(self):
        str = 'Node {} with degree {}, connected to ('.format(self.idx, self.degree)
        for k, v in self.nodes_out.items():
            str += "(->%d x %d), " % (k, v)
        str += ')\n'
        return str


class Network:
    def __init__(self, node_nums, edge_nums):
        self.node_nums = node_nums
        self.edge_nums = edge_nums
        self.nodes = [Node(i) for i in range(self.node_nums)]
        self.remove = None
        self.belongs = None
        self.degrees = None

    def initialize(self):
        """
        randomly generate a graph
        :return:
        """
        return

    def degree_distrib(self):
        """
        solve for degree distribution
        :return:
        """
        degrees = np.array([n.degree for n in self.nodes])
        self.degrees = degrees
        return degrees

    def bfs(self):
        # cluster number belongings
        self.belongs = -1.0 * np.ones(self.node_nums)
        while True:
            indices = np.where(self.belongs == -1)[0]
            if len(indices) == 0:
                break
            # print('Searching from root %d' % indices[0])
            self._bfs(indices[0], indices[0])

        return self.belongs

    def _bfs(self, idx, root):
        # recursive function
        self.belongs[idx] = root
        nexts = self.nodes[idx].nodes_out.keys()
        for i in nexts:
            if self.belongs[i] == -1:
                self.belongs[i] = root
                self._bfs(i, root)
        return

    def remove_nodes(self, fraction):
        # set last belongings to be invalid
        self.belongs = None
        self.degrees = None
        # random select nodes
        candidate = np.where(self.remove == False)[0]
        remove_num = min(int(fraction * self.node_nums), len(candidate))
        # print(len(candidate), remove_num)

        remove = np.random.choice(candidate, remove_num, replace=False)
        for i in remove:
            # print('Removing %d' % i)
            dst_nodes = list(self.nodes[i].nodes_out.keys())
            for d in dst_nodes:
                self.nodes[d].not_link_to(self.nodes[i])
            self.nodes[i].remove()
            self.remove[i] = True

    def __repr__(self):
        str = "Nodes: \n"
        _ellipsis = False
        for idx, node in enumerate(self.nodes):
            if 5 < idx < self.node_nums - 5:
                if not _ellipsis:
                    str += '...\n'
                    _ellipsis = True
                continue

            str += "{}".format(node)
        return str


class ERNetwork(Network):
    def __init__(self, node_nums, lam):
        edge_nums = int(node_nums * lam // 2)
        super(ERNetwork, self).__init__(node_nums, edge_nums)
        self.lam = lam

    def initialize(self):
        # then random generate links, allow duplicate ones
        src_nodes = np.random.choice(self.node_nums, self.edge_nums)
        dst_nodes = np.random.choice(self.node_nums, self.edge_nums)

        for e in range(self.edge_nums):
            src = src_nodes[e]
            dst = dst_nodes[e]
            self.nodes[src].link_it_to(self.nodes[dst])
            self.nodes[dst].link_it_to(self.nodes[src])

        self.remove = np.array([False for _ in range(self.node_nums)])


class BANetwork(Network):
    def __init__(self, node_nums, gamma, maxk, mink=1):
        # calculate constant c
        self.gamma = gamma
        self.mink = mink
        self.maxk = maxk
        kp = np.power(np.arange(mink, maxk + 1), -gamma)
        self.c = 1.0 / np.sum(kp)
        self.kp = kp * self.c
        self.dk = np.sum(self.kp) - np.cumsum(self.kp) + self.kp
        super(BANetwork, self).__init__(node_nums, None)

    def initialize(self):
        """
        https://en.wikipedia.org/wiki/Barab%C3%A1si%E2%80%93Albert_model
        :return:
        """
        r = np.random.rand(self.node_nums)
        self._degrees = np.digitize(r, self.dk) - 1 + self.mink
        self.edge_nums = self._degrees.sum() // 2

        _degree_sequence = self._degrees.copy()

        for i in range(self.node_nums):
            _prob = _degree_sequence[i] * _degree_sequence
            
            _yes = np.random.rand(self.node_nums) < _prob
            for j in np.where(_yes)[0]:
                self.nodes[i].link_it_to(self.nodes[j])
                # self.nodes[j].link_it_to(self.nodes[i])
        self.remove = np.array([False for _ in range(self.node_nums)])
        return


if __name__ == '__main__':
    net = BANetwork(10, gamma=2.1, maxk=5)
    print(net.edge_nums)
