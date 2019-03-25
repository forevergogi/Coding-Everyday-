# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 1:
            return len(points)
        length = len(points)
        res = 0
        for i in range(length-1):
            dict = {}
            duplicate = 1
            for j in range(i+1,length):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicate += 1
                else:
                    dx = points[j].x - points[i].x
                    dy = points[j].y - points[i].y
                    g = self.gcd(dx,dy)
                    pair = (dx/g,dy/g)
                    if pair in dict:
                        dict[pair] += 1
                    else:
                        dict[pair] = 1
            res = max(res,duplicate)
            if len(dict.keys()) != 0:
                max_in_dict = max([dict[key] for key in dict.keys()])
                res = max(res, duplicate + max_in_dict)
        return res

    def gcd(self,x,y):
        return x if y == 0 else self.gcd(y,x%y)

if __name__ == '__main__':
    s = Solution()
    lst = [[1,1],[1,1],[1,1],[1,1],[1,1]]
    points=[]
    for ele in lst:
        points.append(Point(ele[0],ele[1]))
    res = s.maxPoints(points)
    print(res)
