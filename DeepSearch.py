'''马踏棋盘'''

from datetime import datetime


class DeepSearch:

    def __init__(self, entry, size):
        self.entry = entry  # 马的起始位置
        self.size = size  # 棋盘大小
        self.path = [None] * (size * size)  # 马行走的路径
        self.path[0] = entry  # 初始化马的第一步为起始位置
        self.moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]  # 状态空间，马移动的8个方向
        self.flag = False  # 判断马是否成功找到一条路径

    def start(self):
        self.start_time = datetime.now()  # 程序开始时间
        self.subsets(1)  # 进入函数进行寻找路径，参数1代表第1步

    # 冲突检测
    def conflict(self, step):  # 检验马将要走的下一步位置是否符合规则
        size = self.size
        moves = self.moves
        path = self.path
        # 判断马是否越出边界
        if path[step][0] < 0 or path[step][0] >= size or path[step][1] < 0 or path[step][1] >= size:
            return True
        # 判断马在前step步是否已经走过
        if path[step] in path[:step]:
            return True
        return False  # 无冲突

    def subsets(self, step):  # 马走到第step步
        size = self.size
        path = self.path
        moves = self.moves

        if step == size * size:  # 判断马是否走完
            self.flag = True
            end_time = datetime.now()
            self.time = (end_time - self.start_time).total_seconds()  # 算法所用时间

        else:
            for i in moves:  # 遍历元素 path的状态空间: 8个方向
                path[step] = (path[step - 1][0] + i[0], path[step - 1][1] + i[1])  # 马的下一步候选位置
                if not self.conflict(step):  # 判断下一步候选位置是否符合规则
                    self.subsets(step + 1)  # 如果符合规则，那么继续下一步的路径寻找
                    if (self.flag):  # 当找到路径，进行递归回溯的时候，直接返回上一层
                        return
        return

    def getTime(self):  # 获取算法运行时间
        return self.time

    def getPath(self):  # 获取算法找到的解
        return self.path


# 测试
if __name__ == '__main__':
    deep = DeepSearch((2, 2), 5)
    deep.start()
    print(deep.getTime())
    print(deep.getPath())
