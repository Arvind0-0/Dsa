class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for path in paths:
            strs = path.split()
            root = strs[0]
            for s in strs[1:]:
                file_name, _, content = s.partition('(')
                maps[content].append(root+'/'+file_name)
        return [x for x in maps.values() if len(x) > 1]
