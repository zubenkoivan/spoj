import math


class RodsRecovery:
  def __init__(self, rods_count, fusions):
    self._rods_count = rods_count
    self._fusions = fusions
    self._unions = [x for x in range(0, rods_count + 1)]
    self._union_heights = [1 for _ in range(0, rods_count + 1)]
    self._union_sizes = [1 for _ in range(0, rods_count + 1)]
  

  def calculate_cost(self):
    for fusion in self._fusions:
      self._union(fusion[0], fusion[1])
    
    total_cost = 0

    for size in self._union_sizes:
      cost = int(math.ceil(math.sqrt(size))) if size > 1 else size
      total_cost = total_cost + cost
    
    return total_cost - 1


  def _union(self, p, q):
    root_p = self._root(p)
    root_q = self._root(q)
    height_p = self._union_heights[root_p]
    height_q = self._union_heights[root_q]
    union_size = self._union_sizes[root_p] + self._union_sizes[root_q]
    union_height = height_p + 1 if height_p == height_q else max(height_p, height_q)
    root_p, root_q = (root_q, root_p) if height_p > height_q else (root_p, root_q)
    
    self._union_sizes[root_p] = union_size
    self._union_sizes[root_q] = 0
    self._union_heights[root_p] = union_height
    self._union_heights[root_q] = 0
    self._unions[root_q] = root_p


  def _root(self, p):
    while p != self._unions[p]:
      self._unions[p] = self._unions[self._unions[p]]
      p = self._unions[p]
    return p


def parse_fusion(str):
  splitted = str.split()
  return (int(splitted[0]), int(splitted[1]))


def run():
  rods_count = int(input())
  fusions_count = int(input())
  fusions = [parse_fusion(input()) for _ in range(fusions_count)]
  print(RodsRecovery(rods_count, fusions).calculate_cost())


run()