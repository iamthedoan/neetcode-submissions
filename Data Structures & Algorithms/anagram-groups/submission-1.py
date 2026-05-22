class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ana_dict = {}
        # store unique combos in hash, record indices

        for i, word in enumerate(strs):
            word_dict = {}
            for c in word:
                word_dict[c] = 1 + word_dict.get(c,0)
            
            key = tuple(sorted(word_dict.items()))
            if key in ana_dict:
                ana_dict[key].append(i)
            else:
                ana_dict[key] = [i]

        ana_list = []
        for val in ana_dict.values():
            ana_list.append([strs[i] for i in val])

        return ana_list


            




        