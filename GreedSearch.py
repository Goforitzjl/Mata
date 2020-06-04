'''马踏棋盘'''

from datetime import datetime


class GreedSearch:
    def __init__(self, entry, size):
        self.entry = entry
        self.size = size
        self.path = [None] * (size * size)
        self.path[0] = entry
        self.moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]  # 状态空间，8个方向

    def start(self):
        self.start_time = datetime.now()
        self.subsets(1)

    def conflict(self, step, childNode):
        size = self.size
        path = self.path

        if childNode[0] < 0 or childNode[0] >= size or childNode[1] < 0 or childNode[1] >= size:
            return True

        if childNode in path:
            return True
        return False

    def subsets(self, step):
        size = self.size
        path = self.path
        moves = self.moves
        childNodes = []  # 用来存储候选位置它的下一步合法的候选位置
        bestchildNode = ()  # 选出来的下一个候选位置
        min = 8  # 候选位置它的下一步合法的候选位置的最少个数
        if step == size * size:
            self.flag = True
            end_time = datetime.now()
            self.time = (end_time - self.start_time).total_seconds()
        else:
            for i in moves:
                childNode = (path[step - 1][0] + i[0], path[step - 1][1] + i[1])
                if not self.conflict(step, childNode):
                    for j in moves:  # 对下一步候选位置它的下一步候选位置进行校验
                        childchildNode = (childNode[0] + j[0], childNode[1] + j[1])
                        if not self.conflict(step, childchildNode):
                            childNodes.append(childchildNode)  # 添加合法候选位置
                    if len(childNodes) < min:  # 找出下一步候选位置最少的候选
                        bestchildNode = childNode
                        min = len(childNodes)
                    childNodes.clear()
            path[step] = bestchildNode  # 选出来的最优候选位置作为马的下一步
            self.subsets(step + 1)
            if (self.flag):
                return  # 找到路径之后的回溯

        return

    def getTime(self):
        return self.time

    def getPath(self):
        return self.path


# 测试
if __name__ == '__main__':
    greed = GreedSearch((2, 2), 10)
    greed.start()
    print(greed.path)
    print(greed.getTime())
