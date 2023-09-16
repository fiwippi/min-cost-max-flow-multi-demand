import unittest

from flow import *

class TestFlowsMoved(unittest.TestCase):
    def test_choose_closest_single(self):
        sources: Nodes = Nodes({
                Node("A"): Capacity(1),
                Node("B"): Capacity(1),
                })
        sinks: Nodes = Nodes({
                Node("C"): Capacity(0),
                Node("D"): Capacity(1),
                })
        costs: Edges = Edges({
                Edge((Node("A"), Node("C"))): Cost(10),
                Edge((Node("A"), Node("D"))): Cost(15),
                Edge((Node("B"), Node("C"))): Cost(10),
                Edge((Node("B"), Node("D"))): Cost(10),
                })
     
        name = self.id().split(".")[-1]
        s, cost = match_flows(sources, sinks, costs, filename=name)
        self.assertEqual(total_moved(s), AmountMoved(1))
        self.assertEqual(cost, AvgCost(10.0))


    def test_choose_closest_multi(self):
        sources: Nodes = Nodes({
                Node("A"): Capacity(1),
                Node("B"): Capacity(1),
                })
        sinks: Nodes = Nodes({
                Node("C"): Capacity(1),
                Node("D"): Capacity(1),
                })
        costs: Edges = Edges({
                Edge((Node("A"), Node("C"))): Cost(10),
                Edge((Node("A"), Node("D"))): Cost(15),
                Edge((Node("B"), Node("C"))): Cost(10),
                Edge((Node("B"), Node("D"))): Cost(10),
                })
     
        name = self.id().split(".")[-1]
        s, cost = match_flows(sources, sinks, costs, filename=name)
        self.assertEqual(total_moved(s), AmountMoved(2))
        self.assertEqual(cost, AvgCost(10.0))
    
    def test_choose_furthest_single(self):
        sources: Nodes = Nodes({
                Node("A"): Capacity(1),
                Node("B"): Capacity(1),
                })
        sinks: Nodes = Nodes({
                Node("C"): Capacity(0),
                Node("D"): Capacity(1),
                })
        costs: Edges = Edges({
                Edge((Node("A"), Node("C"))): Cost(10),
                Edge((Node("A"), Node("D"))): Cost(10),
                Edge((Node("B"), Node("C"))): Cost(10),
                Edge((Node("B"), Node("D"))): Cost(15),
                })
     
        name = self.id().split(".")[-1]
        s, cost = match_flows(sources, sinks, costs, filename=name)
        self.assertEqual(total_moved(s), AmountMoved(1))
        self.assertEqual(cost, AvgCost(10.0))

    def test_choose_furthest_multi(self):
        sources: Nodes = Nodes({
                Node("A"): Capacity(1),
                Node("B"): Capacity(1),
                })
        sinks: Nodes = Nodes({
                Node("C"): Capacity(1),
                Node("D"): Capacity(1),
                })
        costs: Edges = Edges({
                Edge((Node("A"), Node("C"))): Cost(10),
                Edge((Node("A"), Node("D"))): Cost(15),
                Edge((Node("B"), Node("C"))): Cost(2),
                Edge((Node("B"), Node("D"))): Cost(10),
                })
     
        name = self.id().split(".")[-1]
        s, cost = match_flows(sources, sinks, costs, filename=name)
        self.assertEqual(total_moved(s), AmountMoved(2))
        self.assertEqual(cost, AvgCost(8.5))

    def test_choose_furthest_multi_v2(self):
        sources: Nodes = Nodes({
                Node("A"): Capacity(1),
                Node("B"): Capacity(1),
                Node("C"): Capacity(4),
                })
        sinks: Nodes = Nodes({
                Node("D"): Capacity(3),
                Node("E"): Capacity(3),
                })
        costs: Edges = Edges({
                Edge((Node("A"), Node("D"))): Cost(10),
                Edge((Node("A"), Node("E"))): Cost(15),
                Edge((Node("B"), Node("D"))): Cost(3),
                Edge((Node("B"), Node("E"))): Cost(10),
                Edge((Node("C"), Node("D"))): Cost(5),
                Edge((Node("C"), Node("E"))): Cost(10),
                })
     
        name = self.id().split(".")[-1]
        s, cost = match_flows(sources, sinks, costs, filename=name)
        self.assertEqual(total_moved(s), AmountMoved(6))
        self.assertEqual(cost, AvgCost(8.25))

if __name__ == '__main__':
    unittest.main()

