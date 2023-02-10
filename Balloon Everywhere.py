class Solution:

    def create_Dict(self, word, string): 

        Dict = {}

        for i in range(len(string)):

            if string[i] in word:

                if string[i] not in Dict:

                    Dict[string[i]] = 1

                else:

                    Dict[string[i]] += 1

        return Dict

    

    def maxInstance(self, s : str) -> int:

        word = "balloon"

        Dic1 = self.create_Dict(word, word)

        Dic2 = self.create_Dict(word, s)

        if len(Dic1) == len(Dic2):

            first_key = word[0]

        

            min = Dic2[first_key] // Dic1[first_key]

            for i in Dic2.keys():

            

                if Dic2[i] // Dic1[i] < min:

                    min = Dic2[i] // Dic1[i]

 

            return min

        else:

 

            return 0
