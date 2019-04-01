import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)

        if endWord not in wordList: return []

        layerBegin = collections.defaultdict()
        layerBegin[beginWord] = [[beginWord]]
        wordList -= set(layerBegin.keys())

        layerEnd = collections.defaultdict()
        layerEnd[endWord] = [[endWord]]
        wordList -= set(layerEnd.keys())

        res = []
        met = False

        while layerEnd:

            # forward
            newlayer = collections.defaultdict(list)
            for w in layerBegin:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i] + c + w[i + 1:]
                        if neww in layerEnd:  # judge whether met
                            met = True
                            res += [b + e for b in layerBegin[w] for e in layerEnd[neww]]
                        if (not met) and (neww in wordList):
                            newlayer[neww] += [b + [neww] for b in layerBegin[w]]
            if met: return res
            wordList -= set(newlayer.keys())
            layerBegin = newlayer
            if not layerBegin: break

            # backward
            newlayer = collections.defaultdict(list)
            for w in layerEnd:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i] + c + w[i + 1:]
                        if neww in layerBegin:  # judge whether met
                            met = True
                            res += [b + e for b in layerBegin[neww] for e in layerEnd[w]]
                        if (not met) and (neww in wordList):
                            newlayer[neww] += [[neww] + e for e in layerEnd[w]]
            if met: return res
            wordList -= set(newlayer.keys())
            layerEnd = newlayer
        return []