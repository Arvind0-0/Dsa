class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        '''
        properties.sort()
        N = len(properties)
        result = 0
        for i in range(N - 1):
            for j in range(N - 1, i, -1):
                if properties[i][0] < properties[j][0] and properties[i][1] < properties[j][1]:
                    result += 1
                    break
                if properties[i][0] >= properties[j][0] and properties[i][1] >= properties[j][1]:
                    break
                    
        return result
        '''
        
        max_defense_for_attacks = [0] * int(1e5 + 2)
        max_att = 0
        for att, defense in properties:
            if defense > max_defense_for_attacks[att]:
                max_defense_for_attacks[att] = defense
            if att > max_att:
                max_att = att
            
            # max_defense_for_attacks[att] = max(max_defense_for_attacks[att], defense)
            # max_att = max(max_att, att)
            
        
        # current_max = max_defense_for_attacks[max_att]
        current_max = 0
        for i in range(max_att, 0, -1):
            # if max_defense_for_attacks[i] > current_max:
            #     current_max = max_defense_for_attacks[i]
            # max_defense_for_attacks[i] = current_max
            current_max = max(current_max, max_defense_for_attacks[i])
            max_defense_for_attacks[i] = current_max
          
        result = 0
        for att, defense in properties:
            if defense < max_defense_for_attacks[att + 1]:
                result += 1
                
        return result